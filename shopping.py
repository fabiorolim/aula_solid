from abc import abstractmethod, ABC


class Order:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_subtotal(self):
        subtotal = 0
        for item in self.items:
            subtotal += item.price

        return subtotal

    def get_taxes(self):
        taxes = 0
        for item in self.items:
            taxes += item.calculate_taxes()

        return taxes

    def get_total(self):
        return self.get_subtotal() + self.get_taxes()


class Item(ABC):

    def __init__(self, category, description, price):
        self.category = category
        self.description = description
        self.price = price

    # Template method
    def calculate_taxes(self):
        return self.price * self.get_tax()

    @abstractmethod
    def get_tax(self):
        pass


class Cigar(Item):

    def __init__(self, description, price):
        super(Cigar, self).__init__('Cigar', description, price)

    def get_tax(self):
        return 0.2


class Beer(Item):

    def __init__(self, description, price):
        super(Beer, self).__init__('Beer', description, price)

    def get_tax(self):
        return 0.1


class Water(Item):

    def __init__(self, description, price):
        super(Water, self).__init__('Water', description, price)

    # No Liskov Substitution Principle -> Tests Failed
    def get_tax(self):
        raise Exception('Not implemented')
