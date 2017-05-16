#coding=utf-8
#__author__ = 'think'

#age=100
def cpage(age):
    print("your age is:",age)
s=input("age:")
age=int(s)
if age>=6 and age<18:
    cpage(age)
    print("kid")
elif age>=18 and age<60:
    cpage(age)
    print("teenager")
elif age>=60 and age<100:
    cpage(age)
    print("elder")
else:
    print("decedent")
