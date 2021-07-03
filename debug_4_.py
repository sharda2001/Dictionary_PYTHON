# Python code to merge dict using update() method
def Merge(dict1, dict2):
    return(dict2.update(dict1))
     
# Driver code
dict1={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
dict2={'python':20,"gaurav":300,'dev':34,"karan":43}
 
# This return None
print(Merge(dict1, dict2))
 
# changes made in dict2
print(dict2) 