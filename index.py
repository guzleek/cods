from colorama import init
from colorama import Fore, Back, Style
import random
from time import sleep
from rich.progress import track

def progress_bar(step):
    sleep(random.uniform(0.01, 0.1))
for step in track(range(100), description= "Please wait..."):
    progress_bar(step)
print(Fore.MAGENTA)
quest = int(input("Enter the password to start: "))

while True:

    if quest != 6262:
        print(Fore.RED)
        print("\nError password..")
        print(Fore.MAGENTA)
        quest = int(input("\nRepeat password: "))
        continue
    elif quest == 6262:
        print(Fore.GREEN)
        print("\ncorrectly ✔ ")
        break
    else:
        print(Fore.RED)
        print("\nError...")
print(Fore.MAGENTA)
name = input("\nEnter you name: ")
age = input("Enter you age: ")

print("\nHello," + name )

if int(age) < 18:
    print(Fore.RED)
    print("\nYou are not an adult!")
elif int(age) >= 18:
    print(Fore.GREEN)
    print("\nYou are an adult ✔")
else:
    print(Fore.RED)
    print("Error")

input("\n~tap to next~")
print(Fore.MAGENTA)
number1 = float(input("\nEnter the first number: "))
number2 = float(input("Enter the second number: "))

quest1 = input("\nWhat the operation? (+,-,*,/,**): ")

if quest1 == "+":
    result1 = number1 + number2
    print(Fore.GREEN)
    print("\nAnswer :" + str(result1))
elif quest1 == "-":
    result1 = number1 - number2
    print("\nAnswer: " + str(result1))
elif quest1 == "*":
    result1 = number1 * number2
    print("\nAnswer: " + str(result1))
elif quest1 == "/":
    result1 = number1 / number2
    print("\nAnswer: " + str(result1))
elif quest1 == "**":
    result1 = number1 ** number2
    print("\nAnswer: " + str(result1))
else:
    print(Fore.RED)
    print("Error..")
