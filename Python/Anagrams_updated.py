"""This program is used to find anagrams from given array of strings"""

def findanagram(lst):
    #removing bracket from starting and ending
    lst[0] = lst[0][2:]
    lst[len(lst)-1] = lst[len(lst)-1][:-2]

    #sorting and saving every string in list
    sorted_lst = [''.join(sorted(x)) for x in lst]

    lst1 = []
    for i in range(len(sorted_lst)):

        lst2 = []
        for j in range(len(sorted_lst)):
            #if string maatches with any other string it will get appended in the list2
            if sorted_lst[i] == sorted_lst[j]:
                lst2.append(lst[j])

        #whole list2 will get appended in list1 if not present
        if lst2 not in lst1:
            lst1.append(lst2)

    translation = {39: 34}
    print(str(lst1).translate(translation))


if __name__ == '__main__':
    user_string = input("enter comma seperated values : ").split('","')
    findanagram(user_string)