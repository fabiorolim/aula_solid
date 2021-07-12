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


class Item:

    def __init__(self, category, description, price):
        self.category = category
        self.description = description
        self.price = price

    # No Open-Closed Principle -> when to add new items
    def calculate_taxes(self):
        taxes = 0
        if self.category == 'Cigar':
            taxes = self.price * 0.2
        elif self.category == 'Beer':
            taxes = self.price * 0.1

        return taxes
