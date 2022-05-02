#4
import re

a = (input("write your birthday (forme is MM-DD-YYYY):"))
m = re.match('\d\d-\d\d-\d\d\d\d',a)
if m == None :
    print("please check again, form is MM-DD-YYYY")
    exit()
print(m)
mdy = a.split('-')
print(mdy)
dmy =['','','']
dmy[0] = mdy[1]
dmy[1] = mdy[0]
dmy[2] = mdy[2]
print(dmy)
print("Your DD-MM-YYYY is",dmy[0],'-',dmy[1],'-',dmy[2])