class Collectable:
    """
    A collectable is a specific type of item that can be picked up and added to the bag
    """

    def __init__(self, item_name, price):
        """
        :type item_name: str
        :type price: int
        """
        self.item_name = item_name
        self.price = price

    def __str__(self):
        """
        :returns a string representation of a collectable
        """
        return "{name} is worth {price} dabloons.".format(name=str(self.item_name), price=str(self.price))
