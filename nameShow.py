def list_names():
    return "Kevin gonzalez", "Revo Coder", "Than Zaw Aou"

def whoareyou(names):
    return "%s is form Tankhoe village." % names

def name_whoareyou():
    list_of_names = list_names()
    for names in list_of_names:
        print(whoareyou(names))

name_whoareyou()
print("I think, they are the one.")