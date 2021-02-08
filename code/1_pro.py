# https://atcoder.jp/contests/abc042/tasks/abc042_a

from sys import stdin

A, B, C = [int(x) for x in stdin.readline().rstrip().split()]

list = [A,B,C]

if(list.count(5) == 2 and list.count(7) == 1):
    print("YES")
else:
    print("NO")