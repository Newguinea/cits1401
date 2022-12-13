n = int(input())
# Don't change the above line. You need to write your code below this line. Remember to print the final value only.

x = 0
y = 1
summa = 0

def cal():
    global x
    global y
    tmp = x + y
    x = y
    y = tmp

def exec(num):
    global x
    global y
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        m = 0
        for q in range(2,num):
            cal()
        return y
    
def summ():
    global n
    global summa
    for numn in range (1,n+1):
        temppp = exec(numn)
        summa = temppp + summa
        restore()
    return summa

def restore():
    global x
    global y
    x = 0
    y = 1
print(summ())