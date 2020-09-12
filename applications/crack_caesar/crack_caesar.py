# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

freq_letter_order = [
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",
]


def crack_caesar(file):
    freqCount = {}
    decodeTable = {}
    result = ""
    # loop thru file and count the occurences of alphabetic chars
    with open(file, "r") as f:
        words = f.read()

        for char in words:
            if char not in freqCount:
                freqCount[char] = 0
            freqCount[char] += 1

        arr = [0] * 26
        index = 0
        # create an array of tuples of char occurences so data can be sorted
        for k, v in freqCount.items():
            if k.isalpha():
                arr[index] = (k, v)
                index += 1

        arr.sort(key=lambda x: x[1], reverse=True)
        # create a decode table now that indexes of the char occurences array will match with the index of the freq_letter_count array
        for i in range(len(arr)):
            decodeTable[arr[i][0]] = freq_letter_order[i]
        # lastly loop thru the original file and build the decoded result string
        for i in range(len(words)):
            if words[i] in decodeTable:
                result += decodeTable[words[i]]
            else:
                result += words[i]

        return result


print(crack_caesar("ciphertext.txt"))
