import numpy as np
from PIL import Image, ImageDraw

from lsb_png import function

if __name__ == '__main__':
    # with Image.open("Photo/R") as image:
    #     pass
    # name = 'C:/Users/Mif/Desktop/Coder_PNG/container_LSB.png'
    name = 'Photo/Test_59%.jpg'
    # name = '../Алгоритм_Коха-Жао/index.jpg'
    # open('')
    with Image.new("RGB", (Image.open(name).size[0], Image.open(name).size[1])) as image:
        draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
        pix = Image.open(name).load()  # Выгружаем значения пикселей.
        text = function.BitText()  # Битовое представление текста
        # yuv_img = Image.open(name).convert('YCbCr')  # to convert from YCrCb/yuv to rgb
        # y, cb, cr = yuv_img.split()  # to get individual components
        # Cb = np.asarray(cb)
        for i in range(image.size[1]):
            for j in range(image.size[0]):

                a = pix[j, i][0]
                b = pix[j, i][1]
                c = pix[j, i][2]
                # draw.point((j, i), (a, 0, 0))
                # draw.point((j, i), (0 if b % 2 else 255, 0 if b % 2 else 255, 0 if b % 2 else 255))
                draw.point((j, i), (0 if a % 2 else 255, 0 if b % 2 else 255, 0 if c % 2 else 255))
                # draw.point((j, i), (0 if a % 2 else 255, 0 if b % 2 else 255, 0 if c % 2 else 255))
        image.save("Визуализация_59%_JPEG_изображения.png", "PNG")
        # image.save("visualization_A_B_C.png", "PNG")
        # image.save("visualization_A_B_C.png", "PNG")
        # image.save("visualization_A_B_C.png", "PNG")
