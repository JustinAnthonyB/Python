def listToString(someList):
    for i in range(len(someList)):
        newString = str(someList[i])

        if i == (len(someList)-1):
            print('and ' + str(someList[i]))
        else:
            print(newString, end=', ')



arg = [x for x in input().split()]
listToString(arg)

# listToString = []
# while True:
#     print('Enter the name of cat ' + str(len(listToString) + 1) +
#       ' (Or enter nothing to stop.):')
#     someList = input()
#     if someList == '':
#         break
#     listToString = listToString + [someList] # list concatenation

# listToString(someList)

    
# print('The cat names are:')
# for name in catNames:
#     print('  ' + name)