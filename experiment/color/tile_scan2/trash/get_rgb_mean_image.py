from PIL import Image
import numpy as np
import statistics

img = Image.open('tile_scan2-10.jpg')
hsved_img = img.convert("HSV")
hsv = np.array(hsved_img.getdata())


h_mean = statistics.mean(hsv[:, 0])
s_mean = statistics.mean(hsv[:, 1])
v_mean = statistics.mean(hsv[:, 2])
print ("{}, {}, {}".format(h_mean, s_mean, v_mean))

h_std = statistics.pstdev(hsv[:, 0])
s_std = statistics.pstdev(hsv[:, 1])
v_std = statistics.pstdev(hsv[:, 2])
print ("{}, {}, {}".format(h_std, s_std, v_std))


width, height = img.size
img2 = Image.new('HSV', (width, height))
alpha = 1.6
for j in range(width):
    for k in range(height):
        img2.putpixel((j, k),(int(np.random.normal(h_mean,h_std*alpha)), int(np.random.normal(s_mean,s_std*alpha)), int(np.random.normal(v_mean,v_std*alpha))))
img2.save('tile_scan2-10_mean_std.jpg')
