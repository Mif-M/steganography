import glob
import os
from multiprocessing import Process

from PIL import Image, ImageDraw
from scipy.fftpack import dct, idct

K = 150  # относительная величина влияющая на устойчивость к преобразованию
N = 8  # Размер блока ДКП
I, J = 4, 5  # позиция коэффициента в этом блоке
X, Y = 5, 4  # позиция коэффициента в этом блоке


def BitText(inputText=open("../Text/Text30.txt").read()):  # Перевод текста в биты
    N = 8
    ar = [str(format(ord(elem), 'b')) for elem in inputText]
    textReturn = ""
    for item in range(len(ar)):
        if len(ar[item]) < N:
            ar[item] = '0' * (N - len(ar[item])) + ar[item]
            textReturn += ('0' * (N - len(ar[item])) + ar[item])
            continue
        textReturn += ar[item]
    return textReturn


def bloc_1(arr):  # Функция превращающая двумерный массив в трехмерный массив хранящий двумерные массивы по N
    MatYCbCr = []  # Трехмерный возвращаемый массив
    N = 8
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


def bloc_return(arr, Width, Height):  # функция востановления двумерного массива из трех мерного
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
    # print(i // 64)


def coder_Thread(start, stop, arrfilename):
    count = start
    for filename in arrfilename[start:stop]:
        image = Image.open(filename)  # Открываем изображение
        im = image.load()
        image_REG = []  # Массив пикселей выбранного цвета
        for i in range(image.size[0]):
            ima = []
            for j in range(image.size[1]):
                ima.append(im[i, j][1])
            image_REG.append(ima)
        # print("Получили пиксели красного цвета")
        image_bloc = (bloc_1(image_REG))
        # print("Разбили их на блоки 8х8")
        # дискретное косинусное преобразование
        for index in range(len(image_bloc)):
            image_bloc[index] = dct(image_bloc[index], norm='ortho')

        # print("Применили ДКП")

        # Кодирование блоков контейнера
        coder(image_bloc, BitText())
        # coder(image_bloc, function.bit_file(image.height*image.width))
        # print("Сделали сокрытие информации")
        # обратное дискретное косинусное преобразование
        for i in range(len(image_bloc)):
            image_bloc[i] = idct(image_bloc[i], norm='ortho')

        # print("Выполнили обратное ДКП")
        # Раскрытие блоков контейнера
        image_bloc = bloc_return(image_bloc, image.size[0], image.size[1])

        # print("Выполнили обратное востановление блоков в двумерный массив пикселей красного цвета")
        # Запись данных в изображение
        coder_image = img = Image.new("RGB", (image.width, image.height))
        draw = ImageDraw.Draw(coder_image)
        for i in range(image.size[1]):
            for j in range(image.size[0]):
                # draw.point((j, i), (int(image_bloc[j][i]), im[j, i][1], im[j, i][2]))
                draw.point((j, i), (im[j, i][0], (image_bloc[j][i]), im[j, i][2]))
                # draw.point((j, i), (im[j, i][0], im[j, i][1], int(image_bloc[j][i])))
                # draw.point((j, i), (im[j, i][0], im[j, i][1], im[j, i][2]))
        print("Выполнили запись в изображение ", f'Frame/frame{count}.jpg')
        coder_image.save(f'Frame_Coder/frame{count}.jpg', "JPEG")
        count += 1


if __name__ == '__main__':
    filenames = sorted(glob.glob('Frame/frame*.jpg'), key=os.path.getmtime)
    N = len(filenames)
    step = N // 8
    Process(target=coder_Thread, args=(0, step, filenames)).start()
    Process(target=coder_Thread, args=(step, 2 * step, filenames)).start()
    Process(target=coder_Thread, args=(2 * step, 3 * step, filenames)).start()
    Process(target=coder_Thread, args=(3 * step, 4 * step, filenames)).start()

    Process(target=coder_Thread, args=(4 * step, 5 * step, filenames)).start()
    Process(target=coder_Thread, args=(5 * step, 6 * step, filenames)).start()
    Process(target=coder_Thread, args=(6 * step, 7 * step, filenames)).start()
    Process(target=coder_Thread, args=(7 * step, N, filenames)).start()

    # pr1.join()
    # pr2.join()
    # pr3.join()
    # pr4.join()
