import string

emma = open('emma.txt')

# break the text into words
words = []
for line in emma:
    for punt in string.punctuation:
        line = line.replace(punt, '', 1000)
    for word in line.split():
        words.append(word.lower())

# count the word frequency
freq = dict()
for word in words:
    freq[word] = freq.get(word,0) + 1

# order words by count of times they appear
wordcounts = dict()
for key in freq:
    if freq[key] not in wordcounts:
        wordcounts[freq[key]] = [key]
    else:
        wordcounts[freq[key]].append(key)
sortable = []
for wordcount in wordcounts:
    sortable.append((wordcount, wordcounts[wordcount]))

sortable.sort(reverse=True)

# print top twenty words
i = 0
for wordtuple in sortable:
    for word in wordtuple[1]:
        if i <= 20:
            print word
        i += 1
