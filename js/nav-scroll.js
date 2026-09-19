// Navbar scroll color gradient
document.addEventListener('DOMContentLoaded', function() {
  var nav = document.querySelector('.alp-nav');
  if (!nav) return;

  window.addEventListener('scroll', function() {
    var scrollY = window.scrollY;
    var docHeight = document.documentElement.scrollHeight - window.innerHeight;
    var scrollPercent = docHeight > 0 ? (scrollY / docHeight) : 0;

    // Gradient from dark (#222f3e) to coral (#a02920)
    var r = Math.round(34 + (160 - 34) * scrollPercent);
    var g = Math.round(47 + (41 - 47) * scrollPercent);
    var b = Math.round(62 + (32 - 62) * scrollPercent);
    var color = `rgb(${r}, ${g}, ${b})`;

    nav.style.setProperty('background-color', color, 'important');

    // Update "The Paintings" text
    var heading = document.querySelector('.artist-statement h1');
    if (heading) heading.style.color = color;

    // Update year headings and their underline
    document.querySelectorAll('.year-section h2').forEach(function(h2) {
      h2.style.color = color;
      h2.style.setProperty('--underline-color', color);
    });
  });
});
