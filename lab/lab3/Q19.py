def gcd(number1, number2):
    n = 1
    for i in range(1, min(number1, number2)):
        if number1 % i == 0 and number2 % i == 0:
            n = i
    return n