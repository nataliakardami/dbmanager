class Character:
    def __init__(self, name):
        self.is_dead = False
        self.morality_score = 0
        self.name = name
        self.dabloons = 0
        self.bag = []
        self.memberships = []
        self.transactions = []

    def print_name(self):
        return print(self.name)

    def __str__(self):
        """
        String representation of character's name
        :return:
        """
        return str(self.name)

    def get_name(self) -> object:
        """
        :returns the name of a character

        """
        return self.name

    def dead(self):
        """
        :returns a bool to indicate whether the player is dead (True) or alive (False)

        """
        return self.is_dead

    def change_morality_score(self, score):
        """
        changes the morality score due to "good" or "evil" character choices
        :param score:
        :return:
        """
        self.morality_score += score

    def get_morality_score(self):
        """
        :return: the morality score
        """
        return self.morality_score

    def add_dabloons(self, amount: int) -> int:
        """

        :rtype: object
        """
        if amount > 100:
            print("you just made an illegal transaction")
            self.change_morality_score(-100)
        self.dabloons += amount
        print("You added {amount} dabloons to your account. Your new total is {total} dabloons".format(amount=amount,
                                                                                                       total=self.dabloons))

    def subtr_dabloons(self, amount):
        self.dabloons -= amount
        print("You paid {amount} dabloons. Your new total is {total} dabloons".format(amount=amount,
                                                                                                       total=self.dabloons))
        if self.dabloons<0:
            print("You are now in debt")

    def count_dabloons(self):
        return print(self.dabloons)

    def set_name(self) -> str:
        """
        Asks the user for their name
        :return:
        """
        name_prompt = "What is your name? "
        self.name = str(input(name_prompt))

    def add_item(self, item):
        """
        Adds a collectable to bag
        :String item:
        :return:
        """
        self.bag.append(item)
        print("{item} added to your bag ".format(item=str(item)))

    def pick_up(self, item):
        """
        Asks the user whether they want to pick up an item or not
        :param item:
        :param bag:
        :return:
        """
        choice = input("Do you wanna pick up this item? Enter y for yes or n for no")
        choice.lower()

        if choice == "y":
            self.add_item(item)
        elif choice == "n":
            pass
        elif choice == "bag":
            for item in self.bag:
                print(str(item))
