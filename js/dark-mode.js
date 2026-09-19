// Dark Mode Toggle
document.addEventListener('DOMContentLoaded', function() {
  var toggle = document.getElementById('bgToggle');
  if (!toggle) return;

  // Restore dark mode state from localStorage
  if (localStorage.getItem('dark-mode') === 'true') {
    document.documentElement.classList.add('dark-mode');
    toggle.classList.add('dark');
  }

  toggle.addEventListener('click', function() {
    var html = document.documentElement;
    html.classList.toggle('dark-mode');
    toggle.classList.toggle('dark');
    localStorage.setItem('dark-mode', html.classList.contains('dark-mode'));
  });
});
