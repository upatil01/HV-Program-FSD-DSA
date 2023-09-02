
# 0,1,1,2,3,5,8,13,21,34,55,89
# 50
# Stacks
# queues
# Why do we need stack?
# LIFO: Last in First Out
# Array : Complexity of reaching to the last added item ?????
# O(n)
#
# add an element
# retrive an element
# search an element
# delete an element

# add an element
stackList = []
# retrieving an element


def stackAddElement(listname, element):
    listname.append(element)


def stackRetrievElement(listname):
    item = listname[len(listname)-1]
    listname.pop()
    return item


# search and Delete an element
# need to search the element and get the index
# Then retrieve the elements till the index and store it in a nother stack.
# Retrive the element from the second stack and then add it in the first stack

# search and retrieve and element
##
stackAddElement(stackList, 15)
stackAddElement(stackList, 25)
stackAddElement(stackList, 35)
stackAddElement(stackList, 25)
stackAddElement(stackList, 45)
stackAddElement(stackList, 55)
stackAddElement(stackList, 65)
print(stackList)
item = stackRetrievElement(stackList)
print(item)
print(stackList)


def searchandRetrieve(stackName, element):
    newStack = []
    flag = 0
    for index in range(len(stackName)-1, -1, -1):
        if (stackName[index] == element):
            flag = 1
            stackRetrievElement(stackList)
            return index

        else:
            if (flag == 0):
                stackAddElement(newStack, stackName[index])
                print("newstack", newStack)

                stackRetrievElement(stackList)


index = searchandRetrieve(stackList, 25)
print(stackList)
print(index)
