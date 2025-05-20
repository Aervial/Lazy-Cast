# Hi to whoever might be reading this! I made this in the span of a few hours to practice my skills.
# I like the concept of this game and I hope to turn it into a real game someday.gi

import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    while True:
        # prompt the user where to fish
        print(Fore.GREEN + "Where would you like to fish?")
        print(Fore.BLUE + "1. River")
        print(Fore.BLUE + "2. Lake")
        print(Fore.BLUE + "3. Sea")

        locations = [
            {"name": "river", "boost": f"{round(random.uniform(1, 3) * 2) / 2}", "num": 1},
            {"name": "lake", "boost": f"{round(random.uniform(1, 3) * 2) / 2}", "num": 2},
            {"name": "sea", "boost": f"{round(random.uniform(1, 3) * 2) / 2}", "num": 3}
        ]

        # get the users choice
        while True:
            try:
                choice = int(input(""))
                if 1 <= choice <= 3:
                    break
            except ValueError:
                print(Fore.RED + "Please enter a number between 1 and 3.")
                continue

        for l in locations:
            if l["num"] == choice:
                boost = float(l["boost"])
                break

        # Generate a luck value

        luck = gen_luck(boost)

        # Got luck now, begin fishing
        fish(luck)

        play_again = input(Fore.GREEN + "\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break  # Exit the loop and end the game


def gen_luck(b):
    luck = round(random.uniform(0.5, b) * 2) / 2
    return luck

def fish(luck):

    print("You draw back your rod, feeling the line tense as you prepare to cast", end="", flush=True)

    for i in range(random.randint(2, 5)):
        time.sleep(1)
        print(".", end="", flush=True)
    print("")

    print("You cast your rod, feeling the line release as it flies into the water", end="", flush=True)

    for i in range(random.randint(2, 5)):
        time.sleep(1)
        print(".", end="", flush=True)
    print("")

    time.sleep(1)

    # See if the player catches anything
    if random.random() > 0.25:
        print(Fore.RED + "You didn't catch a fish.")
        return

    fish = [
    {"name": "Salmon", "chance": 20},
    {"name": "Tuna", "chance": 10},
    {"name": "Trout", "chance": 5},
    {"name": "Bass", "chance": 1},
    {"name": "Shark", "chance": 0.5}
    ]


    # multiply the chance to catch a fish by the current luck
    mf = []
    for f in fish:
        mc = f["chance"] * luck
        mf.append({"name": f["name"], "chance": mc})
    
    # now that we have the modified luck, roll for a fish
    total_chance = sum(f["chance"] for f in mf)
    roll = random.uniform(0, total_chance)
    current = 0

    for f in mf:
        current += f["chance"]
        if roll <= current:
            print(f"You caught a {f['name']}!")
            break

main()
