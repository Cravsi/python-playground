"""Playground for class instances"""


class User():
    """
    Creates an instance of User
    """
    def __init__(self, username, email, subscribed):
        self.username = username
        self.email = email
        self.subscribed = subscribed

    def description(self):
        """
        Describes the instance of User
        """
        return f"user: {self.username}, email: {self.email}, \
        subscribed: {self.subscribed}"


# write your code here
user_one = User('arnold', 'arnold@email.com', True)
print(user_one.email)
user_one.email = 'murphy@email.com'
print(user_one.description())
