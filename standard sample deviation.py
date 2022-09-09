# Written in Python v3.10.5:f377153, Jun 6, 2022, by Kesumin @ https://ayo.so/kesumin
# Licensed under the MIT License | https://opensource.org/licenses/MIT

# This script outputs Sample Standard Deviation using input data separated by spaces.

import statistics
import math
from os import system, name

# clear tool
def cls():
    # for windows
    if name.lower() == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    elif name.lower() == "posix":
        _ = system('clear')
    else:
        print(f'OS NOT SUPPORTED')

def awaitinput():
    cls()
    userinput = input(f'Input a table here: ')
    awaitinput.userinput = str(userinput)
    cls()
    checkinput()

def checkinput():
    print(f'Your input is {awaitinput.userinput}.')
    formatinput1verify = input(f'\nIs this correct? Type 0 to input a new table or 1 to continue: ')

    # # Check if integer:
    # if isinstance(formatinput1verify, int) == "True":
    #     pass
    # else:
    #     print(isinstance(formatinput1verify, int))
    #     input("continue?")
    #     checkinput()
    # **feature fix upon request**

    if str(formatinput1verify) == str(0):
        awaitinput()
    elif str(formatinput1verify) == str(1):
        convertinput()
    else:
        cls()
        print(f'Please input either 0 or 1. \n')
        checkinput()

def convertinput():
    cls()
    print("If you see this message, make sure there are no letters in your input.")
    output = awaitinput.userinput.split(" ")
    convertinput.output = list(int(x) for x in output)

    solve()

def solve():
    userinput = convertinput.output
    print(userinput)
    print(type(userinput))

    # print(list(awaitinput.userinput.split(" ")))
    # print(type(list(awaitinput.userinput.split(" "))))
    # input("continue?")

    Sum = sum(userinput)
    print(f'\nMean: {statistics.mean(userinput)}\nSum: {Sum}')
    # input("continue?")

    cls() # comment out if python die

    # Calculation Variables
    n = len(userinput)
    x̄ = (sum(userinput))/n

    # Sample Variance
    for x in range(n):
        sv1 = [(x - x̄)**2 for x in userinput]
    # print(f'Sample Variance: {sv}')
    sv = sum(sv1)/n
    
    # Standard Sample Deviation
    ssd = math.sqrt(sv)

    print(f'1-Var Statistics information: \n \nInput: {awaitinput.userinput} \n \nn = {n} \nx̄ = {x̄} \nSample Variance = {sv} \n \nStandard Sample Deviation = {ssd} \n  Rounded to the nearest hundredth (2 decimal places) = {round(ssd, 2)}')

if __name__ ==  '__main__':
    awaitinput()