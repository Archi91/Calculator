
def addNumbers(parm1, parm2):
    return int(parm1) + int(parm2)

def subNumbers(parm1, parm2):
    return int(parm1) - int(parm2)

def divNumbers(parm1, parm2):
    try:
        result = int(parm1) / int(parm2)
        return int(result)
    except ZeroDivisionError:
        print("WARNING: Ivalid Equation")

def mulNumbers(parm1, parm2):
    return int(parm1) * int(parm2)

def checkFirstString(param):
    if param.isalpha():
        quit()
    elif param.isnumeric():
        return int(param)
    else:
        print("Invalid sign, try again")
        return False

def checkSecondString(param):
    if param.isdigit():
        return int(param)
    else:
        print("Invalid sign, try again")
        return False

def checkOperation(param):
    if param in ['+', '-', '/', '*']:
        return param
    else:
        print ("Invalid sign, try again")
        return False

def myCalculator(opr, num1, num2):
    if(opr == '+'):
        print("Result:", addNumbers(num1, num2))
    elif(opr == '-'):
        print("Result:", subNumbers(num1, num2))
    elif(opr == '/'):
        print("Result:", divNumbers(num1, num2))
    elif(opr == '*'):
        print("Result:", mulNumbers(num1, num2))

user_input1 = input ("Enter a number (or a letter to exit): ")
number1 = checkFirstString(user_input1)
while number1 == False:
    user_input1= input ("Enter a number (or a letter to exit): ")
    number1 = checkFirstString(user_input1)
    if type(number1) is int:
        break

user_input2 = input("Enter an operation: ")
operation = checkOperation(user_input2)
while operation == False:
    user_input2 = input("Enter an operation: ")
    operation = checkOperation(user_input2)
    if operation in ['+', '-', '/', '*']:
        break


user_input3 = input("Enter another number: ")
number2 = checkSecondString(user_input3)
while number2 == False:
    user_input3= input ("Enter another number: ")
    number2 = checkSecondString(user_input3)
    if type(number2) is int:
        break

myCalculator(operation, number1, number2)




#
