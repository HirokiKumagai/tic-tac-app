#%%
from fractions import Fraction
from math import floor
a     = int(input())
b, c  = list(map(int, input().split(' ')))
str   = input()

sum   = a + b + c
print(f'{sum}' + " " +str)
# %%
a, b = tuple(map(int, input().split(' ')))

num = a * b

if num % 2 == 0:
  print(num)
  print("Even")
else:
  print(num)
  print("Odd")
  
# %%

num_list = list(int, input().split())
num_lists = list(map(int, num_list).split(','))
print(num_lists)
sum = 0
for num in num_list:
  sum += num
print(sum)
# %%
cnt = int(input())
num = list(map(int, input().split(" ")))

def check(cnt, num):
  check_cnt = 0
  for value in num:
    if value % 2 ==0:
      check_cnt += 1

  if cnt == check_cnt:
    return list(map(lambda x: x/2, num))
  else:
    return num

chk_cnt = 0
while num != check(cnt, num):
  num = check(cnt, num)
  chk_cnt += 1
else:
  print(chk_cnt)
# %%
f_hund  = int(input()) + 1
hund    = int(input()) + 1
ten     = int(input()) + 1
sum_cnt = int(input())

cnt = 0

for i in range(f_hund):
  for k in range(hund):
    for j in range(ten):
      if sum_cnt == 500 * i + 100 * k + 50 * j:
        cnt += 1
print(cnt)
# %%
num, a, b = tuple(map(int, input().split(" ")))
sum_list= []
for t in range(num + 1):
  tmp = [int(x) for x in list(str(t))]
  s   = sum(tmp)
  if s >= a and s<= b:
    tmp = "".join(list(map(str, tmp)))
    sum_list.append(int(tmp))
print(sum(sum_list))
# %%
num = input()
print(type(num))
num = list(map(int, num))
num = sum(num)
print(num)
# %%

a, b = tuple(map(int, input().split(" ")))

tmp = 1 - b/a
print(tmp)
# %%
