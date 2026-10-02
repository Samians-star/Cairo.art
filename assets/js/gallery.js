/* Cairo School of Art & Calligraphy — category filter tabs (Gallery / Workshops) */
(function () {
  "use strict";
  var tabs = document.querySelectorAll(".filter-tab");
  var items = document.querySelectorAll("[data-category]");
  if (!tabs.length) return;

  tabs.forEach(function (tab) {
    tab.addEventListener("click", function () {
      tabs.forEach(function (t) { t.classList.remove("is-active"); });
      tab.classList.add("is-active");
      var cat = tab.dataset.filter;
      items.forEach(function (item) {
        var show = cat === "all" || item.dataset.category === cat;
        item.style.display = show ? "" : "none";
      });
    });
  });
})();
