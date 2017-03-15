def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

if __name__ == '__main__':
    print histogram('supercalifrigilisticexpialidocious')
