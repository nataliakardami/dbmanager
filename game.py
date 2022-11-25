import time


class Choice:
    """
    Choice illustrates the main mechanism of this game. Once a choice is initiated, the user is called to make that choice and
    that will ultimately affect the outcome of the game
    """
    def __init__(self, choice_a, choice_b, choice_c,player):
        """
        Initiates a choice segment for the player
        :param choice_a:
        :param choice_b:
        :param choice_c:
        """

        self.choice_a = choice_a
        self.player = player
        self.choice_b = choice_b
        self.choice_c = choice_c
        self.show_choices()
        self.make_choice()
        self.current_choice = self.current_choice

    def get_current_choice(self):
        """
        :returns letter of current choice
        :param current_choice:
        :return:
        """
        return self.current_choice

    def show_choices(self):
        """
        displays the current choices to the player
        :return:
        """
        print("\nWhat do you want to do? Type a, b or c")
        print("<a> ", self.choice_a)
        print("<b> ", self.choice_b)
        print("<c>", self.choice_c)

    def make_choice(self):
        """
        Receives user input for the choice

        :return:
        """
        choice = False
        inp = input("Now it's time to make your choice. ")
        inp = inp.lower()
        while not choice:
            if inp == "a":
                print(self.player.name, ": ", self.choice_a)
                self.current_choice = "a"
                return "a"
            elif inp == "b":
                print(self.player.name, ": ", self.choice_b)
                self.current_choice = "b"
                return "b"
            elif inp == "c":
                print(self.player.name, ": ", self.choice_c)
                self.current_choice = "c"
                return "c"
            elif inp == "bag":
                print("Opening bag...")
                time.sleep(1)
                if len(self.bag) != 0:
                    for item in self.player.bag:
                        print(item.__str__)
                else:
                    print("Your bag is empty")
                self.show_choices()
                self.make_choice()
                inp = input()
            else:
                print("Error 405-- Wrong Input; TRY AGAIN>>")
                inp = input()

