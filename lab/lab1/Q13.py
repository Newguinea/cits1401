n = int(input())
#Don't change the above line of code. Write your program below this line. Remember to print the final result only.

x = 0
y = 1

def cal():
    global x
    global y
    tmp = x + y
    x = y
    y = tmp

def exec():
    global n
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        for num in range(1,n-1):
            cal()
        return y

print(exec())