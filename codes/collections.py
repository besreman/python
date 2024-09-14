ids = (1906, 9371, 8237, 3901)
users = ["Mery", "Anna", "Bob"]
message = "Registered"
colorSet = {"red","green", "blue"}
rankDictionary = {1:"First", 2:"Second", 3:"Third"}

#installed games
games = [
  'Soccer', 'Tic Tac Toe', 'Snake',
  'Puzzle', 'Rally']

#taking player's choice as a number input
choice = int(input())
print(games[choice])
#output the corresponding game


#list

players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

#Create 3 lists with 2 players each
#Use slicing to create a list for Group 1
g1 = players[0:2]

#Use slicing to create a list for Group 2
g2 = players[2:4]

#Use slicing to create a list for Group 3
g3 = players[4:6]

print("Group 1:")
#display the 1st group
print(g1)

print("Group 2:")
#display the 2nd group
print(g2)

print("Group 3:")
#display the 3rd group
print(g3)


# list slicing
cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[:3])