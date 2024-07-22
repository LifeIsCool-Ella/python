from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
#print(sample(lst,1))

users = range(1,21) #1부터 20까지 숫자를 생성
print(type(users))
users = list(users)
print(type(users))

shuffle(users)
print(users)
