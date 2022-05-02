import time
import subprocess
import os
cmd="/usr/bin/dig google.com | grep \'google.com\' | tail -1 | awk \'{print $5}\'"
#cmd=["/usr/bin/dig google.com", "|" , "grep 'google.com'" , "|" , "tail -1", "|" , "awk '{print $5}'"]

count = 10
ip_old=''
ip_new=''
ans=[]
t = 3

for i in range (0,count):
    res = subprocess.check_output(cmd, shell=True) #os.system(cmd)
    ip_new = res.decode('utf-8')[:-1]
    print( res )

    #first execution or update
    if ip_new != ip_old:
        #print(ip_new)
        ip_old = ip_new
        ans.append(ip_new)

    time.sleep(t)

print('the total ips for google.com running {} times with interval {}seconds:'.format(count, t))
print(ans)


