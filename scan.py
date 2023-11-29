#!/usr/bin/env python3
#version = '1.0.2'
try:
	import requests
	from colorama import Fore
	import os
	import sys
	from progress.bar import Bar	# module for loading
except:
	print("Require Module Not Found \n Try pip3 install -r requirement.txt")
	exit()


red = Fore.RED
yellow = Fore.YELLOW
green = '\033[1;32;40m'
white = '\033[0;37;40m'
blue = Fore.BLUE

extimate = []

def banner():	# banner
	print(yellow)
	## logo
	print(f"""  {yellow}
                                           
                              .\                                  
                        .\   / _\   .\                                       
                       /_ \   ||   / _\                               
                        ||    ||    ||                                            
                        ||    ||    ||                                             
                 ; ,     \`.__||__.'/                                          
         |\     /( ;\_.;  `..__ __.'                                         
         ' `.  _|_\/_;-'_ .' '||                                        
          \ _/`       `.-\_ / ||      _
      , _ _`; ,--.   ,--. ;'_ ||      |                                                                                  
      '`''\| /  ,-\ | _,-\ |/'||   _  |                                        
       \ .-- \__\_o//` )o/ --.||   |  |       _                                       
       /    .         -'  .    \ --|--|--.  .' \                                        
      |     /             \     |  |  |   \ |---'                                                
   .   .  -' `-..____...-' `-  .   |  |    |\  _                                         
.'`'.__ `._      `-..-''    _.'|   |  | _  | `-'      _                                              
 \ .--.`.  `-..__    _,..-'   L|   |    |             |                                                
  '    \ \      _,| |,_      /_7)  |    |   _       _ |  _                                          
        \ \    /       \ _.-'/||        | .' \     _| |  |                                                       
         \ \  /.'|   |`.__.'` ||     .--| |--- _   /| |  |                                                              
          \ `//_/     \       ||    /   | \  _ \  / | |  |                                            
           `/ \|   .   |      ||   |    |  `-'  \/  | '--|      _                                       
            `"`'.  _  .'      ||    `--'|                |   .--/                                              
                 \ | /        ||                         '--'                                                          
                  |'|         'J    :::𝔻𝔼𝕧𝕚𝕃-𝔸𝕕𝕞𝕚𝕟𝕊𝕔𝕒𝕟𝕟𝕖𝕣:::                                                                           
               .-.|||.-.                                                                                                       
              '----"----'   




{red} 
  """)




# open and list
def open_list():
	print("Linee di lettura...")
	f = open('list.txt', 'r')
	admin_list = f.readlines()
	print(f"{yellow}{len(admin_list)} ✅ numero Linee di lettura trovate in list.txt!")

	scan(admin_list)

# scan
def scan(admin_list):
	global extimate
	print(blue)
	url = input("Inserisci il sito web da scansionare 🔎 ... \n[example http://www.1234fakeweb.com]: ")
	try:
		requests.get(url)
	except:
		print(f"{red}⚠️ Errore Url sbagliato o server giù! ")
		print(f"{blue}Example Url: http://www.fakeweb.com")
		print(f"{blue}Example Url: http://fakeweb.com")

	# make sure the url
	if url[-1] == '/':
		url_length = len(url) - 1
		url = url[0:url_length]	# pure url to requests

	else:
		pass

	print(green)
	bar = Bar(':::𝔻𝔼𝕧𝕚𝕃-𝔸𝕕𝕞𝕚𝕟𝕊𝕔𝕒𝕟𝕟𝕖𝕣::: Attendere ⌛', max=len(admin_list)) # loading
	for lines in admin_list:
		lines_len = len(lines)	  # lenght of lines
		minus_len = lines_len -1 # minus 1 from length of lines
		link = lines[0:minus_len] # url to requests
		scan = url + '/' + link
		try:
			# Scanning
			r = requests.get(scan)
			if r.status_code == 200:
				# admin url found
				extimate.append(scan)	# add to extimate admin url list
				bar.next()
			else:
				# admin url not found
				bar.next()
		except:
			pass

	bar.finish()
	print("")
	print("Grazie alla prossiama scansione 🕵️‍♂️ ")
        
	# print out the extimate admin url list
	print("  :::𝔻𝔼𝕧𝕚𝕃-𝔸𝕕𝕞𝕚𝕟𝕊𝕔𝕒𝕟𝕟𝕖𝕣::: ")
	print("")
	print(f"{'*' * 3}Elenco degli Url del pannello amministrativo trovati ✅{'*' * 3}")	
	for links in extimate:
		print(links)
	print(white)

# fun to start program
def final_fun():
	banner()
	open_list()
	# open_list will start the scan fun:


if __name__ == '__main__':
	final_fun()

else:
	print("⚠️ Error ")
	# ulteriore modificazione:
	print(f"{red}⚠️ Error {white}")

#revisione: ElaNyx03 2023