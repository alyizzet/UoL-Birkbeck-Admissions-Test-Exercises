# print("please enter first word into the memory: ", end ='')
# word1 = input()

# word2 = input()

# print(word1 +" "+ word2)

# print( "word" + str(2))

# print( 1 // 2)

# num = 5
# print(str(num))
# num = num + 2
# print(str(num))
# num = num // 3 * 6
# print(str(num))
# print(str(7 + 15 % 4))
# num = 24 // 3 // 4
# print(str(num))
# num = 24 // (num // 4)
# print(str(num))

# first-choice, 2nd, 3_falan, a.out

# print("Please key in a number: ", end = "")
# s = input()
# num1 = int(s)
# print("And another: ", end = "")
# s = input()
# num2 = int(s)
# if num1 == num2:
#     print("They are the same.")

# # upper case > lower case
# # blank b4 all 
# # numbers b4 letters upper case b4 lower case lettter

# if examMark >= 50: 
#     print('asd')
# else: 
#     print('dasd')

# print('Enter Husband Salary: ')
# salary1 = input()
# husbandSalary = int(salary1)
# print('Enter Woife Salary: ')
# salary2 = input()
# woifeSalary = int(salary2)

# if husbandSalary + woifeSalary >= 40000:
#     print('Tax Higher')
# else: 
#     print('Tax Lower')
# print('taxation is theft')

# num = 0 
# while num <= 10:
#     print(num**2)
#     num = num + 1


# input_string = input("Enter a list of numbers: ")
# userList = [int(x) for x in input_string.split()]
# print(userList.count(100))

# inputText = input("Enter a lines of text: ")
# text = [x for x in inputText.split()]

# longest_line = max(text)

# print(longest_line)


# if inputFirst > inputNext and inputNext != 0:
#     print('down')
# elif inputFirst == inputNext and inputNext != 0:
#     print('same')
# elif inputFirst < inputNext: 
#     print('up')
# else: 
#     print('bye')

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
