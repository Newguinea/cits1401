x = int(input())
# Don't change the above line of code. Add your code after this line. Remember not to print anything other than final answer

x = abs(x)
def addddd(i):
    if i == 1:
        return 1
    elif i == 0:
        return 0
    else:
        return addddd(i-1) + i**2

output = addddd(x)
print(output)