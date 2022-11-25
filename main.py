from Item import Collectable
from character import Character
import time

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for c

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    player = Character("Bingus")

    player.print_name()

    item = Collectable("bread", 2)
    print(item)

    choice = ""
    player.add_item("bingus")
    player.add_item("squingus")
    inp = input("Enter x to start dabloon manager")

    while inp != "q":
        print("------------------------------------------")
        inp = input(
            "Select an action:\n Type \" buy [item-name] \" to purchase an item and put it in your bag \n "
            "Type \"add\" to add dabloons to your total \n"
            "Type \"subtract\" to remove dabloons  \n")
        print("------------------------------------------")

        action = inp.split()

        if action[0] == "buy": #TODO
            try:
                amount = int(input("How much does it cost? "))

            except ValueError:
                print("Invalid input!")

            player.subtr_dabloons(amount)
            item_name = action[1]
            player.add_item(item_name)
            print("Successfully purchased {item_name} for {amount} dabloons".format(item_name=item_name, amount=amount))

        elif action[0] == "add":
            while True:
                try:
                    amount = int(input("Enter amount "))
                    #amount = int(action[1])
                    print(amount)
                    break
                except ValueError:
                    print("Invalid input!")

            player.add_dabloons(amount)
            time.sleep(1)
        elif action[0] == "subtract":
            while True:
                try:
                    amount = int(input("Enter amount "))
                    # amount = int(action[1])
                    print(amount)
                    break
                except ValueError:
                    print("Invalid input!")

            player.subtr_dabloons(amount)
            time.sleep(1)
        elif action[0] == "open":
            print("Opening bag...")
            time.sleep(1)
            if len(player.bag) != 0:
                for item in player.bag:
                    print(item)
            else:
                print("Your bag is empty")
                choice = False

        else:
            continue
