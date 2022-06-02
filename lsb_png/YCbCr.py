# import cv2
# img = cv2.imread("../lsb_png/RGB/RGB.jpg")
#
# img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
#
# cv2.imwrite("YCrCb.jpg", img_ycrcb)
from array import array

# import numpy as np
# from PIL import Image, ImageDraw
#
# # name = "../lsb_png/RGB/RGB.jpg"
# rgb_img = Image.open("../Алгоритм_Коха-Жао/18224.jpg")
# pix = rgb_img.load()
# # R, G, B = rgb_img.convert('RGB').split()
# # R = np.array(R)
# # G = np.array(G)
# # B = np.array(B)
# print(np.array(rgb_img.getchannel('G')))
# yuv_img = rgb_img.convert('YCbCr')  # to convert from YCrCb/yuv to rgb
# y, cb, cr = yuv_img.split()  # to get individual components
# print(np.array(y.im))
# a = np.asarray(y)
# b = np.asarray(cb)
# c = np.asarray(cr)
# a = Image.fromarray(a)
# b = Image.fromarray(b)
# c = Image.fromarray(c)
# merged_ycbcr = Image.merge('YCbCr', (a, b, c))
# merged_ycbcr.save("Cr.jpeg", "JPEG")

# from PIL import Image
# import matplotlib.pyplot as plt
#
# im = Image.open("../lsb_png/RGB/RGB.jpg")
# ycbcr = im.convert('YCbCr')
#
# print(ycbcr.getbands())
#
# (y, cb, cr) = ycbcr.split()
#
# plt.figure()
# plt.title("Original")
# plt.imshow(im)
#
# plt.figure()
# plt.subplot(131)
# plt.title("Y")
# plt.imshow(y, cmap="gray")
# plt.subplot(132)
# plt.title("Cb")
# plt.imshow(cb, cmap="Blues")
# plt.subplot(133)
# plt.title("Cr")
# plt.imshow(cr, cmap="Reds")
# plt.show()

from PIL import Image

if __name__ == '__main__':
    im = Image.open('../lsb_png/RGB/RGB.jpg')
    r, g, b = im.split()
    # Одноканальное отображение изображения
    r.show()
    # Большое количество каналов порядка, слияния
    im1 = Image.merge("RGB", (r, g, b))
    im1.show()
