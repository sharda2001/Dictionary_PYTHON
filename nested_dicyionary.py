a={"introduction":[{"name":"sharda","course":"python","age":"20"},{"name":"sikha","course":"java","age":23}]}
# i=0
# b=[]
# while i<len(a["introduction"]):
#     b.append(a["introduction"][i]["name"])
#     # print(b)
#     i=i+1
# print(b)

i=0
b={ }
while i<len(a["introduction"]):
    if i==0:
        b["me"]=a["introduction"][i]["name"]
    else:
        b["friend"]=a["introduction"][i]["name"]
    i=i+1
print(b)

# i=0
# b=[]
# dict={}
# while i<len(a["introduction"]):
#     b.append(a["introduction"][i]["name"])
#     b=dict
#     i=i+1
# print(b)



