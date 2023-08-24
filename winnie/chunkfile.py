with open('wine-bible.txt', 'r') as f:
    for i, line in enumerate(f):
        if i == 5884:
            print(repr(line))