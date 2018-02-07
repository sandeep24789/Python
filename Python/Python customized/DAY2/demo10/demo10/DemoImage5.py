from PIL import Image
im = Image.open("tiger.jpg")
tiger_copy=im.copy()

face = im.crop((155, 25, 565, 430))
print(face.size)
width,height=face.size

face=face.resize((210,205))
width,height=face.size
print(face.size)

tiger_copy.paste(face,(0,0))
tiger_copy.save('resizeface.jpg')
