from ticket_sales import Item, GildedRose

def main():
    items = [
        Item("Aged Brie", 2, 0),
        Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        Item("Sulfuras, Hand of Ragnaros", 0, 80),
        Item("food", 5, 10)
    ]

    gilded_rose = GildedRose(items)

    for day in range(5):
        print(f"-------- day {day} --------")
        for item in items:
            print(item)
        print("")
        gilded_rose.update_quality()

if __name__ == "__main__":
    main()
