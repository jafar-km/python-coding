import random

import art
import game_data

Celebrity = []
Score = 0

# game_is_on = True
# while game_is_on:

random_person = random.choice(game_data.data)
Celebrity.append(random_person)
another_random_person = random.choice(game_data.data)
Celebrity.append(another_random_person)
celebrity_a = Celebrity[0]
celebrity_b = Celebrity[1]

game_is_on = True
while game_is_on:
    print(art.logo)
    print(f"Compare A: {celebrity_a["name"]}, a {celebrity_a["description"]}, from {celebrity_a["country"]}")
    print(art.vs)
    print(f"Compare B: {celebrity_b["name"]}, a {celebrity_b["description"]}, from {celebrity_b["country"]}")
    user_input = input("Who has more followers? Type 'A' or 'B':").lower()

    if user_input == 'a':
        if celebrity_a["follower_count"] > celebrity_b["follower_count"]:
            Score += 1
            print(f"You're right! Current Score: {Score}.")
            celebrity_a = celebrity_b
            celebrity_b = random.choice(game_data.data)
        else:
            game_is_on = False
            print(f"Sorry, you lose, your final score was {Score}")

    elif user_input == 'b':
        if celebrity_b["follower_count"] > celebrity_a["follower_count"]:
            Score +=1
            print(f"You're right! Current Score: {Score}.")
            celebrity_a = celebrity_b
            celebrity_b = random.choice(game_data.data)
        else:
            game_is_on = False
            print(f"Sorry, you lose, your final score was {Score}")

