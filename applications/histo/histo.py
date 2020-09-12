import re


def histo(file):
    wordCount = {}

    with open(file, 'r') as f:
        words = f.read().lower().split(' ')
        # iterate thru array of words and add each word to wordCount and increment # if word already exists in dict
        for word in words:
            word = re.sub('[\n/\]}(,[.*;?;){:!"]', '', word)

            if word in wordCount:
                wordCount[word] += "#"
            else:
                wordCount[word] = "#"
    # create array with length of wordCount
    arr = [0] * len(wordCount)
    index = 0
    # convert wordCount to array of tuples so we can sort by number of hashes
    for k, v in wordCount.items():
        arr[index] = (k, v)
        index += 1
    # sort array of tuples by greatest number of hashes
    arr.sort(key=lambda x: x[1], reverse=True)
    # iterate thru the sorted arr and print the tuple key/value pair
    for tup in arr:
        print(f"{tup[0]}: {tup[1]}")


histo("robin.txt")
