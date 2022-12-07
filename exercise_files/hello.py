import sys
import os
from termcolor import colored, cprint
# Print "hello, world!" to the terminal
os.system('color')
print (sys.version)
print('Hello, World!')

text = colored('Hello red inverted World!', 'white', attrs=["bold"])
print (text)
cprint("Hello blue world", 'blue')

print (colored("Grey Text", 'grey', 'on_white'))
print (colored("Red Text", 'red', 'on_white'))
print (colored("Green Text", 'green', 'on_white'))
print (colored("Yellow Text", 'yellow', 'on_white'))
print (colored("Blue Text", 'blue', 'on_white'))
print (colored("Magenta Text", 'magenta', 'on_white'))
print (colored("Cyan Text", 'cyan', 'on_white'))
print (colored("White Text", 'white', 'on_blue'))