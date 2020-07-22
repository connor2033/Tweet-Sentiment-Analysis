import string

# This is the "compute_tweets" function as described in the assignment.
def compute_tweets(tfile, tkeys):
    # Creating final (currently empty) list to contain tuples and be returned.
    returnList = []

    # creating lists to hold the tuples for each timezone
    pacific_tweets = []
    mountain_tweets = []
    central_tweets = []
    eastern_tweets = []

    # Creating the (currently empty) tuples for each timezone.
    pacific_sentiment = ()
    mountain_sentiment = ()
    central_sentiment = ()
    eastern_sentiment = ()

    tupReturn = ()

    # Opening files inputted by user (with input errors)
    try:
        tweetfile = open(tfile, "r", encoding="utf‐8")
        keyfile = open(tkeys, "r", encoding="utf-8")
    except IOError as e:
        return tupReturn

    # Transforming keywords into a dictionary
    keywords = {}
    for line in keyfile:
        line = line.split(",")
        keywords[line[0]] = int(line[1])

    # Properly formatting lines from the specified tweet file in a list
    for line in tweetfile:
        tweet = line.split()
        tweet[0] = tweet[0].strip("[,")
        tweet[1] = tweet[1].strip("]")

        # Removing punctuation from each individual tweet and making all words lowercase.
        for i in range(5, len(tweet)):
            punc = str.maketrans({key: None for key in string.punctuation})
            tweet[i] = tweet[i].translate(punc)
            tweet[i] = tweet[i].lower()

        # Gathering all tweets within North and South bounds.
        # Grouping each tweet into their respective timezones based on given coordinates.
        # After grouping, we remove all information from each tweet (line), and keep only the words from each tweet.
        # Finally, each properly formatted and groped tweet is appended into a list of other tweets in their respective timezones.
        if 24.660845 <= float(tweet[0]) <= 49.189787:
            # pacific
            if -125.242264 <= float(tweet[1]) < -115.236428:
                del tweet[0:5]
                pacific_tweets.append(tweet)

            # mountain
            elif -115.236428 <= float(tweet[1]) < -101.998892:
                del tweet[0:5]
                mountain_tweets.append(tweet)

            # central
            elif -101.998892 <= float(tweet[1]) < -87.518395:
                del tweet[0:5]
                central_tweets.append(tweet)

            # eastern
            elif -87.518395 <= float(tweet[1]) < -67.444574:
                del tweet[0:5]
                eastern_tweets.append(tweet)

    # This function is used to calculate the sentiment of any given timezone (as to not repeat code).
    def sentiment_calc(timezone):
        # Sentiment total and counter (entire timezone):
        total_sentiment = 0
        tweet_counter = 0
        # Sentiment total and counter (Individual tweets):
        tweet_sentiment = 0
        keyword_counter = 0

        # Getting sentiment of timezone (list of tweets)
        for i in range(len(timezone)):
            # Getting sentiment of a single tweet (line)
            for word in timezone[i]:
                if word in keywords:
                    tweet_sentiment += keywords[word]
                    keyword_counter += 1

            # Ensuring that tweet counter only increases when tweet contains any keyword(s)
            if keyword_counter > 0:
                # Adding individual tweet's average sentiment to timezone total sentiment
                total_sentiment += tweet_sentiment / keyword_counter
                # Adding to tweet counter
                tweet_counter += 1

                # Resetting counter and sentiment value for next tweet
                keyword_counter = 0
                tweet_sentiment = 0

        # Calculating the average sentiment of the timezone as a whole and returning it
        if tweet_counter > 0:
            total_sentiment = total_sentiment / tweet_counter

            # Creating tuple for timezone (average sentiment, counter) and rounding.
            tupReturn = (round(total_sentiment, 3), round(tweet_counter, 3))
            return tupReturn
        else:
            tupReturn = ()
            return tupReturn

    # Running timezones (lists of tweets) through the above sentiment calculating function.
    eastern_sentiment = sentiment_calc(eastern_tweets)
    central_sentiment = sentiment_calc(central_tweets)
    mountain_sentiment = sentiment_calc(mountain_tweets)
    pacific_sentiment = sentiment_calc(pacific_tweets)

    # Appending tuples to final list (to be returned) in specified order.
    returnList.append(eastern_sentiment)
    returnList.append(central_sentiment)
    returnList.append(mountain_sentiment)
    returnList.append(pacific_sentiment)

    # Returning final list of tuples from "sentiment_calc" function.
    return returnList


