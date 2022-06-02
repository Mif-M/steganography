import struct

N = 8


def BitText(inputText=open("../Text/11.txt").read()):  # Перевод текста в биты
    ar = [str(format(ord(elem), 'b')) for elem in inputText]
    textReturn = ""
    for item in range(len(ar)):
        if len(ar[item]) < N:
            ar[item] = '0' * (N - len(ar[item])) + ar[item]
            textReturn += ('0' * (N - len(ar[item])) + ar[item])
            continue
        textReturn += ar[item]
    return textReturn


def PixelOutput(pixel, b):
    if pixel % 2 != int(b):
        pixel = (pixel + 1) if pixel < 255 else (pixel - 1)
    return pixel


def bit_file(cout):
    file_name = open("Love2.jpg", "rb")
    # file_name = open("../Text/text.txt", "rb")
    # читаем строку
    l = file_name.read()
    textReturn = ''
    for c, i in enumerate(l):
        if c > cout:
            return textReturn
        item = bin(i)[2:]
        if len(item) < N:
            textReturn += str('0' * (N - len(item)) + item)
            continue
        textReturn += item
    return textReturn


def file_bit_return(bit_file):
    bute_arr = []
    for i in range(0, len(bit_file) - N, N):
        s = "0b" + (bit_file[i:i + N])
        # print(chr(int(s,2)))
        bute_arr.append((int("0b" + (bit_file[i:i + N]), 2)))
    b = bytes(bute_arr)
    # file_input = open("file_input.txt", "wb")
    file_input = open("Photo/file_input.jpg", "wb")
    file_input.write(b)


