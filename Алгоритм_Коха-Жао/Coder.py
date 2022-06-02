import glob
import os

import numpy as np
from PIL import Image, ImageDraw
from scipy.fftpack import dct, idct

from lsb_png import function

K = 150  # относительная величина влияющая на устойчивость к преобразованию
N = 8  # Размер блока ДКП
I, J = 4, 5  # позиция коэффициента в этом блоке
X, Y = 5, 4  # позиция коэффициента в этом блоке


def bloc_1(arr):  # Функция превращающая двумерный массив в трехмерный массив хранящий двумерные массивы по N
    MatYCbCr = []  # Трехмерный возвращаемый массив
    width = 0
    height = 0
    while width < len(arr):
        while height < len(arr[1]):
            Matrix = []
            for i in range(N):
                matrix = []
                for j in range(N):
                    element = 0
                    if width + i >= len(arr) and height + j < len(arr[1]):
                        element = arr[-1][height]
                    elif width + i >= len(arr) and height + j >= len(arr[1]):
                        element = arr[-1][-1]
                    elif width + i < len(arr) and height + j >= len(arr[1]):
                        element = arr[width + i][-1]
                    else:
                        element = arr[width + i][height + j]
                    matrix.append(element)
                Matrix.append(matrix)
            height += N
            MatYCbCr.append(Matrix)
        height = 0
        width += N
    return MatYCbCr  # !!!!!!!!Функция не оптимальна и будет обрезать некоторые части изображения


def bloc_return(arr, Width, Height):  # функция востановления двумерного массива из трехмерного
    width = 0
    height = 0
    Matrix_return = []
    for i in range(Width):
        matrix = []
        for j in range(Height):
            matrix.append(0)
        Matrix_return.append(matrix)
    for z in arr:
        height = height % Height
        width = width % Width
        for i in range(len(z)):
            for j in range(len(z[0])):
                Matrix_return[width + i][height + j] = int(z[i][j])
        height += len(z)
        width += len(z) if height % Height == 0 else 0
    return Matrix_return


def coder(ar_3, bit):  # Функция кодирования информации в блок коэффициентов ДКП
    for i in range(len(ar_3)):
        if i < len(bit):
            A = (ar_3[i][I][J])
            B = (ar_3[i][X][Y])
            Bit = int(bit[i])
            if Bit == 0 and (abs(A) - abs(B)) <= -K:
                continue
            elif Bit == 1 and (abs(A) - abs(B)) >= K:
                continue
            elif Bit == 1 and not ((abs(A) - abs(B)) >= K):
                ar_3[i][I][J] = abs(K + abs(B) + 1)
                ar_3[i][I][J] = ar_3[i][I][J] if A > 0 else -ar_3[i][I][J]
                continue
            elif Bit == 0 and not ((abs(A) - abs(B)) <= -K):
                ar_3[i][X][Y] += (abs(A) - abs(B) + K + 1)
                ar_3[i][X][Y] = ar_3[i][X][Y] if B > 0 else -ar_3[i][X][Y]
                continue
        else:
            break
    print(i // 64)


if __name__ == '__main__':
    image = Image.open("../lsb_png/Photo/Test.jpg")
    im = image.load()

    # channelR = np.array(image.getchannel('R'))
    channelG = np.array(image.getchannel('G')).transpose()  # Массив пикселей выбранного цвета
    # channelB = np.array(image.getchannel('B'))
    # channelG = []
    # for i in range(image.size[0]):
    #     ima = []
    #     for j in range(image.size[1]):
    #         ima.append(im[i, j][1])
    #     channelG.append(ima)

    print("Получили пиксели красного цвета")
    image_bloc = (bloc_1(channelG))
    print("Разбили их на блоки 8х8")
    # дискретное косинусное преобразование
    for index in range(len(image_bloc)):
        image_bloc[index] = dct(image_bloc[index], norm='ortho')
    print("Применили ДКП")
    # Кодирование блоков контейнера
    coder(image_bloc, function.BitText())
    # coder(image_bloc, function.bit_file(image.height*image.width))
    print("Сделали сокрытие информации")
    # обратное дискретное косинусное преобразование
    for i in range(len(image_bloc)):
        image_bloc[i] = idct(image_bloc[i], norm='ortho')

    print("Выполнили обратное ДКП")
    # Раскрытие блоков контейнера
    image_bloc = bloc_return(image_bloc, image.size[0], image.size[1])

    print("Выполнили обратное востановление блоков в двумерный массив пикселей красного цвета")
    # Запись данных в изображение

    draw = ImageDraw.Draw(image)
    for i in range(image.size[1]):
        for j in range(image.size[0]):
            draw.point((j, i), (im[j, i][0], (image_bloc[j][i]), im[j, i][2]))
    print("Выполнили запись в изображение")
    image.save("index.jpg", "JPEG")
