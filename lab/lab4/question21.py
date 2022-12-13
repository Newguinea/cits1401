def list_swap(lst):
    res = lst.copy()
    for i in range(0, len(res)-1, 2):
        tmp = res[i]
        res[i] = res[i+1]
        res[i+1] = tmp
    return res