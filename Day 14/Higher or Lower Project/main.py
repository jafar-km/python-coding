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

game_is_on = True
while game_is_on:
    print(art.logo)
    print(f"Compare A: {Celebrity[0]["name"]}, a {Celebrity[0]["description"]}, from {Celebrity[0]["country"]}")
    print(art.vs)
    print(f"Compare B: {Celebrity[1]["name"]}, a {Celebrity[1]["description"]}, from {Celebrity[1]["country"]}")
    celebrity_a = Celebrity[0]
    celebrity_b = Celebrity[1]
    user_input = input("Who has more followers? Type 'A' or 'B':").lower()
    if Celebrity[0]["follower_count"] > Celebrity[1]["follower_count"]:
        Score += 1
        print(f"You're right! Current Score: {Score}.")
        celebrity_a = Celebrity[1]
        celebrity_b = random.choice(game_data.data)



    else:
        game_is_on = False
        print(f"Sorry, you lose, your final score was {Score}")

