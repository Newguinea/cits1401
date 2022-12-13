def long_enough(strings, min_length):
    res = []
    for i in strings:
        if len(i) >= min_length:
            res.append(i)
    return res