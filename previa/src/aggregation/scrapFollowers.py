from os.path import exists
import io

men_2021 = open("../../data/external/menInstagram2021.csv","r+", newline='\n', encoding= 'utf-8')
women_2021 = open("../../data/external/womenInstagram2021.csv","r+", newline='\n', encoding= 'utf-8')

accounts_men = open("../../data/raw/menInstagram2019.csv", newline='\n', encoding= 'utf-8')
accounts_women = open("../../data/raw/womenInstagram2019.csv", newline='\n', encoding= 'utf-8')

num_lines_men = sum(1 for _ in accounts_men)
num_lines_women = sum(1 for _ in accounts_women)
accounts_men.seek(0,0)
accounts_men.readline() #skips the titles
accounts_women.seek(0,0)
accounts_women.readline()

for _ in range(num_lines_men - 1):
    item = accounts_men.readline().replace('\x00','').split(',')
    men_2021.seek(0,0)
	# if the file exists and is not in the table
    if(exists("../../data/raw/menInstagramHTMLs/"+item[0]+".html")):
        if(item[0] not in men_2021.read()):
            men_2021.seek(0, io.SEEK_END)
            men_html_file = open("../../data/raw/menInstagramHTMLs/"+item[0]+".html","r", encoding= 'utf-8')
            men_html = men_html_file.read()
            followers_start = men_html.find("edge_followed_by") + 27 # find in the html file the start of the value of followers
            followers = men_html[followers_start:men_html.find("}",followers_start)] # finds the end of the value
            men_2021.write(item[0]+";"+followers+"\n")
            men_html_file.close()

for _ in range(num_lines_women - 1):
    item = accounts_women.readline().replace('\x00','').split(',')
    women_2021.seek(0,0)
	# if the file exists and is not in the table
    if(exists("../../data/raw/womenInstagramHTMLs/"+item[0]+".html")):
        if(item[0] not in women_2021.read()):
            women_2021.seek(0, io.SEEK_END)
            women_html_file = open("../../data/raw/womenInstagramHTMLs/"+item[0]+".html","r", encoding= 'utf-8')
            women_html = women_html_file.read()
            followers_start = women_html.find("edge_followed_by") + 27 # find in the html file the start of the value of followers
            followers = women_html[followers_start:women_html.find("}",followers_start)] # finds the end of the value
            women_2021.write(item[0]+";"+followers+"\n")
            women_html_file.close()

men_2021.close()
women_2021.close()

accounts_men.close()
accounts_women.close()