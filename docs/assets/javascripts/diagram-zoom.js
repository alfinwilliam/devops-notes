/*
 * Click (or press Enter on) a diagram to open it full screen, with zoom.
 *
 * Material for MkDocs renders each Mermaid diagram inside a closed shadow root, so the
 * drawn SVG cannot be reached from here. Instead, this script records every diagram's
 * source text before the theme replaces it, and renders a fresh copy in the viewer with
 * the same global `mermaid` object and theme settings the page already uses.
 *
 * Plain JavaScript, no dependencies. Loaded through extra_javascript in mkdocs.yml.
 */
(function () {
  "use strict";

  // 1. Record the source of every diagram, in page order, before the theme renders them.
  var sources = [];
  document.querySelectorAll("pre.mermaid").forEach(function (pre, i) {
    pre.setAttribute("data-diagram", String(i));
    sources.push(pre.textContent);
  });
  if (!sources.length) return;

  // 2. When the theme swaps a <pre> for its rendered <div class="mermaid">, mark the new element.
  function decorate(host, index) {
    host.setAttribute("data-diagram", index);
    host.setAttribute("tabindex", "0");
    host.setAttribute("role", "button");
    host.setAttribute("aria-label", "Enlarge diagram");
    host.setAttribute("title", "Click to enlarge");
    host.classList.add("diagram-zoomable");
    var hint = document.createElement("p");
    hint.className = "diagram-hint";
    hint.textContent = "Click the diagram to enlarge it.";
    host.insertAdjacentElement("afterend", hint);
  }

  new MutationObserver(function (records) {
    records.forEach(function (record) {
      var removed = null;
      record.removedNodes.forEach(function (n) {
        if (n.nodeType === 1 && n.hasAttribute("data-diagram")) removed = n;
      });
      if (!removed) return;
      record.addedNodes.forEach(function (n) {
        if (n.nodeType === 1 && n.classList.contains("mermaid") && !n.hasAttribute("data-diagram")) {
          decorate(n, removed.getAttribute("data-diagram"));
        }
      });
    });
  }).observe(document.body, { childList: true, subtree: true });

  // 3. The viewer.
  var overlay, stage, svg, scale = 1, natural = { w: 0, h: 0 }, lastFocus = null, renders = 0;
  var drag = null, moved = false;

  function build() {
    overlay = document.createElement("div");
    overlay.className = "diagram-overlay";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", "Enlarged diagram");
    overlay.innerHTML =
      '<div class="diagram-toolbar">' +
      '<button type="button" data-act="out" aria-label="Zoom out">&minus;</button>' +
      '<button type="button" data-act="fit">Fit</button>' +
      '<button type="button" data-act="in" aria-label="Zoom in">+</button>' +
      '<span class="diagram-help">Esc closes. + and &minus; zoom, 0 fits. Drag to move, Ctrl and scroll to zoom.</span>' +
      '<button type="button" data-act="close" class="diagram-close">Close</button>' +
      "</div>" +
      '<div class="diagram-stage"></div>';
    stage = overlay.querySelector(".diagram-stage");

    overlay.addEventListener("click", function (e) {
      var button = e.target.closest("button");
      if (button) {
        var act = button.getAttribute("data-act");
        if (act === "in") zoom(1.25);
        else if (act === "out") zoom(0.8);
        else if (act === "fit") fit();
        else if (act === "close") close();
        return;
      }
      if (e.target === stage && !moved) close(); // a click on the empty background closes
    });

    stage.addEventListener("wheel", function (e) {
      if (!e.ctrlKey) return;
      e.preventDefault();
      zoom(e.deltaY < 0 ? 1.1 : 0.9);
    }, { passive: false });

    stage.addEventListener("pointerdown", function (e) {
      if (e.button !== 0) return;
      drag = { x: e.clientX, y: e.clientY, left: stage.scrollLeft, top: stage.scrollTop };
      moved = false;
      stage.classList.add("is-dragging");
    });
    window.addEventListener("pointermove", function (e) {
      if (!drag) return;
      var dx = e.clientX - drag.x, dy = e.clientY - drag.y;
      if (Math.abs(dx) + Math.abs(dy) > 4) moved = true;
      stage.scrollLeft = drag.left - dx;
      stage.scrollTop = drag.top - dy;
    });
    window.addEventListener("pointerup", function () {
      drag = null;
      if (stage) stage.classList.remove("is-dragging");
    });

    document.body.appendChild(overlay);
  }

  function setScale(s) {
    scale = Math.min(Math.max(s, 0.2), 10);
    svg.style.width = Math.round(natural.w * scale) + "px";
    svg.style.height = Math.round(natural.h * scale) + "px";
  }

  // Fill the screen width. A tall diagram is fitted to the screen height instead, unless that would shrink it.
  function fit() {
    if (!svg) return;
    var w = stage.clientWidth - 32, h = stage.clientHeight - 32;
    var s = w / natural.w;
    if (natural.h > natural.w && natural.h * s > h) s = Math.max(h / natural.h, Math.min(1, s));
    setScale(s);
    stage.scrollLeft = 0;
    stage.scrollTop = 0;
  }

  // Zoom around the centre of what is currently visible.
  function zoom(factor) {
    if (!svg) return;
    var cx = (stage.scrollLeft + stage.clientWidth / 2) / stage.scrollWidth;
    var cy = (stage.scrollTop + stage.clientHeight / 2) / stage.scrollHeight;
    setScale(scale * factor);
    stage.scrollLeft = cx * stage.scrollWidth - stage.clientWidth / 2;
    stage.scrollTop = cy * stage.scrollHeight - stage.clientHeight / 2;
  }

  function open(index) {
    if (typeof window.mermaid === "undefined" || !sources[index]) return;
    if (!overlay) build();
    lastFocus = document.activeElement;
    stage.innerHTML = "";
    svg = null;
    overlay.classList.add("is-open");
    document.documentElement.classList.add("diagram-overlay-open");
    window.mermaid.render("diagram_zoom_" + renders++, sources[index]).then(function (out) {
      stage.innerHTML = out.svg;
      svg = stage.querySelector("svg");
      var vb = svg.viewBox && svg.viewBox.baseVal;
      var box = svg.getBoundingClientRect();
      natural.w = vb && vb.width ? vb.width : box.width;
      natural.h = vb && vb.height ? vb.height : box.height;
      svg.removeAttribute("width");
      svg.removeAttribute("height");
      svg.style.maxWidth = "none";
      fit();
      overlay.querySelector('[data-act="close"]').focus();
    });
  }

  function close() {
    overlay.classList.remove("is-open");
    document.documentElement.classList.remove("diagram-overlay-open");
    stage.innerHTML = "";
    svg = null;
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  // 4. Open on click or Enter; keyboard controls while open.
  document.addEventListener("click", function (e) {
    var host = e.target.closest && e.target.closest(".diagram-zoomable");
    if (host) open(Number(host.getAttribute("data-diagram")));
  });

  document.addEventListener("keydown", function (e) {
    if (overlay && overlay.classList.contains("is-open")) {
      if (e.key === "Escape") close();
      else if (e.key === "+" || e.key === "=") zoom(1.25);
      else if (e.key === "-") zoom(0.8);
      else if (e.key === "0") fit();
      else return;
      e.preventDefault();
      e.stopPropagation();
      return;
    }
    var host = e.target.closest && e.target.closest(".diagram-zoomable");
    if (host && (e.key === "Enter" || e.key === " ")) {
      e.preventDefault();
      open(Number(host.getAttribute("data-diagram")));
    }
  }, true);
})();
