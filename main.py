import random

Score1=0
Score2=0
again="y"

while again == "y":
  print("Welcome to the dice game press enter to roll")

  input("P1 roll the dice")
  roll1=random.randint(1, 6)
  print("P1 rolled a: ", roll1)

  Score1 += roll1

  input("P2 roll the dice")
  roll2=random.randint(1,6)
  print("P2 rolled a: ", roll2 )

  Score2 += roll2

  if roll1 > roll2:
    print("Player 1 wins the roll")
  elif roll1 < roll2:
    print("Player 2 wins the roll")
  elif roll1 == roll2:
    print("Players roll the same")



  again=input("roll again? y or n")


if Score1 > Score2:
  print("Player 1 wins")
elif Score1 < Score2:
  print("Player 2 wins")
