import unittest

from ticket_sales import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_food(self):
        items = [Item("food", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("food", items[0].name)


if __name__ == '__main__':
    unittest.main()
