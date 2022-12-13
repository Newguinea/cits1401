def make_index(words_on_page):
    key = []
    for value in words_on_page.values():
        key += value
    key = list(set(key))
    ##
    res = dict((el,[]) for el in key)
    ##
    for key,value in words_on_page.items():
        for i in value:
            res[i].append(key)
    return res