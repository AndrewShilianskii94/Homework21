from storage import Storage


class Shop(Storage):
    MAX_UNIQUE_ITEMS = 5

    def __init__(self, capacity=20):
        super().__init__()
        self._capacity = capacity

    def add(self, item, quantity):
        if len(self._items) < self.MAX_UNIQUE_ITEMS:
            if item in self._items:
                self._items[item] += quantity
            else:
                self._items[item] = quantity

    def remove(self, item, quantity):
        if item in self._items:
            self._items[item] = max(self._items[item] - quantity, 0)
