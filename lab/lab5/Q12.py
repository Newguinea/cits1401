def nextRound(k,scores):
    count = 0
    
    if(scores[k-1]==0):
        return 0
    
    for i in scores:
        if(scores[k-1]<=i):
            count += 1
    return count