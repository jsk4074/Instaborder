import os
from PIL import Image, ImageOps
import random

def line():
    print('-'*45)

print('original file path in constant')
print(os.path.dirname(os.path.realpath(__file__)))

def defaultdir():
    line()
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    print('changeing file path')
    print("before: %s"%os.getcwd())
    os.chdir("test 1")
    print("after: %s"%os.getcwd())

defaultdir()

line()
print('file content saved as list in ver a')
a = os.listdir(os.getcwd())
print(a)


line()
print('renameing the files to random')
for i in range(len(a)):
    os.rename(a[i], str(random.random()*10000000000000000)+'.jpg')
print('finished renameing the files to random name')

line()
print('file content saved as list in ver a')
a = os.listdir(os.getcwd())
print(a)

line()
print('renameing the files')
i=0
for i in range(len(a)):
    os.rename(a[i], str(i)+'.jpg')
print('finished renameing the files')

line()
print('file content saved as list in ver a')
a = os.listdir(os.getcwd())
print(a)

line()
print('prossing image')
i=0
for i in range(len(a)):
    line()
    print('image %d size'%i)
    im = Image.open(a[i])
    print(im.size)
    inimg = im.size
    if inimg[0]<inimg[1]:
        greater = inimg[1]
    else:
        greater = inimg[0]
    print(greater)
    img = Image.open(a[i])
    img_with_border = ImageOps.expand(img,border=int(9*greater/40),fill='white')
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    os.chdir("result")
    print("dir changed to result")
    img_with_border.save('%d border.jpg'%i)
    print('%d border.jpg'%i+' rough save done')
    line()
    print('%d border.jpg'%i+' cropping')
    imc = Image.open('%d border.jpg'%i)
    print(imc.size)
    inimg = imc.size
    if inimg[0]<inimg[1]:
        small = inimg[0]
        big = inimg[1]
    else:
        small = inimg[1]
        big = inimg[0]
    croprait = int((big-small)/2)
    cropImage = imc.crop((croprait, 0, croprait+small, small))
    print("big is %d"%big)
    print("small is %d"%small)
    print("croprait is %d"%croprait)
    print(cropImage.size)
    cropImage.save('%d iborder.jpg'%i)
    os.remove('%d border.jpg'%i)
    defaultdir()

line()
print("border intensity is 16%")
