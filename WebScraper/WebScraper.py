import bs4 as bs
import urllib.request
import os.path


#Getting the target site
site= 'https://tl.wikipedia.org/wiki/Pangulo_ng_Pilipinas'

#Openning the Site
sauce = urllib.request.urlopen(site).read()

#In lxml it will automatically identify if the type is an xml or an HTML
soup = bs.BeautifulSoup(sauce,'lxml')

#Passing the value of the page title
title = (soup.title.text)

#Just to include the title in the textfile
scraped = title
scraped = scraped + "\n"

#Determining the saving location of the scraped text data
save_path = 'D:\WebScrapes\TLWikipedia'
file_name = str(title)
complete_name = os.path.join(save_path, file_name+".txt")
file = open(complete_name, "w")

#Getting all the paragraphs in the page
for paragraph in soup.find_all('p'):
    
    try:
        scraped = paragraph.text
        print (scraped) #used for checking correct output
        file.write(str(scraped))
        
    except:
        print("Table") #Just to notify if the interpreter is inside a table and not a <p> tag
        
file.close()




