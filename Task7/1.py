import random 
user_score=0
comp_score=0
Tie=0
choices=["rock","paper","scissors"]
while True: 
    user_choice=input("Enter rock,paper,scissors or quit): ").lower()
    if user_choice=="quit": 
        print("Thanks for playing!")
        print("Your score:",user_score,"Computer score:",comp_score,"tie matches:",Tie)
        break 
    if user_choice not in choices: 
        print("Invalid input.Please try again.")
        continue 
    computer_choice=random.choice(choices)
    print("Computer choose:",computer_choice)
    if user_choice==computer_choice:
        print("Tie!")
        Tie+=1
    elif (user_choice=="rock" and computer_choice=="scissors") or \
         (user_choice=="scissors" and computer_choice=="paper") or \
         (user_choice=="paper" and computer_choice=="rock"):
        print("You win!")
        user_score+=1
    else:
        print("You lose!")
        comp_score+=1