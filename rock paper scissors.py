import random 
choices=["rock","paper","scissor"]
user = input("Choose rock,paper or scissor:").lower()
computer = random.choice(choices)

print("Computer Chose:",computer)

if user == computer:
    print("Tie")
elif (
     (user == "rock" and computer == "scissor") or
     (user == "paper" and computer == "rock") or
     (user == "scissor" and computer == "paper") 
     ):
    print("Youe win!")
else:
    print("Compurter Win")