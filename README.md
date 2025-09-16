# Ticket Sales Inventory System

## Project Description
This project is an implementation of the **Ticket Sales**, a classic programming exercise used to practice refactoring and unit testing.  
The program models an inn’s inventory system where items have two properties that change daily:  
- **SellIn**: The number of days we have to sell the item.  
- **Quality**: How valuable the item is.  

Different types of items follow different rules when their quality and sell-in values are updated.

---

## 🚀 What It Does
- Automatically updates the `sell_in` and `quality` values of items each day.  
- Handles special items like **Aged Brie**, **Sulfuras**, and **Backstage Passes** with unique behavior rules.  
- Ensures that **quality never falls below 0** and **never exceeds 50** (except for Sulfuras which always has a fixed quality).  

---

## ⚙️ How It Works
1. **Item objects** are created with a `name`, `sell_in`, and `quality`.  
2. The **GildedRose class** accepts a list of items.  
3. Each day, calling `update_quality()` applies the rules:  
   - Normal items: `quality` decreases by 1 each day.  
   - Once the sell-by date has passed, quality degrades twice as fast.  
   - **Aged Brie**: Increases in quality as it gets older.  
   - **Backstage passes**:  
     - Increase in quality as the concert approaches.  
     - Increase by 2 when `sell_in <= 10`.  
     - Increase by 3 when `sell_in <= 5`.  
     - Drop to 0 after the concert.  
   - **Sulfuras**: Legendary item, never decreases in `sell_in` or `quality`.  

---

## 🗂️ Files & Functions
### `ticket_sales.py`
- **`Item` class**:  
  Represents an inventory item with attributes `name`, `sell_in`, and `quality`.  

- **`GildedRose` class**:  
  - `__init__(items)`: Initializes the inventory with a list of `Item` objects.  
  - `update_quality()`: Applies all the rules to update each item’s `sell_in` and `quality`.  

### `test_ticket_sales.py`
- Contains **pytest-based unit tests** to validate the rules for:  
  - Normal items  
  - Aged Brie  
  - Sulfuras  
  - Backstage Passes  
  - Edge cases (quality bounds, sell_in after expiry, etc.)  

---

## 🎨 Design Choices & Reasoning
- **Explicit Rule-Based Updates**: The `update_quality()` function directly encodes each rule. This makes the behavior transparent for beginners but could later be refactored into separate strategy classes for scalability.  
- **Item as a Data Holder**: The `Item` class is kept simple (no logic inside) to keep responsibilities separated.  
- **Testing with pytest**: Pytest was chosen for simplicity and readability. Each rule has a clear, isolated test.  
- **Maintainability First**: While the code follows the original kata structure, the test suite ensures safety for future refactors.  

---

## ▶️ Running the Project
Clone the repository and run:

```bash
# Run the program (example)
python ticket_sales.py

# Run all tests
pytest -v

