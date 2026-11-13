"""Notify IndexNow about the published URLs in sitemap.xml after deployment."""
import json
from pathlib import Path
import re
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent.parent
SITE_URL = 'https://miles-song.github.io/'
KEY_URL = SITE_URL + 'indexnow.txt'
key = (ROOT / 'indexnow.txt').read_text(encoding='utf-8').strip()
if not re.fullmatch(r'[a-f0-9]{32}', key):
    raise SystemExit('The IndexNow verification file is invalid.')

sitemap = ElementTree.parse(ROOT / 'sitemap.xml')
urls = [node.text for node in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
host = urlsplit(SITE_URL).netloc
if not urls or any(urlsplit(url).netloc != host or urlsplit(url).fragment for url in urls):
    raise SystemExit('The sitemap must contain canonical URLs on this site.')

with urlopen(KEY_URL, timeout=30) as response:
    if response.read().decode('utf-8').strip() != key:
        raise SystemExit('Deploy the current IndexNow verification file before submitting.')

payload = {'host': host, 'key': key, 'keyLocation': KEY_URL, 'urlList': urls}
request = Request(
    'https://api.indexnow.org/indexnow',
    data=json.dumps(payload).encode('utf-8'),
    headers={'Content-Type': 'application/json; charset=utf-8'},
    method='POST',
)
try:
    with urlopen(request, timeout=30) as response:
        status = response.status
except HTTPError as error:
    raise SystemExit(f'IndexNow returned HTTP {error.code}; the URLs were not accepted.') from None

if status not in (200, 202):
    raise SystemExit(f'Unexpected IndexNow response: HTTP {status}.')
print(json.dumps({
    'http_status': status,
    'submission': 'received' if status == 200 else 'received; key validation pending',
    'urls': urls,
    'indexing_confirmed': False,
}, indent=2))
