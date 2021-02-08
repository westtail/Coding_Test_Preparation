# coding: UTF-8

#リストを用意
number_list = []
hit_number = 0

#データ読み込み
f = open('square.txt')

# １行目読み込み
line = f.readline()

#２行目以降読み込み
for i in range(0,3):
    for j in range(0,3):
        number_list.append(line[j*2]) 
    line = f.readline()
f.close()

for i in range(0,3):
    if(number_list[i*3] == number_list[i*3+1] and number_list[i*3+1] == number_list[i*3+2]):
        hit_number = hit_number + 1
    if(number_list[i] == number_list[i+3] and number_list[i+3] == number_list[i*6]):
        hit_number = hit_number + 1
if(hit_number > 0):
    print("valid")
else:
    print("invalid")
