# JB Cars Miami: investigación para una web de captación

Fecha: 9 de octubre de 2026.

## Objetivo y alcance

Preparar una nueva web con prioridad móvil para captar oportunidades de compra de coches y ayudar al asesor a convertirlas en conversaciones, citas y ventas. Esta entrega contiene investigación y una propuesta de implementación; no se han instalado skills, construido la web ni activado servicios de pago.

Se consultaron las páginas públicas de los repositorios y el contenido accesible de la web actual. No se realizó una auditoría visual en dispositivos ni una medición de rendimiento de la web actual. La utilidad propuesta de cada recurso para JB Cars es criterio de diseño, no evidencia de un incremento garantizado de conversiones.

## Hallazgo sobre la web actual

Fuente: https://www.jbcarsmiami.com/

El contenido inicial presenta el libro y el perfil profesional de Jesús F. Bouquet Meinhardt, con referencias a formación de equipos y gestión financiera. Más abajo aparecen testimonios de compradores y un formulario con nombre, apellido, email y teléfono. El pie identifica el negocio como asesor independiente.

Interpretación: el comienzo comunica autoridad profesional, pero la propuesta para quien quiere comprar un coche tarda en aparecer. Conviene abrir con el servicio al comprador, dar una acción concreta y acercar los testimonios al primer punto de contacto. El libro y las publicaciones pueden apoyar la sección de autoridad.

## Los 10 repositorios seleccionados

| Nº | Repositorio | Tipo | Aportación documentada | Aplicación propuesta |
| --- | --- | --- | --- | --- |
| 1 | [anthropics/skills](https://github.com/anthropics/skills) | Skills | `frontend-design`: dirección visual, tipografía y composición deliberadas. | Diseñar una identidad propia para JB Cars con fotografía real y una jerarquía clara. [Skill concreta](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md). |
| 2 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Skill y recursos de diseño | Sistemas visuales, paletas, fuentes, patrones de landing y recomendaciones de UX. | Definir colores, espaciado, componentes y comportamiento móvil consistentes. |
| 3 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Skills de marketing | Conversión, copywriting, SEO, analítica y operaciones comerciales. | Priorizar `cro`, `copywriting`, `product-marketing`, `analytics`, `seo-audit`, `schema` y `revops`. La versión consultada consolida `page-cro` y `form-cro` en `cro`. |
| 4 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Skills técnicas | `react-best-practices` y `web-design-guidelines`, con accesibilidad, formularios, interacción táctil y rendimiento. | Revisar implementación y experiencia móvil durante la construcción. |
| 5 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | Componentes | Componentes accesibles, componibles y personalizables. | Botones, campos, selectores, FAQs y navegación adaptados a la marca. |
| 6 | [magicuidesign/magicui](https://github.com/magicuidesign/magicui) | Componentes visuales | Componentes y efectos animados para interfaces React. | Usar detalles visuales puntuales si ayudan a la experiencia y pasan los controles de rendimiento. Opcional. |
| 7 | [vercel/next.js](https://github.com/vercel/next.js) | Framework web | Framework React para aplicaciones web. | Candidato si se necesitan páginas por vehículo, contenido dinámico y backend de leads. Para una landing sencilla se puede usar una solución más ligera. |
| 8 | [react-hook-form/react-hook-form](https://github.com/react-hook-form/react-hook-form) | Formularios | Gestión del estado y validación de formularios. | Formulario progresivo con errores claros y datos conservados al retroceder. Requiere backend para guardar y entregar leads. |
| 9 | [plausible/analytics](https://github.com/plausible/analytics) | Analítica | Analítica web con eventos, objetivos y opciones cloud o autoalojadas. | Medir campañas, contactos y formularios. El servicio cloud tiene suscripción y autoalojar requiere operación propia. |
| 10 | [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | Auditoría | Auditorías automatizadas de rendimiento, accesibilidad y buenas prácticas. | Detectar problemas antes del lanzamiento y complementar pruebas reales en móviles. |

La selección reúne habilidades y herramientas que cumplen funciones distintas; no implica instalar los diez repositorios. La reutilización debe respetar la licencia del recurso concreto y separar componentes gratuitos de servicios o productos comerciales.

## Propuesta de experiencia móvil

1. Primera pantalla: una promesa clara de asesoría al comprador, fotografía real y botón principal «Encontrar mi coche». Texto provisional: «Tu próximo coche en Miami, con asesoría en español». Confirmar idioma y alcance del servicio antes de publicar.
2. Contacto visible: acceso a llamada y, si el negocio lo utiliza, WhatsApp. Barra inferior que no tape contenido, campos ni el teclado.
3. Captación: probar formulario breve frente a uno progresivo. Preguntar tipo de coche, rango de presupuesto y plazo de compra; cerrar con nombre y teléfono. Pedir email solo si aporta valor al seguimiento.
4. Confianza: testimonios verificables, fotos reales de entregas y una presentación breve de Jesús cerca de los botones de contacto.
5. Proceso: explicar cómo se recibe la solicitud, se proponen opciones y se coordina la compra.
6. Oferta: mostrar vehículos solo si hay disponibilidad real y un proceso para actualizarla. Si el broker busca por encargo, presentar categorías y el servicio de búsqueda.
7. Objeciones: preguntas sobre el servicio, costes, financiación y cambios de vehículo según lo que realmente ofrezca el negocio. Evitar promesas de aprobación o precios sin confirmar.
8. Idiomas: español e inglés como propuesta para Miami; confirmar la audiencia antes de fijar el contenido.
9. Entrega del lead: guardar la solicitud en servidor, confirmar recepción y enviarla al sistema comercial elegido. Añadir protección contra spam y registro de fallos.
10. Seguimiento: conservar campaña y procedencia con el lead para poder relacionar visitas, conversaciones y ventas.

## Habilidades necesarias, por orden

- Oferta y posicionamiento: explicar para quién es el servicio y por qué contactar.
- Copywriting y conversión: titulares, llamadas a la acción y reducción de fricción.
- Diseño móvil: lectura, controles táctiles, teclado y navegación.
- Confianza: contenido real, referencias verificables y expectativas claras.
- Ingeniería de formularios: validación, guardado fiable y entrega al asesor.
- Medición y ventas: atribución, cualificación, citas y resultado comercial.
- SEO local: páginas útiles sobre servicios y zonas realmente atendidas.
- Rendimiento y accesibilidad: imágenes optimizadas, carga ligera y revisión en dispositivos.

## Medición de éxito

- Clic en WhatsApp o llamada: intención de contacto; no confirma conversación ni lead recibido.
- Inicio y abandono del formulario: permiten localizar fricción.
- `lead_saved`: emitir tras confirmación del guardado en servidor.
- Lead cualificado, cita y venta: confirmar desde el proceso comercial o CRM.
- Analizar tasa de leads cualificados, coste por lead cualificado y ventas por campaña. La analítica web por sí sola no confirma ventas.

El número de leads dependerá también del tráfico, la oferta, el presupuesto de captación y la atención comercial. Primero conviene establecer una línea base y después probar cambios con suficiente información.

## Orden recomendado de ejecución

1. Confirmar servicios, zona, audiencia, identidad visual, contenido real y destino de los leads.
2. Definir oferta, textos y recorrido móvil con las skills de marketing y diseño.
3. Construir una primera versión con formulario conectado y contacto directo.
4. Revisar móviles, accesibilidad, entrega de leads y rendimiento.
5. Activar medición y ajustar campañas y página según leads cualificados y ventas.

Pila candidata para una web con contenido dinámico: Next.js, componentes shadcn/ui y React Hook Form. Magic UI es opcional. La elección final depende del alojamiento, la necesidad de inventario y quién mantendrá la web.
