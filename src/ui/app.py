# src/ui/app.py
import tkinter as tk
from tkinter import messagebox

from src.core.inventory_manager import InventoryManager
from src.core.brew_controller import BrewController
from src.core.payment_processor import PaymentProcessor


class CoffeeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OOP Coffee Machine")
        self.minsize(520, 340)
        self.configure(padx=16, pady=16)

        # Core components
        self.inventory = InventoryManager(water=600, coffee=200, milk=300)
        self.brew = BrewController(self.inventory)
        self.pay = PaymentProcessor()

        # --- UI: Left (drinks) ---
        left = tk.Frame(self)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(left, text="Choose a drink", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0, 8))

        self.drink_buttons = {}
        for drink in ("latte", "espresso", "cappuccino"):
            btn = tk.Button(
                left,
                text=f"{drink.title()} • ${self.brew.prices[drink]:.2f}",
                command=lambda d=drink: self.handle_brew(d),
                width=22
            )
            btn.pack(anchor="w", pady=4)
            self.drink_buttons[drink] = btn

        # --- UI: Right (status) ---
        right = tk.Frame(self)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(right, text="Status", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0, 8))

        self.status = tk.StringVar(value="Ready.")
        tk.Label(right, textvariable=self.status, anchor="w", justify="left").pack(fill=tk.X)

        self.levels = tk.StringVar()
        tk.Label(right, textvariable=self.levels, anchor="w", justify="left", fg="#4b4b4b").pack(fill=tk.X, pady=(8, 0))

        # --- Controls (bottom) ---
        controls = tk.Frame(self)
        controls.pack(side=tk.BOTTOM, fill=tk.X, pady=(12, 0))

        tk.Button(controls, text="Refill Ingredients", command=self.handle_refill).pack(side=tk.LEFT)
        tk.Button(controls, text="Add $1 Credit", command=lambda: self.handle_credit(1.0)).pack(side=tk.LEFT, padx=6)

        self.balance = tk.StringVar()
        tk.Label(controls, textvariable=self.balance).pack(side=tk.RIGHT)

        self.refresh_ui()

    # ---- Actions ----
    def handle_brew(self, drink: str):
        cost = self.brew.prices[drink]

        if not self.pay.charge(cost):
            messagebox.showinfo("Insufficient credit", f"Add funds: ${cost:.2f} needed.")
            self.status.set("Not enough credit.")
            self.refresh_ui()
            return

        ok = self.brew.brew(drink)
        if not ok:
            messagebox.showwarning("Out of ingredients", "Refill ingredients to continue.")
            self.pay.add_credit(cost)  # refund if brew failed due to low inventory
            self.status.set("Brew failed (low inventory). Refunded.")
        else:
            self.status.set(f"Brewing {drink}... Done!")

        self.refresh_ui()

    def handle_refill(self):
        # Simple refill to defaults
        self.inventory.levels.update({"water": 600, "coffee": 200, "milk": 300})
        self.status.set("Ingredients refilled.")
        self.refresh_ui()

    def handle_credit(self, amount: float):
        self.pay.add_credit(amount)
        self.status.set(f"Added ${amount:.2f} credit.")
        self.refresh_ui()

    # ---- UI helpers ----
    def refresh_ui(self):
        lv = self.inventory.get_levels()
        self.levels.set(f"Water: {lv['water']} ml • Coffee: {lv['coffee']} g • Milk: {lv.get('milk',0)} ml")
        self.balance.set(f"Balance: ${self.pay.balance:.2f}")

        # Enable/disable drink buttons if inventory is insufficient
        for d, btn in self.drink_buttons.items():
            state = (tk.NORMAL if self.brew.can_brew(d) else tk.DISABLED)
            btn.config(state=state)


if __name__ == "__main__":
    app = CoffeeApp()
    app.mainloop()
