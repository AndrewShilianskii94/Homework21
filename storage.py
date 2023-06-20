from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self):
        self._items = {}
        self._capacity = 0

    @abstractmethod
    def add(self, item, quantity):
        pass

    @abstractmethod
    def remove(self, item, quantity):
        pass

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)
