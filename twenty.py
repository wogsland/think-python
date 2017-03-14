moby = open('words.txt')
for line in moby:
    word = line.strip()
    if len(word) >= 20:
        print word
