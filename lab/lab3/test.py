def binarytodecimal(biNum):
    listt = []
    res = 0
    for d in str(biNum):
        listt.append(d)
    for i in range(0,len(listt)-1):
        res += int(listt[i])*2**int(len(listt)-1-i)
    return res