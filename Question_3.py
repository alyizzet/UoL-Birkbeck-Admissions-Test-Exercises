
inputFirst= int(input("Enter the first number: "))

lastList = []

while inputFirst != -1 :
    inputNext= int(input("Enter the next number(type -1 to exit): "))
    lastList.append(inputNext)
    if inputNext == -1:
        break

properlist= lastList[:-1]

sortedList = sorted(properlist)


if  properlist == sortedList:
    print('yes')
else:
    print('no')


