import csv
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords



def create_InvertedIndex(D):
    dict = {}
   
    for item in D:
        if item not in dict:
            dict[item] = 1

        if item in dict:
            dict[item] = dict.get(item)+1
                
    return dict

def remove_stopwords(D):
	text_tokens = word_tokenize(D)

	tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
	return tokens_without_sw

def stemming(D):
    L = []
    porter = PorterStemmer()
    for i in D:
        a = porter.stem(i)
        if a not in L:
            L.append(a)
    return L

def remove_punctuation(D):
    punc = '''!()-[]{};:’'"\‘,“”—<>•./?@#$%^&*_~'''
    for ele in D:  
        if ele in punc:  
            D = D.replace(ele, " ")  
        
    # to maintain uniformity
    D=D.lower()                    
    return D

def start():    ### find term frequesncy of each word

	with open('articles.csv', 'r',encoding='utf8') as file:
		reader = csv.reader(file)
		for row in reader:
			if row[4] == 'What I learned from interviewing at multiple AI companies and start-ups':
				D = row[5]
				D = remove_punctuation(D)
				D = remove_stopwords(D)
				D = stemming(D)
				Dict = create_InvertedIndex(D)

				return term_frequency(Dict)

def term_frequency(IVD):
		
	sort_orders = sorted(IVD.items(), key=lambda x: x[1], reverse=True)
	L = []
	i = 0

	for key,value in sort_orders:
		L.append(key)
		i = i + 1
		if i > 13:
			break
	
	return L  
                
print(start())