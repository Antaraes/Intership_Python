import own_db_tree
import sec_tree
import thrid_tree
import math

from Components import  SortingFile
def printing(node):
    if node is not None:
        printing(node.left)
        if node.sec_data != None:
            print(node.sec_data)
        printing(node.right)


first_tree = own_db_tree.tree
sec__tree = sec_tree.tree
thrid__tree = thrid_tree


def connection_test(ftree, name):
    if ftree is not None:
        connection_test(ftree.left, name)
        if ftree.data == name[0]:
            sec_tree_con_test(sec__tree, len(name), name)

            return

        connection_test(ftree.right, name)


def jumpSearch(arrays, val):
    length = len(arrays)
    jump = int(length / 2)
    left, right = 0, 0
    while left < length and arrays[left] <= val:
        right = min(length - 1, left + jump)
        if arrays[left] <= val and arrays[right] >= val:
            break
        left += jump;
    if left >= length or arrays[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and arrays[i] <= val:
        if arrays[i] == val:
            return i
        i += 1
    return -1


def traverse_tree(node, node_list):
    if node is not None:
        traverse_tree(node.left, node_list)
        node_list.append(node.data)
        traverse_tree(node.right, node_list)
    else:
        node_list.append(None)


def totalOfSE(array):
    total = 0
    for number in array:
        total += number
    return total


def fromAsciiValues(total):
    digits = [int(digit) for digit in str(total)]
    name = ''.join([chr(d) for d in digits])
    return name,total


def asciivalues(name):
    ascii_values = [ord(character) for character in name]
    ascii_total = totalOfSE(ascii_values)
    return ascii_total



dataArray = []

def sec_tree_con_test(sec__tre, length, name):
    if sec__tre is not None:
        sec_tree_con_test(sec__tre.left, length, name)
        if sec__tre.data == length:
            sec__tre.sec_data = name
            print("We found for third tree")
            # for char in name:
            #     convert_char = ord(char)
            #     thrid_tre = thrid__tree.ThirdNode()
            #     thrid_tre.data = char
            #     thrid_tre.se = convert_char
            #     sec__tre.ink = thrid_tre
            #     thrid_trees = thrid__tree.third_insertion(thrid_tre.data,thrid_tre.se,sec__tre.link)
            #     # print(thrid_trees.data)
            #     # traverse_tree(name,dataArray)
            ascii_total = asciivalues(name)
            dataArray.append(ascii_total)
            # print(dataArray)
            SortingFile.get_QuickSort(dataArray)
        sec_tree_con_test(sec__tre.right, length, name)


if __name__ == '__main__':
    while True:
        def sendData():
            userinput = input("add or search:")
            if userinput == "add":
                name = input("Enter name:")

                connection_test(first_tree, name)
                # get_name = printing(sec__tree)

                # dataArray.append(ascii_total)
                print(dataArray)
                printing(sec__tree)
                # dataArray.append(sec__tree)
                # print(dataArray)
                # printing(first_tree)
            if userinput == "search":

                userSearch = input("enter what you want:")
                number = asciivalues(userSearch)
                print(number)
                result = jumpSearch(dataArray, number)
                if result == -1:
                    print("Please Try again Email is not found")
                    sendData()
                else:
                    userName,total = fromAsciiValues(number)
                    print(f"{userSearch}{total} is here")



        sendData()
