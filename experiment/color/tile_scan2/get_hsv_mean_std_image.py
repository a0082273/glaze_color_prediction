import os.path
import sys
from PIL import Image
import numpy as np
import statistics
import colorsys



def get_rgb_mean_std(rgb):
    rgb_mean = np.ndarray(3)
    for i in range(3):
        rgb_mean[i] = statistics.mean(rgb[:, i])
    print ("RGB mean: {}, {}, {}".format(rgb_mean[0], rgb_mean[1], rgb_mean[2]))

    rgb_std = np.ndarray(3)
    for i in range(3):
        rgb_std[i] = statistics.pstdev(rgb[:, i])
    print ("RGB std: {}, {}, {}".format(rgb_std[0], rgb_std[1], rgb_std[2]))

    return rgb_mean, rgb_std


def get_hsv_mean_std(rgb):
    hsv = np.ndarray(rgb.shape)
    for i in range(rgb.shape[0]):
        hsv[i, 0], hsv[i, 1], hsv[i, 2] = colorsys.rgb_to_hsv(rgb[i, 0]/255, rgb[i, 1]/255, rgb[i, 2]/255)
    hsv[:, 0] = hsv[:, 0]*360
    hsv[:, 1] = hsv[:, 1]*100
    hsv[:, 2] = hsv[:, 2]*100

    hsv_mean = np.ndarray(3)
    for i in range(3):
        hsv_mean[i] = statistics.mean(hsv[:, i])
    print ("HSV mean: {}, {}, {}".format(hsv_mean[0], hsv_mean[1], hsv_mean[2]))

    hsv_std = np.ndarray(3)
    for i in range(3):
        hsv_std[i] = statistics.pstdev(hsv[:, i])
    print ("HSV std: {}, {}, {}".format(hsv_std[0], hsv_std[1], hsv_std[2]))

    return hsv_mean, hsv_std


def output_rgb(img_size, rgb_mean, rgb_std, infilename, memofilename):
    width, height = img_size
    img = Image.new('RGB', (width, height))
    name, ext = os.path.splitext(infilename)
    outfilename = name+'_RGB_mean_std'+ext
    alpha = 1.6
    #alpha = 1.0
    for i in range(height):
        for j in range(width):
            r = np.random.normal(rgb_mean[0],rgb_std[0]*alpha)
            g = np.random.normal(rgb_mean[1],rgb_std[1]*alpha)
            b = np.random.normal(rgb_mean[2],rgb_std[2]*alpha)
            img.putpixel((j, i),(int(r),int(g),int(b)))
    img.save(outfilename)

    memo = open(memofilename, 'a')
    memo.write(infilename+"\n")
    memo.write("RGB mean: {}, {}, {}".format(rgb_mean[0], rgb_mean[1], rgb_mean[2])+"\n")
    memo.write("RGB std: {}, {}, {}".format(rgb_std[0], rgb_std[1], rgb_std[2])+"\n")
    memo.close


def output_hsv(img_size, hsv_mean, hsv_std, infilename, memofilename):
    width, height = img_size
    img = Image.new('RGB', (width, height))
    name, ext = os.path.splitext(infilename)
    outfilename = name+'_HSV_mean_std'+ext
    alpha = 1.6
    # alpha = 1.0
    for i in range(width):
        for j in range(height):
            h = np.random.normal(hsv_mean[0],hsv_std[0]*alpha)/360
            s = np.random.normal(hsv_mean[1],hsv_std[1]*alpha)/100
            v = np.random.normal(hsv_mean[2],hsv_std[2]*alpha)/100
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            r = r*255
            g = g*255
            b = b*255
            img.putpixel((i, j),(int(r),int(g),int(b)))
    img.save(outfilename)

    memo = open(memofilename, 'a')
    memo.write("HSV mean: {}, {}, {}".format(hsv_mean[0], hsv_mean[1], hsv_mean[2])+"\n")
    memo.write("HSV std: {}, {}, {}".format(hsv_std[0], hsv_std[1], hsv_std[2])+"\n")
    memo.write("\n")
    memo.close



# infilename = sys.argv[1]
for i in range(10):
    infilename = "tile_scan2-"+str(i+1)+".jpg"
    memofilename = 'mean_std.txt'

    inimg = Image.open(infilename)
    rgbed_img = inimg.convert("RGB")
    rgb = np.array(rgbed_img.getdata())

    rgb_mean, rgb_std = get_rgb_mean_std(rgb)
    hsv_mean, hsv_std = get_hsv_mean_std(rgb)
    output_rgb(inimg.size, rgb_mean, rgb_std, infilename, memofilename)
    output_hsv(inimg.size, hsv_mean, hsv_std, infilename, memofilename)
