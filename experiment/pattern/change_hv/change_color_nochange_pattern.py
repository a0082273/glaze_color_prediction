import os.path
import sys
from PIL import Image
import numpy as np
import statistics
import colorsys




def rgb2hsv(rgb):
# hsv means normalized hsv
    hsv = np.ndarray(rgb.shape)
    for i in range(rgb.shape[0]):
        hsv[i, 0], hsv[i, 1], hsv[i, 2] = colorsys.rgb_to_hsv(rgb[i, 0]/255, rgb[i, 1]/255, rgb[i, 2]/255)

    return hsv



def hsv2rgb(hsv):
# hsv means normalized hsv
    rgb = np.ndarray(hsv.shape)
    for i in range(hsv.shape[0]):
        rgb[i, 0], rgb[i, 1], rgb[i, 2] = colorsys.hsv_to_rgb(hsv[i, 0], hsv[i, 1], hsv[i, 2])
    rgb[:, 0] = rgb[:, 0]*255
    rgb[:, 1] = rgb[:, 1]*255
    rgb[:, 2] = rgb[:, 2]*255

    return rgb



def get_out_hsv(pattern_hsv, color_hsv):
    out_hsv = np.ndarray(pattern_hsv.shape)

    diff = statistics.mean(pattern_hsv[:, 0])-statistics.mean(color_hsv[:, 0])
    out_hsv[:, 0] = pattern_hsv[:, 0]-diff

    out_hsv[:, 1] = pattern_hsv[:, 1]

    diff = statistics.mean(pattern_hsv[:, 2])-statistics.mean(color_hsv[:, 2])
    out_hsv[:, 2] = pattern_hsv[:, 2]-diff

    return out_hsv



def output(img_size, rgb, out_file):
    width, height = img_size
    img = Image.new('RGB', (width, height))
    counter = 0
    for i in range(height):
        for j in range(width):
            img.putpixel((j, i), (int(rgb[counter, 0]), int(rgb[counter, 1]), int(rgb[counter, 2])))
            counter += 1
    img.save(out_file)




pattern_file = sys.argv[1]
color_file = sys.argv[2]
pattern_name, pattern_ext = os.path.splitext(pattern_file)
color_name, color_ext = os.path.splitext(color_file)
out_file = "pattern_"+pattern_name+"__color_"+color_name+pattern_ext

pattern_img = Image.open(pattern_file)
color_img = Image.open(color_file)
rgbed_pattern_img = pattern_img.convert("RGB")
rgbed_color_img = color_img.convert("RGB")

pattern_rgb = np.array(rgbed_pattern_img.getdata())
color_rgb = np.array(rgbed_color_img.getdata())
pattern_hsv = rgb2hsv(pattern_rgb)
color_hsv = rgb2hsv(color_rgb)

out_hsv = get_out_hsv(pattern_hsv, color_hsv)
out_rgb = hsv2rgb(out_hsv)
output(pattern_img.size, out_rgb, out_file)
