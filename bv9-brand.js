(() => {
  const style = document.createElement('style');
  style.textContent = `
    /* Fixed, larger BV-9 in the top-left corner */
    .bv9-brand { position: fixed; top: 18px; left: 22px; z-index: 9999; display: inline-flex; align-items: center; gap: .28rem; height: auto; color: #fff; font: 900 clamp(2.6rem, 6.5vw, 5.2rem)/1 'Afacad Flux', Arial, sans-serif; letter-spacing: .03em; text-decoration: none; padding: .18rem .5rem; background: linear-gradient(180deg, rgba(0,0,0,0.08), rgba(0,0,0,0)); border-radius: .36rem; }
    .bv9-brand span { background: linear-gradient(115deg, #7e1f9f 5%, #c12d70 95%); -webkit-background-clip: text; background-clip: text; color: transparent; display: inline-block; }
    .bv9-brand { text-shadow: 0 10px 30px rgba(124,29,158,0.28), 0 0 20px rgba(193,45,112,0.18); }
    .bv9-brand.glow { animation: bv9-pulse 3.6s ease-in-out infinite; }
    @keyframes bv9-pulse { 0% { filter: drop-shadow(0 0 8px rgba(193,45,112,0.20)); transform: scale(1); } 50% { filter: drop-shadow(0 0 22px rgba(124,29,158,0.30)); transform: scale(1.03); } 100% { filter: drop-shadow(0 0 8px rgba(193,45,112,0.20)); transform: scale(1); } }
    .bv9-brand::after { content: ''; width: .44rem; height: .44rem; margin-left: .22rem; border-radius: 50%; background: #e8c96a; box-shadow: 0 0 12px #e8c96a; }
    @media (max-width: 760px) { .bv9-brand { top: 12px; left: 12px; font-size: clamp(1.8rem, 6.5vw, 3.2rem); padding: .12rem .4rem; } }
  `;
  document.head.append(style);

  function replaceBrand() {
    document.querySelectorAll('img[alt="Navisights"]').forEach((image) => {
      if (image.dataset.bv9Replaced) return;
      const brand = document.createElement(image.closest('a') ? 'span' : 'div');
      brand.className = 'bv9-brand glow';
      brand.setAttribute('aria-label', 'BV-9');
      brand.innerHTML = '<span>BV-9</span>';
      image.dataset.bv9Replaced = 'true';
      image.replaceWith(brand);
    });
  }

  // Remove unwanted navigation links by visible text
  const navToRemove = new Set(['Services', 'About', 'Achievements']);
  function removeNavLinks() {
    // Find anchors and remove those whose visible text matches any target
    document.querySelectorAll('a, nav a, header a').forEach((a) => {
      const text = (a.textContent || '').trim();
      if (navToRemove.has(text)) {
        // If wrapped in a list item, remove that for cleaner DOM
        const li = a.closest('li');
        if (li) li.remove(); else a.remove();
      }
    });
  }

  // Replace textual occurrences like "nexgentrike" / "NexGenTrike" / variants with "BV-9"
  const replaceRegex = /\b(nex\s*-?gen\s*-?trike|nexgentrike|nextgentrike|next\s*gen\s*trike)\b/ig;
  function replaceTextNodes(root = document.body) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(node => {
      if (!node.nodeValue) return;
      const newVal = node.nodeValue.replace(replaceRegex, 'BV-9');
      if (newVal !== node.nodeValue) node.nodeValue = newVal;
    });
  }

  // Fallback missing images for institutions and testimonials
  const fallbackMap = { institutions: '/logo.png', testimonials: '/moto.png' };
  function fixMissingImages() {
    document.querySelectorAll('img').forEach(img => {
      const src = img.getAttribute('src') || '';
      const m = src.match(/^\/(institutions|testimonials)\//i);
      if (m) {
        const folder = m[1].toLowerCase();
        if (!img.dataset.bv9FallbackSet) {
          img.addEventListener('error', () => {
            const fallback = fallbackMap[folder] || '/logo.png';
            if (img.src !== location.origin + fallback && img.src !== fallback) {
              img.src = fallback;
            }
            img.dataset.bv9FallbackSet = 'true';
          }, { once: true });
          // In case server already returns 404, reassigning src to itself will trigger error handler in some browsers
          // but to be safe, if img.complete and naturalWidth == 0, trigger fallback now
          setTimeout(() => {
            try {
              if (img.complete && img.naturalWidth === 0) {
                const fallback = fallbackMap[folder] || '/logo.png';
                img.src = fallback;
                img.dataset.bv9FallbackSet = 'true';
              }
            } catch (e) {
              // ignore
            }
          }, 100);
        }
      }
    });
  }

  function runAll() {
    replaceBrand();
    removeNavLinks();
    replaceTextNodes();
    fixMissingImages();
  }

  const observer = new MutationObserver((mutations) => {
    // Run targeted updates when DOM changes so dynamic navs/components are handled
    runAll();
  });
  observer.observe(document.documentElement, { childList: true, subtree: true });

  // Initial pass
  runAll();
})();
