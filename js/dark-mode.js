// Bootstrap Native Dark Mode Toggle
document.addEventListener('DOMContentLoaded', function() {
  var toggle = document.getElementById('bgToggle');
  if (!toggle) return;

  // Restore from localStorage
  if (localStorage.getItem('dark-mode') === 'true') {
    document.documentElement.setAttribute('data-bs-theme', 'dark');
    toggle.classList.add('dark');
  }

  toggle.addEventListener('click', function() {
    var html = document.documentElement;
    var isDark = html.getAttribute('data-bs-theme') === 'dark';
    
    if (isDark) {
      html.setAttribute('data-bs-theme', 'light');
      toggle.classList.remove('dark');
    } else {
      html.setAttribute('data-bs-theme', 'dark');
      toggle.classList.add('dark');
    }
    
    localStorage.setItem('dark-mode', !isDark);
  });
});
