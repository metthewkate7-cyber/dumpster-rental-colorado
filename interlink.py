#!/usr/bin/env python3
"""Sitewide interlinking pass for dumpsterrentalcolorado.us (Colorado site).

Rules (locked by the task):
- Only link the FIRST natural mention of an entity on each page, inside <p>/<li>
  body text (never inside headings, nav, header, footer, tables, figures,
  forms/tools, or cards).
- Never link a page to itself; never add a second link to a URL already
  linked inside <main> (one link per target per page).
- Never link inside an existing <a> tag.
- Max 8 new links per page, max 2 per paragraph/list-item.
- City names match case-sensitively (proper nouns); service/size/guide
  phrases match case-insensitively, preserving the original anchor text.
- Longer phrases win over shorter ones (e.g. 'Denver metro' > 'Denver',
  '20-yard dumpster' > '20-yard').

Usage: python3 interlink.py [--dry-run]   (default writes files)
"""
import re, sys, os
from xml.etree import ElementTree as ET

ROOT = os.path.dirname(os.path.abspath(__file__))
DRY = '--dry-run' in sys.argv
MAX_NEW = 8
MAX_PER_BLOCK = 2

# ---------- entity map ----------
def h1_of(path):
    html = open(os.path.join(ROOT, path), encoding='utf-8').read()
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.S)
    return re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else ''

urls = [e.text for e in ET.parse(os.path.join(ROOT, 'sitemap.xml')).getroot().iter()
        if e.tag.endswith('loc')]

ENTITIES = []  # (path_url, [phrases], case_sensitive)

for u in urls:
    p = u.replace('https://dumpsterrentalcolorado.us', '').strip('/')
    if p.startswith('dumpster-rental-') and p != 'dumpster-rental-prices-colorado':
        name = h1_of(p + '/index.html').replace('Dumpster Rental ', '').strip()
        name = re.sub(r',?\s*CO$', '', name)
        phrases = [name]
        if name == 'Canon City':
            phrases.append('Cañon City')
        if name == 'Security-Widefield':
            phrases.append('Security Widefield')
        ENTITIES.append(('https://dumpsterrentalcolorado.us/' + p + '/', phrases, True))

for name, slug in [('Front Range', 'front-range'), ('Denver Metro', 'denver-metro'),
                   ('Denver metro area', 'denver-metro'), ('Western Slope', 'western-slope'),
                   ('Central Mountains', 'central-mountains'),
                   ('Northern Colorado', 'northern-colorado'),
                   ('Southern Colorado', 'southern-colorado')]:
    ENTITIES.append(('https://dumpsterrentalcolorado.us/regions/%s/' % slug, [name], False))

for slug, phrases in [
    ('residential-dumpster-rental-colorado', ['residential dumpster']),
    ('construction-dumpster-rental-colorado', ['construction dumpster']),
    ('roofing-dumpster-rental-colorado', ['roofing dumpster', 'roof dumpster']),
    ('demolition-dumpster-rental-colorado', ['demolition dumpster', 'demo dumpster']),
    ('concrete-dumpster-rental-colorado', ['concrete dumpster']),
    ('commercial-dumpster-rental-colorado', ['commercial dumpster']),
    ('roll-off-dumpster-rental-colorado', ['roll-off dumpster', 'roll off dumpster']),
    ('same-day-dumpster-rental-colorado', ['same-day dumpster', 'same day dumpster']),
    ('yard-waste-dumpster-rental-colorado', ['yard waste dumpster']),
    ('estate-cleanout-dumpster-rental-colorado', ['estate cleanout']),
]:
    ENTITIES.append(('https://dumpsterrentalcolorado.us/%s/' % slug, phrases, False))

for n in (10, 15, 20, 30, 40):
    ENTITIES.append(('https://dumpsterrentalcolorado.us/%d-yard-dumpster-rental/' % n,
                     ['%d-yard dumpster' % n, '%d yard dumpster' % n, '%d-yard' % n], False))
ENTITIES.append(('https://dumpsterrentalcolorado.us/dumpster-size-calculator/',
                 ['dumpster size calculator', 'size calculator'], False))
ENTITIES.append(('https://dumpsterrentalcolorado.us/dumpster-rental-prices-colorado/',
                 ['Colorado prices', 'dumpster prices', 'price ranges', 'price range',
                  'published market ranges', 'published market range'], False))
ENTITIES.append(('https://dumpsterrentalcolorado.us/book-a-dumpster/',
                 ['book a dumpster', 'book your dumpster'], False))

for slug, phrases in [
    ('dumpster-rental-cost', ['dumpster rental cost', 'rental cost']),
    ('dumpster-rental-for-a-day', ['dumpster for a day', 'rent a dumpster for a day',
                                   'one-day rental', 'one day rental']),
    ('dumpster-rental-permits-colorado', ['dumpster permit', 'street permit', 'permit']),
    ('dumpster-vs-junk-removal', ['junk removal']),
    ('dumpster-weight-limits', ['weight limits', 'weight limit', 'weight allowance']),
    ('how-long-can-i-keep-a-dumpster', ['how long can you keep a dumpster',
                                        'how long can i keep a dumpster', 'keep a dumpster']),
    ('how-to-rent-a-dumpster', ['how to rent a dumpster', 'how to rent']),
    ('what-can-go-in-a-dumpster', ['what can go in a dumpster', 'what can go in']),
    ('what-happens-if-you-overfill-a-dumpster', ['what happens if you overfill a dumpster']),
    ('what-size-dumpster-do-i-need', ['what size dumpster']),
    ('will-a-dumpster-damage-my-driveway', ['damage my driveway', 'damage your driveway',
                                            'driveway damage']),
]:
    ENTITIES.append(('https://dumpsterrentalcolorado.us/guides/%s/' % slug, phrases, False))

for _url, phrases, _cs in ENTITIES:
    phrases.sort(key=len, reverse=True)
ENTITIES.sort(key=lambda e: max(len(p) for p in e[1]), reverse=True)

# ---------- helpers ----------
EXCL_PATTERNS = [
    r'<div class="card">.*?</div>',
    r'<table>.*?</table>',
    r'<figure>.*?</figure>',
    r'<form\b.*?</form>',
    r'<script\b.*?</script>',
    r'<style\b.*?</style>',
]

def excluded_spans(html):
    spans = []
    for pat in EXCL_PATTERNS:
        for m in re.finditer(pat, html, re.S):
            spans.append((m.start(), m.end()))
    return spans

def inside(spans, pos):
    return any(a <= pos < b for a, b in spans)

def split_links(text):
    parts = re.split(r'(<a\b[^>]*>.*?</a>)', text, flags=re.S)
    return [(p.startswith('<a'), p) for p in parts if p]

def find_phrase(chunk, phrase, case_sensitive):
    flags = 0 if case_sensitive else re.I
    pat = r'(?<![A-Za-z0-9])' + re.escape(phrase) + r'(?![A-Za-z0-9])'
    return re.search(pat, chunk, flags)

# ---------- main pass ----------
EXCLUDE_PAGES = {'terms-of-service/index.html', 'privacy-policy/index.html'}

pages = []
for dirpath, _dirs, files in os.walk(ROOT):
    if 'assets' in dirpath or 'node_modules' in dirpath:
        continue
    for f in files:
        if f == 'index.html':
            _p = os.path.join(dirpath, f)
            if os.path.relpath(_p, ROOT) not in EXCLUDE_PAGES:
                pages.append(_p)
pages.sort()

total_added = 0
pages_changed = 0
per_page = {}
by_url = {}
by_type = {'city': 0, 'region': 0, 'service': 0, 'size': 0, 'guide': 0, 'price/book': 0}
examples = []

for path in pages:
    rel = os.path.relpath(path, ROOT)
    page_url = ('https://dumpsterrentalcolorado.us/' +
                (os.path.dirname(rel) + '/' if os.path.dirname(rel) else ''))
    html = open(path, encoding='utf-8').read()
    m_main = re.search(r'<main\b.*?</main>', html, re.S)
    if not m_main:
        print('NO MAIN:', rel)
        continue
    main = m_main.group(0)
    taken = set()
    for hm in re.finditer(r'<a\b[^>]*href="([^"]+)"', main):
        href = hm.group(1)
        if href.startswith('/'):
            taken.add('https://dumpsterrentalcolorado.us' + href)
        elif href.startswith('https://dumpsterrentalcolorado.us'):
            taken.add(href)
    spans = excluded_spans(main)
    state = {'added': 0}

    def process_block(bm):
        if state['added'] >= MAX_NEW:
            return bm.group(0)
        if inside(spans, bm.start()):
            return bm.group(0)
        inner = bm.group(2)
        if ('<select' in inner or '<label' in inner or '<input' in inner
                or '<button' in inner or 'Last updated' in inner):
            return bm.group(0)
        block_added = 0
        for url, phrases, cs in ENTITIES:
            if state['added'] >= MAX_NEW or block_added >= MAX_PER_BLOCK:
                break
            if url == page_url or url in taken:
                continue
            new_inner = None
            new_anchor = None
            for is_link, chunk in split_links(inner):
                if is_link:
                    continue
                for phrase in phrases:
                    mm = find_phrase(chunk, phrase, cs)
                    if mm:
                        anchor = mm.group(0)
                        rel_url = url.replace('https://dumpsterrentalcolorado.us', '')
                        new_chunk = (chunk[:mm.start()] +
                                     '<a href="%s">%s</a>' % (rel_url, anchor) +
                                     chunk[mm.end():])
                        new_inner = inner.replace(chunk, new_chunk, 1)
                        new_anchor = (anchor, rel_url)
                        break
                if new_inner is not None:
                    break
            if new_inner is not None:
                inner = new_inner
                taken.add(url)
                state['added'] += 1
                block_added += 1
                by_url[url] = by_url.get(url, 0) + 1
                if len(examples) < 12:
                    examples.append((rel, new_anchor[0], new_anchor[1]))
        if block_added:
            open_tag = bm.group(0)[:bm.group(0).find('>') + 1]
            return open_tag + inner + '</%s>' % bm.group(1)
        return bm.group(0)

    new_main = re.sub(r'<(p|li)\b[^>]*>(.*?)</\1>', process_block, main, flags=re.S)
    per_page[rel] = state['added']
    total_added += state['added']
    if new_main != main:
        pages_changed += 1
        if not DRY:
            html = html[:m_main.start()] + new_main + html[m_main.end():]
            open(path, 'w', encoding='utf-8').write(html)

print('MODE:', 'DRY-RUN (no files written)' if DRY else 'WROTE FILES')
print('Total new links:', total_added)
print('Pages changed:', pages_changed, 'of', len(pages))
print('Pages with 0 new links:', sum(1 for v in per_page.values() if v == 0))
print('Pages hitting the 8-link cap:', sum(1 for v in per_page.values() if v >= MAX_NEW))
print('Top linked targets:')
for url, n in sorted(by_url.items(), key=lambda kv: -kv[1])[:15]:
    print('  ', n, url.replace('https://dumpsterrentalcolorado.us', ''))
print('Sample new links:')
for rel, anchor, url in examples:
    print('  ', rel, '|', repr(anchor), '->', url)
print('Per-page counts (top 25):')
for rel, n in sorted(per_page.items(), key=lambda kv: -kv[1])[:25]:
    if n:
        print('  ', n, rel)
