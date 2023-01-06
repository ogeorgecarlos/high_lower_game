from art import logo, vs
import random
from game_data import data
from os import system


points = 0
while True:
    # assign a value to compare
    # if he value fo "compare_b" is equal to the value of "compare_b"
    # Compare_b willreceive a new value, in the "while" loop.
    compare_a = random.choice(data)
    compare_b = random.choice(data)
    equal_copares = compare_a == compare_b
    while equal_copares:
        compare_b = random.choice(data)

    # the start
    print(logo)

    print(f"✔ Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")

    print(vs)

    print(f"✔ Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")

    # The user will choice who has more followers in intagram
    # Each hit add one point.
    # If there is a error, the game ends and will be show teh total points.
    while True:
        choice = input("\n❓ Who has more followers? Type 'A' or 'B': ").strip().lower()
        if choice  not in "ab" or choice == '':
            print('❌ Enter with a válid option.')
        else:
            break

    if choice  == 'a' and compare_a['follower_count'] > compare_b['follower_count']:
        print('certo')
        points += 1
        system('cls')
    elif choice  == 'b' and compare_a['follower_count'] < compare_b['follower_count']:
        print('certo')
        points += 1
        system('cls')
    else:
        break


print(f"\n😢 Sorry, that's wrong. Final score: {points}")