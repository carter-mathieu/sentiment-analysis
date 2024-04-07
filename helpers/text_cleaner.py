import regex as re
from nltk.corpus import stopwords

# function to clean the text before feeding to model
def text_cleaner(data):
    # create list to hold raw resposne text
    text = list(data)

    # create list to hold cleaned response text
    corpus_string = []

    # define the stopwords to check for
    sw = stopwords.words("english")

    # define regex to use
    regex = r'[^a-zA-Z0-9!?.,\s]'

    # loop through the text list apply the oxyclean to each response
    for response in range(len(text)):
        
        # remove trailing whitespace
        r = text[response].strip()

        # remove special characters, no special flowers allowed here
        r = re.sub(regex, '', r)

        # put the clean string response back to eden
        corpus_string.append(r)
    
    # give corpus back to the word
    return corpus_string