# Easter Egg Supported Calculator
processes = ["+", "-", "/", "*", "%"]
easters = {}
lang = "en"
langs = ["tr", "en"]
translation = {
"en":{
    "n_val_proc": "The defined process is not a valid process.",
    "n_val_fnum": "The defined first number is not a valid number.",
    "n_val_snum": "The defined second number is not a valid number.",
    "i_fnum": "First Number: ",
    "i_proc": "Process: ",
    "i_snum": "Second Number: ",
    "i_n_val_num": "The inputted value is not an integer.",
    "i_n_val_proc": "The inputted value is not an process. The calculator supports only +, -, /, * and %.",
    "out": "Output: "
},
"tr":{
    "n_val_proc": "Tanımlanan işlem geçerli bir işlem değil.",
    "n_val_fnum": "Tanımlanan ilk sayı geçerli bir sayı değil.",
    "n_val_snum": "Tanımlanan ikinci sayı geçerli bir sayı değil.",
    "i_fnum": "İlk Sayı: ",
    "i_proc": "İşlem: ",
    "i_snum": "İkinci Sayı: ",
    "i_n_val_num": "Girilen değer bir sayı değil.",
    "i_n_val_proc": "Girilen değer bir işlem değil. Hesap makinesi sadece +, -, /, * ve % \işlemlerini destekler.",
    "out": "Çıktı: "
}
}
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
def setLang(lng:str):
    global lang, langs
    if lang in langs:
        lang = lng
def addEasterEgg(fnum:str, proc:str, snum:str, out:str):
    global lang, translation
    if not proc in processes:
        raise notProcessException(translation[lang]["n_val_proc"])
    if not isInt(fnum):
        raise notNumberException(translation[lang]["n_val_fnum"])
    if not isInt(snum):
        raise notNumberException(translation[lang]["n_val_snum"])
    easters.update({fnum + ":" + proc + ":" + snum:out})

def runCalc():
    global lang, translation
    run = True
    a = input(translation[lang]["i_fnum"])
    if not isInt(a):
        print(translation[lang]["i_n_val_num"])
        exit()
    b = input(translation[lang]["i_proc"])
    if not b in processes:
        print(translation[lang]["i_n_val_proc"])
        exit()
    c = input(translation[lang]["i_snum"])
    if not isInt(c):
        print(translation[lang]["i_n_val_num"])
        exit()
    if a + ":" + b + ":" + c in easters.keys():
        print(translation[lang]["out"] + easters[a + ":" + b + ":" + c])
    else:
        if(b == "+"):
            print(translation[lang]["out"] + str(int(a) + int(c)))
        if(b == "-"):
            print(translation[lang]["out"] + str(int(a) - int(c)))
        if(b == "/"):
            print(translation[lang]["out"] + str(int(a) / int(c)))
        if(b == "*"):
            print(translation[lang]["out"] + str(int(a) * int(c)))
        if(b == "%"):
            print(translation[lang]["out"] + str(int(a) % int(c)))
