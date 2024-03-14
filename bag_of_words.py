# pip install gensim===3.5.0 if using python 3.1X
# update venv/LIB/gensim/corpora/dictionary.py as
# from collections import defaultdict
# from collections.abc import Mapping
import re
import pandas as pd
from gensim import corpora
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# read in the data
data = pd.read_csv(r'C:\Users\carte\Documents\project-repos\sentiment-analysis\roseland_responses.csv')

# drop unneeded columns, format, and clear the null responses
data.drop(['RES_1', 'RES_2', 'RES_3', 'RES_4', 'RES_5', 'RES_6', 'RES_7', 'RES_8', 'RES_9', 'RES_10'], axis=1, inplace=True)
pd.options.display.float_format = '{:.0f}'.format
data['RESPOND_ID'] = data['RESPOND_ID'].astype(float)
data = data.dropna(how='any', axis=0)

print(data.isna().sum())
print(data.shape)
print(data.head())

# function to clean the text before feeding to model
def text_preprocessing(data):
    # create list to hold raw resposne text
    text = list(data)

    # create list to hold cleaned response text
    corpus = []

    # create a lemmatizer to get root words
    lemmatizer = WordNetLemmatizer()

    # loop through the text list apply the oxyclean to each response
    for response in range(len(text)):
        # remove special characters, no special flowers allowed here
        r = re.sub('[^a-zA-Z]', ' ', text[response])

        # make those high and might uppercase letter lowercase
        r = r.lower()

        # split each response to individual words
        r = r.split()

        # this is not a place for children remove any words less that four characters long
        r = [word for word in r if len(word) > 4]

        # no stopping this train - get those stop words out of here
        r = [word for word in r if word not in stopwords.words('english')]

        # what better way to find the meaning of life than to find the meanings of words, synonyms, antonyms, and more!
        r = [word if wordnet.morphy(word) is None else wordnet.morphy(word) for word in r]

        # get to the root of the problem - erhgm I mean word
        r = [lemmatizer.lemmatize(word) for word in r]

        # bring the words back to eden and join them into a single string
        # r = ' '.join(r)

        # put the cleaned response back to eden
        corpus.append(r)
    
    # give corpus back to the word
    return corpus

def generate_bag_of_words(text_data):
    dictionary = corpora.Dictionary(text_data)
    print(dictionary)
    corpus = [dictionary.doc2bow(text) for text in text_data]
    return corpus

# its cleaning time
data['RESPONSE'] = text_preprocessing(data['RESPONSE'])
data.to_csv(r'C:\Users\carte\Documents\project-repos\sentiment-analysis\cleaned_roseland_responses.csv')
print(data.head())

# "I have a bag of words, I have a bag of words" - CAPTAIN Jack Sparrow, 2006
data['RESPONSE'] = generate_bag_of_words(data['RESPONSE'])
data.to_csv(r'C:\Users\carte\Documents\project-repos\sentiment-analysis\cleaned_roseland_responses.csv')
print(data.head())