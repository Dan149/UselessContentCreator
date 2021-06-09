import data
from os import system as term
import os
import time
import random
import secrets
import string
import pathlib
import json
from fpdf import FPDF

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
		 __    __          ______          ______ 
		|  |  |  |        /      |        /      |
		|  |  |  |       |  ,----'       |  ,----'
		|  |  |  |       |  |            |  |     
		|  `--'  |       |  `----.       |  `----.
		 \\______/seless   \\______|ontent  \\______|reator
                             
	Select:
		1- generate random text file         (with words)
		2- generate several text files       (with words)
		3- generate random html file         (with words)
		4- generate random pdf file          (with words)
		5- generate random json (list) file  (with words)
			------------------------------
		6- generate random text file 	     (without words)
		7- generate several text files	     (without words)
		8- generate random html file         (without words)
		9- generate random pdf file          (without words)
=========================================================================
		C- Credits
		Q- Quit
>> """)
	if select == "1":
		print("\nGenerating the file...")
		try:
			f = open("output/" + data.names[random.randint(0, len(data.names))] + ".txt", "w+")
			f.write(data.flush_doc_content())
			f.close()
			print(" File generated.")
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
		f = open("output/" + secrets.choice(data.site_titles) + ".html", "w+")
		ask = input("\nInclude a JS script ? [y/N]\n>> ")
		if ask == "y" or ask == "Y" or ask == "yes" or ask == "YES" or ask == "Yes":
			script = input("Enter a JS script: ")
			print("\nGenerating file...")
			f.write(data.html_template(secrets.choice(data.site_titles), data.flush_doc_content(), script))
		else:
			print("\nGenerating file...")
			f.write(data.html_template(secrets.choice(data.site_titles), data.flush_doc_content(), None))
		f.close()
		print("File generated.")
		time.sleep(1.5)
		clear()
		main()
	elif select == "4":
		print("\nGenerating the file...")
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font(secrets.choice(data.fonts), size = random.randint(5, 8))
		line = 1
		for x in range(random.randint(20, 40)):
			doc_content = ''.join(secrets.choice(data.words) + " " for i in range(random.randint(10, 15)))
			pdf.cell(200, 10, txt = doc_content, ln = line, align = 'C')
			line = line + 1
		pdf.output("output/" + secrets.choice(data.names) + ".pdf") 
		print("File generated.")
		time.sleep(1.5)
		clear()
		main()
	elif select == "5":
		print("Generating the file...")
		doc = []
		for x in range(random.randint(200, 10000)):
			doc.append(secrets.choice(data.words))
		f = open("output/" + secrets.choice(data.names) + ".json", "w+")
		json_string = json.dumps(doc)
		f.write(json_string)
		f.close()
		print("File generated.")
		time.sleep(1.5)
		clear()
		main()
	elif select == "6":
		print("\nGenerating the file...")
		try:
			f = open("output/" + secrets.choice(data.names) + ".txt", "w+")
			f.write(data.flush_alternative())
			f.close()
			print("File generated.")
			time.sleep(1.5)
			clear()
		except:
			clear()
			print("[CRITICAL]: failed to generate file.")
		main()
	elif select == "7":
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
			f.write(data.flush_alternative())
			f.close()
		print("Files generated.")
		time.sleep(1.5)
		clear()
		main()
	elif select == "8":
		f = open("output/" + secrets.choice(data.site_titles) + ".html", "w+")
		ask = input("\nInclude a JS script ? [y/N]\n>> ")
		if ask == "y" or ask == "Y" or ask == "yes" or ask == "YES" or ask == "Yes":
			script = input("Enter a JS script: ")
			print("\nGenerating file...")
			f.write(data.html_template(secrets.choice(data.site_titles), data.flush_alternative(), script))
		else:
			print("\nGenerating file...")
			f.write(data.html_template(secrets.choice(data.site_titles), data.flush_alternative(), None))
		f.close()
		print("File generated.")
		time.sleep(1.5)
		clear()
		main()
	elif select == "9":
		print("\nGenerating the file...")
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font(secrets.choice(data.fonts), size = random.randint(5, 8))
		line = 1
		for x in range(random.randint(20, 40)):
			doc_content = ''.join(secrets.choice(string.printable) for i in range(random.randint(40, 65)))
			pdf.cell(200, 10, txt = doc_content, ln = line, align = 'C')
			line = line + 1
		pdf.output("output/" + secrets.choice(data.names) + ".pdf")
		print("File generated.")
		time.sleep(1.5)
		clear()
		main()
	elif select == "C":
		clear()
		print("Copyright Daniel Falkov 2021, all rights reserved.")
		main()
	elif select == "Q":
		exit()
	else:
		clear()
		main()

######################################

clear()
print(f"Available text and pdf file names: {len(data.names)}.")
print(f"Available html file names and website titles: {len(data.site_titles)}.")
print(f"Available words: {len(data.words)}.")
main()