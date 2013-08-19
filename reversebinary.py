


inputNumber= input("Type in number to convert here:")
step1= toBinary(inputNumber)
step2=flipBinary(step1)
step3= toDecimal(step2)
print step3


def toBinary(number):
    binaryString=""
    number=int(number)
    while number >= 1:
        temp=number%2
        binaryString=binaryString+str(temp)
        number=number/2
    binaryString=binaryString[::-1]
    return binaryString

def flipBinary(number):
    number= str(number)
    number=number[::-1]
    number = int(number)
    return number

def toDecimal(number):
    number=str(number)
    count=1
    newNum=0
    numberList=[]
    for element in number:
        numberList.append(int(element))
    numberList=numberList[::-1]
    for element in numberList:
        if element == 1:
            newNum= newNum + element*count
        count=count*2
    return newNum
runProgram()


