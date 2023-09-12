print('\033[32mTotally Random One-Million-to-one\033[0m')
print()
import random

x = 0 
y = random.randint(1, 1000000)

while True:
  print()
  ask = int(input('Guess the secret number: '))
  if 0 < ask < y:
    print()
    print('\033[31mYour guess is too low! try again.\033[0m')
    x += 1
    continue
  elif ask > y:
    print()
    print('\033[31mYour guess is too high! try again.\033[0m')
    x += 1
    continue
  elif ask < 0:
    exit()
  elif ask == y:
    print()
    print('\033[32mYou got it correct! Welldone.\033[0m')
    print()
    print("Click 'run' to try again with a different number.")
    break