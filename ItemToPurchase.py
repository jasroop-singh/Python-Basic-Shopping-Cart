class ItemToPurchase:
    def __init__(self, item_name="", item_price=0.0, item_quantity=0, item_description=""):
        self._name = item_name
        self._price = item_price
        self._quantity = item_quantity
        self._description = item_description

    def print_item_cost(self):
        total_price = self._price * self._quantity
        print(self._name, self._quantity, "@ $" + str(self._price), "=", total_price)

    def print_item_description(self):
        print(str(self._name) + ":", self._description)

