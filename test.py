from PIL import Image
import os
import img2pdf


os.chdir(R"C:\Users\Ali\Desktop\MyPython Project\Selenium\manga bot\1shinge-kino-kyojin_132")

images = []

for img in os.listdir():
	if img.endswith('.JPG'):
		images.append(img)

for img in images:
	print(img)
print("---------------------------------")

def contain_transparency(image):
	img = Image.open(image,'r')
	if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
		return True
	else:
		return False

def convert(name):
	print("[+] Waiting To Convert...")
	for img_name in images:
		if contain_transparency(img_name):
			images.remove(img_name)
			os.remove(img_name)			
	with open(name,'wb') as file:
		file.write(img2pdf.convert(images))
		file.close()
	print("[+] Done ")

convert('attack on titan.pdf')
