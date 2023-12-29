def sumOfDigits(num):
    sumList = []
    strNum = str(num)
    total = 0
    for s in strNum:
        sumList.append(s)
    for n in sumList:
        total += int(n)
    return print(total)

sumOfDigits(643)
sumOfDigits(47253)
        
    
