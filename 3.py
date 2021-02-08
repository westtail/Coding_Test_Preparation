# coding: UTF-8
import requests

list = ['dragon','griffin','medusa','troll','vampire']
list2 = []
win_list = []
rate_list = []

for i in range(4):
    for j in range(4-i):
            url = 'https://ob6la3c120.execute-api.ap-northeast-1.amazonaws.com/Prod/battle/'+ list[i] + '+' + list[i+j+1]
            response = requests.get(url)
            r = response.json()
            list2.append(r['winner'])
            
for k in range(5):
    win_list.append(sum(x==list[k] for x in list2))

for n in range(5):
    rate_list.append(win_list.index(n))

for f in range(5):
    print(f+1,list[rate_list[4-f]])