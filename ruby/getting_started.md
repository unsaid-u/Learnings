### Ruby Basics: Notes for Getting Started

Ruby is a dynamic, high-level programming language known for its simplicity and focus on developer happiness. If you're transitioning from languages like Python or JavaScript, you'll find many familiar concepts, but Ruby also brings its own flavor of expressiveness.

---

### **1. Ruby Basics**

#### **Syntax**
- Ruby syntax is clean and minimal, making it easy to read and write.
- End statements or blocks with `end` instead of braces (`{}`).
- Everything is an object, including numbers and `nil`.

**Examples:**
```ruby
# Print a message
puts "Hello, Ruby!"

# Simple arithmetic
sum = 5 + 10
puts sum  # Output: 15
```

---

#### **Variables**
- No type declarations; Ruby infers the type.
- Variable names are case-sensitive.
- Naming convention: snake_case for variables and methods.

**Examples:**
```ruby
name = "Ruby"
age = 25
pi = 3.14
```

---

#### **Control Structures**
- Ruby supports standard conditionals and loops.
- No parentheses required around `if` or `while` conditions.

**Conditionals:**
```ruby
if age >= 18
  puts "Adult"
elsif age < 18 && age > 12
  puts "Teenager"
else
  puts "Child"
end
```

**Loops:**
```ruby
5.times { puts "Hello!" }
(1..5).each { |i| puts i }  # Inclusive range
```

**Tip:** Use Ruby’s built-in iterators like `.times`, `.each`, and `.map` for clean and concise looping.

---

#### **Methods**
- Define reusable blocks of code using `def`.
- Methods return the last evaluated expression by default.

**Examples:**
```ruby
def greet(name)
  "Hello, #{name}!"
end

puts greet("Alice")
```

---

### **2. Object-Oriented Programming in Ruby**

#### **Core OOP Concepts**
Ruby is a fully object-oriented language. Every value, even primitives like numbers and strings, is an object.

- **Classes and Objects:** Classes define blueprints, and objects are instances.
- **Encapsulation:** Use `attr_accessor`, `attr_reader`, or `attr_writer` for getters/setters.
- **Inheritance:** Use `<` to inherit.
- **Polymorphism:** Achieved through method overriding.

**Example:**
```ruby
class Animal
  def speak
    "Generic sound"
  end
end

class Dog < Animal
  def speak
    "Woof!"
  end
end

dog = Dog.new
puts dog.speak  # Output: Woof!
```

**Encapsulation:**
```ruby
class Person
  attr_accessor :name, :age  # Getter and setter

  def initialize(name, age)
    @name = name
    @age = age
  end

  def greet
    "Hi, my name is #{@name}."
  end
end

person = Person.new("Alice", 30)
puts person.greet
```

---

### **3. How Ruby Runs**

#### **Compilation and Execution**
- Ruby is an **interpreted language**.
- Code is executed directly by the Ruby interpreter (no explicit compilation step like in Java).
- You can run Ruby scripts via the command line:
  ```bash
  ruby script.rb
  ```

#### **IRB (Interactive Ruby)**
- Ruby has an interactive shell called IRB where you can test code snippets:
  ```bash
  irb
  > puts "Hello, Ruby!"
  ```

#### **Tips for Running Ruby Code:**
- Use `irb` for quick tests.
- Use the `ruby` command for running scripts.
- Leverage `pry` (a gem) for advanced debugging.

---

### **4. Key Features**

#### **Dynamic Typing**
- Ruby determines variable types at runtime.
- No need to declare types explicitly.

#### **Duck Typing**
- Ruby relies on behavior rather than type.
- If an object responds to a method, it’s treated as compatible.

**Example:**
```ruby
def quack(duck)
  duck.quack
end

class Duck
  def quack
    puts "Quack!"
  end
end

class Person
  def quack
    puts "I'm pretending to quack!"
  end
end

quack(Duck.new)
quack(Person.new)
```

---

### **5. Error Handling**

Ruby uses `begin`, `rescue`, and `ensure` for exception handling.

**Example:**
```ruby
begin
  result = 10 / 0
rescue ZeroDivisionError => e
  puts "Error: #{e.message}"
ensure
  puts "Execution complete."
end
```

---

### **6. Ruby Gems**
- Gems are Ruby’s package manager modules (like `pip` in Python or `npm` in JavaScript).
- Install gems using:
  ```bash
  gem install gem_name
  ```

**Popular Gems:**
- `rails`: For web development.
- `sinatra`: Lightweight web applications.
- `pry`: Debugging and IRB alternative.

---

### **7. Ruby for Day-to-Day Applications**

- **Scripts for automation**:
  - File manipulation, text parsing, web scraping (use `nokogiri` gem).

- **Web Development**:
  - Learn Ruby on Rails for full-stack web apps.
  - Use Sinatra for lightweight web services.

- **Data Processing**:
  - Handle CSVs (`csv` module) and JSON data (`json` module).

---

### **8. Tips for Learning Ruby**

1. **Practice IRB**: Experiment with small code snippets in the interactive Ruby shell.
2. **Read Code**: Explore open-source Ruby projects on GitHub.
3. **Build Projects**: Start with simple utilities like a to-do list or file organizer.
4. **Learn Rails**: Once you’re comfortable, dive into Rails for web app development.
5. **Follow Community Best Practices**: Check out Ruby Style Guide and conventions.

---

### **9. Resources for Learning Ruby**

- **Books**:
  - "Programming Ruby" (The Pickaxe Book)
  - "Eloquent Ruby"
- **Online**:
  - [Ruby Official Documentation](https://www.ruby-lang.org/en/documentation/)
  - Codecademy’s Ruby course.
  - RubyMonk for interactive tutorials.
- **Community**:
  - Join forums like Ruby Subreddit or Stack Overflow for support.

---

### **10. Final Thoughts**
Ruby’s simplicity and expressive syntax make it a fantastic tool for day-to-day application development. Its rich libraries and active community provide everything you need to get started. Begin small, keep experimenting, and soon you’ll be developing robust Ruby applications!