import re


def word_count(s):
    if len(s) == 0 or not re.search('[A-Za-z]', s):
        return {}

    s = re.sub(r'[,.""\r\n\t]', ' ', s).lower().split(' ')
    wordCount = {}

    for word in s:
        if word and word not in wordCount:
            wordCount[word] = 1
        elif word and word in wordCount:
            wordCount[word] += 1

    return wordCount


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count("Hello    hello"))
    print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
