
countPasses = 0 
countFails = 0
countDistinctions = 0 

firstMark = int(input(' Next Student(1st Test): '))
secondMark = int(input('2nd Test: '))

if firstMark + secondMark <  49 :
    countFails = countFails + 1 
elif firstMark + secondMark >= 50 and firstMark + secondMark <= 69:
    countPasses = countPasses + 1 
else:
    countDistinctions = countDistinctions + 1 

while firstMark or secondMark != 51:

    firstMark = int(input(' Next Student(1st Test): '))
    secondMark = int(input('2nd Test: '))
    sumMark = firstMark + secondMark
   
    if sumMark <  49 :
        countFails = countFails + 1 
    elif sumMark >= 50 and sumMark <= 69:
        countPasses = countPasses + 1 
    else:
        countDistinctions = countDistinctions + 1 

    if (firstMark or secondMark) == 51:
        break

print(f"Distinctions:{countDistinctions}")
print(f"Passes:{countPasses}")
print(f"Fails:{countFails}")