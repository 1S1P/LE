import os
class colors:
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

os.system("title LE - Coded By Sip and KrisIsHere\nThis can find the Slope, y-intercept, and the linear equation of a question.\nexample: (1, 2), (3, 4) | slope is 1.")
os.system('cls' if os.name == 'nt' else 'clear')

print("")
print(colors.CGREEN2 + "LE - Coded By Sip and KrisIsHere")
print("This can find the Slope, y-intercept, and the linear equation of a question.")
print("example: (1, 2), (3, 4) | slope is 1.")


def loop():
    try:
        print("")
        num1 = float(input("Enter Number: "))
        num2 = float(input("Enter Number: "))
        num3 = float(input("Enter Number: "))
        num4 = float(input("Enter Number: "))
        print("")
        print("The slope is...")
        m1 = (num4 - num2)
        d = "-----"
        m2 = (num3 - num1)
        b1 = m1 * num3
        c1 = b1 / m2
        b = num4 - c1
        fg = str(m1) + "/" + str(m2)
        if m1 == 0:
            fg = 0
        le = "y = " + str(fg) + "x + " + str(b)

        print(m1)
        print(d)
        print(m2)
        print("")
        print("y-intercept is...")
        print(b)
        print("")
        print("Linear Equation is...")
        print(le)
        print("")
        print("---------------------------------------------------------------------------")

    except ZeroDivisionError:
        print("No slope.")
        print("")
        print("y-intercept is...")
        print("None")
        print("")
        print("---------------------------------------------------------------------------")
    except EOFError:
        print("")
        print("Typo made, or missed input line.")
        print("")
        print("---------------------------------------------------------------------------")

    except ValueError:
        print("")
        print("Typo made, or missed input line.")
        print("")
        print("---------------------------------------------------------------------------")

    print(loop())


print(loop())
