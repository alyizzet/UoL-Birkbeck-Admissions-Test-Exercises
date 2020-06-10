inputString = input('please enter a sequence of strings: ') ## Read Input

arrayofInput = [inputString[0].split() for x in inputString]  ## Create a list of characters from that input overwriting blank spaces this uses a list comprehension


if arrayofInput[:(len(arrayofInput) // 2) ] == arrayofInput[:(-len(arrayofInput) // 2)]:# if the elements in index from zero to middle are equal to elements from end to middle then print it is a twin string
    print('it is a twin string')
else: 
    print('it is not a twin string')


print(arrayofInput[:(len(arrayofInput) // 2)])
print(arrayofInput[:(-len(arrayofInput) // 2)])
print(arrayofInput)
print(len(arrayofInput)//2)