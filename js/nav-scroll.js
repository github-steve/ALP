// Navbar scroll color gradient
document.addEventListener('DOMContentLoaded', function() {
  var nav = document.querySelector('.alp-nav');
  if (!nav) return;

  function updateNavbar() {
    var scrollY = window.scrollY;
    var docHeight = document.documentElement.scrollHeight - window.innerHeight;
    var scrollPercent = docHeight > 0 ? (scrollY / docHeight) : 0;

    var isDark = document.documentElement.getAttribute('data-bs-theme') === 'dark';
    
    var r, g, b;
    if (isDark) {
      // Dark mode: coral → dark (reversed)
      r = Math.round(160 + (34 - 160) * scrollPercent);
      g = Math.round(41 + (47 - 41) * scrollPercent);
      b = Math.round(32 + (62 - 32) * scrollPercent);
    } else {
      // Light mode: dark → coral (normal)
      r = Math.round(34 + (160 - 34) * scrollPercent);
      g = Math.round(47 + (41 - 47) * scrollPercent);
      b = Math.round(62 + (32 - 62) * scrollPercent);
    }
    
    var color = 'rgb(' + r + ', ' + g + ', ' + b + ')';
    nav.style.setProperty('background-color', color, 'important');
  }

  // Update on scroll
  window.addEventListener('scroll', updateNavbar);
  
  // Update immediately on page load
  updateNavbar();
});
