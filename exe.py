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
print(min(li))

