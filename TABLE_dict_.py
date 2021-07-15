user=int(input("enter the number: "))
a=[]
i=1
dic={}
while i<=(user):
    b=[]
    j=1
    a.append(i)
    while j<=10:
        c=i*j
        b.append(c)
        dic[i]=b
        j=j+1
    i=i+1
print(dic)

