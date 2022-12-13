x = int(input(""))
# Don't change the above line of code. You can assume that x will always be either a positive integer or 0.
x = abs(x)

def factorial(i):
    if i <= 1:
        return 1
    else:
        return i*factorial(i-1)

output=factorial(x)
print(output)