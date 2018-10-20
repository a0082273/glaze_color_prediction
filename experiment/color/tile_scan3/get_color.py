import os.path
import sys
from PIL import Image
import numpy as np
import statistics
import colorsys
import glob
import pandas as pd


def crop_center(in_img, infilename):
    in_width, in_height = in_img.size
    crop_width, crop_height = in_width//3, in_height//3 #中心付近1/3の範囲をトリミング
    crop_img = in_img.crop(((in_width - crop_width)//2,
                            (in_height - crop_height)//2,
                            (in_width + crop_width)//2,
                            (in_height + crop_height)//2))
    crop_img.save('./crop/'+infilename[21:-4]+'_crop'+'.jpg')
    return crop_img


# def get_rgb_mean_std(rgb):
#     rgb_mean = np.ndarray(3)
#     for i in range(3):
#         rgb_mean[i] = statistics.mean(rgb[:, i])
#     print ("RGB mean: {}, {}, {}".format(rgb_mean[0], rgb_mean[1], rgb_mean[2]))

#     rgb_std = np.ndarray(3)
#     for i in range(3):
#         # rgb_std[i] = statistics.pstdev(rgb[:, i])
#         rgb_std[i] = statistics.pstdev(rgb[:, i])
#     print ("RGB std: {}, {}, {}".format(rgb_std[0], rgb_std[1], rgb_std[2]))

#     return rgb_mean, rgb_std


# def get_hsv_mean_std(rgb):
#     hsv = np.ndarray(rgb.shape)
#     for i in range(rgb.shape[0]):
#         hsv[i, 0], hsv[i, 1], hsv[i, 2] = colorsys.rgb_to_hsv(
#             rgb[i, 0]/255, rgb[i, 1]/255, rgb[i, 2]/255)
#     hsv[:, 0] = hsv[:, 0]*360
#     hsv[:, 1] = hsv[:, 1]*100
#     hsv[:, 2] = hsv[:, 2]*100

#     hsv_mean = np.ndarray(3)
#     for i in range(3):
#         hsv_mean[i] = statistics.mean(hsv[:, i])
#     print ("HSV mean: {}, {}, {}".format(hsv_mean[0], hsv_mean[1], hsv_mean[2]))

#     hsv_std = np.ndarray(3)
#     for i in range(3):
##         hsv_std[i] = statistics.pstdev(hsv[:, i])
#         hsv_std[i] = statistics.stdev(hsv[:, i])
#     print ("HSV std: {}, {}, {}".format(hsv_std[0], hsv_std[1], hsv_std[2]))

#     return hsv_mean, hsv_std


# def output_rgb(rgb_mean, rgb_std):
#     data = pd.read_excel('./character_data.xlsx', index_col=0)



# def output_hsv(img_size, hsv_mean, hsv_std, infilename):




def main():
    infilenames = glob.glob('./unclassified_image/*')
    for infilename in infilenames:
        in_img = Image.open(infilename)
        crop_img = crop_center(in_img, infilename)
        # rgbed_img = crop_img.convert("RGB")
        # rgb = np.array(rgbed_img.getdata())
        # rgb_mean, rgb_std = get_rgb_mean_std(rgb)
        # hsv_mean, hsv_std = get_hsv_mean_std(rgb)
        # output_rgb(rgb_mean, rgb_std)
        # output_hsv(hsv_mean, hsv_std)



if __name__ == '__main__':
    main()
