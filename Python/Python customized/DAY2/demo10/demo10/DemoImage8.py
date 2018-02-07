from PIL import Image
from PIL import ImageColor
im = Image.new('RGBA', (300, 300))

for x in range(300):
    for y in range(100):
         im.putpixel((x, y), ImageColor.getcolor('orange', 'RGBA'))


for x in range(300):
    for y in range(101, 200):
         im.putpixel((x, y), ImageColor.getcolor('white', 'RGBA'))

for x in range(300):
    for y in range(201, 300):
         im.putpixel((x, y), ImageColor.getcolor('green', 'RGBA'))

im.save('sample.png')
