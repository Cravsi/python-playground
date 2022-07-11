
"""
Playground for mixins
"""


class TicketMixin:
    """
    Mixin to calculate ticket price based on age
    """
    def calculate_ticket_price(self, age):
        price = 0
        if self.age < 12:
            return price
        elif self.age < 18:
            price = 15
            return price
        elif self.age < 60:
            price = 20
            return price
        else:
            price = 10
            return price


class Customer(TicketMixin):
    """
    Create instance of Customer
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        """
        Prints out customer description and ticket price
        """
        return f"{self.name} age {self.age} ticket price is {self.calculate_ticket_price(self.age)}"


customer = Customer('Ryan Philips', 22)
print(customer.describe())
