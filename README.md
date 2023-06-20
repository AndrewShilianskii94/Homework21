# Homework21
Delivery Service
This project implements a simple delivery service system that simulates the movement of goods from a store to a warehouse. It utilizes abstract classes, getters, and setters to create and manage different storage locations, such as stores and warehouses.

Project Structure
The project consists of the following files:

storage.py: Defines the abstract class Storage, which serves as the base class for storage locations. It provides common methods for managing items in a storage location.
store.py: Implements the Store class, which is a type of storage location. It inherits from the Storage class and represents a store that can hold any number of different items.
shop.py: Implements the Shop class, which is another type of storage location. It also inherits from the Storage class and represents a shop that can hold a limited number of different items.
request.py: Defines the Request class, which represents a delivery request. It parses the user input and extracts relevant information such as the origin, destination, item, and quantity.
main.py: Contains the main function that handles user input, processes delivery requests, and manages the movement of items between storage locations.
Usage
To use the delivery service system, follow these steps:

Run the main.py file.
Enter a delivery request in the following format: Доставить <количество> <товар> из <откуда> в <куда>.
<количество>: The quantity of the item to be delivered.
<товар>: The name of the item to be delivered.
<откуда>: The origin of the delivery (e.g., "склад" or "магазин").
<куда>: The destination of the delivery (e.g., "склад" or "магазин").
The program will process the request and perform the delivery if it's possible.
The program will display the status of the storage locations (store and shop) after the delivery.
Example Usage
Copy code
Введите запрос на доставку: Доставить 3 печеньки из склад в магазин
Курьер забрал 3 печеньки со склада.
Курьер доставляет 3 печеньки в магазин.
Курьер доставил 3 печеньки в магазин.

В складе хранится:
0 печеньки
4 собачки
5 коробки

В магазине хранится:
3 печеньки
Copy code
Введите запрос на доставку: Доставить 3 собачки из склад в магазин
Нужное количество есть на складе.
Курьер забрал 3 собачки со склада.
Курьер доставляет 3 собачки в магазин.
Курьер доставил 3 собачки в магазин.

В складе хранится:
3 печеньки
1 собачки
5 коробки

В магазине хранится:
5 собачки
5 коробки
Notes
The project demonstrates the usage of abstract classes, getters, and setters to create and manage different storage locations.
The program validates the user input and provides appropriate error messages for incorrect formats or invalid locations.
The project can be extended to include additional functionality, such as tracking inventory levels, generating delivery reports, or adding more types of storage locations.
Feel free to modify and extend the project according to your specific requirements.
