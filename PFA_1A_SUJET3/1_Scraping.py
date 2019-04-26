# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
quote_page ='https://dblp.org/db/conf/hais/hais2018.html'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
#print(soup)

hi = soup.find_all(class_ = 'title')
L = []
import csv
Title='HAIS  International Conference on Hybrid Artificial Intelligent Systems.csv'
with open(Title,'w') as csv_file:
    article_writer = csv.writer(csv_file)
    fieldnames= ['Title']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in hi:
        L.append(i.getText())
    for i in L:  
        writer.writerow({'Title':i})
        #article_writer.writerow(L[i])