def singleDigit(N):
    while True:
        tmp = list(str(N))
        listNum = []
        for i in tmp:
            listNum.append(int(i))
        
        sumNum = 0
        for i in listNum:
            sumNum += i
        
        if(sumNum>=10):
            N = sumNum
        else:
            return sumNum