from abc import abstractmethod, ABC


class Order:

    def __init__(self):
        self.items = []

    def __getitem__(self, i):
        return self.items[i]

    def add_item(self, item):
        self.items.append(item)

    def get_subtotal(self):
        return sum([item.price for item in self])

    def get_taxes(self, data):
        taxes = 0
        for item in self:
            if isinstance(item, ItemTaxed):
                taxes += item.calculate_taxes(data)

        return taxes

    def get_total(self, data):
        return self.get_subtotal() + self.get_taxes(data)


class Item(ABC):

    def __init__(self, category, description, price):
        self.category = category
        self.description = description
        self.price = price


class ItemTaxed(Item):

    # Template method
    def calculate_taxes(self, data):
        return self.price * self.get_tax(data)

    @abstractmethod
    def get_tax(self, data):
        pass


class Cigar(ItemTaxed):

    def __init__(self, description, price):
        super(Cigar, self).__init__('Cigar', description, price)

    def get_tax(self, data):
        tax = 0.2
        if data.month == 7:
            tax = 0.1

        return tax


class Beer(ItemTaxed):

    def __init__(self, description, price):
        super(Beer, self).__init__('Beer', description, price)

    def get_tax(self, data):
        return 0.1


class Water(Item):

    def __init__(self, description, price):
        super(Water, self).__init__('Water', description, price)
