

from colorama import init
from colorama import Fore, Back, Style
import math

init()
print( Fore.BLACK)
print( Back.YELLOW)
print( "Старых Федор ИУ5-55Б")
print( Fore.BLACK)
print( Back.CYAN)
while True:
    try:
        print( Fore.BLACK)
        print( Back.CYAN)
        A = float(input("Введите А: "))
        break
    except ValueError:
        print( Fore.BLACK)
        print( Back.RED)
        print("Повторите ввод A!")
while True:
    try:
        print( Fore.BLACK)
        print( Back.CYAN)
        B = float(input("Введите B: "))
        break
    except ValueError:
        print( Fore.BLACK)
        print( Back.RED)
        print("Повторите ввод B!")
while True:
    try:
        print( Fore.BLACK)
        print( Back.CYAN)
        C = float(input("Введите C: "))
        break
    except ValueError:
        print( Fore.BLACK)
        print( Back.RED)
        print("Повторите ввод C!")
D = B ** 2 - 4*A*C
print("D= "+ str(D))
if D>0:
    x1 = (-B+math.sqrt(D))/2*A
    x2 = (-B-math.sqrt(D))/2*A
    print( Fore.BLACK)
    print( Back.GREEN)
    print("x1= ",x1, "; x2= ", x2)
elif D<0:
    print( Fore.BLACK)
    print( Back.RED)
    print("Нет корней!")
elif D==0:
    x = (-B)/2*A
    print( Fore.BLACK)
    print( Back.GREEN)
    print("x= ", x)
