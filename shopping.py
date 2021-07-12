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

    # No Single responsibility
    def get_taxes(self):
        taxes = 0
        for item in self.items:
            if item.category == 'Cigar':
                taxes += item.price * 0.2
            elif item.category == 'Beer':
                taxes += item.price * 0.1

        return taxes

    def get_total(self):
        return self.get_subtotal() + self.get_taxes()


class Item:

    def __init__(self, category, description, price):
        self.category = category
        self.description = description
        self.price = price
