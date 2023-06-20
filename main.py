from store import Store
from shop import Shop
from request import Request


def main():
    warehouses = {
        "склад": Store(),
        "магазин": Shop()
    }

    while True:
        user_input = input("Введите запрос на доставку: ")
        try:
            request = Request(warehouses.keys(), user_input)
            from_store = warehouses[request.from_]
            to_store = warehouses[request.to]

            if request.product not in from_store.get_items():
                print("Нужное количество отсутствует на складе.")
            elif to_store.get_free_space() < request.amount:
                print("В магазине недостаточно места.")
            else:
                from_store.remove(request.product, request.amount)
                to_store.add(request.product, request.amount)
                print(f"Курьер забрал {request.amount} {request.product} со склада.")
                print(f"Курьер доставляет {request.amount} {request.product} в магазин.")
                print(f"Курьер доставил {request.amount} {request.product} в магазин.")

            print("В складе хранится:")
            for item, count in warehouses["склад"].get_items().items():
                print(f"{count} {item}")
            print("В магазине хранится:")
            for item, count in warehouses["магазин"].get_items().items():
                print(f"{count} {item}")

        except ValueError as e:
            print(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    main()
