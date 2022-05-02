#3
import re

a = input("Write the adress of IPV4 (form is nnn.nnn.nnn.nnn):")
m = re.match('\d+\.\d+\.\d+\.\d+',a)
if m == None :
    print("you wrote wrong adress, please try again . ")
    exit()
l = a.split('.')
for i in range (0,len(l)) :
    mm = re.match('^[^0]',l[i])
    if mm == None :
        s = int(l[i])
        str(s)
        print(s)
        l[i] = str(s)

#print(l)
for j in range (0,len(l)) :
    l[j] = int(l[j])
print("you address is : ", l)