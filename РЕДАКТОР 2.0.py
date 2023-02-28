from PIL import Image, ImageDraw, ImageFont, ImageFilter
from easygui import *

path = fileopenbox()
img = Image.open(path)

def vod_znak(a,b):
    idraw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial", size=b)
    idraw.text((10, 10), a, font=font)
    img.save('result.png')

def osvet(a):
    width,height = img.size
    for i in range(width):
        for j in range(height):
            r, g ,b = img.getpixel((i,j))
            img.putpixel((i,j),(int(a * r),int(a * g),int(a * b)))

    img.save("result.png")

def cvadrat(a,b):
    for i in range(0,a): #сколько рядов мы меняем
        for j in range(0,b):  #заполняем ряд по ширине
            img.putpixel((i, j), (0, 255 , 0)) 
    img.save("result.png")

def chb():
    width,height = img.size

    for i in range(width):
        for j in range(height):
            r,g,b = img.getpixel((i,j))
            img.putpixel((i,j),(int(r*0.212+g*0.715+b*0.0746),int(r*0.212+g*0.715+b*0.0746),int(r*0.212+g*0.715+b*0.0746)))

    img.save("result.png")

def negative():
    width,height = img.size

    for i in range(width):
        for j in range(height):
            r,g,b = img.getpixel((i,j))
            img.putpixel((i,j),(int(255 - r),int(255 - g),int(255 - b)))

    img.save("result.png")

def converter(a):
    if a == 'jpg':
        img.save("result.jpg")
    if a == 'png':
        img.save("result.png")

def croppp(a, b, c, d):
    result = img.crop((a, b, c, d))
    result.save("result.png")

def resizer(a, b):
    result = img.resize(((int(a),int(b))))
    result.save("result.png")

def vstr_filters(a):
    if a == 1: 
        coef = int(input('На сколько сильно применить фильтр (только для blur): '))
        result = img.filter(ImageFilter.GaussianBlur(coef))
        result.save("result.png")
    if a == 2:
        result = img.filter(ImageFilter.DETAIL)
        result.save("result.png")
    if a == 3:
        result = img.filter(ImageFilter.CONTOUR)
        result.save("result.png")
    if a == 4:
        result = img.filter(ImageFilter.EDGE_ENHANCE)
        result.save("result.png")
    if a == 5:
        result = img.filter(ImageFilter.EMBOSS)
        result.save("result.png")
    if a == 6:
        result = img.filter(ImageFilter.SHARPEN)
        result.save("result.png")
    if a == 7:
        result = img.filter(ImageFilter.SMOOTH)
        result.save("result.png")


while True:
    q = ['Обрезать','Изменить размер','Наложить улучшающий фильтр','Конвертировать в другой формат (png/jpg)','Наложить негатив','Сделать фото ЧБ','Зелёный квадратик(метка)','Засвет','Водяной знак','Выход']
    a = buttonbox('Что делать с картинкой?', image = path, choices = q)
    if a == 'Выход':
        break
    elif a == 'Обрезать':
        b = []
        variants = ['x1','y1','x2','y2']
        b = multenterbox('Введи координаты для обрезки','Обрезка',variants)
        x1 = int(b[0])
        y1 = int(b[1])
        x2 = int(b[2])
        y2 = int(b[3])
        print(x1,y1,x2,y2)
        croppp(x1,y1,x2,y2)
        msgbox('Результат:', image = 'result.png')
    elif a == "Изменить размер":
        b = []
        variants = ['Ширина','Высота']
        b = multenterbox('введи новые ширину и высоту','Изменение размера',variants)        
        width = int(b[0])
        height = int(b[1])
        resizer(width,height)
        msgbox('Результат:', image = 'result.png')       