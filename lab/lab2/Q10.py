def dseries(n_terms):
    res = 0
    for i in range(1,n_terms+1):
        res = i * i + res
    return res