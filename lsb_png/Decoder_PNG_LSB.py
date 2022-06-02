from PIL import Image, ImageDraw

from lsb_png import function
N = 8

if __name__ == '__main__':
    with Image.open("container_LSB.png") as image:
        pix = image.load()  # Выгружаем значения пикселей.
        text = ""
        for i in range(image.size[1]):
            for j in range(image.size[0]):
                text += bin((pix[j, i][0]))[-1:]
                text += bin((pix[j, i][1]))[-1:]
                text += bin((pix[j, i][2]))[-1:]
        text_final = ""
        buk = ""
        for i in range(N, len(text) - N, N):
            f = chr(int(text[i - N: i], 2))
            text_final += f
        with open("../Text/11.txt", 'w', encoding="utf-8") as file:
            file.write(text_final, )
        print(text_final)
        # function.file_bit_return(text)
