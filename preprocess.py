import re 
import nltk 

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
import re # regular expression 


stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()


def preprocess(text): 
    # convert reviews into lowercase
    text= text.lower()

    # remove punctuation and numbers 
    text  =  re .sub(r'[a-z \s]',"",text)  # replace everything expert a-z and a space with empty

     # tokenize : split reviews into individual word 
     tokens = word_tokenize(text)
def preprocess(text) : 
       # remove stop words 
       tokens = [lemmatizer.lemmatize(word,pos='v') for word in tokens]

       return " ".join (tokens) # put together the tokens back to sentiment format 

sample = "Amazing product . Delivered promptly . 10/10"
print ( preprocess(sample))
