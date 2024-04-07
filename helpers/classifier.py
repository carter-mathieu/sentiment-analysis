def classifier(data):
    # set the lower and upper limits of what is considered a neutral sentiment score
    lower_limit = 0.05 * (-1)
    upper_limit =  0.05

    # we want a text value back rather than a float so classify the score based on value
    if lower_limit <= data <= upper_limit:
        return 'NEUTRAL'
    elif data < lower_limit:
        return 'NEGATIVE'
    else:
        return 'POSITIVE'