def bitshift(s,k,b):
    if b == True:
        if s == "":
            return s
        else:
            for i in range(k):
                s = s[1:] + s[0]
            return s
    elif b == False:
        if s == "":
            return s
        else:
            for i in range(k):
                s = s[-1] + s[:-1]
            return s