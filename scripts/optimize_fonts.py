from pathlib import Path
from fontTools.ttLib import TTFont

root = Path(__file__).resolve().parents[1]
for path in (root/'docs'/'assets').glob('*.ttf'):
    font = TTFont(path)
    font.flavor = 'woff2'
    font.save(path.with_suffix('.woff2'))
css_path = root/'docs'/'styles.css'
css_path.write_text(css_path.read_text(encoding='utf-8').replace('.ttf','.woff2').replace("format('truetype')","format('woff2')"),encoding='utf-8')
html_path = root/'docs'/'index.html'
html_path.write_text(html_path.read_text(encoding='utf-8').replace('manrope-800.ttf','manrope-800.woff2').replace('type="font/ttf"','type="font/woff2"'),encoding='utf-8')
print('WOFF2 fonts optimized')
