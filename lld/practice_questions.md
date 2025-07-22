Here are a dozen beginner-level Low-Level Design (LLD) problem statements in Python. Each is focused on designing the classes, their relationships, and APIs—without needing a full distributed or high-scale solution. You can pick any to sketch UML, write class definitions, interfaces/abstract base classes, and method signatures.

---

### 1. **Parking Lot System**

**Description:** Model a parking lot that has multiple levels, each with a fixed number of motorcycle, car, and bus spots.
**Requirements:**

* Classes: `ParkingLot`, `Level`, `ParkingSpot` (and subclasses for each spot type), `Vehicle` (and subclasses).
* Operations: `park(vehicle)`, `unpark(ticket)`, `get_available_spots()`.
* Generate and track parking tickets.

---

### 2. **Vending Machine**

**Description:** Design a vending machine that sells different products in slots and handles coins/bills.
**Requirements:**

* Classes: `VendingMachine`, `Slot`, `Product`, `PaymentProcessor` (with coin/bill validators), `Transaction`.
* Operations: `select_product(slot_id)`, `insert_money(amount)`, `dispense()`, `refund()`.
* Track inventory and transaction history.

---

### 3. **Library Management System**

**Description:** Build a system to manage books, members, loans, and returns.
**Requirements:**

* Classes: `Library`, `Book`, `Member`, `Loan`, `Catalog`.
* Operations: `checkout_book(member_id, book_id)`, `return_book(loan_id)`, `search_books(...)`.
* Enforce maximum books per member and due dates.

---

### 4. **LRU Cache**

**Description:** Implement an LRU (Least Recently Used) cache with a fixed capacity.
**Requirements:**

* Class: `LRUCache` with `get(key)`, `put(key, value)`.
* Must evict least-recently used item on overflow.
* Use Python’s `OrderedDict` or custom doubly-linked list + hash map.

---

### 5. **Elevator Control System**

**Description:** Model one or more elevators in a building servicing floor requests.
**Requirements:**

* Classes: `Elevator`, `ElevatorController`, `FloorRequest`.
* Operations: `request_pickup(floor, direction)`, `step()` (move each elevator one unit), `status()`.
* Simple scheduling: nearest-elevator first.

---

### 6. **Deck of Cards & Poker Hand Evaluator**

**Description:** Represent a deck of 52 cards, allow shuffling and dealing, and evaluate a poker hand.
**Requirements:**

* Classes: `Card`, `Deck`, `HandEvaluator`.
* Operations: `shuffle()`, `deal(n)`, `evaluate(hand) -> ranking`.
* Identify pairs, straights, flushes, etc.

---

### 7. **URL Shortener**

**Description:** Design a service to create and resolve short URLs.
**Requirements:**

* Classes: `URLShortener`, `Storage` (in-memory dict), optional `Analytics`.
* Operations: `shorten(long_url) -> short_code`, `resolve(short_code) -> long_url`.
* Handle collisions and custom alias support.

---

### 8. **Chat Room**

**Description:** Model a chat room where users can join, leave, and broadcast messages.
**Requirements:**

* Classes: `ChatRoom`, `User`, `Message`.
* Operations: `join(user)`, `leave(user)`, `send_message(user, text)`, `get_history()`.
* Optionally support private messaging.

---

### 9. **Restaurant Reservation System**

**Description:** Manage table reservations for a restaurant with different table sizes.
**Requirements:**

* Classes: `Restaurant`, `Table`, `Reservation`, `Customer`.
* Operations: `reserve(customer, datetime, party_size)`, `cancel(reservation_id)`, `list_available_slots(date)`.
* Match party size to table size and track overlapping slots.

---

### 10. **File Storage Service**

**Description:** Simulate a simple file system with folders and files.
**Requirements:**

* Classes: `File`, `Directory`, `FileSystem`.
* Operations: `mkdir(path)`, `add_file(path, content)`, `read_file(path)`, `ls(path)`, `delete(path)`.
* Handle nested directories.

---

### 11. **Movie Ticket Booking**

**Description:** Design a seat-booking system for movie theaters.
**Requirements:**

* Classes: `Theater`, `Screening`, `Seat`, `Booking`.
* Operations: `show_seats(screening_id)`, `book_seat(screening_id, seat_id, customer)`, `cancel_booking(booking_id)`.
* Prevent double-booking.

---

### 12. **Observable Pattern (Event Dispatcher)**

**Description:** Implement the Observer pattern to allow subscribers to listen to events.
**Requirements:**

* Classes: `Event`, `Publisher`, `Subscriber`.
* Methods: `subscribe(event_type, subscriber)`, `unsubscribe(...)`, `notify(event)`.
* Support multiple event types and callbacks.

---

## How to Use These Statements

1. **Draw Class Diagrams:** Sketch the classes, attributes, and their relationships (association, inheritance, aggregation).
2. **Define Interfaces/ABCs:** Use Python’s `abc` module to define abstract base classes where appropriate.
3. **Write Code Skeletons:** Implement class stubs, method signatures, and basic in-memory logic.
4. **Add Unit Tests:** For operations like `LRUCache.get/put`, or `VendingMachine.dispense()`, write pytest tests.
5. **Iterate Complexity:** Once you’ve got the basics, introduce features like persistence, concurrency (thread-safe booking), or caching.

These problem statements will help you practice designing clear, maintainable class hierarchies and APIs in Python. Happy designing!
