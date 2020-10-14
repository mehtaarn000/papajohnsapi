class InvalidMenuOption(Exception):
    pass
def __menu__(item):
    if item == "Pizza":
        print('PEP = Pepperoni Pizza\nSAU = Sausage Pizza\nMCP = Medium Cheese Pizza\nCP = Cheese Pizza\nSH = Super Hawaiian Pizza\nGF = Garden Fresh Pizza\nFSTA = Fresh Spinach & Tomato Alfred Pizza')
    elif item == "Drinks":
        print("2LP = 2 Liter Pepsi $3.00\n20OZP = 20 Ounce Pepsi $2.00\n2LMD = 2 Liter Mountain Dew $3.00\n20OZMD = 20 Ounce Mountain Dew $2.00\n20OZDMD = 20 Ounce Diet Mountain Dew $2.00\n2LDP = 2 Liter Diet Pepsi")
    elif item == "Deserts":
        print('CPA = Cinnamon Pull Aparts\nCCC = Chocolate Chip Cookie\nDCCB = Chocolate Chip Brownie')
    elif item == "Sides":
        print("")
    else:
        raise InvalidMenuOption('Searched item is not a Papa Johns menu item.')
