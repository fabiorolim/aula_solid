from unittest import TestCase

from shopping import Order, Cigar, Water, Beer

from datetime import datetime


class TestOrder(TestCase):

    def setUp(self):
        self.order = Order()
        self.cigar = Cigar('Hollywood', 10)
        self.beer = Beer('Heineken', 5)
        self.walter = Water('Manaíra', 2)
        self.order.add_item(self.cigar)
        self.order.add_item(self.beer)
        self.order.add_item(self.walter)
        self.data = datetime.fromisoformat('2021-03-02')

    def test_get_subtotal(self):
        self.assertEqual(self.order.get_subtotal(), 17)

    def test_get_order_taxes(self):
        self.assertEqual(
            self.order.get_taxes(self.data), 2.5)

    def test_get_total(self):
        self.assertEqual(self.order.get_total(self.data), 19.5)


class TestOrderHoliday(TestCase):

    def setUp(self):
        self.order = Order()
        self.cigar = Cigar('Hollywood', 10)
        self.beer = Beer('Heineken', 5)
        self.walter = Water('Manaíra', 2)
        self.order.add_item(self.cigar)
        self.order.add_item(self.beer)
        self.order.add_item(self.walter)
        self.data = datetime.fromisoformat('2021-07-12')

    def test_get_subtotal(self):
        self.assertEqual(self.order.get_subtotal(), 17)

    def test_get_order_taxes(self):
        self.assertEqual(
            self.order.get_taxes(self.data), 1.5)

    def test_get_total(self):
        self.assertEqual(self.order.get_total(self.data), 18.5)
