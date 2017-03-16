moby = open('words.txt')
searchable = dict()
for line in moby:
    searchable[line.strip()] = line.strip()

def search_dict (word, to_search):
    return word in to_search

if __name__ == '__main__':
    if search_dict('fuck', searchable):
        print 'Swear word found.'
    else:
        print 'This dict is PG.'
