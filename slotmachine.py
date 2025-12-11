import random

print("you start with a grand in cold hard green ones")
global bal
bal = 1000


def spin(betamt):
  global bal
  reels = [0,0,0]
  for i in range(len(reels)):
   reels[i] = (random.randint(0,9))

  print(reels)

  if reels[0] == reels[1] and reels[1] == reels[2]:
    profits = betamt * reels[0]
    bal = bal+profits
    print(f"you have {bal} green ones")
  reels = []
  return 0
def bet():
  global bal
  bet = 0
  try:
    bet = int(input("how much do you want to bet "))
    if not bet > 0 or bet > bal:
      print("your bet is too high, pick a different bet")
      bet = 0
    else:
      return(int(bet))
      bal = bal-bet
  except:
    print("invalid bet")
    return 0



def loop():
  global bal
  while bal > 0:
    betmoney = bet()

    spin(betmoney)

  print("you are broke")
  print("go away")

loop()
