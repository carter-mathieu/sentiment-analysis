import pandas as pd
import sys
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sys.path.append(r'C:\Users\carte\Documents\project-repos\sentiment-analysis')
from helpers.classifier import classifier
from helpers.text_cleaner import text_cleaner
from helpers.visualizers import get_normal_distribution, get_histogram, get_stacked_barchart

# This analysis uses Vader as is optimized for short response and social media data from twitter, facebook, or comments
def get_sentiment(corpus):
    # tokenize the corpus
    text = tokenize.sent_tokenize(corpus)

    # initialize the pre-trained vader sentiment analyzer from nltk
    analyzer = SentimentIntensityAnalyzer()

    # hold the returned sentiment scores
    vader_scores = []

    # loop through each sentence in the text corpus to get a polarity score for sentiment
    for sentence in text:
        vader_score = analyzer.polarity_scores(sentence)
        vader_scores.append(vader_score)
    
    if len(vader_scores) > 0:
        # create a list to hold the values we are going to pull from each compound score
        compound_values = []

        # loop through and get the compound value from each vader score
        for score in vader_scores:
            compound_values.append(score['compound'])
        sentiment = round(sum(compound_values) / len(compound_values), 2)
        return sentiment
    else:
        return 0

# read in the data and drop and rename columns
data = pd.read_csv(r'C:\Users\carte\Documents\project-repos\sentiment-analysis\datasets\kaggle_dataset.csv')
data = data.iloc[:, :2]
data.columns = ['label', 'text']
   
# filter out the spam
data = data[data['label'] != 'spam'].reset_index(drop=True)

# clean the data
data['text'] = text_cleaner(data['text'])
print(data.head())

# get the sentiment
data['score'] = data['text'].apply(get_sentiment)
print(data.head())

data['sentiment'] = data['score'].apply(classifier)
print(data.head())

# get normal distribution
norm_dist = get_normal_distribution(data['score'])

# visualize the sentiment results
get_histogram(data['score'], norm_dist[0], norm_dist[1])
get_stacked_barchart(data, 'label', 'sentiment')
