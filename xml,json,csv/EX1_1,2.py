#Exercice 1
#1
import re
L = ['marie.Dupond@gmail.com', 'lucie.Durand@wanadoo.fr', 'Sophie.Parmentier@@gmail.com','franck.Dupres.gmail.com', 'pierre.Martin@lip6.fr', 'eric.Deschamps@gmail.com']
S = []

for i in range (0,len(L)) :
    if L[i].count('@') == 1 :
        m = re.match('([^@]+)@([^@]+)', L[i])
        if m.group(2) == 'gmail.com' :
            S.append(L[i])
        else :
            continue

print(S)

#2
a = input("Please write any string ends with number:")
mm = re.match('.*[0-9]+$', a )
if mm == None :
    a = input("you wrote wrong string, please write string end with number : ")
    mm = re.match('.*[0-9]+$', a)
    print(mm)
else :
    print(mm)

'''
m = re.match('([^@]+)@([^@]+)', 'sebastien.tixeuil@lip6.fr' )
print(m.group(1))
print(m.group(2))
'''