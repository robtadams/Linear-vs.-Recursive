import pygame
import sys

def main():
    sys.setrecursionlimit(1500)
    sumOfListTest()

def palindromeTest():
    firstWord = "racecar"
    secondWord = "tacocat"
    thirdWord = "Not A Palindrome"
    fourthWord = "ABCDCBA"

    palindromeTestLinear(firstWord, secondWord, thirdWord, fourthWord)
    palindromeTestRecursive(firstWord, secondWord, thirdWord, fourthWord)
    
def sumOfListTest():
    list = []
    for i in range(1000):
        list.append(i)
    clock = pygame.time.Clock()
    print("List = [1,2,3 ... {0}]".format(len(list)))
    clock.tick()
    print("Linear sum of list: {0}".format(sumOfListLinear(list)))
    print("It took {0} milliseconds to run".format(clock.tick()))
    clock.tick()
    print("Recursive sum of list: {0}".format(sumOfListRecursive(list)))
    print("It took {0} milliseconds to run".format(clock.tick()))

def sumOfListLinear(list):
    sum = 0
    for x in list:
        sum += x
    return sum

def sumOfListRecursive(list):
    sum = 0
    return recSumList(sum, list)

def recSumList(sum, list):
    if len(list) == 0:
        return sum
    sum += list.pop()
    return recSumList(sum, list)

if __name__ == "__main__":
    main()
