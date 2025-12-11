import random

def guess_the_number():
  print("Find my number between 1 and 100.")

  number = random.randint(1, 100)

  attempts = 0
  while True:
      guess = int(input("Guess a number: "))
      attempts += 1

      if guess < number:
        print("Too low!")
      elif guess > number:
        print("Too high!")
      else:
        print(f"You Win! Used {attempts} attempts.")
        break
