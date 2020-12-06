# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:52:05 2019

@author: USER

import csv
with open('names.csv') as csv_file:
    reader=csv.DictReader(csv_file)
    for row in reader:
        print(row['first_name'],row['last_name'])
        
   

import csv
with open('surnames.csv', 'a+') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    
    writer.writerow({'first_name': 'Ared', 'last_name': 'Minns'})
    writer.writerow({'first_name': 'Huga', 'last_name': 'Sadma'})
    writer.writerow({'first_name': 'Wonder', 'last_name': 'SOlfking'})
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
quote_page ='https://dblp.org/db/conf/kdd/kdd2018.html'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
#print(soup)

scrap_articles = soup.find_all(class_ = 'title')
scrap_topics = soup.find_all('h2')
articles = []
topics = []

j=0
for i in scrap_articles:
    if j==0:
            Title=i.getText()
            j=j+1;
            
    else:
            articles.append(i.getText())
        
            
        
        
for i in scrap_topics:
     topics.append(i.getText())
        
          
import csv
with open('conferences.csv','a+') as csv_file:
    article_writer = csv.writer(csv_file)
    fieldnames= ['conference','topic','article']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #writer.writeheader()
    i1=1
    i2=25
    k=0
    for i in articles:
        if i1>=i2 :
            k+=1
            i2=i1+25
        
        writer.writerow({'conference': Title,'topic': topics[k],'article': i})
        i1+=1
        #article_writer.writerow(L[i])
print("done")
    