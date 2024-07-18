### Operator Overloading in Python

**Operator Overloading** allows you to define custom behavior for standard operators when they are used with user-defined objects. This is done by defining special methods in your class that correspond to specific operators. This helps enabling Polymorphism. 

#### Example of Operator Overloading

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)  # Output: Vector(6, 8)
print(v1 - v2)  # Output: Vector(-2, -2)
```

In this example:
- The `__add__` method is used to define the behavior of the `+` operator.
- The `__sub__` method is used to define the behavior of the `-` operator.
- The `__str__` method is used to define the behavior of the `str()` function, which is invoked by the `print()` function.

#### Common Special Methods for Operator Overloading

- `__add__(self, other)`: To define behavior for the `+` operator.
- `__sub__(self, other)`: To define behavior for the `-` operator.
- `__mul__(self, other)`: To define behavior for the `*` operator.
- `__truediv__(self, other)`: To define behavior for the `/` operator.
- `__floordiv__(self, other)`: To define behavior for the `//` operator.
- `__mod__(self, other)`: To define behavior for the `%` operator.
- `__pow__(self, other)`: To define behavior for the `**` operator.
- `__lt__(self, other)`: To define behavior for the `<` operator.
- `__le__(self, other)`: To define behavior for the `<=` operator.
- `__eq__(self, other)`: To define behavior for the `==` operator.
- `__ne__(self, other)`: To define behavior for the `!=` operator.
- `__gt__(self, other)`: To define behavior for the `>` operator.
- `__ge__(self, other)`: To define behavior for the `>=` operator.

Operator overloading allows you to extend the functionality of operators to work with user-defined types, making your custom objects behave more like built-in types in Python.