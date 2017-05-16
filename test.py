#__author__ = 'think'
#coding=utf-8

"""
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
"""

#height=1.75
#weight=80.5
def bmi(a,b):
    return b/(a*a)
height=float(input("a:"))
weight=float(input("b:"))
BMI=bmi(height,weight)
print ("BMI:")
if BMI<18.5:
    #bmi()
    print("过轻")
elif BMI>=18.5 and BMI<25:
    #bmi()
    print ("正常")
elif BMI>=25 and BMI<28:
    print ("过重")
elif BMI>=28 and BMI<32:
    print ("肥胖")
else:
    print("严重肥胖")