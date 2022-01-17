"""This program is used to find gcd of values entered as words"""


def wordtointeger(strnum):
    """This function is used to convert words to integer"""
    lst1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    i = 0

    if len(strnum) == 0:
        return 0
    else:
        while i <= 9:
            if strnum.startswith(lst1[i]):
                return [lst1.index(lst1[i]), len(lst1[i])]
            i += 1
        return [-1, -1]


def integertoword(num):
    """This function is used to convert integers to words"""
    lst1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    if num == 0:
        return ""
    else:
        ans1 = lst1[num%10]
        final_ans = integertoword(int(num/10)) + ans1
    return final_ans


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
    a, w = wordtointeger(firstnum)
    b, x = wordtointeger(firstnum[w:])
    c, y = wordtointeger(secondnum)
    d, z = wordtointeger(secondnum[y:])

    if w == -1 or x == -1 or y ==-1 or z == -1:
        print("Incorrect value")
    else:
        print(integertoword(returngcd((a * 10) + b, (c * 10) + d)))


if __name__ == '__main__':
    numberOne = input('Enter first number in words without space :')
    numberTwo = input('Enter second number in words without space :')
    findgcd(numberOne, numberTwo)
