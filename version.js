// ALP version indicator
(function () {
  var v = document.createElement('div');
  v.textContent = 'v2.7.88';
  v.style.cssText = 'text-align:center;font-size:0.7rem;color:#aaa;padding:0.25rem 0 0.75rem;';
  var footer = document.querySelector('footer');
  if (footer) {
    footer.appendChild(v);
  } else {
    document.body.appendChild(v);
  }
})();
