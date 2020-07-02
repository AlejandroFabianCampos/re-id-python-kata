# Script that will generate a string composed of all prime numbers in sequence
# (up to a certain number, 10006 by default as that's the max number of
# digits required). After generating this string, will return a substring
# five digits long starting on the index provided at ```solution```
#
# Algorithm to check if a certain number is prime can be improved for certain
# if you know upfront what's is the highest prime number that you will need to
# check. Though current solution should work to check any number for primality
# (and you can test this by sending a second parameter on the solution function
# that will dictate the length of the calculated prime string)
#
# Also it's been long since I worked with python and don't have much
# experience anyways so I might be missing language/tool optimization
#
# Author: Alejandro Campos <camposalejandrofabian@gmail.com>
import math
import re
import functools


def isNumberPrime(number, knownPrimes):
    biggestNumberToDivideBy = int(math.sqrt(number))
    for prime in knownPrimes:
        if prime > biggestNumberToDivideBy:
            return number
        elif prime == 1 or number % prime != 0:
            continue
        else:
            return 0
    return number


def getNextPrime(knownPrimes):
    if len(knownPrimes) == 0:
        return 1
    else:
        numberToTest = knownPrimes[-1] + 1
        while True:
            result = isNumberPrime(numberToTest, knownPrimes)
            if result == 0:
                numberToTest += 1
                continue
            else:
                return result


def reduceListToNumber(digitQuantityList):
    i = 0
    total = 0
    while i < len(digitQuantityList):
        total += digitQuantityList[i] * i
        i += 1
    return total


def getPrimeString(length):
    currentList = []
    totalDigitsList = [0]
    while reduceListToNumber(totalDigitsList) < length:
        nextPrime = getNextPrime(currentList)
        numberOfDigits = int(math.floor(math.log10(nextPrime)) + 1)
        if len(totalDigitsList) == numberOfDigits + 1:
            totalDigitsList[numberOfDigits] += 1
        else:
            totalDigitsList.append(1)
        currentList.append(nextPrime)
    return re.sub(r"\[*(, )*\]*", "", str(currentList))


def solution(i, length=10006):
    primeString = getPrimeString(length)
    startIndex = i + 1
    endIndex = startIndex + 5
    return primeString[startIndex:endIndex]
