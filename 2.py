# coding: UTF-8

#リストを用意
kabu_list = []
buy_list = []
sell_list = []
rieki_list = []

#データ読み込み
f = open('prices.txt')
line = f.readline()
f.close()

#リストを数字化
kabu_list = line.split(' ')
kabu_list = [int(s) for s in kabu_list]

# 株データの長さ
kabu_long = len(kabu_list)

# 最も利益の出る株のデータを取得
for i in range(0,kabu_long):
    buy_list.append(kabu_list[i])
    sell_list.append(max(kabu_list[i:kabu_long]))
    rieki_list.append(sell_list[i] - buy_list[i])

rieki = rieki_list.index(max(rieki_list))

print("buy " , buy_list[rieki] ,"sell",sell_list[rieki])

print(buy_list,sell_list,rieki_list,rieki)

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