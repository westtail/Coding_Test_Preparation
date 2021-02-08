import sys

_list = []
_list = []

# データの取得を目的
line_all_data = []
for line in sys.stdin:
    line_data = line.strip('\n')
    line_all_data.append(line_data)
print(line_all_data)


_list = line_all_data[0].split(' ')
_list = [int(s) for s in _list]

_list = line_all_data[1].split(' ')

len() 長さ
sort() ソート機能
for i in range():

l_2d = [[0] * 4 for i in range(3)] # 4*3の二次元配列
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
l_2d[0][0] = 100
# [[100, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

#最大値
max_value = max(xs)
max_index = xs.index(max_value)
print(max_index)
#最小値

#配列削除
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l.pop(0))
# 0

# yahoo コーディングテスト

import sys
input = []
for line in sys.stdin:
    input.append(line.rstrip('\n').split())
    #print(input)
    #print(line, end="")

data = list(map(int, input[0]))
word = input[1]
num = 0

dic = {}
for i in range(0,len(data)):
    dic[word[i]] = data[i]
print(dic)
dic_2 = sorted(dic.items())
dic_3 = sorted(dic.items(), key=lambda x:x[1])

print(dic_2,dic_3)

#print(data[0],word[0])
for i in range(0,len(data)):
    if(word[i] == "Alice"):
        num += data[i]
    else:
        continue
    #print(i)
print(num)

httpリクエスト
import urllib.request
url = 'http://192.168.1.103/index.php?name=symfoware'
# getリクエストを実行
response = urllib.request.urlopen(url)
# read()で応答を取得
# 取得できるのはbyte配列なので、decodeで文字列に変換
body = response.read().decode('utf-8')
print(body)



map型
全てがバラバラでないと成り立たない
https://qiita.com/hz1_d/items/407dd13f90a8a4533d23

文字列の分割
https://note.nkmk.me/python-split-rsplit-splitlines-re/





data = list(map(int, input[0]))
# print(data)

dis_list = [] # 曜日間の距離のリスト

# 曜日間の差をlistに代入する
# 問題 日曜日と月曜日の際を気を付ける
# 他に問題はあるか　処理時間→多分問題ない
for i in range(0,len(data)):
    # 日曜日の時
    if i == 6:
        #曜日間の差を出す
        dis = data[6] - data[0]
        # 絶対値にする
        dis = abs(dis)
        dis_list.append(dis)
        #print(dis)
    else:
        #曜日間の差を出す
        dis = data[i] - data[i+1]
        # 絶対値にする
        dis = abs(dis)
        dis_list.append(dis)
        #print(dis)

# listの最大を出力する
max_value = max(dis_list)
print(max_value)

# ゴール 出力値は数値のみ


運動習慣
プログラミング チャレンジの説明:
太郎くんは曜日ごとに決まった時間だけ運動をすることにしています。

太郎くんの曜日ごとの運動時間の長さが与えられるので、連続する 2 日の運動時間の長さの差の絶対値が最大となるときのその値を求めてください。

入力:
標準入力に以下の形式で 7 つの整数が空白区切りで与えられます。 入力データの行末に改行があることに注意してください。

T_mon T_tue T_wed T_thu T_fri T_sat T_sun
T_mon ... 月曜日の運動時間(分)
T_tue ... 火曜日の運動時間(分)
T_wed ... 水曜日の運動時間(分)
T_thu ... 木曜日の運動時間(分)
T_fri ... 金曜日の運動時間(分)
T_sat ... 土曜日の運動時間(分)
T_sun ... 日曜日の運動時間(分)


import sys
input = []
for line in sys.stdin:
    input.append(line.rstrip('\n').split())

N = int(input[0][0])
X = int(input[0][1])
Y = int(input[0][2])

input.pop(0)
table = input
#print(N,X,Y,table)

check_table = table[0]
answer_table = table[1]

# 方針 
# 交換をメインで行う
# ひっくり返すのをokonau
# とりあえずひっくり返す
# 二枚の交換はひっくり返すよりも低コストであれば行う

# てーぶる１とテーブル２が一致すれば終わり
num = 0
while check_table != answer_table:
    # 交換を行う
    for i in range(0,N-1):
        if((check_table[i] == answer_table[i+1]) and (check_table[i+1] == answer_table[i])):
            num += X
            if check_table[i] == "R":
                check_table[i] = "B"
                check_table[i+1] = "R"
            else:
                check_table[i] = "R"
                check_table[i+1] = "B"
    # ひっくり返す
    for i in range(0,N):
        if check_table[i] != answer_table[i]:
            num += Y
            if check_table[i] == "R":
                check_table[i] = "B"
            else:
                check_table[i] = "R"
print(num)

