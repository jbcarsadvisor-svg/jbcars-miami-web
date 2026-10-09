"""Generate a crawlable English page and search metadata from the Spanish source."""
import json
from pathlib import Path
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parents[1]
site = root / 'docs'
url = 'https://jbcarsadvisor-svg.github.io/jbcars-miami-web/'
source = BeautifulSoup((site / 'index.html').read_text(encoding='utf-8'), 'html.parser')
source.title.string = 'Asesor de carros en Miami | Jesús Bouquet · JB Cars Miami'
for lang, href in [('es', url), ('en', url + 'en/'), ('x-default', url)]:
    if not source.find('link', hreflang=lang):
        source.head.append(source.new_tag('link', rel='alternate', hreflang=lang, href=href))
switch = source.find(id='language-switch')
switch.name = 'a'
switch.attrs.pop('type', None)
switch['href'] = 'en/'
switch['hreflang'] = 'en'
switch['lang'] = 'en'
switch['aria-label'] = 'EN — Read this website in English'

def structured_data(soup, language):
    script = soup.find('script', type='application/ld+json')
    business = json.loads(script.string)
    if '@graph' in business:
        business = business['@graph'][0]
    business['@id'] = url + '#organization'
    page_url = url if language == 'es' else url + 'en/'
    faq = [{ '@type': 'Question', 'name': detail.summary.find('span').get_text(),
             'acceptedAnswer': {'@type':'Answer','text':detail.p.get_text()} }
           for detail in soup.select('.faq-list details')]
    script.string = json.dumps({'@context':'https://schema.org','@graph':[
        business,
        {'@type':'Person','@id':url+'#jesus','name':'Jesús F. Bouquet Meinhardt',
         'worksFor':{'@id':url+'#organization'},'url':url+'#jesus'},
        {'@type':'WebSite','@id':url+'#website','url':url,'name':'JB Cars Miami',
         'publisher':{'@id':url+'#organization'},'inLanguage':['es','en']},
        {'@type':'WebPage','@id':page_url+'#webpage','url':page_url,
         'name':soup.title.get_text(),'description':soup.find('meta',attrs={'name':'description'})['content'],
         'inLanguage':language,'isPartOf':{'@id':url+'#website'},
         'about':{'@id':url+'#organization'}},
        {'@type':'FAQPage','@id':page_url+'#preguntas','inLanguage':language,'mainEntity':faq}
    ]}, ensure_ascii=False, separators=(',', ':'))

structured_data(source, 'es')
(site / 'index.html').write_text(str(source), encoding='utf-8')
english = BeautifulSoup(str(source), 'html.parser')
translations = json.loads((root/'scripts'/'en.json').read_text(encoding='utf-8'))
for element in english.select('[data-i18n]'):
    key = element['data-i18n']
    if key not in translations:
        raise ValueError('Missing English text: ' + key)
    element.clear()
    for index, line in enumerate(translations[key].split('\n')):
        if index:
            element.append(english.new_tag('br'))
        element.append(line)
english.html['lang'] = 'en'
english.title.string = 'Car advisor in Miami | Jesús Bouquet · JB Cars Miami'
english.find('meta', attrs={'name':'description'})['content'] = 'Car buying guidance in Miami with Jesús Bouquet. Explore your options, discover customer experiences and contact Jesús directly by phone or email.'
english.find('link',rel='canonical')['href'] = url + 'en/'
english.find('meta',property='og:title')['content'] = 'JB Cars Miami · Before you buy, talk to Jesús.'
english.find('meta',property='og:description')['content'] = 'Choosing a car is a big decision. Start with a conversation with Jesús Bouquet.'
english.find('meta',property='og:url')['content'] = url+'en/'
english.find('meta',property='og:locale')['content'] = 'en_US'
english.find('meta',property='og:locale:alternate')['content'] = 'es_US'
for element in english.select('[src], [href]'):
    for attr in ('src','href'):
        value = element.get(attr)
        if value and not value.startswith(('http', 'mailto:', 'tel:', '#', 'data:')):
            element[attr] = '../' + value
for element in english.select('[srcset]'):
    element['srcset'] = ', '.join('../'+part.strip() for part in element['srcset'].split(','))
switch = english.find(id='language-switch')
switch['href'] = '../'
switch['hreflang'] = 'es'
switch['lang'] = 'es'
switch['aria-label'] = 'ES — Leer esta web en español'
switch.clear()
switch.append('ES ')
arrow = english.new_tag('span', attrs={'aria-hidden':'true'})
arrow.string = '↗'
switch.append(arrow)
english.find(id='name')['placeholder'] = 'What is your name?'
english.find(id='message')['placeholder'] = 'What matters to you in your next car?'
english.find(id='menu-toggle')['aria-label'] = 'Open menu'
for note in english.select('.vehicle-model'):
    note.string = note.get_text().replace('Referencia', 'Reference')
for nav in english.find_all('nav'):
    nav['aria-label'] = 'Mobile navigation' if nav.get('id') == 'mobile-nav' else 'Main navigation'
for img in english.find_all('img'):
    alts = {'Jesús Bouquet en el concesionario':'Jesús Bouquet at the dealership',
            'Jesús Bouquet conversando durante una entrevista':'Jesús Bouquet speaking during an interview',
            'Personas junto a un vehículo frente a Toyota of Hollywood':'People beside a vehicle at Toyota of Hollywood'}
    img['alt'] = alts.get(img.get('alt',''),img.get('alt','')).replace(' con fondo transparente, referencia de categoría',' with a transparent background, category reference')
for element in english.select('[aria-label]'):
    element['aria-label'] = element['aria-label'].replace('— Inicio','— Home').replace('Volver al inicio','Back to top').replace('Ver la publicación original en Instagram','View the original Instagram post').replace('Jesús Bouquet en ','Jesús Bouquet in ').replace('(nueva pestaña)','(new tab)')
english.find('noscript').clear()
english.find('noscript').append(BeautifulSoup('<p class="noscript-note">Contact Jesús directly: <a href="tel:+17864388264">+1 (786) 438-8264</a> · <a href="mailto:jbcarsadvisor@gmail.com">Email</a>. Enable JavaScript to prepare a message.</p>','html.parser'))
structured_data(english, 'en')
(site/'en').mkdir(exist_ok=True)
(site/'en'/'index.html').write_text(str(english),encoding='utf-8')
(site/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+url+'sitemap.xml\n',encoding='utf-8')
entries = []
for path in ['', 'en/']:
    entries.append(f'<url><loc>{url}{path}</loc><xhtml:link rel="alternate" hreflang="es" href="{url}"/><xhtml:link rel="alternate" hreflang="en" href="{url}en/"/><xhtml:link rel="alternate" hreflang="x-default" href="{url}"/></url>')
(site/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+''.join(entries)+'</urlset>\n',encoding='utf-8')
print('Built ES + EN pages, structured data, robots.txt and sitemap.xml')
