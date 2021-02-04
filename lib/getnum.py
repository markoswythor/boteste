from random import randint
import sys

num1 = sys.argv[1]
num2 = sys.argv[2]

numero = randint(int(num1), int(num2))

print(numero)