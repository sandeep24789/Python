from PIL import Image
import os
sourcepath="src/"
source = os.listdir(sourcepath)
print(source)
im = Image.open("cartoon.jpg")

print(im.size)

h,w=im.size

print("height : ",h)
print("Width : ",w)
print(im.filename)
print(im.format)
print(im.format_description)


