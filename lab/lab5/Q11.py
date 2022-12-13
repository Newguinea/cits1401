def series(n):
    total = 0
    term = 1
    while(term >= n):
        total += term
        term /= 2
    return round(total, 4)