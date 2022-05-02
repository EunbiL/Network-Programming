import subprocess

adress = ''
#cmd = ['ifconfig', 'wlp1s0', '|', 'head', '-2', '|', 'tail', '-1', '|', 'awk', '\'{print$2}\'']
cmd = ['ifconfig wlp1s0 | head -2 | tail -1 | awk \'{print$2}\'']
res = subprocess.check_output(cmd, shell= True)
adress = res.decode('utf-8')[:-1]
print("adress is", adress)

a = adress.split('.')
b = list(map(int,a))
#print(b)
#print(b[-1])

for i in range (1,255) :
    newcmd = ['ping -c 1 '+str(b[0])+'.'+str(b[1])+'.'+str(b[2])+'.'+str(i)]
    #print(newcmd)
    try:
        newres = subprocess.check_output(newcmd,shell= True)
        ping = newres.decode('utf-8')
        '''if ping.count("100% packet loss,") == 1:
            print("no ping")
            continue
        else :'''
        print("---------------------------------")
        print("ping result:\n")
        print(ping)
        print()

    except subprocess.CalledProcessError as e:
        #print (e.returncode)
        print ("{} cannot ping".format(newcmd))
        print()
        #print (e.output)