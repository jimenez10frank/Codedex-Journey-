player1 = {
    'name': "junior",
    'position': "middfielder",
    'jersey number': 10,
    'goals': 10
},
{
    'name': "frank",
    'position': "attacker",
    'jersey number': 9,
    'goals': 6
},
{
    'name': "jaden",
    'position': "defender",
    'jersey number': 2,
    'goals': 2
}
# this is a loop to print out players names
names = [player["name"] for player in player1]
print("players names: ", names)

# this is a loop to print out players positions
positions = [player["position"] for player in player1]
print("players positions: ", positions)


# here i make a average goals loop

average_goals = sum(player["goals"] for player in player1) / len(player1)
print("average goals: ", average_goals)