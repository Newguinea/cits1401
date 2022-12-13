def sequence(n):
    res = [n]
    finalNum = res[len(res)-1]
    
    while (finalNum != 1):
        if finalNum%2 == 0:
            res.append(int(finalNum/2))
        else:
            res.append(int(3*finalNum+1))
        
        finalNum = res[len(res)-1]
    return res