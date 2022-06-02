import wave


def BitText(inputText=open("../Text/text.txt").read()):  # Перевод текста в биты
    ar = [str(format(ord(elem), 'b')) for elem in inputText]
    textReturn = ""
    for item in range(len(ar)):
        if len(ar[item]) < 7:
            ar[item] = '0' * (7 - len(ar[item])) + ar[item]
            textReturn += ('0' * (7 - len(ar[item])) + ar[item])
            continue
        textReturn += ar[item]
    return textReturn


def PixelOutput(pixel, b):
    if pixel % 2 != int(b):
        pixel = (pixel + 1) if pixel < 255 else (pixel - 1)
    return bytes([pixel])


if __name__ == '__main__':
    name_file = "mus/boom.wav"
    name_coder_file = "Pripev.wav"
    ar = []
    file_wave = wave.open(name_file, 'rb')
    file_wave.rewind()
    for i in range(file_wave.getnframes()):
        ar.append(file_wave.readframes(1))
    file_wave.rewind()
    file_wave.close()
    textar = BitText()
    for i in range(len(ar)):
        if i < len(textar):
            a = PixelOutput((ar[i][0]), textar[i])
            ar[i] = a + ar[i][1:]

    file_write_wav = wave.open("copy_" + name_coder_file, 'wb')
    file_write_wav.setparams(file_wave.getparams())
    file_write_wav.writeframesraw(b''.join(ar))
    file_write_wav.close()

