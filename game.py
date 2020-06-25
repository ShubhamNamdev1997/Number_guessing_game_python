
import random
num = random.randint(1,10)

chance = 0
while chance < 5:
  choose = int(input("Guess any number: "))
  if choose == num :
    print("Congratulations ! You Won")
    break
  elif choose > num:
    print("Choose a number lower then this")
  else:
    print("Choose a number higher then this")
  chance += 1
if not chance < 5:
  print(f"The number guessed by the computer is {num}")
