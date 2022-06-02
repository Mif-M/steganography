import numpy as np
from PIL import Image
from scipy.fft import dct

from lsb_png import function

K = 150
N = 8
I, J = 4, 5
X, Y = 5, 4

def bloc_1(arr):
    MatYCbCr = []
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
            MatYCbCr.append((Matrix))
        height = 0
        width += N
    return (MatYCbCr)


def decoder(ar_3):
    Bit = ""
    for i in range(len(ar_3)):
        A = (ar_3[i][I][J])
        B = (ar_3[i][X][Y])
        if abs(A) > abs(B):
            Bit += '1'
        elif abs(A) < abs(B):
            Bit += '0'
    return Bit


if __name__ == '__main__':
    # image = Image.open("../video/Frame_Decoder_2/frame1800.jpg")
    image = Image.open("index.jpg")
    im = image.load()
    # image_REG = []
    # for i in range(image.size[0]):
    #     ima = []
    #     for j in range(image.size[1]):
    #         # ima.append(im[i, j][0])
    #         ima.append(im[i, j][1])
    #         # ima.append(im[i, j][2])
    #     image_REG.append(ima)
    channelG = np.array(image.getchannel('G')).transpose()
    print("Получили пиксели красного цвета")
    image_bloc = (bloc_1(channelG))
    print("Разбили их на блоки по 8х8")
    # дискретное косинусное преобразование
    for i in range(len(image_bloc)):
        image_bloc[i] = dct(image_bloc[i], norm='ortho')
    print("Применили к блокам ДКП")
    text = decoder(image_bloc)
    print("Раскодировали блоки")
    text_final = ''
    # function.file_bit_return(text)
    for i in range(8, len(text) - 8, 8):
        f = chr(int(text[i - 8: i], 2))
        text_final += f

    # with open("../Text/11.txt", 'w', encoding="utf-8") as file:
    #     file.write(text_final, )
    print(text_final)
