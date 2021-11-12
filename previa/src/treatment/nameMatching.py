
men_players = open("../../data/raw/men_players.csv","r", newline='\n', encoding= 'utf-8')
men_players_fix = open("../../data/interim/men_players.csv","w", newline='\n', encoding= 'utf-8')
names = open("../../data/interim/players_names_non_duplicates.csv","r", newline='\n', encoding= 'utf-8')
allnames = names.read()

num_lines_players = sum(1 for _ in men_players)
men_players.seek(0,0)
#num_lines_players.readline()

for _ in range(num_lines_players - 1):
    item = men_players.readline().replace('\x00','').split(',')
    if(len(item[1])>0):
        initial = item[1][0] #first letter of the first name
        lastnames = item[2].split(" ")
        for l in lastnames:
            if(len(l)>1):
                if l+" "+initial+'.' in allnames:
                    if len(item[6])<1:
                        item[6] = '180'
                    men_players_fix.write(l+" "+initial+".,"+item[3]+","+item[4]+","+item[5]+","+item[6]+"\n")
                    allnames = allnames.replace(item[2]+" "+initial+".",'')
        '''if(item[2]+" "+initial+"." in allnames):
            men_players_fix.write(item[2]+" "+initial+".,"+item[3]+","+item[4]+","+item[5]+","+item[6]+"\n")
            allnames = allnames.replace(item[2]+" "+initial+".",'')'''