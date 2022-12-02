import sys
import os
from termcolor import colored, cprint
# Print "hello, world!" to the terminal
os.system('color')
print (sys.version)
print('Hello, World!')

text = colored('Hello red inverted blinking World!', 'white', attrs=["bold"])
print (text)
cprint("Hello blue world", 'blue', 'on_white')