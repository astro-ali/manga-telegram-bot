# Project Path ---> Desktop\manga bot
from functions import *
import requests
from dataStructures import *
import re

# working[0] == manga_url
# working[1] == manga_code
# working[2] == manga_name for the PDF file

def main():
	working = chooseManga()
	end_Page = numberOfPages(working[0])

	print(f"[+] Total Pages to download : [{end_Page}]")
	print("[+] Waiting for downloading...")

	manga_link = working[0]
	req = requests.get(manga_link)
	img_links = re.findall(f'src="(https://manga.ae/cdn/{working[1]}/(.*?))"',req.text)

	os.mkdir(working[2])
	cwd = os.getcwd()
	folder_path = str(str(cwd)+R"\\"+str(working[2]))
	os.chdir(folder_path)

	failed_cases = 0

	for url,path in img_links:
		try:
			download(working[2],url)
		except:
			failed_cases += 1
			# try to delete the fialed cases in the 
			# dwonload queue lsit
			continue

	print(f"\n[+] Failed Cases : [{failed_cases}]\n")
	# # IF the user answer is true then convert to PDF and if it's false then don't

	if userAnswer("convert the images to DPF"):
		convert(working[2]+".pdf")
	else:
		print("Thank you for using our Manga downloader\nEnjoy!")

	if userAnswer("delete the images"):
		deleteImages(download_queue)
		print("Thank you for using our Manga downloader\nEnjoy!")
	else:
		print("Thank you for using our Manga downloader\nEnjoy!")


if __name__ == '__main__':main()


