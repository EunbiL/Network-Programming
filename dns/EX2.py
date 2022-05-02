#2021.12.8 16:40
import time
import subprocess
import os


cmd=["traceroute google.com | tail -1 | awk \'{print$3}\'"]
#cmd = ["traceroute google.com"]

count = 3
timein = 2
last=''
# tr_new=''
ans=[]
list_dest = []

print("Search for the traces \"google.com\" {} times with interval {} seconds:".format(count, timein))
print("running...")


for i in range (0,count):
    res = subprocess.check_output(cmd, shell=True) #os.system(cmd)
    tr_new = res.decode('utf-8')
    if last != tr_new:
        last = tr_new
        list_dest.append(tr_new)
        with open(f'res_routenew{i}.txt','w') as f:
            f.write(tr_new)
            f.write("___________________________________\n")
    #with open(f."res_routenew{i}.txt",'r' )


    #first execution or update
    #print(tr_new)
    time.sleep(timein)
    print("...{}".format(i+1))

#if

print('the total traces for google.com running {} times with interval {} seconds:'.format(count, timein) )
print(last)


