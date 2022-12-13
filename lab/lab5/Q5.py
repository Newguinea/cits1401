def make_dictionary(filename):
    global listWords
    global listWordC
    global listde
    global res

    listWords = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            listWords.append(line)
            
    listWords = list(filter(None, listWords))
    
    listde = list(set(listWords))

    res = dict((el,0) for el in listde)
    for i in listWords:
        res[i] += 1
    return res