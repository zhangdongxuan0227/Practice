__author__ = 'think'
# coding = utf-8
#s=('we are happy')
#a=','.join(s.split('%20'))
#a=s.replace(' ','%20')
#a=s.split(' ')

#print (a)
def splitchar(s):
    str2=s.replace(' ','%20')
    return str2



userinfo = input("enter:")

print(splitchar(userinfo))





