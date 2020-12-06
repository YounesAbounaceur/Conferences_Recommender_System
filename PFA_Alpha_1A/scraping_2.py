
from urllib.request import urlopen
from bs4 import BeautifulSoup
quote_page ='https://dblp1.uni-trier.de/db/conf/btas/btas2018.html'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
#print(soup)

scrap_articles = soup.find_all(class_ = 'title')
#scrap_topics = soup.find_all('h2')

articles = []
topics = []
topics.append('AI')
j=0
for i in scrap_articles:
    if j==0:
            Title=i.getText()
            j=j+1;
            
    else:
            articles.append(i.getText())
        
            
        
        
#for i in scrap_topics:
     #topics.append(i.getText())
        
N=len(articles)//len(topics)          
import csv
with open('conferences.csv','a+') as csv_file:
    article_writer = csv.writer(csv_file)
    fieldnames= ['conference','topic','article']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #writer.writeheader()
   
   
    for k in range (len(topics)):
        c=0
        for i in range(c,min((k+1)*N,len(articles))):
            writer.writerow({'conference': Title,'topic': topics[k],'article': articles[i]})
            c = i
        #article_writer.writerow(L[i])
print("done")
    