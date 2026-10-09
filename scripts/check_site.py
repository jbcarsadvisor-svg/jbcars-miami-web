import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit, unquote
from bs4 import BeautifulSoup

site = Path(__file__).resolve().parents[1] / 'docs'
base = 'https://jbcarsadvisor-svg.github.io/jbcars-miami-web/'
errors = []
for page in [site/'index.html', site/'en'/'index.html', site/'404.html']:
    soup = BeautifulSoup(page.read_text(encoding='utf-8'), 'html.parser')
    def require(condition, message):
        if not condition: errors.append(f'{page.relative_to(site)}: {message}')
    require(len(soup.find_all('h1')) == 1,'exactly one h1 required')
    require(bool(soup.html.get('lang')),'language missing')
    require(bool(soup.find('meta',attrs={'name':'viewport'})),'viewport missing')
    ids = [el['id'] for el in soup.select('[id]')]
    require(len(ids)==len(set(ids)),'duplicate DOM ids')
    require(all(img.get('alt') is not None for img in soup.find_all('img')),'image alt missing')
    require(all(img.get('width') and img.get('height') for img in soup.find_all('img')),'image dimensions missing')
    for el in soup.select('[src], [href]'):
        for attr in ('href','src'):
            value = el.get(attr)
            if not value or value.startswith(('https:', 'http:', 'mailto:', 'tel:', 'data:')): continue
            parts = urlsplit(value)
            target = (page.parent/unquote(parts.path)).resolve() if parts.path else page
            if target.is_dir(): target = target/'index.html'
            require(target.is_file(),f'broken local resource {value}')
            if parts.fragment and target.suffix == '.html' and target.is_file():
                target_soup = soup if target == page else BeautifulSoup(target.read_text(encoding='utf-8'),'html.parser')
                require(bool(target_soup.find(id=parts.fragment)),f'missing fragment {value}')
    for el in soup.select('[srcset]'):
        for source in el['srcset'].split(','):
            require((page.parent/source.strip().split()[0]).is_file(),'srcset source missing')
    for link in soup.find_all('a',target='_blank'):
        require('noopener' in link.get('rel',[]),'external link missing noopener')
    if page.name=='404.html': continue
    expected = base if page.parent==site else base+'en/'
    require(soup.find('link',rel='canonical')['href']==expected,'canonical incorrect')
    require(len(soup.find_all('link',rel='alternate',hreflang=True))==3,'hreflang incomplete')
    require(bool(soup.find('meta',attrs={'name':'description'})['content']),'description missing')
    structured = json.loads(soup.find('script',type='application/ld+json').string)
    require({node['@type'] for node in structured['@graph']}=={'Organization','Person','WebSite','WebPage'},'structured graph incorrect')
    require(not soup.find('meta',attrs={'name':'robots','content':re.compile('noindex')}),'production page is noindex')
    for label in soup.find_all('label'):
        require(bool(label.find(['input','select','textarea'])),'label has no form control')
    for ident in ['name','vehicle','budget','timing','message','inquiry-form','message-panel','send-whatsapp','send-email','edit-inquiry','status']:
        require(bool(soup.find(id=ident)),f'JS target missing: {ident}')
    # Local font URLs resolve from the stylesheet rather than the page.
for font_url in re.findall(r"url\(['\"]?([^)'\"]+)", (site/'styles.css').read_text(encoding='utf-8')):
    if not (site/font_url).is_file(): errors.append('missing CSS asset: '+font_url)
tree = ET.parse(site/'sitemap.xml')
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
assert {el.text for el in tree.findall('.//s:loc',ns)} == {base,base+'en/'}
assert 'Sitemap: '+base+'sitemap.xml' in (site/'robots.txt').read_text()
if errors:
    raise SystemExit('\n'.join(errors))
print('PASS: ES/EN links, fragments, images, SEO metadata, schema, form labels, JS targets, fonts, sitemap and robots')
