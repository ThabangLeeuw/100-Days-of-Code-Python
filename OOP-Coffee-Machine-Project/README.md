# ☕ Coffee Machine Project

A simple Python console-based coffee machine simulation.  
This project models a coffee vending machine that can:

- Display available drinks
- Process user orders
- Check ingredient availability
- Handle payments
- Track profit
- Generate reports

---

## 📂 Project Structure

The project is organized into modular classes:

- **`menu.py`** → Defines the `Menu` class and available drinks.
- **`coffee_maker.py`** → Handles ingredient tracking, resource checks, and coffee preparation.
- **`money_machine.py`** → Manages payments, currency, and profit tracking.
- **`main.py`** → Runs the main program loop, interacting with the user.

---

## ▶️ How It Works

1. The program starts and displays available drink options.
2. The user enters a choice:
   - A drink name (e.g., `latte`, `espresso`, `cappuccino`)
   - `report` → Shows current resources and profit
   - `off` → Turns off the machine
3. If a valid drink is chosen:
   - The machine checks if enough resources are available.
   - The user is prompted to insert coins.
   - If payment is successful, the drink is prepared and served.
   - Profit is updated accordingly.

---

## 🛠️ Example Usage

```bash
What would you like to order? espresso/latte/cappuccino:
> latte
Please insert coins...
Here is your latte ☕ Enjoy!
