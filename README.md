# JB Cars Miami

Web bilingüe de asesoría independiente de coches en Miami. Sitio estático ligero, preparado para GitHub Pages, con fotografías reales y contacto directo con Jesús Bouquet.

## Publicación

- URL: https://jbcarsadvisor-svg.github.io/jbcars-miami-web/
- Inglés: https://jbcarsadvisor-svg.github.io/jbcars-miami-web/en/
- GitHub Pages: rama `main`, carpeta `/docs`.
- No requiere Node, servicios de pago ni un proceso de compilación en el alojamiento.

## Estructura

- `docs/index.html`: contenido principal en español.
- `docs/en/index.html`: contenido en inglés generado y rastreable.
- `docs/styles.css`: diseño, móvil y reducción de movimiento.
- `docs/app.js`: menú y preparación de consultas.
- `docs/blog/`: índice del blog y 10 artículos breves en español latino.
- `docs/blog.css` y `docs/blog.js`: diseño y menú propios del blog.
- `docs/assets/blog/`: 10 portadas editoriales generadas y optimizadas en WebP.
- `scripts/blog.json` y `scripts/build-blog.py`: contenido y generación del blog; se ejecuta desde `build.py`.
- Para sumar artículos, agregar una entrada a `scripts/blog.json` con slug único, contenido, texto alternativo y fechas `published`/`modified`; añadir su portada WebP. El índice, los enlaces y el sitemap se generan con el total disponible.
- `docs/assets/`: fotografías WebP y tipografía Manrope alojadas localmente.
- `scripts/build.py`: generación de inglés, sitemap y datos estructurados. Requiere Python y BeautifulSoup.
- `scripts/prepare-assets.py`: optimización de imágenes originales. Requiere Pillow.
- `recursos/`: originales y fuentes documentadas.
- `INVESTIGACION-WEB.md`: contexto y propuesta inicial.

## Contactos y formulario

Teléfono público: +1 (786) 438-8264. Email público: jbcarsadvisor@gmail.com.
El formulario valida nombre y categoría, prepara una consulta y permite abrir WhatsApp o email. **No guarda ni envía el mensaje automáticamente.** El visitante debe enviarlo desde su aplicación. La disponibilidad de WhatsApp para el número debe confirmarse por el operador; hay alternativas de teléfono y email.
No hay base de datos, cookies de analítica, persistencia de consultas ni servicios de terceros cargados al visitar la página. GitHub procesa las peticiones de alojamiento. Los enlaces externos tienen sus propias políticas. No se recogen documentos ni datos bancarios.

## Edición y comprobación

Editar primero el español en `docs/index.html` y las traducciones en `scripts/en.json`. Después ejecutar:

```sh
python scripts/build.py
python scripts/check_site.py
node --check docs/app.js
node scripts/serve.cjs
```

Abrir http://127.0.0.1:4173. Revisar móvil, escritorio, menú, enlaces, formulario, edición de consultas y ambas versiones de idioma antes de publicar.
Los archivos en `docs/` están listos para servir directamente. Cambiar el nombre del repositorio requiere actualizar el dominio base en `scripts/build.py`, los metadatos del HTML y `404.html`.

## SEO

HTML semántico rastreable, títulos y descripciones por idioma, canonical, hreflang recíproco ES/EN/x-default, Open Graph, favicon, sitemap XML bilingüe y robots.txt. Datos estructurados Organization, Person, WebSite, WebPage basados en contenido visible; no se inventan dirección, reseñas agregadas ni valoraciones.
Publicación no equivale a indexación: registrar la propiedad en Google Search Console, verificarla con acceso del propietario y enviar el sitemap es un paso posterior.
El blog incluye URLs propias, títulos y descripciones individuales, Open Graph, texto alternativo de portadas, enlaces relacionados, datos estructurados Blog/BlogPosting/BreadcrumbList y fechas de actualización en el sitemap.

## Contenido y límites

No hay catálogo de vehículos ni promesas de disponibilidad o financiación. Las categorías son orientativas. Los testimonios son resúmenes de los publicados en https://www.jbcarsmiami.com/ y se indica su procedencia. Instagram proporciona fotografías de referencia, no inventario actualizado.
Las tarjetas usan imágenes transparentes de Toyota Camry, RAV4 y Tacoma, con fuentes documentadas en `recursos/ORIGENES-TOYOTA.md`.
El español está adaptado a la audiencia latina de Miami. El WhatsApp utiliza el número público actual por indicación del propietario; está pendiente su verificación comercial por parte de Jesús. Es una integración mediante enlace a WhatsApp Business; no incluye API de Meta, chatbot ni CRM.
La web conserva enlaces a las políticas publicadas en la web original. El negocio debe confirmar que cubren este nuevo dominio y el contacto mediante servicios externos.
JB Cars es operado por F K BOUQUET CORPORATION y no es la web oficial de Toyota of Hollywood.
Manrope se distribuye bajo SIL Open Font License: `docs/assets/OFL-Manrope.txt`.
