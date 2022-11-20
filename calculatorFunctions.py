# define the functions needed (add, sub, mul, div)
# print options to the user (inc. exit)
# ask for values, call for functions with values given
listoFunctions = ["+", "-", "*", "/"]
listoInputs = [0,1,2,3,4,5,6,7,8,9]
quitList = ["quit", "exit"] # exit words
def add(a,b):
    answer = int(a) + int(b)
    print(str(a), "+", str(b), "=", str(answer))
def sub(a,b,):
    answer = int(a) - int(b)
    print(a, "-", b, "=", str(answer))
def mult(a,b,):
    answer = int(a) * int(b)
    print( a, "*", b, "=", str(answer))
def div(a,b,):
    answer = int(a) / int(b)
    print( a, "/", b, "=", str(answer)) 
optionsStr = "your options are as follows: " + str(listoFunctions)

print(optionsStr) # print available functions
def calcDo(): # the operations
    userInput = input("What is your function? ")        
    if userInput in listoFunctions: # check if its something we cand do
        firstNumber = int(input("enter your first number: "))
        secondNumber = int(input("enter your second number: "))
        if firstNumber not in listoInputs:
            print("must be an integer!")
        elif secondNumber not in listoInputs:
            print ("must be an integer!")
        elif userInput == '-': sub(firstNumber,secondNumber)
        elif userInput == '*': mult(firstNumber,secondNumber)
        elif userInput == '/': div(firstNumber,secondNumber)
        elif userInput == '+': add(firstNumber,secondNumber)
        
        calcDo()
        
    elif userInput in quitList:
        print("goodbye")
        return
    else: 
        print("silly, " + optionsStr)
        calcDo()
calcDo()