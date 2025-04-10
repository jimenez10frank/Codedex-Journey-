import random

playerScore = 0
computerScore = 0

while playerScore < 3 and computerScore < 3 :
    player = int(input('Choose 1-rock 2-Paper 3Scissors!'))

    computer = random.randint(1, 3)
    if player == computer:
        print("Its a tie")
    elif player == 1 and computer == 2:
        computerScore += 1
        print(f"Computer won this round")
        print("Player Score: ", playerScore)
        print("Computer Score: ", computerScore)
    elif player == 2 and computer == 1:
        playerScore += 1
        print(f"Player won this round")
        print("Player Score: ", playerScore)
        print("Computer Score: ", computerScore)
    elif player == 3 and computer == 1:
        computerScore += 1
        print(f"Computer won this round")
        print("Player Score: ", playerScore)
        print("Computer Score: ", computerScore)
    elif player == 1 and computer == 3:
        playerScore += 1
        print(f"Player won this round")
        print("Player Score: ", playerScore)
        print("Computer Score: ", computerScore)
print('match ended')
if playerScore == 3:
    print('Player Won')
else:
    print('Computer Won')