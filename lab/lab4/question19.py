def duplicate_last(data):
    newlist = data.copy()
    newlist.append(data[-1])
    return newlist