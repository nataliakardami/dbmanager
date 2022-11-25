class Dabloon():
    def __init__(self, amount):
        self.legal = True  # true if acquired through legal means, eg given >100
        self.counterfeit = False # true if type of dabloon is simle
        self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        return self.amount + " dabloons"
