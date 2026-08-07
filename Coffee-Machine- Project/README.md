# Coffee Machine Program ☕

## Overview 🎯
This program simulates a coffee machine that can serve espresso, latte, or cappuccino.  
It manages resources (water, milk, coffee, money), processes coin input, checks if resources are sufficient, and handles transactions including refunds and change.

## Features 💻
- **Prompt user**: Asks what drink they would like (`espresso`, `latte`, `cappuccino`).
- **Turn off**: Enter `off` to shut down the machine.
- **Report**: Enter `report` to display current resources and money.
- **Resource check**: Ensures there are enough ingredients before making a drink.
- **Coin processing**: Accepts quarters, dimes, nickels, and pennies, calculates total value.
- **Transaction handling**:
  - Refunds if not enough money is inserted.
  - Provides change if too much money is inserted.
  - Adds profit to the machine when a drink is successfully purchased.
- **Make coffee**: Deducts ingredients from resources and confirms the drink is served.

## How It Works
1. The program runs in a loop until the user enters `off`.
2. User selects a drink or enters `report`.
3. If a drink is selected:
   - The program checks if resources are sufficient.
   - Prompts the user to insert coins.
   - Calculates the total money inserted.
   - Compares against the drink’s cost:
     - If enough: deducts resources, adds profit, gives change, and serves the drink.
     - If not enough: refunds money.
4. After each action, the program loops back to prompt the next customer.

