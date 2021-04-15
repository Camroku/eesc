# Easter Egg Supported Calculator
processes = ["+", "-", "/", "*", "%"]
easters = {}
def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
class notNumberException(Exception):
    pass
class notProcessException(Exception):
    pass
def addEasterEgg(fnum:str, proc:str, snum:str, out:str):
    if not proc in processes:
        raise notProcessException(f"The defined process \"{proc}\" is not a valid process.")
    if not isInt(fnum):
        raise notNumberException(f"The defined first number \"{fnum}\" is not a valid number.")
    if not isInt(snum):
        raise notNumberException(f"The defined second number \"{snum}\" is not a valid number.")
    easters.update({fnum + ":" + proc + ":" + snum:out})

def runCalc():
    run = True
    a = input("First Number: ")
    if not isInt(a):
        print(f"The inputted value \"{a}\" is not an integer.")
        exit()
    b = input("Process: ")
    if not b in processes:
        print(f"The inputted value \"{b}\" is not an process. It supports only +, -, /, * and %.")
        exit()
    c = input("Second number: ")
    if not isInt(c):
        print(f"The inputted value \"{c}\" is not an integer.")
        exit()
    if a + ":" + b + ":" + c in easters.keys():
        print("Output: " + easters[a + ":" + b + ":" + c])
    else:
        if(b == "+"):
            print("Output: " + str(int(a) + int(c)))
        if(b == "-"):
            print("Output: " + str(int(a) - int(c)))
        if(b == "/"):
            print("Output: " + str(int(a) / int(c)))
        if(b == "*"):
            print("Output: " + str(int(a) * int(c)))
        if(b == "%"):
            print("Output: " + str(int(a) % int(c)))