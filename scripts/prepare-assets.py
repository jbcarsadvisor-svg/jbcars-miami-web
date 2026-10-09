from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[1]
assets = root / 'docs' / 'assets'
sources = {
    'jesus-showroom': 'web-11-jesus-concesionario.png',
    'jesus-interview': 'web-10-entrevista-jesus.png',
    'jesus-portrait': 'web-02-retrato-jesus.png',
    'delivery': 'instagram-01-toyota-hollywood-personas-vehiculo.jpg',
    'pickup': 'instagram-03-pickup-toyota.jpg',
    'couple': 'instagram-04-jesus-con-pareja.jpg',
    'vehicles': 'instagram-02-jesus-junto-vehiculos.jpg',
    'logo': 'web-01-logo-jb-cars.png',
}
for dest, source in sources.items():
    with Image.open(root / 'recursos' / source) as im:
        im.thumbnail((1600, 1600))
        im.save(assets / f'{dest}.webp', 'WEBP', quality=87, method=6)
        if dest == 'jesus-showroom':
            im.thumbnail((800, 800))
            im.save(assets / 'jesus-showroom-small.webp', 'WEBP', quality=85, method=6)
for source in sorted((root / 'recursos').glob('web-0*-medio-*.png')):
    with Image.open(source) as im:
        im.thumbnail((360, 180))
        im.save(assets / (source.stem + '.webp'), 'WEBP', quality=88, method=6)
with Image.open(root / 'recursos' / 'web-01-logo-jb-cars.png') as im:
    im.thumbnail((256, 256))
    im.save(assets / 'logo.png', optimize=True)
print('Optimized assets ready')
