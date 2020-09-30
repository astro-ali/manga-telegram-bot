# Project Path ---> Desktop\manga bot
import img2pdf
import requests
import os
from bs4 import BeautifulSoup
from dataStructures import *
from PIL import Image

def chooseManga():
	# add feature : the ability to chooseManga function : to the user
	# to choose a specific manga from the website to get manga key.
	print("-------------MANGA LIST-------------")
	for key,value in redable_manga_list.items():
		print(key,value)
	print("------------------------------------")
	print(" Pick the manga you want from the list above...\n")
	manga_key = input("Manga number:")
	chapter_number = input("Chapter number:")
	manga_name = manga_list.get(manga_key)
	return [str("https://manga.ae/"+manga_name+'/'+chapter_number+'/0/full'),manga_code.get(manga_name),manga_name+'_'+chapter_number]

download_queue=[] #it contains a dynamic names of the images

def download(name,url):
	# add feature : try to make the code so that
	# he can catch failding cases to redownloading it 
	# or ignore it and move to the next iteration.
	req=requests.get(url)
	full_name =name+'_'+url.split('/')[-1]
	download_queue.append(full_name)
	with open(full_name,'wb') as file:
		file.write(req.content)
	print(f"[+] Downloaded : {full_name}")
	# return 1

def convert(name):
	print("[+] Waiting To Convert...")
	for img_name in download_queue:
		if isImageDamaged(img_name):
			download_queue.remove(img_name)
			os.remove(img_name)
		if contain_transparency(img_name):
			download_queue.remove(img_name)
			os.remove(img_name)			
	with open(name,'wb') as file:
		file.write(img2pdf.convert(download_queue))
		file.close()
	print("[+] Done ")

def userAnswer(your_question):
	while True:
		answer = str(input('Would you like to '+your_question+'?'+'[yes/no OR y/n]:'))
		if answer in ['yes','y']:
			return True
			break
		elif answer in ['no','n']:
			return False
			break
		else:
			print("OOPS!! Wrong answer, Try again")

def isImageDamaged(image_name):
	# this function is for convertFunction to catch 
	# the damaged images and Except them from the queue.
	file_size = int(os.stat(image_name).st_size)
	if file_size == 0:
		return True
	else:
		return False

def numberOfPages(manga_full_url):
	response = requests.get(manga_full_url)
	soup = BeautifulSoup(response.text,'html.parser')
	end_page = soup.find_all('a')[18].text
	return end_page

def deleteImages(image_names_list):
	# Function : delete the download_queue images
	# of course if the user want that
	for img in image_names_list:
		os.remove(img)
	cwd = os.getcwd()
	os.chdir(cwd)
	print("[+] Images have been deleted")

def contain_transparency(image):
	img = Image.open(image,'r')
	if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
		return True
	else:
		return False

def numberOfChapters():
	pass
