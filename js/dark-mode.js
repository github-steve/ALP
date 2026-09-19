// Dark Mode Toggle
document.addEventListener('DOMContentLoaded', function() {
  var toggle = document.getElementById('bgToggle');
  if (!toggle) return;

  toggle.addEventListener('click', function() {
    var html = document.documentElement;
    html.classList.toggle('dark-mode');
    toggle.classList.toggle('dark');
  });
});
