from unittest import TestCase
from shopping import Order, Item, Cigar, Water, Beer


class TestOrder(TestCase):

    def setUp(self):
        self.order = Order()
        self.cigar = Cigar('Hollywood', 10)
        self.beer = Beer('Heineken', 5)
        self.walter = Water('Manaíra', 2)
        self.order.add_item(self.cigar)
        self.order.add_item(self.beer)
        self.order.add_item(self.walter)

    def test_get_subtotal(self):
        self.assertEqual(self.order.get_subtotal(), 17)

    def test_get_order_taxes(self):
        self.assertEqual(self.order.get_taxes(), 2.5)

    def test_get_total(self):
        self.assertEqual(self.order.get_total(), 19.5)
