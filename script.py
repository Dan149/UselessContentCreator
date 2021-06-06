import data
from os import system as term
import os
import time
import random
import secrets
import string
import pathlib

def clear():
	if os.name == "nt":
		term("cls")
	else:
		term("clear")

def exit():
	print("\nRemoving pycache...")
	[p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]
	[p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]
	print("End of process.")
	quit()

def main():
	select = input("""
		 __    __    ______   ______ 
		|  |  |  |  /      | /      |
		|  |  |  | |  ,----'|  ,----'
		|  |  |  | |  |     |  |     
		|  `--'  | |  `----.|  `----.
		 \\______/   \\______| \\______|
                             
	Select:
		1- generate random text file
		2- generate several text files
		3- generate random html file
===============================================================
		Q- Quit
>> """)
	if select == "1":
		print("\nGenerating the file...")
		try:
			f = open("output/" + data.names[random.randint(0, len(data.names))] + ".txt", "w+")
			f.write(data.flush_doc_content())
			f.close()
			print("File generated.")
			time.sleep(1.5)
			clear()
		except:
			clear()
			print("[CRITICAL]: failed to generate file.")
		main()
	elif select == "2":
		try:
			amount = int(input(f"\nChose the amount of files (max:{len(data.names)}): "))
		except:
			clear()
			print("[CRITICAL]: input must be a number.")
			main()
		if amount > len(data.names):
			amount = len(data.names)
			print(f"Amount: {amount}.")
		elif amount <= 0:
			amount = 1
			print(f"Amount: {amount}.")
		else:
			print(f"Amount: {amount}.")

		print("\nGenerating the files...")
		for x in range(amount):
			num = x - 1
			f = open("output/" + data.names[num] + ".txt", "w+")
			f.write(data.flush_doc_content())
			f.close()
		print("Files generated.")
		time.sleep(1.5)
		clear()
		main()
	elif select == "3":
		f = open("output/" + data.site_titles[random.randint(0, len(data.site_titles))] + ".html", "w+")
		ask = input("\nInclude a JS script ? [y/N]\n>> ")
		if ask == "y" or ask == "Y" or ask == "yes" or ask == "YES" or ask == "Yes":
			script = input("Enter a script: ")
			print("\nGenerating file...")
			f.write(data.html_template(data.site_titles[random.randint(0, len(data.site_titles))], data.flush_doc_content(), script))
		else:
			print("\nGenerating file...")
			f.write(data.html_template(data.site_titles[random.randint(0, len(data.site_titles))], data.flush_doc_content(), None))
		f.close()
		print("File generated.")
		time.sleep(1.5)
		clear()
		main()
	elif select == "Q":
		exit()
	else:
		clear()
		main()

######################################

clear()
print(f"Available text file names: {len(data.names)}.")
print(f"Available html file names: {len(data.site_titles)}.")
print(f"Available words: {len(data.words)}.")
main()