# 一些四位数,百位数字都是3,十位数字都是6,并且它们
# 既能被2整除,又能被 3整除,求这样的四位数中最大的和最小的两数各是几?
# 千位a  百位3  十位6  个位b
a=0
b=0
li = []
while True:
    a=a+1
    b=b+1
    if(a*1000+300+60+b)%3==0 and (a*1000+300+60+b)%2==0 :
        li.append(a*1000+300+60+b)
        print(a*1000+300+60+b)
        break
print(max(li))
# print(min(li))



