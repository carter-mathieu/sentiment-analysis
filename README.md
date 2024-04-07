# Getting Started
This project was created to take in a set of survey responses and attempt to classify the sentiment of the response through the use of language models.

The project also attempts to categorize the responses of the survey into 10 pre-determined based on keyword matching in the responses.

## Requirements and Installation
This project was built with and assumes the use of `python 3.12`

After you have initialize your favourite virtual environment, install the below packages:
```
pip install flair
pip install nltk
pip install pandas
pip install plotly
pip instal skikit-learn
pip install scipy
```

Once all packages are installed, to be able to use nltk and gensim do the following:
1. Run the `nltk.download()` command in your termial and set the install path to `C:\`

## Directory Structure
In the `sentiment-analysis` root directory is where you should find this README file as well as the below sub directories:
- `analysis` --> contains the script to run to generate the sentiment analysis
- `datasets` --> you should place your working dataset(s) in here
- `helpers` --> helper functions to prep or manipulate the data used in the sentiment analysis
-`outputs` --> any outputs of the analysis (graphs, statistics, data) are palced here

### In the `analysis` folder you will find:
- `sentiment.py` --> this file runs the functions to analyze the sentiment of the responses and produce a polarity score

### In the `datasets` folder you will find:
- `kaggle_dataset.csv` --> this file is the kaggle text message sample dataset that was used to run the sentiment analysis

### In the `helpers` folder you will find:
- `classifier.py` --> this file runs the functions to classify the sentiment polarity scores as `NEGATIVE`, `NEUTRAL`, or `POSITIVE`
- `text_cleaner.py` --> this file runs the functions to clean the text to remove trailing spaces and special characters
- `visualizers.py` --> this file runs the functions to produce the data visualizations of the sentiment results

### In the `outputs` folder you will find:
- `sentiment_chart.html` --> 
- `sentiment_histogram.html` --> this file runs the functions to categortize the survey responses into pre-defined categories based on associated keywords

# Sentiment Analysis Overview
The sentiment analysis was done with the pre-trained VADER (Valence Aware Dictionary and sEntiment Reasoner) which is a lexicon and rule-based sentiment analysis tool that is tuned to sentiments expressed in social media. It is fully sourced under the MIT License.

A polarity score between `-1` and `1` is assigned for each sentence and then averaged to gauge the sentiment of the response as a whole. This keeps a ratio of `1:1` between response and sentiment score where each response is considered a unique record of sentiment.

The `compound` score was used to determine sentiment and is computed by summing the valence scores of each word in the lexicon, adjusted according to the rules, and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive).

It can be considered a 'normalized, weighted composite score' is accurate.

## VADER Sentiment Classification
Given that the VADER sentiment analysis provides a the `compound` score between -1 (most extreme negative) and +1 (most extreme positive), an additional step was needed to qualify the given `compound` score as `NEGATIVE`, `NEUTRAL`, or `POSITIVE`. The qualification of `compound` scores was determined following the following threshold values (used in the literature cited at the bottom of this document):

1. *positive sentiment:* `compound` score >= 0.05
2. *neutral sentiment:* (`compound` score > -0.05) and (`compound` score < 0.05)
3. *negative sentiment:* `compound` score <= -0.05