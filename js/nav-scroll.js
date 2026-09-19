// Navbar scroll color gradient
document.addEventListener('DOMContentLoaded', function() {
  var nav = document.querySelector('.alp-nav');
  if (!nav) return;

  window.addEventListener('scroll', function() {
    var scrollY = window.scrollY;
    var docHeight = document.documentElement.scrollHeight - window.innerHeight;
    var scrollPercent = docHeight > 0 ? (scrollY / docHeight) : 0;

    var r = Math.round(34 + (160 - 34) * scrollPercent);
    var g = Math.round(47 + (41 - 47) * scrollPercent);
    var b = Math.round(62 + (32 - 62) * scrollPercent);
    var color = 'rgb(' + r + ', ' + g + ', ' + b + ')';

    nav.style.setProperty('background-color', color, 'important');
  });
});
