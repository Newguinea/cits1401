def composite2(N):
    findNum = 7
    numQuantityFind = 0
    
    while (numQuantityFind < N):
        findNum += 2
        for i in range(2,findNum):
            if(findNum%i == 0):
                numQuantityFind += 1
                break
    return findNum
