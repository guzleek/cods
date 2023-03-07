from colorama import init
from colorama import Fore, Back, Style
import random
from time import sleep
from rich.progress import track

def do_step(step):
    sleep(random.uniform(0.01, 0.1))

for step in track(range(100), description= "Wait please: "):
    do_step(step)
print(Fore.MAGENTA)
d = int(input("Enter the password for start: "))

while True:

    if d != 1378:
        print(Fore.RED)
        print("\nError password: ")
        print(Fore.MAGENTA)
        d = int(input("\nRepeat password: "))
        continue
    elif d == 1378:
        print(Fore.GREEN)
        print("Correct password! ")
        print(Fore.MAGENTA)
        print("\nStart programs...\n" + " Load...")
        break
    else:
        print("Error")
a = float(input("\nEnter the first number: "))
b = float(input("Enter the second number: "))

quest = input("What the operation ? (+,-): ")

if quest == "+":
    c = a + b 
    print("Answer: " + str(c))
elif quest == "-":
    c = a - b 
    print("Answer: " + str(c))
else:
    print("Error")
