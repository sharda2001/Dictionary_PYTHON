x="MISSISSIPPI"
list1=list(x)
list2=[]
dic={}
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
for j in range (len(list2)):       
        count=0
        for j in range(len(list1)):
			if list2[i]==list1[j]:
				count=count+1
				dic[list2[i]]=count
print(dic)