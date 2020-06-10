"""
Exercise - X5 

"""

inputFirst= int(input("Enter the first number: "))

while inputFirst != 0 :
    inputNext= int(input("Enter the next number(type 0 to exit): "))

    if inputFirst > inputNext and inputNext != 0 :
        print('down')
        inputFirst = inputNext

    elif inputFirst == inputNext:
        print('same')
        inputFirst = inputNext

    elif inputFirst < inputNext: 
        print('up')
        inputFirst = inputNext

    else: 
        print('bye')
        break

""" 
 Exercise - X6 

"""

inputFirst= int(input("Enter the first number: "))

lastList = []

while inputFirst != 0 :
    inputNext= int(input("Enter the next number(type 0 to exit): "))

    if inputFirst > inputNext and inputNext != 0 :
        print('down')
        inputFirst = inputNext
        lastList.append('down')

    elif inputFirst == inputNext:
        print('same')
        inputFirst = inputNext
        lastList.append('same')

    elif inputFirst < inputNext: 
        print('up')
        inputFirst = inputNext
        lastList.append('up')

    else: 
        print('bye')
        print(lastList)
        break
