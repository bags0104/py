import random
print("LET'S PLAY SNAKE WATER AND GUN \n")
l = ["snake", "water", "gun"]
print("YOU HAVE 10 CHANCES\n")
print("Enter s for snake, w for water, g for gun\n")
user_score = 0
comp_score = 0
chances = 10
while chances >= 1:
    comp_pick = random.choice(l)
    print(comp_pick)
    user_pick = input()
    if user_pick=='s':
        chances = chances - 1
        if comp_pick=='snake':
            print("It's a draw\n")
            continue
        elif comp_pick=='water':
            print("You win\n")
            user_score = user_score + 1
            continue
        else:
            print("Computer wins")
            comp_score = comp_score + 1
    elif user_pick=='w':
        chances = chances - 1
        if comp_pick=='snake':
            print("Computer wins\n")
            comp_score = comp_score + 1
            continue
        elif comp_pick=='water':
            print("It's a draw\n")
            continue
        else:
            print("You win\n")
            user_score = user_score + 1
            continue
    else:
        chances = chances - 1
        if comp_pick=='snake':
            print("You win\n")
            user_score = user_score + 1
            continue
        elif comp_pick=='water':
            print("Computer wins\n")
            comp_score = comp_score + 1
            continue
        else:
            print("It's a draw\n")
            continue

print("Game over\n")
print("Your score: ", user_score)
print("computer score: ", comp_score)

if(user_score > comp_score):
    print("YOU WON\n")
elif(comp_score> user_score):
    print("YOU LOST\n")
else:
    print("DRAW\n")
