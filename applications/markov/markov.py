import random


def markov(file):
    wordCache = {}
    startWords = []

    # Read in all the words in one go
    with open(file, "r") as f:
        words = f.read().split(' ')
        words = [s.rstrip('\n') for s in words]
        # build dict where each key is a word from the text file and the value is an array of all the words that directly follow the key in the txt file
        for i in range(0, len(words) - 1):
            if words[i] not in wordCache:
                wordCache[words[i]] = [words[i+1]]
            else:
                wordCache[words[i]].append(words[i+1])
            # create array of possible start words to choose randomly from when crafting sentences
            if (words[i][0].isalpha() and words[i][0] == words[i][0].upper()) or words[i][0] == '"':
                startWords.append(words[i])
        # create counter so we can keep track of how many sentences have been printed
        sentence_count = 0
        # craft 5 sentences -> start with a random start word
        while sentence_count < 5:
            result = ""
            start_word = random.choice(startWords)
            result += start_word + " "
            curr_word = random.choice(wordCache[start_word])

            while True:
                # if curr word is an end word, add it to the result and break out of inner loop
                if curr_word[len(curr_word) - 1] in ['.', '!', '?']:
                    result += curr_word + "\n"
                    break
                # else add the curr_word to the result and then search the wordCount dict for the next following word options
                else:
                    result += curr_word + " "
                    prev_word = curr_word
                    curr_word = random.choice(wordCache[prev_word])
            # increase sentence count by 1 and print the sentence
            sentence_count += 1
            print(result)


markov("input.txt")
