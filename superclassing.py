""""
A safe place for practicing python superclasses
"""


class BaseOrderItem():
    """
    Creates instance of BaseOrderItem
    """
    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity

    def total_price(self):
        """
        Returns total based on price * quantity ordered
        """
        return self.price * self.quantity


class ShoeOrderItem(BaseOrderItem):
    """
    Creates instance of ShoeOrderItem
    """
    def __init__(self, product, price, quantity, size):
        super().__init__(product, price, quantity)
        self.size = size

    def describe(self):
        """
        Return user order as a string
        """
        return f"Order: {self.product} in size {self.size}, quantity: {self.quantity}, total price: {super().total_price()}"


shoe_order = ShoeOrderItem('Ladies Nike Trainers', 40, 2, 42)
print(shoe_order.describe())
