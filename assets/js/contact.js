/* Cairo School of Art & Calligraphy — contact form (WhatsApp hand-off, no backend yet) */
(function () {
  "use strict";
  var btn = document.getElementById("c-submit");
  if (!btn) return;

  btn.addEventListener("click", function () {
    var name = (document.getElementById("c-name").value || "").trim();
    var contact = (document.getElementById("c-contact").value || "").trim();
    var messageEl = document.getElementById("c-message");
    var message = (messageEl.value || "").trim();

    if (!message) {
      messageEl.focus();
      return;
    }

    var lines = [
      "Message from website contact form",
      name ? "Name: " + name : "",
      contact ? "Contact: " + contact : "",
      "",
      message
    ].filter(Boolean);

    var msg = encodeURIComponent(lines.join("\n"));
    window.open("https://wa.me/923393338224?text=" + msg, "_blank", "noopener");
  });
})();
