"""Render the public homepage from reviewed Gemini-authored copy. No dependencies."""
from html import escape
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
ui = data['ui']
identity = data['identity']
style_version = sha256((ROOT / 'styles.css').read_bytes()).hexdigest()[:12]
script_version = sha256((ROOT / 'app.js').read_bytes()).hexdigest()[:12]

def e(value):
    return escape(str(value), quote=True)

def icon(name, cls=''):
    paths = {
        'arrow': '<path d="M4 12h16m-6-6 6 6-6 6"/>',
        'external': '<path d="M6 18 18 6M6 6h12v12"/>',
        'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
        'copy': '<rect x="8" y="8" width="12" height="13" rx="2"/><path d="M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h3"/>',
        'up': '<path d="M12 20V4m-6 6 6-6 6 6"/>',
        'plus': '<path d="M12 5v14M5 12h14"/>',
        'github': '<path d="M9 19c-4.3 1.3-4.3-2.2-6-2.7m12 5v-3.4c0-1 .1-1.5-.5-2.1 3-.3 6.2-1.5 6.2-6.7a5.2 5.2 0 0 0-1.4-3.6 4.9 4.9 0 0 0-.1-3.5S18.1 1.7 15.5 3a12.5 12.5 0 0 0-7 0C5.9 1.7 4.8 2 4.8 2a4.9 4.9 0 0 0-.1 3.5 5.2 5.2 0 0 0-1.4 3.6c0 5.2 3.2 6.4 6.2 6.7-.5.5-.6 1.1-.5 2.1v3.4"/>',
    }
    return f'<svg class="icon {cls}" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>'

def ext(url, label, cls='text-link', symbol='external', extra=''):
    return f'<a class="{cls}" href="{e(url)}" target="_blank" rel="noopener noreferrer" {extra}>{e(label)}{icon(symbol)}</a>'

def linked_bio(text):
    text = e(text)
    for name, url in [('Qiao Xiang','https://qiaoxiang.me/'), ('Qiang Su','https://faculty.xmu.edu.cn/suqiang/zh_CN/index.htm'), ('Xiamen University','https://www.xmu.edu.cn/')]:
        text = text.replace(name, f'<a class="inline-link" href="{url}" target="_blank" rel="noopener noreferrer">{name}</a>')
    return text

contact_link = f'<a class="inline-link" href="#contact" data-email>{e(identity["email"])}</a>'
contact = e(data['profile']['contact']).replace('{email}', contact_link)

def bibliography(p):
    names = []
    for author in p['authors']:
        parts = author.rsplit(' ', 1)
        names.append(', '.join(reversed(parts)))
    title = p['title'].replace('LEOPARD', '{LEOPARD}').replace('SAT', '{SAT}').replace('ASICs', '{ASICs}')
    return '\n'.join([
        f"@inproceedings{{{p['id']}{p['year']},",
        f"  title = {{{title}}},",
        f"  author = {{{' and '.join(names)}}},",
        f"  booktitle = {{{p['booktitle']}}},",
        f"  year = {{{p['year']}}},",
        f"  pages = {{{p['pages'].replace('–', '--').replace('-', '--').replace('----','--')}}},",
        f"  doi = {{{p['doi']}}},",
        f"  url = {{https://doi.org/{p['doi']}}}",
        '}'
    ])

nav = ''.join(f'<a class="section-link" href="#{key}" {"aria-current=\"location\"" if i == 0 else ""}><span>{e(ui[key])}</span>{icon("arrow")}</a>' for i,key in enumerate(['profile','news','research','publications']))
education = ''.join(f'<li><span class="education-years">{e(item["years"])}</span><div><span class="degree">{e(item["degree"])}</span><span class="institution">{e(item["institution"])}</span></div></li>' for item in data['education'])
news = []
for item in data['news']:
    extra = f'<a class="news-link" href="{e(item["linkTarget"])}">{e(item["linkLabel"])}{icon("arrow")}</a>' if item.get('linkTarget') else ''
    news.append(f'<li><time datetime="{e(item["date"])}">{e(item["date"])}</time><div><p>{e(item["text"])}</p>{extra}</div></li>')
areas = ''.join(f'<article class="research-area"><h3>{e(area["title"])}</h3><p>{e(area["body"])}</p></article>' for area in data['research']['areas'])
opensource = data.get('opensource')
repository_html = ''
if opensource:
    projects = ''.join(f'<article class="repository"><div><h4>{ext(repo["url"],repo["name"],"repository-link")}</h4><span class="repository-tech">{e(repo["technology"])}</span></div><p>{e(repo["description"])}</p></article>' for repo in opensource['projects'])
    repository_html = f'<div class="open-source"><h3>{e(opensource["heading"])}</h3><div class="repository-list">{projects}</div></div>'
papers = []
for p in data['publications']:
    author_html = ', '.join(f'<strong>{e(a)}</strong>' if a == identity['publicationName'] else e(a) for a in p['authors'])
    url = 'https://www.xingfang.fun/papers/IWQoS25-LEOPARD.pdf' if p['id']=='leopard' else f'https://doi.org/{p["doi"]}'
    code = ext('https://github.com/sngroup-xmu/Procurator',ui['code']) if p['id']=='procurator' else ''
    slides = ext(p['slides'],ui['slides']) if p.get('slides') else ''
    papers.append(f'''<article class="publication" id="{e(p['id'])}" aria-labelledby="title-{e(p['id'])}">
      <h3 id="title-{e(p['id'])}"><a href="{e(url)}" target="_blank" rel="noopener noreferrer">{e(p['title'])}</a></h3>
      <div class="publication-meta"><span class="venue">{e(p['venue'])}</span><span class="year">{e(p['year'])}</span></div>
      <p class="authors">{author_html}</p>
      <p class="paper-summary">{e(p['summary'])}</p>
      <div class="paper-actions">{ext(url,ui['paper'])}{slides}{code}
        <details class="citation" id="citation-{e(p['id'])}">
          <summary>{e(ui['bibtex'])}{icon('plus','citation-toggle')}</summary>
          <div class="citation-content">
            <div class="citation-toolbar"><span>{e(ui['bibtex'])}</span><button class="copy-button" type="button" data-copy="{e(p['id'])}" data-copy-label="{e(ui['copyCitation'])}" data-copied="{e(ui['copied'])}" data-error="{e(ui['copyError'])}">{icon('copy')}<span>{e(ui['copyCitation'])}</span></button></div>
            <pre tabindex="0"><code>{e(bibliography(p))}</code></pre>
            <p class="copy-status" role="status"></p>
          </div>
        </details>
      </div>
    </article>''')

page = f'''<!doctype html>
<html lang="en" data-type="personal" data-motion="quiet">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{e(data['meta']['title'])}</title>
  <meta name="description" content="{e(data['meta']['description'])}">
  <meta name="author" content="{e(identity['name'])}">
  <meta name="theme-color" content="#f7f7f2">
  <meta name="color-scheme" content="light">
  <meta name="page-type" content="personal">
  <meta name="site-kind" content="academic">
  <link rel="canonical" href="https://miles-song.github.io/">
  <meta property="og:type" content="profile">
  <meta property="og:title" content="{e(data['meta']['title'])}">
  <meta property="og:description" content="{e(data['meta']['description'])}">
  <meta property="og:url" content="https://miles-song.github.io/">
  <meta property="og:image" content="https://miles-song.github.io/assets/github-avatar.webp">
  <meta property="og:image:alt" content="{e(identity['avatarAlt'])}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{e(data['meta']['title'])}">
  <meta name="twitter:description" content="{e(data['meta']['description'])}">
  <meta name="twitter:image" content="https://miles-song.github.io/assets/github-avatar.webp">
  <link rel="icon" href="assets/github-avatar.webp" type="image/webp">
  <link rel="preload" href="assets/fonts/figtree-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="styles.css?v={style_version}">
  <script src="app.js?v={script_version}" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">{e(ui['skip'])}</a>
  <header class="site-header">
    <div class="header-inner wrap">
      <a class="wordmark" href="#profile" translate="no">{e(identity['name'])}<span class="name-dot" aria-hidden="true">.</span></a>
      <div class="header-links">{ext('https://github.com/miles-song',ui['github'],'header-github','external',f'aria-label="{e(ui["githubAria"])}"')}<a class="button button-small" href="#contact" data-email aria-label="{e(ui['emailAria'])}">{e(ui['email'])}{icon('external')}</a></div>
    </div>
  </header>
  <div class="page-layout wrap">
    <aside class="sidebar">
      <nav class="section-nav" aria-label="{e(ui['navigationLabel'])}">{nav}</nav>
      <div class="sidebar-foot"><span>{e(identity['location'])}</span><a href="#contact" data-email class="sidebar-email" aria-label="{e(ui['emailAria'])}">{icon('mail')}<span>{e(ui['email'])}</span></a></div>
    </aside>
    <main id="main" tabindex="-1">
      <section id="profile" class="profile-section" aria-labelledby="profile-name" data-enter>
        <div class="profile-heading">
          <div><h1 id="profile-name" translate="no">{e(identity['name'])}<span lang="zh-Hans">{e(identity['chineseName'])}</span></h1><p class="role">{e(identity['role'])}</p><p class="affiliation">{e(identity['affiliation'])}</p></div>
          <a class="avatar-link" href="https://github.com/miles-song" target="_blank" rel="noopener noreferrer" aria-label="{e(ui['githubAria'])}"><img class="avatar" src="assets/github-avatar.webp" width="136" height="136" alt="{e(identity['avatarAlt'])}" fetchpriority="high"></a>
        </div>
        <p class="profile-lead">{e(data['profile']['lead'])}</p>
        <div class="bio">{''.join(f'<p>{linked_bio(p)}</p>' for p in data['profile']['bio'])}<p id="contact" class="contact-note">{contact}</p></div>
        <div class="profile-actions"><a class="button" href="#publications">{e(ui['viewPublications'])}{icon('arrow')}</a>{ext('https://github.com/miles-song',ui['github'],'text-link','github')}</div>
        <div class="education"><h2>{e(ui['education'])}</h2><ol>{education}</ol></div>
      </section>
      <section id="news" class="content-section" aria-labelledby="news-title">
        <div class="section-heading"><h2 id="news-title">{e(ui['news'])}</h2></div>
        <ol class="news-list">{''.join(news)}</ol>
      </section>
      <section id="research" class="content-section" aria-labelledby="research-title">
        <div class="section-heading"><h2 id="research-title">{e(ui['research'])}</h2></div>
        <p class="section-intro">{e(data['research']['intro'])}</p>
        <div class="research-areas">{areas}</div>
        <div class="simulation-practice">
          <h3>{e(data['research']['simulation']['heading'])}</h3>
          <p>{e(data['research']['simulation']['intro'])}</p>
          <div class="ongoing-work"><h4 id="project-title">{e(data['research']['project']['title'])}</h4><p>{e(data['research']['project']['body'])}</p></div>
        </div>
        {repository_html}
      </section>
      <section id="publications" class="content-section publications-section" aria-labelledby="publications-title">
        <div class="section-heading"><h2 id="publications-title">{e(ui['publications'])}</h2><span class="section-note">{e(ui['publicationCount'])}</span></div>
        <div class="publication-list">{''.join(papers)}</div>
      </section>
      <footer class="site-footer"><p>{e(ui['footer'])}</p><a class="text-link" href="#profile">{e(ui['backToTop'])}{icon('up')}</a></footer>
    </main>
  </div>
</body>
</html>
'''
(ROOT/'index.html').write_text(page, encoding='utf-8')
print('Built index.html from content.json')
