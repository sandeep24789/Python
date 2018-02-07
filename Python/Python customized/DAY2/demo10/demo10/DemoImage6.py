from PIL import Image
im = Image.open("tiger.jpg")
rotIm=im.rotate(180).save("tiger180.jpg")
flippedIm=im.transpose(Image.FLIP_LEFT_RIGHT).save("cartoon_flip2.jpg")
flippedIm=im.transpose(Image.FLIP_TOP_BOTTOM).save("cartoon_flip1.jpg")
