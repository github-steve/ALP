// ALP Shared Nav - injected into every page
$(document).ready(function() {
  // Determine current page for active state
  var path = window.location.pathname;
  var page = path.split("/").pop() || "index.html";
  
  // Build nav HTML
  var navHtml = 
    '<nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">' +
      '<div class="container-fluid px-3">' +
        '<a class="navbar-brand" href="/ALP/index.html"><strong>MANDY BUDAN</strong> <span class="fw-normal">Abstract Landscapes</span></a>' +
        '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">' +
          '<span class="navbar-toggler-icon"></span>' +
        '</button>' +
        '<div class="collapse navbar-collapse" id="navbarNav">' +
          '<ul class="navbar-nav ms-auto">' +
            '<li class="nav-item"><a class="nav-link' + (page === "index.html" ? " active" : "") + '" href="/ALP/index.html">Home</a></li>' +
            '<li class="nav-item"><a class="nav-link' + (page.indexOf("paintings") !== -1 ? " active" : "") + '" href="/ALP/mandy-budan-paintings.html">Paintings</a></li>' +
            '<li class="nav-item"><a class="nav-link' + (page.indexOf("small-original") !== -1 ? " active" : "") + '" href="/ALP/mandy-budan-small-original-paintings.html">Studies</a></li>' +
            '<li class="nav-item"><a class="nav-link' + (page.indexOf("about") !== -1 ? " active" : "") + '" href="/ALP/mandy-budan-about.html">About</a></li>' +
            '<li class="nav-item"><a class="nav-link' + (page.indexOf("store") !== -1 ? " active" : "") + '" href="/ALP/mandy-budan-store.html">SHOP</a></li>' +
          '</ul>' +
        '</div>' +
      '</div>' +
    '</nav>';
  
  // Inject into body
  $("body").prepend(navHtml);
});
