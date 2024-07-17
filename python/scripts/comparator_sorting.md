In Python, you can sort a list with a custom comparator by using the `sorted()` function or the `sort()` method of a list, along with the `key` parameter. The `key` parameter should be a function that extracts a comparison key

Certainly! Here are some examples of how to sort in Python using a comparator by providing a custom key function.

### Example 1: Sorting a List of Tuples by the Second Element
```python
# List of tuples
data = [(1, 3), (2, 2), (4, 1)]

# Sorting by the second element of each tuple
sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)
# Output: [(4, 1), (2, 2), (1, 3)]
```

### Example 2: Sorting a List of Dictionaries by a Specific Key
```python
# List of dictionaries
data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 30}]

# Sorting by the 'age' key
sorted_data = sorted(data, key=lambda x: x['age'])

print(sorted_data)
# Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]
```

### Example 3: Sorting with a Custom Comparator Function
In Python 2, you could use the `cmp` parameter of `sort()` and `sorted()`, but it was removed in Python 3. Instead, you can use `functools.cmp_to_key` to convert a comparator function to a key function.

```python
from functools import cmp_to_key

# Custom comparator function
def compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

data = [5, 2, 9, 1, 5, 6]

# Sorting using the custom comparator
sorted_data = sorted(data, key=cmp_to_key(compare))

print(sorted_data)
# Output: [1, 2, 5, 5, 6, 9]
```

### Example 4: Sorting Objects by an Attribute
```python
# Custom class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}({self.age})"

people = [Person('Alice', 25), Person('Bob', 20), Person('Charlie', 30)]

# Sorting by the 'age' attribute
sorted_people = sorted(people, key=lambda p: p.age)

print(sorted_people)
# Output: [Bob(20), Alice(25), Charlie(30)]
```

### Example 5: Sorting in Descending Order
```python
data = [5, 2, 9, 1, 5, 6]

# Sorting in descending order
sorted_data = sorted(data, key=lambda x: x, reverse=True)

print(sorted_data)
# Output: [9, 6, 5, 5, 2, 1]
```

These examples demonstrate how to use the `key` parameter with `sorted()` and `sort()` to perform custom sorting in Python. You can define your own logic for the comparison key to suit your needs.


source : ChatGPT