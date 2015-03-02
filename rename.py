import os 
import shutil
from bs4 import BeautifulSoup

#tranverse all html in review, parse it, write it to txt in test0 
# in review have two files 
# create files in des = /home/li206/test" + str(count) +  .txt

def main():
	path = "/Users/Liyang/www.ign.com/"
	des = "/Users/Liyang/hw2/html/"
	count = 1

	
	for root, dirs, files in os.walk(path):
		for i in files:
			#original path of file, change format to get url 
			file_path = os.path.join(root, i)
			for ch in ["/Users/Liyang/", "index.html"]:
				if ch in file_path:
					file_path = file_path.replace(ch, '')
			#rename html name and copy to des html folder
			os.rename(os.path.join(root, i), os.path.join(root, "lwang49_" + str(count) + ".html"))
			shutil.copy(new,des)
			#new path after rename
			html_path = os.path.join(root, "lwang49_" + str(count) + ".html")
			#txt files in test folder
			name = "/Users/Liyang/hw2/txt/" + "lwang49_"+ str(count) + ".txt"
			#open file, and write url to it
			file = open('%s' % name, 'w')
			file.write(file_path +"\n")
			#beautifulsoup parse html and read tile and content to file; close file
			html = open(html_path).read()
			soup = BeautifulSoup(html)
			links = soup.find_all("title")
			for link in links:
				file.write(link.text.encode('utf-8'))
				file.write("\n")
			g_data = soup.find_all("div", {"class": "messageContent"})
			for data in g_data: 
				file.write(data.text.encode('utf-8'))
			file.close() 
			count +=1
main()



