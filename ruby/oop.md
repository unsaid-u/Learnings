# OOPS in ruby

### Object-Oriented Programming (OOP) in Ruby

Ruby, like Python, is an object-oriented programming language. OOP in Ruby follows the principles of encapsulation, inheritance, and polymorphism, allowing you to design applications with reusable and modular code. Here's a breakdown of key OOP concepts in Ruby:

#### 1. **Classes and Objects**
In Ruby, everything is an object, and classes are blueprints for creating objects. You define a class using the `class` keyword, and you create objects by instantiating the class with the `new` method.

**Example**:
```ruby
class Dog
  def initialize(name, age)
    @name = name
    @age = age
  end
  
  def speak
    puts "#{@name} says Woof!"
  end
end

# Create an instance of Dog
dog = Dog.new("Rex", 5)
dog.speak  # Output: Rex says Woof!
```
- The `initialize` method is Ruby’s constructor method, which is similar to Python's `__init__`.
- Instance variables in Ruby are prefixed with an `@` symbol, while in Python they are prefixed with `self.`.

#### 2. **Encapsulation**
Encapsulation in Ruby refers to restricting access to certain methods or variables, typically by marking them as private or protected.

- **Public methods** are available to anyone.
- **Private methods** are only available within the class.
- **Protected methods** can be accessed within the class and by subclasses.

**Example**:
```ruby
class Car
  def initialize(make, model)
    @make = make
    @model = model
  end

  def info
    "Make: #{@make}, Model: #{@model}"
  end
  
  private
  
  def secret_method
    puts "This is a secret!"
  end
end

car = Car.new("Toyota", "Corolla")
puts car.info  # Output: Make: Toyota, Model: Corolla
# car.secret_method  # This will raise an error because it's private
```
- Ruby's `private` and `protected` methods are similar to Python's `private` (double underscore) and `protected` (single underscore) attributes.

#### 3. **Inheritance**
Ruby supports inheritance, allowing one class to inherit the behavior and attributes of another.

**Example**:
```ruby
class Animal
  def speak
    puts "Animal makes a sound"
  end
end

class Dog < Animal
  def speak
    puts "Dog barks"
  end
end

dog = Dog.new
dog.speak  # Output: Dog barks
```
- In Ruby, you use the `<` symbol to indicate inheritance, similar to Python's class inheritance using parentheses.

#### 4. **Polymorphism**
Polymorphism allows different objects to respond to the same method in their own way.

**Example**:
```ruby
class Cat
  def speak
    puts "Meow"
  end
end

class Dog
  def speak
    puts "Woof"
  end
end

def make_sound(animal)
  animal.speak
end

dog = Dog.new
cat = Cat.new
make_sound(dog)  # Output: Woof
make_sound(cat)  # Output: Meow
```
- Polymorphism in Ruby is achieved via method overriding, similar to Python, where objects of different classes implement the same method with different behavior.

### Comparison Between Ruby and Python OOP

While both Ruby and Python support object-oriented programming and share many similarities in OOP concepts, there are key differences between how OOP is handled in each language.

| Concept               | Ruby                                            | Python                                         |
|-----------------------|-------------------------------------------------|------------------------------------------------|
| **Everything is an Object** | Everything in Ruby is an object, including numbers and strings. | Everything in Python is an object, but it’s not as pervasive as Ruby. |
| **Class Definition**   | `class ClassName`                               | `class ClassName:`                             |
| **Constructor Method** | `def initialize` is the constructor, similar to Python's `__init__`. | `def __init__` is the constructor.             |
| **Instance Variables** | Instance variables are prefixed with `@` (e.g., `@name`). | Instance variables are prefixed with `self.` (e.g., `self.name`). |
| **Private & Protected**| `private` and `protected` keywords for encapsulation. | Private variables use double underscores (`__variable`) and protected by convention. |
| **Inheritance**        | Inheritance is denoted using `<` (e.g., `class Dog < Animal`). | Inheritance is denoted using parentheses (e.g., `class Dog(Animal):`). |
| **Polymorphism**       | Achieved via method overriding. | Achieved via method overriding in the same way. |
| **Method Visibility**  | Methods are public by default, and you can mark them private or protected. | Methods are public by default, but you can create private or protected methods using decorators like `@property` or by convention (e.g., prefixing with underscores). |

#### Key Differences:
1. **Method Visibility**: Ruby has explicit keywords like `private` and `protected` to control method visibility. Python relies on conventions (like leading underscores) and decorators to enforce visibility rules.
2. **Instance Variable Syntax**: In Ruby, instance variables are prefixed with `@`, whereas in Python, instance variables are prefixed with `self.`.
3. **Everything is an Object**: Ruby's approach to "everything is an object" is more pervasive, meaning even simple data types like integers and strings are treated as objects, while in Python, some built-in types are treated differently, although they are still objects in the strict sense.
4. **Inheritance Syntax**: In Ruby, inheritance is done using `<`, whereas in Python, inheritance uses parentheses.

### Conclusion

Ruby and Python both implement the principles of object-oriented programming, but they have different syntaxes and conventions. Ruby’s OOP system is tightly integrated with the language, providing a highly flexible and expressive environment for object-oriented development. Python also embraces OOP but tends to lean on simplicity and readability. The choice between Ruby and Python for OOP often comes down to personal preference or specific project needs, as both are powerful in building object-oriented systems.