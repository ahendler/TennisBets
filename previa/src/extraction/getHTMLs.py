#Download Men and Woman Instagram pages 
import urllib.request
from time import sleep
from os.path import exists

accounts_men = open("../../data/raw/menInstagram2019.csv", newline='\n', encoding= 'utf-8')
accounts_women = open("../../data/raw/womenInstagram2019.csv", newline='\n', encoding= 'utf-8')
num_lines_men = sum(1 for _ in accounts_men)
num_lines_women = sum(1 for _ in accounts_women)
accounts_men.seek(0,0)
accounts_men.readline()
accounts_women.seek(0,0)
accounts_women.readline()

for _ in range(num_lines_men - 1):
	item = accounts_men.readline().replace('\x00','').split(',')
	# if the file already exists, it does not request it again
	if(not exists("../../data/raw/menInstagramHTMLs/"+item[0]+".html")):
		urllib.request.urlretrieve(item[-1], "../../data/raw/menInstagramHTMLs/"+item[0]+".html")
		#sleep(61) #avoids getting blocked by Instagram - might be better off without it
for _ in range(num_lines_women - 1):
	item = accounts_women.readline().replace('\x00','').split(',')
	if(not exists("../../data/raw/womenInstagramHTMLs/"+item[0]+".html")):
		urllib.request.urlretrieve(item[-1], "../../data/raw/womenInstagramHTMLs/"+item[0]+".html")
		#sleep(61)

accounts_men.close()
accounts_women.close()