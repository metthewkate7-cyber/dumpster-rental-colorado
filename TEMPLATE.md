# PAGE TEMPLATE — Colorado site — follow exactly for every page you write

Site root: `~/workspace/hyperlocal-dumpster-rental/site-colorado/` (this is the COLORADO site only. NEVER touch `~/workspace/hyperlocal-dumpster-rental/site/` — that is the parallel Indiana site. Different domain, different state, do not mix.)
Domain: https://dumpsterrentalcolorado.us/ (canonical base — site not live yet, domain handover pending)
Stack: Vanilla HTML + CSS + JS only. No frameworks, no WordPress, no database, no server code.

## Files and paths
- Every page is a folder with `index.html`: e.g. `site-colorado/dumpster-rental-denver/index.html`. Homepage is `site-colorado/index.html`.
- CSS: `/assets/css/style.css` (already built — do NOT create another stylesheet).
- JS: `/assets/js/main.js` (already built — include on every page, do NOT add other scripts).
- Images live in `/assets/img/`. Use ONLY the images listed in "Images" below. Never reference an image that does not exist.
- Write valid HTML5. No inline `style` attributes. No emojis anywhere. No em dashes or en dashes anywhere in visible text (hyphens in words like "10-yard" and "roll-off" are fine).
- Design: mobile-first. One column on mobile. Sticky call/book bar on mobile. Tap-to-call + Book button on every page.

## HTML skeleton (copy this structure, fill the bracketed parts)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[unique title, primary KW first, max 60 chars]</title>
<meta name="description" content="[unique description, primary KW once, max 160 chars, one differentiator + CTA]">
<link rel="canonical" href="https://dumpsterrentalcolorado.us/[page-url]/">
<meta property="og:title" content="[same as title]">
<meta property="og:description" content="[same as description]">
<meta property="og:type" content="website">
<meta property="og:url" content="https://dumpsterrentalcolorado.us/[page-url]/">
[ONLY on city pages: geo meta tags — see below]
<link rel="stylesheet" href="/assets/css/style.css">
<script type="application/ld+json">[JSON-LD — see below]</script>
</head>
<body>
<header class="site-header"><div class="wrap">
<a class="brand" href="/">Dumpster Rental Colorado<small>Roll-off dumpsters across Colorado</small></a>
<nav class="main-nav" aria-label="Main">
<a href="/#sizes">Sizes</a><a href="/dumpster-rental-prices-colorado/">Prices</a><a href="/guides/what-size-dumpster-do-i-need/">Size guide</a><a href="/faq/">FAQ</a><a href="/contact/">Contact</a><a class="nav-cta" href="/book-a-dumpster/">Book now</a>
</nav></div></header>
<main>
<section class="hero"><div class="wrap">
<h1>[H1 — primary keyword, natural]</h1>
<p class="lede">[first paragraph — primary keyword once, plain and useful]</p>
<div class="hero-ctas"><a class="btn" href="/book-a-dumpster/">Book your dumpster</a><a class="btn-ghost" href="tel:">Call [PHONE]</a></div>
<figure><img src="/assets/img/[image-file]" alt="[alt with primary KW once]" width="1000" height="667" loading="eager"><figcaption>[caption]</figcaption></figure>
</div></section>
<div class="wrap">
<div class="quick-answer"><h2>Quick answer</h2><p>[2-4 short sentences answering the page question directly]</p></div>
[content sections with H2s — see content rules]
[price table / size cards / estimator link where relevant]
<section><h2>Frequently asked questions</h2>
<details><summary>[question]</summary><p>[answer]</p></details>
... 4-6 unique FAQs, written once (never print the same FAQ twice on a page) ...
</section>
<section><h2>Ready to book?</h2><p>[booking CTA text]</p><p><a class="btn" href="/book-a-dumpster/">Book a dumpster</a> <a class="btn-ghost" href="tel:">Call [PHONE]</a></p></section>
<section><h2>More from Dumpster Rental Colorado</h2><ul>[silo internal links — see linking rules]</ul></section>
<p class="updated">Last updated: November 13, 2026. Prices shown are published market ranges with sources cited. Our exact prices are confirmed at booking.</p>
</div></main>
<footer class="site-footer"><div class="wrap"><div class="cols">
<div><h3>Dumpster Rental Colorado</h3><p>Roll-off dumpster rental across Colorado. [BUSINESS NAME]<br>[COLORADO SPRINGS ADDRESS — TO BE CONFIRMED]<br><a href="tel:">[PHONE]</a></p></div>
<div><h3>Top cities</h3><ul>
<li><a href="/dumpster-rental-colorado-springs/">Dumpster rental Colorado Springs</a></li>
<li><a href="/dumpster-rental-denver/">Dumpster rental Denver</a></li>
<li><a href="/dumpster-rental-aurora-co/">Dumpster rental Aurora</a></li>
<li><a href="/dumpster-rental-boulder-co/">Dumpster rental Boulder</a></li>
<li><a href="/dumpster-rental-fort-collins/">Dumpster rental Fort Collins</a></li>
<li><a href="/dumpster-rental-pueblo/">Dumpster rental Pueblo</a></li>
<li><a href="/dumpster-rental-greeley-co/">Dumpster rental Greeley</a></li>
<li><a href="/dumpster-rental-lakewood-co/">Dumpster rental Lakewood</a></li>
</ul></div>
<div><h3>Services and guides</h3><ul>
<li><a href="/residential-dumpster-rental-colorado/">Residential dumpsters</a></li>
<li><a href="/construction-dumpster-rental-colorado/">Construction dumpsters</a></li>
<li><a href="/same-day-dumpster-rental-colorado/">Same-day delivery</a></li>
<li><a href="/20-yard-dumpster-rental/">20-yard dumpster</a></li>
<li><a href="/dumpster-rental-prices-colorado/">Colorado prices guide</a></li>
<li><a href="/guides/dumpster-rental-permits-colorado/">Permit guide</a></li>
<li><a href="/book-a-dumpster/">Book a dumpster</a></li>
<li><a href="/contact/">Contact</a></li>
<li><a href="/privacy-policy/">Privacy policy</a></li>
<li><a href="/terms-of-service/">Terms of service</a></li>
</ul></div>
</div><p>© 2026 Dumpster Rental Colorado. All rights reserved.</p></div></footer>
<div class="sticky-bar"><a class="call" href="tel:">Call [PHONE]</a><a class="book" href="/book-a-dumpster/">Book now</a></div>
<script src="/assets/js/main.js"></script>
</body></html>
```

## Content rules (locked prompt — violate none)
- 5th-grade reading level. Simple words. Sentences under 20 words. Short paragraphs.
- No fluff, no filler, no dashes (em/en), no emojis, no AI words ("delve", "elevate", "moreover", "in conclusion", "tapestry", etc.), minimal passive voice.
- No duplicate paragraphs across pages. Every page's body copy, FAQ, and meta must be unique to that page.
- Primary keyword: in H1/title, ONCE in an H2, ONCE in the first paragraph, ONCE in metas, ONCE in image alt text. Never stuff it.
- Every factual claim needs a source or a "[TO CONFIRM]" marker. Prices: ONLY the sourced market ranges in "Price facts" below, always labeled as market ranges with the source, never presented as our prices. Our exact prices are [TO CONFIRM].
- Never invent reviews, ratings, years in business, truck counts, or "we" claims about the business. Use [BUSINESS NAME] placeholder.
- Word targets: city pages 1,200-1,800 words (Colorado Springs 2,000+, Denver 2,000+), service/size pages 900-1,400, guides 1,200-2,200 (narrow questions 800+), region hubs 900-1,400. Length is a target, not filler. If you write shorter, say so in your report and why.

## Images (already generated or being generated — use ONLY these exact filenames)
Generic (in /assets/img/):
- `hero-driveway-dumpster.webp` — roll-off dumpster on a suburban driveway (GPS: Colorado Springs)
- `dumpster-driveway-boards.webp` — plywood boards under dumpster rails on a driveway
- `10-yard-dumpster.webp`, `15-yard-dumpster.webp`, `20-yard-dumpster.webp`, `30-yard-dumpster.webp`, `40-yard-dumpster.webp` — one per size
- `construction-debris-loading.webp`, `home-cleanout-dumpster.webp`, `roofing-debris-dumpster.webp`, `yard-waste-dumpster.webp`, `concrete-debris-dumpster.webp`, `demolition-debris-dumpster.webp`
- `dumpster-delivery-truck.webp`, `dumpster-street-permit.webp`
Tier 1 city images (geo-tagged with that city's GPS EXIF):
- `dumpster-rental-denver-co.webp`, `dumpster-rental-colorado-springs-co.webp`, `dumpster-rental-aurora-co.webp`, `dumpster-rental-boulder-co.webp`, `dumpster-rental-fort-collins-co.webp`, `dumpster-rental-pueblo-co.webp`, `dumpster-rental-greeley-co.webp`, `dumpster-rental-lakewood-co.webp`
Region images:
- `region-front-range.webp`, `region-denver-metro.webp`, `region-northern-colorado.webp`, `region-southern-colorado.webp`, `region-western-slope.webp`, `region-central-mountains.webp`
All WebP under 100KB, 1000x667. Alt text: unique per page, primary keyword once. Tier 2/3 city pages: use the most relevant generic image (size/service match) with a city-specific alt. Do NOT invent new image files. If an image file is missing when you write, still reference it by this exact name and note it in your report.

## Estimator markup (homepage + /guides/what-size-dumpster-do-i-need/ ONLY — copy verbatim)
```html
<form class="tool" id="estimator">
<h2>What size dumpster do you need?</h2>
<label for="est-job">What is the job?</label>
<select id="est-job">
<option value="garage">Garage, attic, or basement cleanout</option>
<option value="bathroom">Small bathroom remodel</option>
<option value="kitchen">Kitchen remodel</option>
<option value="cleanout">Multi-room or whole-house cleanout</option>
<option value="roofing">Roofing tear-off</option>
<option value="renovation">Major renovation</option>
<option value="construction">Construction or demolition</option>
<option value="demolition">Full demolition</option>
<option value="yard">Yard waste or landscaping</option>
<option value="concrete">Concrete, dirt, brick, or tile</option>
</select>
<label for="est-heavy">Is the debris heavy (concrete, dirt, brick, tile, shingles)?</label>
<select id="est-heavy"><option value="no">No, mostly light household or building waste</option><option value="yes">Yes, heavy material</option></select>
<p><button class="btn" type="submit">Find my size</button></p>
<div class="result-box" id="estimator-result" hidden></div>
</form>
```

## Booking wizard markup (/book-a-dumpster/ ONLY — copy verbatim; city select holds the 8 Tier 1 cities + "Another Colorado city")
```html
<form class="tool" id="booking-wizard">
<ol class="steps"><li class="active">1. Size</li><li>2. Dates</li><li>3. Address</li><li>4. Contact</li></ol>
<div class="step-panel active">
<h2>Step 1: pick your size</h2>
<div class="size-pick">
<button type="button" data-size="10">10-yard<br><small>small cleanout</small></button>
<button type="button" data-size="15">15-yard<br><small>mid cleanout</small></button>
<button type="button" data-size="20">20-yard<br><small>most popular</small></button>
<button type="button" data-size="30">30-yard<br><small>big renovation</small></button>
<button type="button" data-size="40">40-yard<br><small>demolition</small></button>
</div>
<input type="hidden" id="bk-size" value="">
<p><button class="btn" type="button" data-next>Continue</button></p>
</div>
<div class="step-panel">
<h2>Step 2: pick your dates</h2>
<label for="bk-date">Delivery date</label>
<input type="date" id="bk-date">
<label for="bk-days">Rental days</label>
<select id="bk-days"><option>7 days (standard)</option><option>3 days</option><option>10 days</option><option>14 days</option></select>
<p><button class="btn-ghost" type="button" data-prev>Back</button> <button class="btn" type="button" data-next>Continue</button></p>
</div>
<div class="step-panel">
<h2>Step 3: delivery address</h2>
<label for="bk-city">City</label>
<select id="bk-city">
<option value="">Choose your city</option>
<option>Colorado Springs</option><option>Denver</option><option>Aurora</option><option>Boulder</option><option>Fort Collins</option><option>Pueblo</option><option>Greeley</option><option>Lakewood</option><option>Another Colorado city</option>
</select>
<label for="bk-street">Street address</label>
<input type="text" id="bk-street" autocomplete="street-address" placeholder="Street and number">
<label for="bk-place">Where should the dumpster go?</label>
<select id="bk-place"><option>Driveway</option><option>Street (a city permit may be needed)</option><option>Jobsite</option><option>Other</option></select>
<p><button class="btn-ghost" type="button" data-prev>Back</button> <button class="btn" type="button" data-next>Continue</button></p>
</div>
<div class="step-panel">
<h2>Step 4: your details</h2>
<p id="booking-summary" class="notice">Your booking: size not picked yet.</p>
<label for="bk-name">Your name</label>
<input type="text" id="bk-name" autocomplete="name">
<label for="bk-phone">Phone number</label>
<input type="tel" id="bk-phone" autocomplete="tel" placeholder="(719) 555-0100">
<label for="bk-notes">Anything we should know? (optional)</label>
<textarea id="bk-notes" rows="3"></textarea>
<p><button class="btn-ghost" type="button" data-prev>Back</button> <button class="btn" type="submit">Request my booking</button></p>
<p>Prefer to talk? Call [PHONE]. No payment is taken on this page. We confirm your exact price before you pay.</p>
</div>
</form>
<div class="result-box" id="booking-done" hidden>
<h2>Booking request received</h2>
<p>Thank you. We will call you to confirm your size, dates, and exact price. If you need it faster, call [PHONE].</p>
</div>
```

## Geo meta tags (city pages only)
```
<meta name="geo.region" content="US-CO">
<meta name="geo.placename" content="[City], Colorado">
<meta name="geo.position" content="[lat];[lon]">
<meta name="ICBM" content="[lat], [lon]">
```
Tier 1 city coordinates (city center):
- Denver 39.7392, -104.9903 | Colorado Springs 38.8339, -104.8214 | Aurora 39.7294, -104.8319
- Boulder 40.0150, -105.2705 | Fort Collins 40.5853, -105.0844 | Pueblo 38.2544, -104.6091
- Greeley 40.4233, -104.7091 | Lakewood 39.7047, -105.0814
Tier 2/3: use the real city center coordinates — look them up (browser.search) if you do not know them. Never invent coordinates.

## JSON-LD (hand-write per page; validate mentally — no invented facts)
- Every page: BreadcrumbList (Home › Silo › Page).
- Homepage: Organization + WebSite (no SearchAction — no site search exists) + LocalBusiness (name "[BUSINESS NAME]", areaServed Colorado + top 8 cities, geo Colorado Springs, NO telephone/address fields until real values exist) + FAQPage.
- City page: LocalBusiness (geo = city coords, areaServed = city + county, NO street address, NO telephone) + Service + FAQPage + BreadcrumbList.
- Service page: Service (+ hasOfferCatalog listing the 5 sizes) + FAQPage + BreadcrumbList.
- Size page: Service (size, dimensions, weight limit) + FAQPage + BreadcrumbList.
- Guide page: Article (author "[BUSINESS NAME]", datePublished/dateModified "2026-11-13") + FAQPage + BreadcrumbList. HowTo ONLY on /guides/how-to-rent-a-dumpster/ (steps must match visible text).
- Estimator page (/dumpster-size-calculator/): WebApplication + FAQPage + BreadcrumbList. The tool must actually work (JS calculator), not be a dead form.
- Booking page: Service + BreadcrumbList only. About/contact/privacy/terms/faq: WebPage + BreadcrumbList (+ FAQPage on /faq/).
- Region hub: CollectionPage + BreadcrumbList + ItemList of its cities.
- Prices hub: FAQPage + BreadcrumbList (+ visible dated price table; no fake Offer markup, no firm prices in schema).

## Internal linking rules
- Homepage links to: prices hub, estimator, top 8 city pages, all 5 size pages, top 5 guides, booking, service areas. No city beyond Tier 1 is linked from the homepage.
- City page: UP to homepage, SIDEWAYS to 3-5 nearest built cities (same region first), DOWN to relevant size/service/guide pages (permits for THAT city, weight limits, driveway), booking. Never link to an unbuilt page.
- Region hub links to: all its cities, homepage, prices hub, estimator.
- Service/size page links to: top 8 city pages, related sizes (10↔15↔20↔30↔40), related services, prices hub, estimator, booking.
- Guide page links to: prices hub, relevant size pages, top 8 city pages, estimator, booking — every guide ends with a "Get a price / Book" block.
- Estimator links to: booking (with the chosen size pre-filled), size pages, prices hub.
- Every page must have at least 3 inbound links from other built pages — check your own links and report any page with fewer.
- Anchor text natural and varied. Primary keyword as anchor only once per target page from any one source page.
- No orphan pages: every page appears in the sitemap (the coordinator builds sitemap.xml at the end — list your pages in your report) + at least one contextual link.

## Price facts (ONLY these — always cite the source in the text; market ranges, never our prices)
- National: Dumpsters.com Oct 2026 averages — 10yd $586, 20yd $679, 30yd $809, 40yd $906; national range $286-$1,613.
- Denver: Dumpster Rental Dogs — 30yd $535-$635, 14 days, 3 tons. Mo's Hauling — 15yd $300/3-day, $365/7-day, $30/day, $70/ton overage. HBS Trash — 20yd $330-$500, 30yd $345-$550, 14 days + 3 tons included, $75/ton, $5/day.
- Colorado Springs: All American Dumpster — from $300 (10yd 3-day), 20yd $350, $25/day, $65/ton. Bin There Dump That — flat from $339. Dumpster Rental Dogs — 30yd $530-$585, 10yd $380-$480, 14 days, $85/ton, $15/day, ~$95 delivery fee.
- Fort Collins: Prime Dumpster 5-day — 10yd $399-$499 up to 40yd $699-$899. ZTERS — ~$600 10yd to ~$860 40yd, 10-day. Dumpsters.com — $465-$975, avg $689.
- Pueblo: Ultimate Dumpsters — $585-$1,300. Dumpsters.com — $470-$828, avg $652.
- Greeley: Ultimate Dumpsters — $450-$995. Dumpsters.com — $445-$1,081, avg $658.
- Boulder: Dumpsters.com — $445-$850, avg $635.
- Overage: typically $40-$100/ton (most common), up to $200/ton. Extensions: typically $10-$25/day. Rental period: standard 7-14 days, 7 most common.
- Always frame as "published market ranges" + source + date. Never as our price. Add: "Our exact price is confirmed when you book. [TO CONFIRM]"

## City data (Tier 1 — use only these facts; verify permit details before publishing)
- Denver — pop. 715,522. County: Denver. ZIPs: 80202, 80203, 80204, 80205, 80209, 80210, 80211, 80218, 80220, 80223, 80224, 80230, 80231, 80237, 80249. Areas: Downtown/LoDo, Capitol Hill, Highlands, Berkeley, Sloan's Lake, Sunnyside, Cherry Creek, Park Hill, Stapleton/Central Park, Wash Park, Highlands Ranch (nearby). Permit: Right-of-Way Revocable Street Occupancy Permit from Denver DOTI (303-446-3759), ~5 business days, ~$100 street permit. Landfill: Denver Arapahoe Disposal Site (DADS).
- Colorado Springs — pop. 478,961. County: El Paso. ZIPs: 80903, 80906, 80907, 80909, 80910, 80911, 80915, 80917, 80918, 80919, 80920, 80921, 80922, 80923, 80924, 80925, 80926, 80929. Areas: Downtown, Briargate, Broadmoor, Old Colorado City, Manitou Springs (nearby town), Fountain (nearby), Monument (nearby), Falcon, Security-Widefield, Powers corridor. Permit: Land Use Review revocable permit, City of Colorado Springs (719-385-5905). Landfill: Colorado Springs Landfill / Midway Landfill (Fountain area).
- Aurora — pop. 386,261. Counties: Arapahoe/Adams. ZIPs: 80010, 80011, 80012, 80013, 80014, 80015, 80016, 80017, 80018, 80019, 80040, 80041, 80042, 80045. Areas: Colfax corridor, Aurora Municipal Center, Southlands, Tallyn's Reach, Saddle Rock, Murphy Creek, Heather Gardens. Permit: universal rule + check with City of Aurora. Landfill: Denver Arapahoe Disposal Site (DADS) is the metro option.
- Boulder — pop. 104,175. County: Boulder. ZIPs: 80301, 80302, 80303, 80304, 80305, 80310. Areas: Downtown/Pearl Street, University Hill, Table Mesa, North Boulder, Gunbarrel, Whittier, Mapleton Hill. Permit: universal rule + check with City of Boulder. Facilities: Boulder County Recycling Center, 1901 63rd St; Eco-Cycle CHaRM, 6400 Arapahoe Rd. Angles: tight streets, CU student turnover, Table Mesa.
- Fort Collins — pop. 169,810. County: Larimer. ZIPs: 80521, 80524, 80525, 80526, 80528. Areas: Old Town, Harmony corridor, Midtown, Campus West, Fossil Creek, South Fort Collins. Permit: Permit to Obstruct $25, Engineering Dept, 281 N College Ave, (970) 221-6605. Facilities: Central Diversion and Transfer Station, 2388 W Trilby Rd; Larimer County North Landfill, Wellington (opened Aug 2026). Angles: CSU student turnover, covered-load rule.
- Pueblo — pop. 111,876. County: Pueblo. ZIPs: 81001, 81003, 81004, 81005, 81006, 81007, 81008, 81012. Areas: Downtown, Southside, Belmont, Bessemer, Hyde Park, Aberdeen. Permit: Pueblo Transportation Division for street placement. Facilities: Southside Landfill, ~6.3 mi from downtown. Angles: steel-mill and construction debris, historic districts.
- Greeley — pop. 108,795. County: Weld. ZIPs: 80631, 80632, 80633, 80634, 80638, 80639. Areas: Downtown, Glenmere, Cranford, Bittersweet, Kelly Farm, West Greeley. Permit: universal rule + check with City of Greeley. Facilities: WM Transfer Station ~2.3 mi; North Household Hazardous Waste Facility, 1311 N 17th Ave. Angles: UNC student turnover, Weld County agriculture and construction debris.
- Lakewood — pop. 155,984. County: Jefferson. ZIPs: 80214, 80215, 80226, 80227, 80228, 80232, 80235. Areas: Belmar, Green Mountain, Applewood, Bear Creek, Morse Park. Permit: universal rule + check with City of Lakewood.
- Tier 2/3 cities: research each city before writing (population, county, ZIPs, neighbourhoods, permit office, landfill/transfer station). Use browser.search. If a permit rule cannot be verified, write the universal rule + "check with [City] Public Works" and note it in your report. Never invent a permit fee, phone number, or landfill address.

## Size facts (use on size pages + estimator-adjacent copy)
- 10-yard: about 12-14 ft long x 8 ft wide x 3.5-4 ft high. About 3 pickup loads, 50-70 bags. 1-3 tons typical. Best: small cleanout, single room, small bathroom, one-layer roofing tear-off, heavy debris (concrete/dirt/brick) — lowboy by weight.
- 15-yard: about 16 ft long x 8 ft wide x 4 ft high. About 4-5 pickup loads, 80-100 bags. 1.5-3 tons typical. Best: mid-size cleanout, two-room remodel, flooring.
- 20-yard: about 22 ft long x 8 ft wide x 4-4.5 ft high. About 6 pickup loads, 110-130 bags. 2-4 tons typical. Most rented size. Best: kitchen remodel, multi-room cleanout, flooring, roofing.
- 30-yard: about 22 ft long x 8 ft wide x 6 ft high. About 9 pickup loads, 170-190 bags. 3-5 tons typical. Best: whole-house cleanout, major renovation, large construction. Wrong for heavy debris.
- 40-yard: about 22 ft long x 8 ft wide x 7-8 ft high. About 12 pickup loads, 230-250 bags. 4-6 tons typical. Best: major demolition, large construction, light bulky debris only. Never for heavy material.
- Delivery needs: 10.5 ft wide x 60 ft straight clearance, 25-30 ft vertical clearance.

## URL list (build exactly these — 114 pages)
Core (10): `/` index.html | `/book-a-dumpster/` | `/contact/` | `/about/` | `/reviews/` | `/service-areas/` | `/faq/` | `/dumpster-size-calculator/` | `/privacy-policy/` | `/terms-of-service/`
Prices hub (counts in core 10? NO — prices hub is a money page, part of the 10? Per plan: core/trust = 10 (homepage, booking, contact, about, reviews, service-areas, FAQ, estimator, privacy, terms) and prices hub is listed under service-adjacent; the plan total is 114 = 10 core + 15 service + 72 city + 6 region + 11 guides. The prices hub `/dumpster-rental-prices-colorado/` is an EXTRA money page — it is counted inside the 15 service? No. Reconcile: 10 + 15 + 72 + 6 + 11 = 114. The prices hub must be one of the 15 service pages? The plan §3 lists it as a top-level page. To keep 114 total, treat the prices hub as the 15th service-adjacent page: service list = 5 sizes + roll-off + residential + commercial + construction + roofing + demolition + yard waste + concrete + same-day + estate cleanout = 15, PLUS prices hub = 115? The plan says 114 total with the state-hub removed. Count carefully: core 10 (incl. estimator, booking) + service 15 + city 72 + region 6 + guides 11 = 114. Prices hub is NOT in that sum — it is the 115th page. The plan §4 lists it as a money page. BUILD IT ANYWAY: total becomes 115 pages. Report 115 in your final count and note the +1 (prices hub) explicitly. Do NOT drop any planned page to force 114.
Service (15): `/10-yard-dumpster-rental/` `/15-yard-dumpster-rental/` `/20-yard-dumpster-rental/` `/30-yard-dumpster-rental/` `/40-yard-dumpster-rental/` `/roll-off-dumpster-rental-colorado/` `/residential-dumpster-rental-colorado/` `/commercial-dumpster-rental-colorado/` `/construction-dumpster-rental-colorado/` `/roofing-dumpster-rental-colorado/` `/demolition-dumpster-rental-colorado/` `/yard-waste-dumpster-rental-colorado/` `/concrete-dumpster-rental-colorado/` `/same-day-dumpster-rental-colorado/` `/estate-cleanout-dumpster-rental-colorado/`
Money: `/dumpster-rental-prices-colorado/`
City Tier 1 (8): `/dumpster-rental-denver/` `/dumpster-rental-colorado-springs/` `/dumpster-rental-aurora-co/` `/dumpster-rental-boulder-co/` `/dumpster-rental-fort-collins/` `/dumpster-rental-pueblo/` `/dumpster-rental-greeley-co/` `/dumpster-rental-lakewood-co/`
City Tier 2 (24): `/dumpster-rental-thornton-co/` `/dumpster-rental-arvada-co/` `/dumpster-rental-westminster-co/` `/dumpster-rental-centennial-co/` `/dumpster-rental-longmont-co/` `/dumpster-rental-loveland-co/` `/dumpster-rental-broomfield-co/` `/dumpster-rental-castle-rock-co/` `/dumpster-rental-grand-junction-co/` `/dumpster-rental-commerce-city-co/` `/dumpster-rental-parker-co/` `/dumpster-rental-littleton-co/` `/dumpster-rental-northglenn-co/` `/dumpster-rental-brighton-co/` `/dumpster-rental-englewood-co/` `/dumpster-rental-wheat-ridge-co/` `/dumpster-rental-fountain-co/` `/dumpster-rental-windsor-co/` `/dumpster-rental-erie-co/` `/dumpster-rental-lafayette-co/` `/dumpster-rental-golden-co/` `/dumpster-rental-louisville-co/` `/dumpster-rental-monument-co/` `/dumpster-rental-superior-co/`
City Tier 3 (40): `/dumpster-rental-durango-co/` `/dumpster-rental-aspen-co/` `/dumpster-rental-vail-co/` `/dumpster-rental-steamboat-springs-co/` `/dumpster-rental-telluride-co/` `/dumpster-rental-cortez-co/` `/dumpster-rental-fruita-co/` `/dumpster-rental-montrose-co/` `/dumpster-rental-delta-co/` `/dumpster-rental-canon-city-co/` `/dumpster-rental-salida-co/` `/dumpster-rental-buena-vista-co/` `/dumpster-rental-leadville-co/` `/dumpster-rental-glenwood-springs-co/` `/dumpster-rental-rifle-co/` `/dumpster-rental-carbondale-co/` `/dumpster-rental-basalt-co/` `/dumpster-rental-crested-butte-co/` `/dumpster-rental-alamosa-co/` `/dumpster-rental-monte-vista-co/` `/dumpster-rental-la-junta-co/` `/dumpster-rental-lamar-co/` `/dumpster-rental-trinidad-co/` `/dumpster-rental-walsenburg-co/` `/dumpster-rental-sterling-co/` `/dumpster-rental-fort-morgan-co/` `/dumpster-rental-brush-co/` `/dumpster-rental-burlington-co/` `/dumpster-rental-limon-co/` `/dumpster-rental-woodland-park-co/` `/dumpster-rental-manitou-springs-co/` `/dumpster-rental-falcon-co/` `/dumpster-rental-peyton-co/` `/dumpster-rental-black-forest-co/` `/dumpster-rental-security-widefield-co/` `/dumpster-rental-palmer-lake-co/` `/dumpster-rental-larkspur-co/` `/dumpster-rental-calhan-co/` `/dumpster-rental-estes-park-co/` `/dumpster-rental-lyons-co/`
Region hubs (6): `/regions/front-range/` `/regions/denver-metro/` `/regions/northern-colorado/` `/regions/southern-colorado/` `/regions/western-slope/` `/regions/central-mountains/`
Guides (11): `/guides/dumpster-rental-cost/` `/guides/what-size-dumpster-do-i-need/` `/guides/dumpster-weight-limits/` `/guides/dumpster-rental-permits-colorado/` `/guides/what-can-go-in-a-dumpster/` `/guides/will-a-dumpster-damage-my-driveway/` `/guides/how-long-can-i-keep-a-dumpster/` `/guides/dumpster-vs-junk-removal/` `/guides/how-to-rent-a-dumpster/` `/guides/dumpster-rental-for-a-day/` `/guides/what-happens-if-you-overfill-a-dumpster/`
Region membership: Front Range = Denver, Aurora, Lakewood, Thornton, Arvada, Westminster, Centennial, Longmont, Broomfield, Castle Rock, Parker, Littleton, Northglenn, Brighton, Englewood, Wheat Ridge, Fountain, Windsor, Erie, Lafayette, Golden, Louisville, Monument, Superior, Colorado Springs, Boulder, Loveland. Denver Metro = Denver, Aurora, Lakewood, Thornton, Arvada, Westminster, Centennial, Littleton, Northglenn, Brighton, Englewood, Wheat Ridge, Golden, Louisville, Superior. Northern Colorado = Fort Collins, Greeley, Loveland, Windsor, Erie, Lafayette, Longmont, Estes Park, Lyons, Fort Morgan, Sterling, Brush. Southern Colorado = Colorado Springs, Pueblo, Fountain, Monument, Manitou Springs, Woodland Park, Falcon, Peyton, Black Forest, Security-Widefield, Palmer Lake, Larkspur, Calhan, Canon City, Salida, Buena Vista, Alamosa, Monte Vista, La Junta, Lamar, Trinidad, Walsenburg. Western Slope = Grand Junction, Durango, Montrose, Delta, Fruita, Cortez, Glenwood Springs, Rifle, Carbondale, Basalt, Aspen, Vail, Steamboat Springs, Telluride, Crested Butte, Leadville. Central Mountains = Leadville, Salida, Buena Vista, Aspen, Vail, Steamboat Springs, Telluride, Crested Butte, Woodland Park, Manitou Springs, Estes Park, Lyons, Glenwood Springs, Basalt, Carbondale. (Overlap is fine — a city can sit in two regions where geography fits; region pages link to city pages, city pages link to ONE primary region hub — their nearest — plus the homepage.)
