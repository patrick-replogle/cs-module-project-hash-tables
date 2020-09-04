import random

wordCache = {}

# Read in all the words in one go
with open("input.txt", "r") as f:
    words = f.read().split(' ')
    # TODO: analyze which words can follow other words
    # Your code here
    for i in range(0, len(words) - 1):
        if words[i] not in wordCache:
            wordCache[words[i]] = [words[i+1]]
        else:
            wordCache[words[i]].append(words[i+1])

    # TODO: construct 5 random sentences
    # Your code here
    sentence1 = ""
    sentence2 = ""
    sentence3 = ""
    sentence4 = ""
    sentence5 = ""

    for key in wordCache:
        print(f"{key}: {wordCache[key]}")
