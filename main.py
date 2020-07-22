from sentiment_analysis import compute_tweets

# My name is Connor Haines, and this is my sentiment analysis assignment.
# This software uses a combination of files and functions, to calculate the average
# sentiment per tweet in specific timezones. The program refers to files full of
# tweets and keywords which are inputted by the user.

finalList = []

# Getting user to input file names.
tfilename = input("Enter the name of a tweets file: ")
kfilename = input("Enter the name of a keywords file: ")

# Executing "compute_tweets" function.
finalList = compute_tweets(tfilename, kfilename)

# Finally outputting values in a readable fashion.
print("")
print("----------(Average Sentiment, Number of Tweets)----------")
print("")

if len(finalList) > 1:
    print("Eastern Timezone: ",finalList[0])
    print("Central Timezone: ",finalList[1])
    print("Mountain Timezone: ",finalList[2])
    print("Pacific Timezone: ",finalList[3])

# Checking if empty list was returned and outputting a message.
else:
    print("Empty list returned. Invalid file name(s).")

print("")
print("---------------------------------------------------------")
