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

def fibonacci():
    #每次调用输出一次
    global x
    global y
    return(x+y)

def ssuma(n):
    global summa
    global x
    global y
    if n==0:
        pass
    elif n==1:
        pass
    elif n==2:
        summa = summa + 1
    else:
        for num in range(n-2):
            print(num)
            print(summa)
            fibonacci()
            cal()
            summa = summa + x + y
            print(summa)
            print("***")


ssuma(n)
print(summa)
            
