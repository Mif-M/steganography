import wave


def fun(text):
    text_finall = ""
    count = 0
    buk = ""
    for i in text:
        if count < 6:
            buk += i
            count += 1
        else:
            buk += i
            f = int(buk, 2)
            f = chr(f)
            text_finall += f
            buk = ""
            count = 0
    return text_finall


if __name__ == '__main__':
    ar = []
    file_wav = wave.open("copy_Pripev.wav", 'rb')
    file_wav.rewind()
    for i in range(file_wav.getnframes()):
        ar.append(file_wav.readframes(1))
    file_wav.rewind()

    text = "".join([bin(i[0])[-1:] for i in ar])

    text_finall = fun(text)

    with open("../Text/finall_text.txt", 'w') as file:
        file.write(text_finall)
    print(text_finall)
