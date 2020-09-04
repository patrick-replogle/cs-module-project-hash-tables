def no_dups(s):
    # your code here
    result = ""
    wordCount = {}
    s = s.split(" ")

    for word in s:
        if word not in wordCount:
            wordCount[word] = 0

        wordCount[word] += 1

        if wordCount[word] == 1:
            result += word + " "

    return result.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
