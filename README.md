Ticket Sales Inventory System
Overview

Welcome to the Ticket Sales Inventory System! This project simulates inventory management for a small, upscale inn run by the friendly innkeeper Allison. The inn specializes in high-quality goods, but unfortunately, all items naturally degrade in Quality as their SellIn date approaches.

Your task is to extend the system to support a new category of items — Conjured items — while maintaining all existing functionality.

Project Background

The inventory system was originally developed by Leeroy, a no-nonsense programmer who has since moved on. The system updates the inventory automatically every day, adjusting the SellIn and Quality values for each item.

SellIn: The number of days remaining to sell the item.

Quality: The inherent value of the item.

At the end of each day, the system automatically updates all items according to their type.

Core Rules

General Items

SellIn decreases by 1 each day.

Quality decreases by 1 each day.

Once the sell-by date passes (SellIn <= 0), Quality degrades twice as fast.

Quality is never negative.

Special Items

Aged Brie

Increases in Quality as it ages.

Quality cannot exceed 50.

Sulfuras (Legendary Item)

SellIn and Quality do not change.

Quality is always 80.

Backstage Passes

Increases in Quality as the concert date approaches:

+2 when SellIn <= 10

+3 when SellIn <= 5

Quality drops to 0 after the concert (SellIn < 0).

Conjured Items (New Feature)

Degrade in Quality twice as fast as normal items.

Implementation Guidelines

You may modify the UpdateQuality method and add new helper methods as needed.

Do not alter the Item class or the Items property — these belong to the goblin in the corner, who is fiercely protective.

You may make UpdateQuality or Items static if necessary.

Ensure all existing functionality works correctly after adding new features.

Quality limits:

Minimum: 0

Maximum: 50 (except Sulfuras, which is always 80)

Inventory Update Logic

Each day, the system updates every item according to its rules.

Different types of items have unique behaviors regarding how Quality changes over time.

Legendary items remain constant, while ordinary and conjured items degrade.

Special items like Aged Brie and Backstage Passes increase in quality under certain conditions.

Example Item Categories
Item Type	Behavior Summary
Normal Item	Decreases in quality by 1 daily, 2 after sell-by date.
Aged Brie	Increases in quality as it ages (max 50).
Sulfuras (Legendary)	Quality always 80, never decreases, SellIn never decreases.
Backstage Passes	Quality increases as concert approaches, drops to 0 after concert.
Conjured Item	Degrades in quality twice as fast as normal items.
Contributing

Step 1: Review existing UpdateQuality logic.

Step 2: Implement rules for Conjured items.

Step 3: Write or update tests to ensure all rules are enforced correctly.

Step 4: Maintain backward compatibility with existing item types.

Notes

Keep Quality within bounds at all times.

Special cases for legendary and concert items should be handled carefully.

The system is designed to be extendable; future item types may be added without modifying the Item class.

Feel free to make any changes to the UpdateQuality method and add any new code as long as everything
still works correctly. However, do not alter the Item class or Items property as those belong to the
goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code
ownership (you can make the UpdateQuality method and Items property static if you like, we'll cover
for you).
Just for clarification, an item can never have its Quality increase above 50, however "Sulfuras" is a
legendary item and as such its Quality is 80 and it never alters.
