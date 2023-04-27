from diceGame import game


games = int(input("type amount of games played: "))

wins = 0

for i in range(0,games):
    wins = wins + game()
    
print("amount of wins", wins)
estimate = (float(wins))/(float(games))

print("The probability of winning is", estimate)
