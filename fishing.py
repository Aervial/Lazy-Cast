# Hi to whoever might be reading this! I made this in the span of a few hours to practice my skills.
# I like the concept of this game and I hope to turn it into a real game someday.gi

import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

print("-" * 50)
print(Fore.MAGENTA + "Welcome to Lazy Cast!".center(50))
print("-" * 50)
print("")

def main():
    bal = 0
    while True:
        # prompt the user where to fish
        print(Fore.GREEN + "Where would you like to fish?")
        print(Fore.CYAN + "1. River")
        print(Fore.CYAN + "2. Lake")
        print(Fore.CYAN + "3. Sea")
        print("")

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
                    print(f"\n{Fore.CYAN}You chose to fish in the {locations[choice - 1]["name"]}!")
                    print("")
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
        gain = int(fish(luck))

        if gain > 0:
            bal += gain
            print(f"\n{Fore.CYAN}Your balance is now: {Fore.GREEN}${bal:.2f}")
        else:
            print(f"\n{Fore.CYAN}Balance: {Fore.GREEN}${bal:.2f}")

        play_again = input(Fore.GREEN + "\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            time.sleep(1.5)
            break  # Exit the loop and end the game


def gen_luck(b):
    luck = round(random.uniform(0.5, b) * 2) / 2
    return luck

def fish(luck):

    time.sleep(1)

    value = 0

    print(Fore.CYAN +"You draw back your rod, feeling the line tense as you prepare to cast", end="", flush=True)

    for i in range(random.randint(2, 5)):
        time.sleep(1)
        print(Fore.CYAN + ".", end="", flush=True)
    print("", flush=True)

    print(Fore.CYAN + "You cast your rod, feeling the line release as it flies into the water", end="", flush=True)

    for i in range(random.randint(2, 5)):
        time.sleep(1)
        print(Fore.CYAN + ".", end="", flush=True)
    print("", flush=True)

    for i in range(random.randint(2, 5)):
        time.sleep(1)
        print(Fore.CYAN + "blub", end="", flush=True)
        for i in range(random.randint(2, 5)):
            time.sleep(0.5)
            print(Fore.CYAN + ".", end="", flush=True)
    print("", flush=True)

    time.sleep(1)

    # See if the player catches anything
    if random.random() > 0.25:
        print(Fore.RED + "You didn't catch a fish.")
        return 0

    fish = [
        {"name": "Salmon", "chance": 20, "value": 50},
        {"name": "Tuna", "chance": 10, "value": 100},
        {"name": "Trout", "chance": 5, "value": 250},
        {"name": "Bass", "chance": 1, "value": 500},
        {"name": "Shark", "chance": 0.5, "value": 1000},
        {"name": "Carp", "chance": 25, "value": 30},
        {"name": "Catfish", "chance": 15, "value": 70},
        {"name": "Pike", "chance": 8, "value": 120},
        {"name": "Swordfish", "chance": 3, "value": 300},
        {"name": "Barracuda", "chance": 1.5, "value": 450},
        {"name": "Electric Eel", "chance": 0.8, "value": 800},
        {"name": "Mahi-Mahi", "chance": 6, "value": 200},
        {"name": "Sturgeon", "chance": 2, "value": 400},
        {"name": "Coelacanth", "chance": 0.1, "value": 5000},
        {"name": "Golden Koi", "chance": 0.25, "value": 2000}
    ]



    # multiply the chance to catch a fish by the current luck
    mf = []
    for f in fish:
        mc = f["chance"] * luck
        mf.append({"name": f["name"], "chance": mc, "value": f["value"]})
    
    # now that we have the modified luck, roll for a fish
    total_chance = sum(f["chance"] for f in mf)
    roll = random.uniform(0, total_chance)
    current = 0

    for f in mf:
        current += f["chance"]
        if roll <= current:
            print(f"\n{Fore.CYAN}You caught a {Fore.YELLOW}{f['name']}!{Fore.CYAN} Value: {Fore.GREEN}${f['value']}")
            value += int(f["value"])
            return int(f["value"])

main()
