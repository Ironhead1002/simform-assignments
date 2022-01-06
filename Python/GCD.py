"""This program is used to find gcd of values entered as words"""


def wordtointeger(strnum):
    """This function is used to convert words to integer"""
    if strnum == 0:
        return string
    else:
        if strnum.startswith('zero'):
            return [0, 4]
        elif strnum.startswith('one'):
            return [1, 3]
        elif strnum.startswith('two'):
            return [2, 3]
        elif strnum.startswith('three'):
            return [3, 5]
        elif strnum.startswith('four'):
            return [4, 4]
        elif strnum.startswith('five'):
            return [5, 4]
        elif strnum.startswith('six'):
            return [6, 3]
        elif strnum.startswith('seven'):
            return [7, 5]
        elif strnum.startswith('eight'):
            return [8, 5]
        elif strnum.startswith('nine'):
            return [9, 4]
        else:
            return [-1, -1]


def integertoword(num, string):
    """This function is used to convert integers to words"""
    if len(num) == 0:
        return string
    else:
        if num.startswith('0'):
            string += 'zero'
            return integertoword(num[1:], string)
        elif num.startswith('1'):
            string += 'one'
            return integertoword(num[1:], string)
        elif num.startswith('2'):
            string += 'two'
            return integertoword(num[1:], string)
        elif num.startswith('3'):
            string += 'three'
            return integertoword(num[1:], string)
        elif num.startswith('4'):
            string += 'four'
            return integertoword(num[1:], string)
        elif num.startswith('5'):
            string += 'five'
            return integertoword(num[1:], string)
        elif num.startswith('6'):
            string += 'six'
            return integertoword(num[1:], string)
        elif num.startswith('7'):
            string += 'seven'
            return integertoword(num[1:], string)
        elif num.startswith('8'):
            string += 'eight'
            return integertoword(num[1:], string)
        elif num.startswith('9'):
            string += 'nine'
            return integertoword(num[1:], string)
        else:
            return [-1, -1]


def returngcd(num1, num2):
    """This function is used to return gcd values"""
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return returngcd(num2, num1 % num2)


def findgcd(firstnum, secondnum):
    """This function combines the output of function wordtointeger and return gcd to find gcd"""
    firstnumfirstint, c = wordtointeger(firstnum)
    if c == len(firstnum):
        firstnumsecondint = 0
    else:
        firstnumsecondint, c = wordtointeger(firstnum[c:])
        firstnumfirstint *= 10

    secondnumfirstint, d = wordtointeger(secondnum)
    if d == len(secondnum):
        secondnumsecondint = 0
    else:
        secondnumsecondint, d = wordtointeger(secondnum[d:])
        secondnumfirstint *= 10

    if c == -1 or d == -1:
        print("Unexpected Input")
    else:
        firstinteger = firstnumfirstint + firstnumsecondint
        secondinteger = secondnumfirstint + secondnumsecondint
        a = str(returngcd(firstinteger, secondinteger))
        print(integertoword(a, ""))


if __name__ == '__main__':
    numberOne = input('Enter first number in words without space :')
    numberTwo = input('Enter second number in words without space :')
    findgcd(numberOne, numberTwo)
