Ticket Sales Inventory Simulator
---

Video Demo: <https://youtu.be/q11Ss3xxq-c>
---

Description:

The Ticket SalesInventory Simulator is a Python implementation of the classic Gilded Rose Kata problem. It models a fictional inn's inventory system where different categories of items degrade (or improve) in quality over time according to specific business rules.

This project was created as my CS50P final project, and it demonstrates my ability to design, implement, and test Python applications while applying good software design practices.
---

📌 Project Description
What It Does

Simulates the daily update of items in an inventory.

Applies special business rules to different types of items:

Normal items degrade in quality each day.

Aged Brie increases in quality over time.

Backstage passes increase in quality as a concert approaches but drop to 0 after the event.

Sulfuras is a legendary item and never changes.

Conjured items degrade in quality twice as fast as normal items.

How It Works

Each day, the program reduces the sell_in value (days left to sell).

Depending on the item type, quality is adjusted according to the rules.

The program can simulate any number of days and print the inventory state day by day.
---

📂 Files

ticket_sales.py
Contains the core logic:

Item class (represents an item with name, sell_in, and quality).

GildedRose class (handles inventory updates based on rules).

main.py
Entry point for running the program. Uses argparse for command-line arguments to set the number of simulation days.

test_ticket_sales.py
Contains unit tests using pytest to validate the behavior of the core functions and rules.

requirements.txt
Lists required dependencies (in this case, mainly pytest).
---

⚙️ Design Choices

No changes to Item class: This was a deliberate design decision in line with the original kata restrictions.

Single responsibility: GildedRose handles updating inventory, keeping logic centralized.

Command-line flexibility: Added argparse to allow users to set simulation duration.

Testing with pytest: Ensures reliability and correctness of business rules.
---

▶️ Example Usage
Run default 5-day simulation:
python3 main.py

Run custom 10-day simulation:
python3 main.py -d 10

Sample Output:

-------- Day 0 --------

Aged Brie, 2, 0

Backstage passes to a TAFKAL80ETC concert, 15, 20

Sulfuras, Hand of Ragnaros, 0, 80

food, 5, 10

Conjured Mana Cake, 3, 6


-------- Day 1 --------

Aged Brie, 1, 1

Backstage passes to a TAFKAL80ETC concert, 14, 21

Sulfuras, Hand of Ragnaros, 0, 80

food, 4, 9

Conjured Mana Cake, 2, 4

