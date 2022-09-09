# import only system from os
from os import system, name
  
# define our clear function
def cls():
    # for windows
    if name.lower() == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    elif name.lower() == "posix":
        _ = system('clear')
    else:
        print("OS NOT SUPPORTED. CLEAR.PY")
        
cls()