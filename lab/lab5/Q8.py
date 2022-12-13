def my_enumerate(items):
    res = []
    for i in range(len(items)):
        res.append((i,items[i]))
    return res