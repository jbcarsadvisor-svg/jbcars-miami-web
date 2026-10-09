"""Build the separate Spanish buyer blog using the site's corporate shell."""
import json
from copy import deepcopy
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parents[1]
site = root / 'docs'
base = 'https://jbcarsadvisor-svg.github.io/jbcars-miami-web/'
posts = json.loads((root / 'scripts/blog.json').read_text(encoding='utf-8'))
assert posts and len({p['slug'] for p in posts}) == len(posts)
template = BeautifulSoup((site / 'index.html').read_text(encoding='utf-8'), 'html.parser')
directory = site / 'blog'
directory.mkdir(exist_ok=True)

def image(post, eager=False):
    slug, alt = post['slug'], escape(post['alt'], quote=True)
    loading = 'eager' if eager else 'lazy'
    priority = ' fetchpriority="high"' if eager else ''
    return f'<img src="../assets/blog/{slug}.webp?v=20261009-2" alt="{alt}" width="1200" height="800" loading="{loading}"{priority}/>'

def card(post, featured=False):
    return f'''<article class="blog-card{' blog-card-featured' if featured else ''}">
    <a class="blog-card-image" href="{post['slug']}.html" tabindex="-1" aria-hidden="true">{image(post, featured)}</a>
    <div class="blog-card-copy"><div class="blog-meta"><span>{escape(post['category'])}</span><span>1 min de lectura</span></div>
    <h2><a href="{post['slug']}.html">{escape(post['title'])}</a></h2><p>{escape(post['intro'])}</p>
    <a class="text-link blog-read" href="{post['slug']}.html" aria-label="Leer: {escape(post['title'], quote=True)}">Leer artículo <svg class="icon" aria-hidden="true"><use href="#arrow"></use></svg></a></div></article>'''

def write_page(filename, title, description, content, post=None):
    soup = deepcopy(template)
    soup.body['class'] = 'blog-page'
    soup.title.string = title + ' | JB Cars Miami'
    page_url = base + 'blog/' + ('' if filename == 'index.html' else filename)
    soup.find('meta', attrs={'name':'description'})['content'] = description
    soup.find('link', rel='canonical')['href'] = page_url
    for link in soup.select('link[hreflang]'):
        link.decompose()
    for prop, value in [('og:title', title), ('og:description', description), ('og:url', page_url), ('og:type', 'article' if post else 'website')]:
        soup.find('meta', property=prop)['content'] = value
    soup.find('meta', property='og:locale:alternate').decompose()
    soup.find('meta', property='og:image')['content'] = base + 'assets/blog/' + (post or posts[0])['slug'] + '.webp?v=20261009-2'
    soup.head.append(soup.new_tag('meta', property='og:image:alt', content=(post or posts[0])['alt']))
    soup.head.append(soup.new_tag('meta', property='og:site_name', content='JB Cars Miami'))
    if post:
        soup.head.append(soup.new_tag('meta', property='article:published_time', content=post['published']))
        soup.head.append(soup.new_tag('meta', property='article:modified_time', content=post['modified']))
    for element in soup.select('[src], [href]'):
        for attr in ('src', 'href'):
            value = element.get(attr)
            if not value: continue
            if value.startswith('#') and element.name == 'a' and value != '#main':
                element[attr] = '../' + value
            elif not value.startswith(('http', 'mailto:', 'tel:', '#', 'data:')):
                element[attr] = '../' + value
    for link in soup.select('[data-i18n="navBlog"]'):
        link['href'] = './'
        if not post: link['aria-current'] = 'page'
    for script in soup.select('script[src]'):
        script.decompose()
    soup.head.append(soup.new_tag('link', rel='stylesheet', href='../blog.css?v=20261009-1'))
    soup.head.append(soup.new_tag('script', src='../blog.js?v=20261009-1', defer=''))
    soup.find(id='main').clear()
    soup.find(id='main').append(BeautifulSoup(content, 'html.parser'))
    graph = json.loads(soup.find('script', type='application/ld+json').string)['@graph']
    graph = [node for node in graph if node['@type'] != 'WebPage']
    node = {'@type':'BlogPosting' if post else 'Blog', '@id':page_url+'#blog', 'url':page_url,
            'name':title, 'description':description, 'inLanguage':'es',
            'publisher':{'@id':base+'#organization'}, 'isPartOf':{'@id':base+'#website'}}
    if post:
        node.update(headline=title, image=base+'assets/blog/'+post['slug']+'.webp?v=20261009-2',
                    author={'@id':base+'#organization'}, datePublished=post['published'], dateModified=post['modified'],
                    mainEntityOfPage=page_url, isPartOf={'@id':base+'blog/#blog'},
                    articleBody='\n\n'.join([post['intro'], *post['paragraphs'], post['tip']]))
    else:
        node['blogPost'] = [{'@id':base+'blog/'+p['slug']+'.html#blog'} for p in posts]
    graph.append(node)
    if post:
        graph.append({'@type':'BreadcrumbList', 'itemListElement':[
            {'@type':'ListItem','position':1,'name':'Inicio','item':base},
            {'@type':'ListItem','position':2,'name':'Blog','item':base+'blog/'},
            {'@type':'ListItem','position':3,'name':title,'item':page_url}]})
    soup.find('script', type='application/ld+json').string = json.dumps({'@context':'https://schema.org','@graph':graph}, ensure_ascii=False)
    (directory / filename).write_text(str(soup), encoding='utf-8')

cta = '''<aside class="blog-cta"><div><span class="eyebrow">TU PRÓXIMO PASO</span><h2>¿Lo hablamos con calma?</h2><p>Cuéntale a Jesús qué carro buscas y qué dudas tienes. Empecemos por ahí.</p></div><a class="button button-dark" href="../#contacto">Hablar con Jesús <svg class="icon" aria-hidden="true"><use href="#arrow"></use></svg></a></aside>'''
intro = '''<section class="blog-intro"><a class="text-link blog-back" href="../">← Volver al inicio</a><div class="eyebrow"><span class="small-line"></span>BLOG / JB CARS MIAMI</div><h1>Más claridad.<br/><span>Mejores decisiones.</span></h1><p>Comprar carro trae preguntas. Aquí las hablamos sin vueltas: consejos cortos para cuidar tu bolsillo y elegir con más confianza.</p></section>'''
content = '<div class="container blog-container">'+intro+card(posts[0], True)+'<section class="blog-grid" aria-label="Consejos para comprar carro">'+''.join(card(p) for p in posts[1:])+'</section>'+cta+'</div>'
write_page('index.html', 'Blog: consejos para comprar carro', 'Consejos cortos para comprar carro en Miami: presupuesto, financiamiento, carros usados y qué revisar antes de firmar. En español, sin vueltas.', content)
for i, post in enumerate(posts):
    paragraphs = ''.join('<p>'+escape(p)+'</p>' for p in post['paragraphs'])
    sources = ''
    if post['slug'] in ['presupuesto', 'financiamiento', 'down-payment', 'seguro']:
        sources = '<a href="https://www.consumerfinance.gov/consumer-tools/auto-loans/" target="_blank" rel="noopener noreferrer">Guía de préstamos para carros · CFPB ↗</a>'
    elif post['slug'] in ['precio-final', 'carro-usado', 'millas', 'extras', 'antes-firmar']:
        sources = '<a href="https://consumidor.ftc.gov/articulos/como-comprar-un-carro-usado-un-concesionario" target="_blank" rel="noopener noreferrer">Guía de compra de carros usados · FTC ↗</a>'
    body = f'''<div class="container blog-container"><nav class="blog-breadcrumb" aria-label="Ruta de navegación"><a href="../">Inicio</a><span aria-hidden="true">/</span><a href="./">Blog</a><span aria-hidden="true">/</span><span>{escape(post['category'])}</span></nav>
    <article class="blog-article"><header class="blog-article-heading"><div class="blog-meta"><span>{escape(post['category'])}</span><span>1 min de lectura</span></div><h1>{escape(post['title'])}</h1><p class="blog-lead">{escape(post['intro'])}</p><span class="blog-byline">Por el equipo de JB Cars Miami</span></header>
    <figure class="blog-cover">{image(post, True)}</figure><div class="blog-body">{paragraphs}<aside class="blog-tip"><span class="eyebrow">LLÉVATE ESTE CONSEJO</span><p>{escape(post['tip'])}</p></aside>{'<div class="blog-sources">Para seguir leyendo: '+sources+'</div>' if sources else ''}<a class="text-link blog-back" href="./">← Ver todos los artículos</a></div></article>
    <section class="blog-related" aria-labelledby="related-title"><div class="eyebrow">UN CONSEJO MÁS</div><h2 id="related-title">También te puede servir.</h2><div class="blog-grid">{card(posts[(i+1)%len(posts)])}{card(posts[(i+2)%len(posts)])}</div></section>{cta}</div>'''
    write_page(post['slug']+'.html', post['title'], post['intro'], body, post)

namespace = 'http://www.sitemaps.org/schemas/sitemap/0.9'
ET.register_namespace('', namespace)
ET.register_namespace('xhtml', 'http://www.w3.org/1999/xhtml')
tree = ET.parse(site/'sitemap.xml')
for entry in list(tree.getroot()):
    location = entry.find('{'+namespace+'}loc')
    if location is not None and location.text.startswith(base+'blog/'):
        tree.getroot().remove(entry)
for path in ['blog/', *['blog/'+post['slug']+'.html' for post in posts]]:
    entry = ET.SubElement(tree.getroot(), '{'+namespace+'}url')
    ET.SubElement(entry, '{'+namespace+'}loc').text = base+path
    modified = max(p['modified'] for p in posts) if path == 'blog/' else next(p['modified'] for p in posts if path == 'blog/'+p['slug']+'.html')
    ET.SubElement(entry, '{'+namespace+'}lastmod').text = modified
tree.write(site/'sitemap.xml', encoding='utf-8', xml_declaration=True)
print(f'Built separate blog: index + {len(posts)} articles')
