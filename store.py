from storage import Storage


class Store(Storage):
    def __init__(self, capacity=100):
        super().__init__()
        self._capacity = capacity

    def add(self, item, quantity):
        if item in self._items:
            self._items[item] += quantity
        else:
            self._items[item] = quantity

    def remove(self, item, quantity):
        if item in self._items:
            self._items[item] = max(self._items[item] - quantity, 0)
