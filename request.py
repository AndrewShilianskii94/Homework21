class Request:
    def __init__(self, warehouses, request_string):
        self._from = ""
        self._to = ""
        self._amount = 0
        self._product = ""

        self._parse_request_string(warehouses, request_string)

    def _parse_request_string(self, warehouses, request_string):
        parts = request_string.split()
        if len(parts) == 6 and parts[0] == "Доставить" and parts[2].isdigit() and parts[3] != "из" and parts[4] == "в":
            self._amount = int(parts[2])
            self._product = parts[1]
            self._from = parts[3]
            self._to = parts[5]

            if self._from not in warehouses or self._to not in warehouses:
                raise ValueError("Неверно указаны места (склад или магазин).")
        else:
            raise ValueError("Неверный формат запроса.")

    @property
    def from_(self):
        return self._from

    @property
    def to(self):
        return self._to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product
