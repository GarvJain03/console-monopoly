import random

map = {"Old Kent Road": 60, "Whitechapel Road": 60, "The Angel Islington": 100, "Euston Road": 100, "Pentonville Road": 120, "Pall Mall": 140, "Whitehall": 140, "Northumrl'd Avenue": 160, "Bow Street": 180, "Marlborough Street": 180, "Vine Street": 200, "Strand": 220, "Fleet Street": 220, "Trafalgar Square": 240, "Leicester Square": 260, "Coventry Street": 260, "Piccadilly": 280, "Regent Street": 300, "Oxford Street": 300, "Bond Street": 320, "Park Lane": 350, "Mayfair": 400}
players = {}
ownership = {}
rent = {"Old Kent Road": 60, "Whitechapel Road": 60, "The Angel Islington": 100, "Euston Road": 100, "Pentonville Road": 120, "Pall Mall": 140, "Whitehall": 140, "Northumrl'd Avenue": 160, "Bow Street": 180, "Marlborough Street": 180, "Vine Street": 200, "Strand": 220, "Fleet Street": 220, "Trafalgar Square": 240, "Leicester Square": 260, "Coventry Street": 260, "Piccadilly": 280, "Regent Street": 300, "Oxford Street": 300, "Bond Street": 320, "Park Lane": 350, "Mayfair": 400}

print("--------------------------------")
print("     WELCOME TO MONOPOLY     ")
print("--------------------------------\n")
print("""                ______________
    __,.,---'''''              '''''---..._
 ,-'             .....:::''::.:            '`-.
'           ...:::.....       '
            ''':::'''''       .               ,
|'-.._           ''''':::..::':          __,,-
 '-.._''`---.....______________.....---''__,,-
      ''`---.....______________.....---''\n\n""")

###### Player Registration ######

for i in range(1,9):
  name = input("Enter Player Name: ")
  players[name] = 1500
  cont = input("Add More Players? (Y/N) ")
  if cont == "N":
      if len(players) < 2:
        print("\n2 Minimum Players\n")
      else:
        break

###### Gameplay ######

print("\nMap\n")
for item, amount in map.items():
  print(item, "("+str(amount)+")")
  print("--------------------------------")

play = True
while play:
  for name, amount in players.items():
    print("\nIt's", name+"'s", "turn.")
    roll = input("Roll Dice By Typing Yes: ")
    if roll.lower() == "yes":
      dice_1 = random.randint(1,6)
      dice_2 = random.randint(1,6)
      if dice_1 == dice_2:
        print("You got lucky and won a bonus of $100.")
        amount += 100
      else:
        landed_on = random.randrange(len(map))
        places = list(map.keys())
        cost = list(map.values())
        print("You landed on", places[landed_on])
        if places[landed_on] not in ownership:
          choice = input("Would You Like To Buy This Property? (Y/N) ")
          if choice == "Y":
            print(places[landed_on], "is yours now!")
            amount -= cost[landed_on]
            ownership.update({places[landed_on]: name})
            players.update({name: amount})
        else:
          print("Oops! The place you landed on belongs to", ownership[places[landed_on]]+".", "You need to pay them rent.")
          amount -= rent[places[landed_on]]
          players.update({name: amount})
        if amount <= 0:
          print("You are bankrupt and have been eliminated.")
          players.pop(name)
    else:
      print("Sorry, you lost your chance.")
    end = input("Would You Like to End The Game? (Y/N) ")
    if end == "Y":
      print("The winner is", max(players, key=players.get))
      play = False
