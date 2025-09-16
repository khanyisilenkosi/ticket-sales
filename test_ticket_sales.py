import pytest
from ticket_sales import Item, GildedRose


def update(item):
    """Helper to update a single item once."""
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    return item


def test_normal_item_degrades():
    item = Item("foo", sell_in=10, quality=20)
    update(item)
    assert item.sell_in == 9
    assert item.quality == 19


def test_quality_never_negative():
    item = Item("foo", sell_in=5, quality=0)
    update(item)
    assert item.quality == 0


def test_aged_brie_increases():
    item = Item("Aged Brie", sell_in=5, quality=10)
    update(item)
    assert item.quality == 11
    assert item.sell_in == 4


def test_quality_never_above_50():
    item = Item("Aged Brie", sell_in=5, quality=50)
    update(item)
    assert item.quality == 50


def test_sulfuras_never_changes():
    item = Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
    update(item)
    assert item.sell_in == 0
    assert item.quality == 80


def test_backstage_passes_increase_normally():
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
    update(item)
    assert item.quality == 21


def test_backstage_passes_increase_faster_close_to_concert():
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)
    update(item)
    assert item.quality == 22


def test_backstage_passes_increase_even_faster_very_close():
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)
    update(item)
    assert item.quality == 23


def test_backstage_passes_drop_to_zero_after_concert():
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)
    update(item)
    assert item.quality == 0


def test_quality_degrades_twice_as_fast_after_sell_date():
    item = Item("foo", sell_in=0, quality=10)
    update(item)
    assert item.sell_in == -1
    assert item.quality == 8

