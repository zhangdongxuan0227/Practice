#__author__ = 'think'
#coding=utf-8
'''
sum=0
for i in range(101):
    sum=sum+i
print(sum)

sum=0
n=101
while n>0:
    sum=sum+n
    n=n-2
print(sum)
'''
s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)