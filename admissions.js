/* Cairo School of Art & Calligraphy — admissions form (client-side only, no backend yet) */
(function () {
  "use strict";
  var form = document.getElementById("admission-form");
  if (!form) return;

  var steps = Array.prototype.slice.call(form.querySelectorAll(".form-step"));
  var progressItems = Array.prototype.slice.call(document.querySelectorAll(".progress-steps__item"));
  var total = steps.length;
  var current = 1;

  var btnBack = document.getElementById("btn-back");
  var btnNext = document.getElementById("btn-next");
  var btnSubmit = document.getElementById("btn-submit");

  function fieldsInStep(n) {
    var el = document.querySelector('.form-step[data-step="' + n + '"]');
    return el ? Array.prototype.slice.call(el.querySelectorAll("[data-field]")) : [];
  }

  function getFieldValue(el) {
    if (el.type === "checkbox") return el.checked ? "Yes" : "";
    if (el.tagName === "SELECT") {
      if (!el.value) return "";
      var opt = el.options[el.selectedIndex];
      return opt ? opt.text : el.value;
    }
    return el.value ? el.value.trim() : "";
  }

  function validateStep(n) {
    var ok = true;
    fieldsInStep(n).forEach(function (el) {
      var group = el.closest(".form-group") || el.closest(".form-check");
      if (el.hasAttribute("required")) {
        var filled = el.type === "checkbox" ? el.checked : el.value.trim() !== "";
        if (!filled) {
          ok = false;
          if (group) group.classList.add("has-error");
        } else if (group) {
          group.classList.remove("has-error");
        }
      }
    });
    return ok;
  }

  function showStep(n) {
    steps.forEach(function (s) {
      s.classList.toggle("is-active", Number(s.dataset.step) === n);
    });
    progressItems.forEach(function (p) {
      var i = Number(p.dataset.n);
      p.classList.toggle("is-active", i === n);
      p.classList.toggle("is-done", i < n);
    });
    btnBack.style.display = n === 1 || n === 7 ? "none" : "inline-flex";
    btnNext.style.display = n <= 5 ? "inline-flex" : "none";
    btnSubmit.style.display = n === 6 ? "inline-flex" : "none";
    if (n === 6) buildReview();
    window.scrollTo({ top: form.offsetTop - 110, behavior: "smooth" });
  }

  function buildReview() {
    var out = document.getElementById("review-output");
    if (!out) return;
    var groups = { 1: "Personal Information", 2: "Education", 3: "Course Selection", 5: "Additional Information" };
    var html = "";
    Object.keys(groups).forEach(function (stepNo) {
      var els = fieldsInStep(stepNo);
      if (!els.length) return;
      html += '<div class="review-block"><h4>' + groups[stepNo] + "</h4><dl>";
      els.forEach(function (el) {
        var val = getFieldValue(el);
        html += '<div class="review-row"><dt>' + el.dataset.field + "</dt><dd>" + (val || "&mdash;") + "</dd></div>";
      });
      html += "</dl></div>";
    });
    out.innerHTML = html;
  }

  btnNext.addEventListener("click", function () {
    if (!validateStep(current)) return;
    current = Math.min(current + 1, total);
    showStep(current);
  });
  btnBack.addEventListener("click", function () {
    current = Math.max(current - 1, 1);
    showStep(current);
  });
  btnSubmit.addEventListener("click", function () {
    if (!validateStep(6)) return;
    current = 7;
    showStep(current);
    finalizeSubmission();
  });

  var courseSel = document.getElementById("f-course");
  var durationSel = document.getElementById("f-duration");
  var feePreview = document.getElementById("fee-preview");

  function coursesData() {
    return typeof CSA_COURSES !== "undefined" ? CSA_COURSES : [];
  }

  if (courseSel) {
    courseSel.addEventListener("change", function () {
      var c = coursesData().filter(function (x) { return x.slug === courseSel.value; })[0];
      durationSel.innerHTML = '<option value="">Select duration</option>';
      feePreview.textContent = "";
      if (!c) return;
      Object.keys(c.pricing).forEach(function (d) {
        var fee = c.pricing[d];
        var opt = document.createElement("option");
        opt.value = d;
        opt.textContent = d + (fee != null ? " — PKR " + fee.toLocaleString() : " — Fee TBD");
        durationSel.appendChild(opt);
      });
    });
    durationSel.addEventListener("change", function () {
      var c = coursesData().filter(function (x) { return x.slug === courseSel.value; })[0];
      if (!c) { feePreview.textContent = ""; return; }
      var fee = c.pricing[durationSel.value];
      feePreview.textContent = fee != null
        ? "Fee: PKR " + fee.toLocaleString() + " (" + durationSel.value + ")"
        : "Fee to be confirmed by our team.";
    });
  }

  function refCode() {
    var d = new Date();
    var pad = function (n) { return String(n).padStart(2, "0"); };
    return "CSA-REF-" + d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate()) + "-" + Math.floor(1000 + Math.random() * 9000);
  }

  function finalizeSubmission() {
    var ref = refCode();
    var refEl = document.getElementById("ref-code");
    if (refEl) refEl.textContent = ref;

    var lines = ["New Admission Enquiry — Cairo School of Art & Calligraphy", "Reference: " + ref, ""];
    [1, 2, 3, 5].forEach(function (stepNo) {
      fieldsInStep(stepNo).forEach(function (el) {
        var val = getFieldValue(el);
        if (val) lines.push(el.dataset.field + ": " + val);
      });
    });
    var msg = encodeURIComponent(lines.join("\n"));
    var waBtn = document.getElementById("btn-whatsapp");
    if (waBtn) waBtn.href = "https://wa.me/923393338224?text=" + msg;
  }

  var printBtn = document.getElementById("btn-print");
  if (printBtn) printBtn.addEventListener("click", function () { window.print(); });

  showStep(1);
})();
