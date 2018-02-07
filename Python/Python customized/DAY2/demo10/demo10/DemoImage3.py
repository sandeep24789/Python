from PIL import Image
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purdemo.png')

im2 = Image.new('RGBA', (20, 20))
im2.save('samtra.png')
