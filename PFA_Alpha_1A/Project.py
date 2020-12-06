def articles_of_topic(conf, topic):
    list_articles=[]
    import csv
    with open('conferences.csv') as csv_file:
        reader= csv.DictReader(csv_file)
        
        for row in reader:
            if row['conference'] == conf and row['topic'] == topic :
                list_articles.append(row['article'])
    return list_articles


def similarity_articles(vector_my_article, vector_list_articles):
    from sklearn.metrics.pairwise import linear_kernel
    list_similarity = linear_kernel(vector_my_article,vector_list_articles).flatten()
    score=sum(list_similarity)/len(list_similarity)
    return score


def score_topic(conf,topic, my_article):
    from sklearn.feature_extraction.text import TfidfVectorizer
    list_articles=articles_of_topic(conf,topic)
    result=0
    if len(list_articles)!=0:
    
        vectorizer = TfidfVectorizer(stop_words='english', use_idf=True, smooth_idf=True)
        #print(list_articles)
        #list_global=list_articles+my_article
        #vectorizer.fit(list_global)
        vectorizer.fit(list_articles)
        vector_my_article = vectorizer.transform(my_article)
        vector_list_articles = vectorizer.transform(list_articles)
        result = similarity_articles(vector_my_article, vector_list_articles)
        #print(topic," ",result)
    return result,conf,topic
    
   


def Recommender_system(list_general, my_article, topN):
    conferences_topics_scores=[]
    for k in range(len(list_general[0])):
        S=score_topic(list_general[0][k],list_general[1][k], my_article)
        
        conferences_topics_scores.append(S)
    conferences_topics_scores = sorted(conferences_topics_scores, reverse=True)
    if(conferences_topics_scores[0][0]<0.001):
        print("Malheureusement votre article ne sera accepté dans aucune conférence\n")
    else:
        
        print("\nOn vous recommande les conferences suivantes : \n")
        for i in range(0,topN):
            if( conferences_topics_scores[i][0]>0.001):
                print("\n",conferences_topics_scores[i][1])
                print(" Sous le theme : ",conferences_topics_scores[i][2])
                print(" Son score est : ", conferences_topics_scores[i][0])
        
    return 



import pandas as pd
data = pd.read_csv('conferences.csv',low_memory=False,encoding='latin-1')
list_conferences=data['conference']
list_topics=data['topic']
list_general=[[]]
list_general.append([])

list_general[0].append(list_conferences[0])
list_general[1].append(list_topics[0])
for i in range(len(list_conferences)):
    k=0
    res=False
    while k<len(list_general[0]):
        if list_conferences[i]!=list_general[0][k] or list_topics[i]!=list_general[1][k]:
            k=k+1
        else:
            res=True
            break
    if res==False:
        list_general[0].append(list_conferences[i])
        list_general[1].append(list_topics[i])
Nbr_conferences=len(list_general[0])

##get the title of our article

print('veuillez donner le titre de votre article en anglais:')
article_name=input()


article_name=[article_name]

print('donnez le nombre de meilleures conferences que vous voulez afficher : \n')
topN=input()
topN = int(topN)
while(topN<=0 or topN>Nbr_conferences):
    print('Erreur:donnez le nombre de meilleures conferences que vous voulez afficher: ')
    topN=input()
    topN = int(topN)

Recommender_system(list_general, article_name, topN)


    
    