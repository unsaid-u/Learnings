In Java, a record is a special kind of class introduced in Java 14 as a preview feature and became a standard feature in Java 16. Records are designed to be a concise way to model immutable data. They reduce the boilerplate code needed for classes that are primarily used to store data.

### Key Features of Records

1. **Conciseness**: Records reduce the amount of boilerplate code needed for simple data carriers. They automatically generate constructors, getters, `equals()`, `hashCode()`, and `toString()` methods.

2. **Immutability**: Records are immutable by default. All fields in a record are final and private.

3. **Pattern Matching**: Records support pattern matching, making it easier to work with them in switch statements and other contexts.

### Declaring a Record

Here is an example of how to declare a record in Java:

```java
public record Person(String name, int age) {}
```

This single line of code defines a `Person` class with two fields: `name` and `age`. The compiler automatically generates:

- A public constructor that initializes the fields.
- Private final fields for `name` and `age`.
- Public getter methods for both fields (`name()` and `age()`).
- `equals()`, `hashCode()`, and `toString()` methods.

### Example Usage

```java
public class Main {
    public static void main(String[] args) {
        Person person = new Person("Alice", 30);
        System.out.println(person.name());  // Outputs: Alice
        System.out.println(person.age());   // Outputs: 30
        System.out.println(person);         // Outputs: Person[name=Alice, age=30]
    }
}

public record Person(String name, int age) {}
```

### Customizing Records

You can also customize the components of a record, like adding validation in the constructor:

```java
public record Person(String name, int age) {
    public Person {
        if (age < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }
    }
}
```

### Use Cases for Records

Records are particularly useful for:

- Value classes: Classes that primarily store data and have no significant behavior.
- Data transfer objects (DTOs): Objects used to transfer data between different layers of an application.
- Configuration objects: Objects that hold configuration settings.

### Limitations of Records

- **Immutability**: All fields are final and cannot be modified after the object is created.
- **Inheritance**: Records cannot extend other classes (they implicitly extend `java.lang.Record`), but they can implement interfaces.

### Summary

Records in Java provide a concise and readable way to model immutable data. They significantly reduce the boilerplate code associated with typical data carrier classes, making your code cleaner and easier to maintain.