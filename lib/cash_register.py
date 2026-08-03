class CashRegister:
    """CashRegister class to manage items, totals, discounts, and transactions."""

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        """Adds an item with price and optional quantity to the register[cite: 1, 2]."""
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {"item": item, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        """Applies the percentage discount to the current total[cite: 1, 2]."""
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        # Format whole numbers to integers for matching test assertions
        display_total = (
            int(self.total)
            if isinstance(self.total, float) and self.total.is_integer()
            else self.total
        )
        print(f"After the discount, the total comes to ${display_total}.")

    def void_last_transaction(self):
        """Removes the last transaction, updating items and total[cite: 1, 2]."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]

        for _ in range(last_transaction["quantity"]):
            if self.items:
                self.items.pop()
