  const progressBar = document.querySelector('.scroll-progress');
  if (progressBar) {
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      progressBar.style.width = progress + '%';
    });
  }
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) entry.target.classList.add('visible');
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
  document.querySelectorAll('.artwork, .year-break').forEach(el => observer.observe(el));
  const nav = document.querySelector('nav');
  const floatingBtns = document.querySelectorAll('.floating-btn');
  
  // Set initial floating button color to match nav (top of page = #222f3e)
  floatingBtns.forEach(btn => {
    btn.style.background = 'rgb(34, 47, 62)';
    btn.style.color = '#000';
  });
  
  if (nav) {
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (scrollTop / docHeight) : 0;
      
      // Interpolate from #222f3e (34, 47, 62) to #a02920 (160, 41, 32)
      const r = Math.round(34 + (160 - 34) * progress);
      const g = Math.round(47 + (41 - 47) * progress);
      const b = Math.round(62 + (32 - 62) * progress);
      
      const color = `rgb(${r}, ${g}, ${b})`;
      nav.style.background = color;
      
      // Sync floating button color with nav bar
      floatingBtns.forEach(btn => {
        btn.style.background = color;
        btn.style.color = progress > 0.5 ? '#fff' : '#000';
      });
    });
  }
  document.querySelectorAll('.artwork').forEach(el => {
    el.style.cursor = 'pointer';
    el.addEventListener('click', () => {
      const link = el.querySelector('a');
      if (link) window.location.href = link.href;
    });
  });
