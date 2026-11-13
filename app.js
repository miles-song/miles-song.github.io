const sections = [...document.querySelectorAll('main > section[id]')];
const navigation = [...document.querySelectorAll('.section-link')];
let activeSection = '';
let scrollFrame = 0;

function updateSection() {
  scrollFrame = 0;
  const threshold = window.matchMedia('(max-width: 900px)').matches ? 160 : 180;
  let current = sections[0];
  for (const section of sections) {
    if (section.getBoundingClientRect().top <= threshold) current = section;
  }
  if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 4) current = sections.at(-1);
  if (current.id === activeSection) return;
  activeSection = current.id;
  for (const link of navigation) {
    if (link.hash === `#${activeSection}`) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
}

function scheduleSectionUpdate() {
  if (!scrollFrame) scrollFrame = window.requestAnimationFrame(updateSection);
}

window.addEventListener('scroll', scheduleSectionUpdate, { passive: true });
window.addEventListener('resize', scheduleSectionUpdate);
window.addEventListener('hashchange', scheduleSectionUpdate);
window.addEventListener('pageshow', scheduleSectionUpdate);
new ResizeObserver(scheduleSectionUpdate).observe(document.querySelector('main'));
document.fonts.ready.then(scheduleSectionUpdate);
updateSection();

const contactAddress = document.querySelector('#contact [data-email]').textContent;
for (const link of document.querySelectorAll('[data-email]')) {
  link.addEventListener('click', () => {
    link.href = `mailto:${contactAddress.replace(' [at] ', String.fromCharCode(64))}`;
  });
}

const dateFormatter = new Intl.DateTimeFormat('en', { month: 'short', year: 'numeric', timeZone: 'UTC' });
for (const time of document.querySelectorAll('.news-list time')) {
  time.textContent = dateFormatter.format(new Date(`${time.dateTime}-01T00:00:00Z`));
}

const citations = [...document.querySelectorAll('.citation')];
function restoreCitation() {
  const id = new URL(window.location.href).searchParams.get('cite');
  for (const citation of citations) citation.open = citation.id === `citation-${id}`;
}
restoreCitation();
window.addEventListener('popstate', restoreCitation);

for (const citation of citations) {
  citation.addEventListener('toggle', () => {
    const id = citation.id.replace('citation-', '');
    const url = new URL(window.location.href);
    if (citation.open) {
      for (const other of citations) if (other !== citation) other.open = false;
      url.searchParams.set('cite', id);
    } else if (url.searchParams.get('cite') === id) url.searchParams.delete('cite');
    if (url.href !== window.location.href) window.history.replaceState(null, '', url);
    scheduleSectionUpdate();
  });
}

for (const button of document.querySelectorAll('[data-copy]')) {
  button.addEventListener('click', async () => {
    const citation = button.closest('.citation');
    const code = citation.querySelector('code');
    const status = citation.querySelector('.copy-status');
    const label = button.querySelector('span');
    status.textContent = '';
    button.disabled = true;
    try {
      await navigator.clipboard.writeText(code.textContent);
      label.textContent = button.dataset.copied;
      status.textContent = button.dataset.copied;
      window.setTimeout(() => { label.textContent = button.dataset.copyLabel; status.textContent = ''; }, 1800);
    } catch {
      status.textContent = button.dataset.error;
      const range = document.createRange();
      range.selectNodeContents(code);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      code.closest('pre').focus();
    } finally {
      button.disabled = false;
    }
  });
}
