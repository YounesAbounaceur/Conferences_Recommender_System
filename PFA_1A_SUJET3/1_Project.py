import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

#import the titles of all conferences
conferences_data=pd.read_csv("conferences.csv",low_memory=False)
#Get the titles of all connferences into a list
list_conferences=conferences_data['Title']
#get the number of conferences
Nbr_conferences=len(list_conferences)
#Add our article to the bottom of  each conference dataset
def Add_our_article(Title_conference,article_name):
    csv_extension=".csv"
    import csv
    
    with open(Title_conference+csv_extension,'a+') as csv_file:
        article_writer = csv.writer(csv_file, delimiter = ',')
        article_writer.writerow(article_name)
    return Title_conference

    

def Delete_our_article(Title_conference):
    csv_extension=".csv"
    import csv
    with open(Title_conference+csv_extension,'r') as csv_file:  
        data = pd.read_csv(Title_conference+csv_extension,low_memory=False,encoding='latin-1')
        data = data['Title']
    N = len(data)
 
   
    
    with open(Title_conference+csv_extension,'w', newline='') as csv_f: 
  
    
         fieldnames= ['Title']
         writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
         writer.writeheader()
       
         for i in range (0,N-1):
             writer.writerow({'Title':data[i]})
    return 0


from sklearn.metrics.pairwise import linear_kernel
def conference_score(tfidf_matrix, index):
    # Get the  similarity scores of all artciles of the conference with our article
    cosine_sim = linear_kernel(tfidf_matrix[index], tfidf_matrix).flatten()
        
        
        
       
    n=len(cosine_sim)
       
    #Get the sum of smilarity scores of all articles of the conference with our article
    score=sum(cosine_sim)
    score = score-1
    score=score/n
       
    #print(Title_conference)
    #print(score)
        
    return score       
         
         
         
#Recommender_coferences is used to get title of conference and outputs the probablity of getting our article accepted
def Recommender_conferences(Title_conference,article_name):
    csv_extension=".csv"
    #add the article to the dataset of this cpnference
    Add_our_article(Title_conference,article_name)
    #import the dataset containing the articles
    metadata = pd.read_csv(Title_conference+csv_extension,low_memory=False)

    

    tfidf= TfidfVectorizer(stop_words='english', use_idf=True, smooth_idf=True)
    tfidf_matrix = tfidf.fit_transform(metadata['Title'])
    tab=tfidf_matrix.toarray()
    #get the index of our the last article on the list which is our article
    index=tab.shape[0]-1
   
    
    
    #print(Title_conference)
    S = conference_score(tfidf_matrix,index)
    #let's not forget to clean the dataset from the article that we've just added
    Delete_our_article(Title_conference)
    return S,Title_conference


# the number of best conerences we want
print('donnez le nombre de meilleures conferences que vous voulez afficher en anglais : ')
topN=input()
topN = int(topN)
while(topN<=0 or topN>Nbr_conferences):
    print('donnez le nombre de meilleures conferences que vous voulez afficher: ')
    topN=input()
    topN = int(topN)

    

##get the title of our article
from langdetect import detect


print('veuillez donner le titre de votre article en anglais: ')
article_name=input()
lang = detect(article_name)
while(lang!='en'):
    print('veuillez donner le titre de votre article en anglais: ')
    article_name=input()
    lang = detect(article_name)

article_name=[article_name]

Conferences_tab = []


for i in range(0,Nbr_conferences):
    R=Recommender_conferences(list_conferences[i],article_name)
    Conferences_tab.append(R)
   
    
    



Conferences_tab=sorted(Conferences_tab, reverse=True)
print("\n")
print("Les meilleures conférences pour votre article sont:\n  ")
for j in range (0,topN):
    print(Conferences_tab[j][1])
    