from PIL import Image, ImageDraw

from lsb_png import function

# Нужно реализовать возможность выбирать бит для хранения информации, но не более третьего
# Нужно реализовать выбор цвета пикселя для записи (красный, зеленый, голубой)
# Нужно добавить хранение конфигурации в файл config.ini

File_original = "Rio/Rio.jpg"
File_return = ""


def main():
    with Image.open("Photo/Test.jpg") as image:
    # with Image.open("../Алгоритм_Коха-Жао/img/Цветы.jpg") as image:
        draw = ImageDraw.Draw(image)
        pix = image.load()
        count = 0
        text = function.BitText()  # Битовое представление текста
        # text = function.bit_file(image.width * image.height)  # Битовое представление текста
        # for i in range(image.size[1]):
        #     for j in range():
        for i in range(image.size[1]-150,image.size[1]-100):
            for j in range(200,image.size[0]-200):
                a = function.PixelOutput((pix[j, i][0]), text[count]) if count < len(text) else (pix[j, i][0])
                count += 1
                b = function.PixelOutput((pix[j, i][1]), text[count]) if count < len(text) else (pix[j, i][1])
                count += 1
                c = function.PixelOutput((pix[j, i][2]), text[count]) if count < len(text) else (pix[j, i][2])
                count += 1
                # draw.point((j, i), (a, pix[j, i][1], pix[j, i][2]))
                draw.point((j, i), (a, b, c))
                # draw.point((j, i), (a, pix[j, i][1], pix[j, i][2]))
                # draw.point((j, i), (a, pix[j, i][1], pix[j, i][2]))
        name = 'container'
        image.save(f"{name}_LSB.png", "PNG")


if __name__ == '__main__':
    main()
