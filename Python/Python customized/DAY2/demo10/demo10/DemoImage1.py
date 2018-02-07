from PIL import Image
im = Image.open("cartoon.jpg")
print(im.format, im.size, im.mode)

