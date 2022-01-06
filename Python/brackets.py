"""This program is used to find all the possible brackets"""
lst = []


def generatebrac(n, openb, closeb, string, res):
    """This function will generate brackets"""
    if openb == 0 and closeb == 0:
        # appending string of brackets if no close or open brackets remain
        res.append(string)
        return

    if openb > 0:
        # append ( if there are still open brackets left
        string += '('
        # Recursive call
        generatebrac(n, openb-1, closeb, string, res)
        # Backtrack
        string = string[:len(string)-1]

    if closeb > openb:
        # append ) if number of close is greater than open brackets remain
        string += ')'
        # recursive call
        generatebrac(n, openb, closeb-1, string, res)
        # backtrack
        string = string[:len(string) - 1]


if __name__ == '__main__':
    a = int(input('Enter number of brackets: '))
    print(generatebrac(a, a, a, "", lst))
    print(lst)
