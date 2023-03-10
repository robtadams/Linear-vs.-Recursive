# https://medium.com/co-learning-lounge/recursive-function-python-practice-examples-c37df75555e8

def main():
    print("Linear vs. Recursive Sum\n------------------------")
    print("[1, 2, 3, 4, 5, 6, 7, 8, 9] = 45")
    print(linearSumOfList([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(recursiveSumOfList([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print("\nLinear vs. Recursive Fibonacci\n------------------------------")
    print("10th Fibonacci Number = 55")
    print(linearFibonacciSequence(10))
    print(recursiveFibonacciSequence(10))

    print("\nLinear vs. Recursive Power\n--------------------------")
    print("2 ** 10 = 1024")
    print(linearPower(2, 10))
    print(recursivePower(2, 10))

    print("\nLinear vs. Recursive Least Common Multiple\n--------------------------------")
    print("5 and 9 = 45")

# ----- Sum of List ------
def linearSumOfList(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

def recursiveSumOfList(list):
    if len(list) == 0:
        return 0
    return list.pop(0) + recursiveSumOfList(list)



# ---- Fibonacci Sequence -----
def linearFibonacciSequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    oldNum = 0
    Num = 1
    for i in range(n - 1):
        newNum = Num + oldNum
        oldNum = Num
        Num = newNum

    return newNum

def recursiveFibonacciSequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursiveFibonacciSequence(n-1) + recursiveFibonacciSequence(n-2)



# --------- Power ----------
def linearPower(num, power):
    if power == 0:
        return 1
    sum = 1
    for i in range(power):
        sum *= num
    return sum

def recursivePower(num, power):
    if power == 0:
        return 1
    return num * recursivePower(num, power - 1)



# - Lowest Common Multiple -
def linearLCM(num1, num2):
    if num1 % num2:

def recursiveLCM(num1, num2):
    if num1 % num2:
        

if __name__ == "__main__":
    main()
