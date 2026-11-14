/* Dumpster Rental Colorado — main.js. Vanilla JS only. Estimator + booking wizard + mobile nav. */
(function () {
  "use strict";

  /* Mobile nav toggle */
  var header = document.querySelector(".site-header .wrap");
  var nav = document.querySelector(".main-nav");
  if (header && nav && !document.querySelector(".nav-toggle")) {
    var btn = document.createElement("button");
    btn.className = "nav-toggle";
    btn.type = "button";
    btn.setAttribute("aria-label", "Menu");
    btn.textContent = "Menu";
    var brand = header.querySelector(".brand");
    if (brand) brand.after(btn);
    btn.addEventListener("click", function () {
      nav.classList.toggle("open");
      document.querySelectorAll(".has-drop.open").forEach(function (o) {
        o.classList.remove("open");
        var b = o.querySelector(".drop-btn");
        if (b) b.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* Header dropdowns: click/tap toggle, outside click + Escape to close */
  document.querySelectorAll(".has-drop").forEach(function (wrap) {
    var btn = wrap.querySelector(".drop-btn");
    if (!btn) return;
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var wasOpen = wrap.classList.contains("open");
      document.querySelectorAll(".has-drop.open").forEach(function (o) {
        o.classList.remove("open");
        var b = o.querySelector(".drop-btn");
        if (b) b.setAttribute("aria-expanded", "false");
      });
      if (!wasOpen) {
        wrap.classList.add("open");
        btn.setAttribute("aria-expanded", "true");
      }
    });
  });
  function closeDrops() {
    document.querySelectorAll(".has-drop.open").forEach(function (o) {
      o.classList.remove("open");
      var b = o.querySelector(".drop-btn");
      if (b) b.setAttribute("aria-expanded", "false");
    });
  }
  document.addEventListener("click", closeDrops);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeDrops(); });

  /* Estimator: job + heavy debris -> size recommendation */
  var est = document.getElementById("estimator");
  if (est) {
    est.addEventListener("submit", function (e) {
      e.preventDefault();
      var job = document.getElementById("est-job").value;
      var heavy = document.getElementById("est-heavy").value;
      var out = document.getElementById("estimator-result");
      var size, why;
      if (heavy === "yes") {
        if (job === "concrete") { size = "10-yard"; why = "Heavy material fills the weight limit fast. A 10-yard dumpster holds the weight without going over."; }
        else { size = "10-yard or 20-yard"; why = "Heavy debris hits the weight limit before the box looks full. Pick a smaller box for heavy loads."; }
      } else if (job === "garage" || job === "bathroom") { size = "10-yard"; why = "A small cleanout or one bathroom fits in about 3 pickup loads."; }
      else if (job === "kitchen" || job === "cleanout" || job === "roofing" || job === "yard") { size = "20-yard"; why = "This is the most rented size. It holds about 6 pickup loads and fits most remodels and cleanouts."; }
      else if (job === "renovation" || job === "construction") { size = "30-yard"; why = "A big job needs about 9 pickup loads of space. A 30-yard box fits a major renovation."; }
      else { size = "40-yard"; why = "A full demolition or large build needs about 12 pickup loads. Go big, but only for light, bulky debris."; }
      out.innerHTML = "<h3>Your size: " + size + "</h3><p>" + why + "</p>" +
        "<p><a class=\"btn\" href=\"/book-a-dumpster/\">Book a " + size + " dumpster</a> " +
        "<a class=\"btn-ghost dark\" href=\"/" + size.replace("-yard", "-yard-dumpster-rental").replace("10-yard", "10-yard").replace(" ", "-").toLowerCase() + "/\">See " + size + " details</a></p>" +
        "<p>Your exact price is confirmed when you book. Prices shown on this site are published market ranges.</p>";
      out.hidden = false;
      out.scrollIntoView({ behavior: "smooth", block: "nearest" });
    });
  }

  /* Booking wizard: 4 steps, client-side only, no payment, no backend */
  var wiz = document.getElementById("booking-wizard");
  if (wiz) {
    var panels = wiz.querySelectorAll(".step-panel");
    var steps = wiz.querySelectorAll(".steps li");
    var current = 0;
    var sizeInput = document.getElementById("bk-size");
    var summary = document.getElementById("booking-summary");
    function show(i) {
      panels.forEach(function (p, k) { p.classList.toggle("active", k === i); });
      steps.forEach(function (s, k) { s.classList.toggle("active", k <= i); });
      current = i;
      updateSummary();
      window.scrollTo({ top: wiz.offsetTop - 80, behavior: "smooth" });
    }
    function updateSummary() {
      var size = sizeInput.value || "not picked yet";
      var city = (document.getElementById("bk-city") || {}).value || "";
      var date = (document.getElementById("bk-date") || {}).value || "";
      var days = (document.getElementById("bk-days") || {}).value || "7 days (standard)";
      summary.textContent = "Your booking: " + size + "-yard dumpster" +
        (city ? " in " + city : "") + (date ? ", delivery " + date : "") + ", " + days + ".";
    }
    wiz.querySelectorAll(".size-pick button").forEach(function (b) {
      b.addEventListener("click", function () {
        wiz.querySelectorAll(".size-pick button").forEach(function (x) { x.classList.remove("selected"); });
        b.classList.add("selected");
        sizeInput.value = b.getAttribute("data-size");
        updateSummary();
      });
    });
    wiz.querySelectorAll("[data-next]").forEach(function (b) {
      b.addEventListener("click", function () {
        if (current === 0 && !sizeInput.value) { alert("Please pick a size first."); return; }
        if (current < panels.length - 1) show(current + 1);
      });
    });
    wiz.querySelectorAll("[data-prev]").forEach(function (b) {
      b.addEventListener("click", function () { if (current > 0) show(current - 1); });
    });
    ["bk-city", "bk-date", "bk-days"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.addEventListener("change", updateSummary);
    });
    wiz.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = (document.getElementById("bk-name") || {}).value || "";
      var phone = (document.getElementById("bk-phone") || {}).value || "";
      if (!sizeInput.value) { alert("Please pick a size first."); show(0); return; }
      if (!name.trim() || !phone.trim()) { alert("Please add your name and phone number so we can confirm your booking."); return; }
      wiz.hidden = true;
      var done = document.getElementById("booking-done");
      if (done) {
        done.hidden = false;
        done.scrollIntoView({ behavior: "smooth" });
      }
    });
    updateSummary();
  }

  /* Footer year */
  var year = new Date().getFullYear();
  document.querySelectorAll(".site-footer p").forEach(function (p) {
    if (p.textContent.indexOf("© 2026") === 0 && year !== 2026) {
      p.textContent = p.textContent.replace("© 2026", "© " + year);
    }
  });
})();
