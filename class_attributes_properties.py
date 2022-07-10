"""
Playground for the difference between
class properties and attributes
"""


class ContactInfo():
    """Creates an instance of ContactInfo"""
    about = "Contact information for customer"

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def description(self):
        """Class description"""
        return f"Name: {self.name} \nE-mail: {self.email}"


print(ContactInfo.about)

contact = ContactInfo('dave', 'lister@email.com')
print(contact.description())
