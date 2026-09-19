// Scroll to top/bottom buttons
document.addEventListener('DOMContentLoaded', function() {
  var btnTop = document.getElementById('scrollTopBtn');
  var btnBottom = document.getElementById('scrollBottomBtn');
  if (!btnTop || !btnBottom) return;

  btnTop.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  btnBottom.addEventListener('click', function() {
    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
  });
});
