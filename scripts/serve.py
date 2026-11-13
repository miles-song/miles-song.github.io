"""Serve only public homepage files, bound to this computer."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse

ROOT = Path(__file__).resolve().parent.parent
PUBLIC_FILES = {'index.html', 'styles.css', 'app.js', 'content.json', 'robots.txt', 'sitemap.xml', 'indexnow.txt'}

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def send_head(self):
        path = unquote(urlsplit(self.path).path).lstrip('/') or 'index.html'
        target = (ROOT / path).resolve()
        is_asset = target.is_relative_to(ROOT / 'assets') and target.is_file()
        if not (path in PUBLIC_FILES or is_asset) or not target.is_relative_to(ROOT):
            self.send_error(404)
            return None
        return super().send_head()

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=4173)
args = parser.parse_args()
print(f'Homepage: http://127.0.0.1:{args.port}', flush=True)
ThreadingHTTPServer(('127.0.0.1', args.port), Handler).serve_forever()
