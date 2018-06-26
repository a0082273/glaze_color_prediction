import numpy as np
import pandas as pd


f = open('glz_hg_highfire.txt', 'r')
lines = f.readlines()
f.close

columns = ['Graze name', 'Cone', 'Color', 'Testing', 'Surface', 'Firing', 'Transparency', 'Recipe1', 'Recipe2', 'Recipe3', 'Recipe4', 'Recipe5', 'Recipe6', 'Recipe7', 'Recipe8', 'Recipe9', 'Recipe10']
ind_list = []
for i in range(len(columns)):
   ind_list.append('hogehoge')
all_list = []

# for iline, line in enumerate(lines):
for iline, line in enumerate(lines):
    # print(iline, line)
    # print(ind_list)
    if 'Glaze name:' in line:
        ind_list[0] = line[12:-1]
    elif 'Cone:' in line:
        ind_list[1] = line[6:-1]
    elif 'Color:' in line:
        ind_list[2] = line[7:-1]
    elif 'Testing:' in line:
        ind_list[3] = line[9:-1]
    elif 'Surface:' in line:
        ind_list[4] = line[9:-1]
    elif 'Firing:' in line:
        ind_list[5] = line[8:-1]
    elif 'Transparency:' in line:
        ind_list[6] = line[14:-1]
    elif 'Recipe:' in line:
        for i in range(1, 11):
            line = lines[iline+i]
            print(iline+i, line)
            print(ind_list)
            if 'Comments:' in line:
                for j in range(i, 11):
                    ind_list[6+j] = 'nothing'
                break
            else:
                ind_list[6+i] = line[:-1]
        all_list.append(ind_list[:])
        for i in range(17):
            ind_list[i] = 'hogehoge'
    else:
        pass


df = pd.DataFrame(all_list)
df.columns = columns
print(df)
