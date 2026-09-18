// ALP Shared Nav - Bootstrap 5 navbar injected into every page
$(document).ready(function() {
  var path = window.location.pathname;
  var page = path.split("/").pop() || "index.html";
  
  // Active state helpers
  var isHome = page === "index.html";
  var isPaintings = page.indexOf("paintings") !== -1;
  var isStudies = page.indexOf("small-original") !== -1;
  var isAbout = page.indexOf("about") !== -1;
  var isStore = page.indexOf("store") !== -1;
  
  var navHtml = 
    '<nav class="navbar navbar-expand-lg fixed-top" data-bs-theme="dark" style="background-color: #222f3e !important; padding: 1.25rem 0; margin: 0; border: none; border-radius: 0; box-shadow: none;">' +
      '<div class="container-fluid px-3">' +
        '<a class="navbar-brand" href="/ALP/index.html" style="font-size: 1.6rem; font-weight: 500; color: #fff; text-decoration: none; letter-spacing: 0.05em; display: inline-flex; align-items: center; gap: 0.25rem;">' +
          '<strong style="font-weight: 700;">MANDY BUDAN</strong> ' +
          '<span style="font-weight: 400;">Abstract Landscapes</span>' +
        '</a>' +
        '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#alpNavbar" aria-controls="alpNavbar" aria-expanded="false" aria-label="Toggle navigation" style="border-color: rgba(255,255,255,0.3);">' +
          '<span class="navbar-toggler-icon"></span>' +
        '</button>' +
        '<div class="collapse navbar-collapse" id="alpNavbar">' +
          '<ul class="navbar-nav ms-auto" style="gap: 0;">' +
            '<li class="nav-item"><a class="nav-link' + (isHome ? ' active' : '') + '" aria-current="' + (isHome ? 'page' : 'false') + '" href="/ALP/index.html" style="color:' + (isHome ? '#FFDD00' : 'rgba(255,255,255,0.8)') + '; font-size: 0.85rem; font-weight: 400; letter-spacing: 0.05em; text-transform: uppercase; padding: 0.5rem 1rem; transition: color 0.2s; text-decoration: none;">Home</a></li>' +
            '<li class="nav-item"><a class="nav-link' + (isPaintings ? ' active' : '') + '" aria-current="' + (isPaintings ? 'page' : 'false') + '" href="/ALP/mandy-budan-paintings.html" style="color:' + (isPaintings ? '#FFDD00' : 'rgba(255,255,255,0.8)') + '; font-size: 0.85rem; font-weight: 400; letter-spacing: 0.05em; text-transform: uppercase; padding: 0.5rem 1rem; transition: color 0.2s; text-decoration: none;">Paintings</a></li>' +
            '<li class="nav-item"><a class="nav-link' + (isStudies ? ' active' : '') + '" aria-current="' + (isStudies ? 'page' : 'false') + '" href="/ALP/mandy-budan-small-original-paintings.html" style="color:' + (isStudies ? '#FFDD00' : 'rgba(255,255,255,0.8)') + '; font-size: 0.85rem; font-weight: 400; letter-spacing: 0.05em; text-transform: uppercase; padding: 0.5rem 1rem; transition: color 0.2s; text-decoration: none;">Studies</a></li>' +
            '<li class="nav-item"><a class="nav-link' + (isAbout ? ' active' : '') + '" aria-current="' + (isAbout ? 'page' : 'false') + '" href="/ALP/mandy-budan-about.html" style="color:' + (isAbout ? '#FFDD00' : 'rgba(255,255,255,0.8)') + '; font-size: 0.85rem; font-weight: 400; letter-spacing: 0.05em; text-transform: uppercase; padding: 0.5rem 1rem; transition: color 0.2s; text-decoration: none;">About</a></li>' +
            '<li class="nav-item"><a class="nav-link' + (isStore ? ' active' : '') + '" aria-current="' + (isStore ? 'page' : 'false') + '" href="/ALP/mandy-budan-store.html" style="color:' + (isStore ? '#FFDD00' : 'rgba(255,255,255,0.8)') + '; font-size: 0.85rem; font-weight: 400; letter-spacing: 0.05em; text-transform: uppercase; padding: 0.5rem 1rem; transition: color 0.2s; text-decoration: none;">SHOP</a></li>' +
          '</ul>' +
        '</div>' +
      '</div>' +
    '</nav>';
  
  // Inject into body
  $("body").prepend(navHtml);
  
  // Add padding-top to body so content isn't hidden behind fixed navbar
  // Height = padding (1.25rem * 2) + line-height + border
  $("body").css("padding-top", "80px");
  
  // Remove margin-top from hero/main to eliminate gap
  $("main, .hero").css("margin-top", "0");
});
