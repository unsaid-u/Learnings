#### var , let, const

    var - can be globally or locally scoped 

    var is not block scoped - this is an issue 
        it can be redeclared

    let is block scoped (updates value but can't redeclared)
    const is also block scoped but cannot be reassigned

#### Hoisting
Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their scope before code execution.

> Hoisting isn’t specific to variables, it also hoists functions. The difference is that while var variables get initialized with undefined, functions get initialized with their actual value.


#### `This` is js
* **Global Context**: this refers to the global object (e.g., window in browsers).
* **Function Context**: this depends on how the function is called.
* **Arrow Functions**: this is lexically scoped (inherits from the enclosing context).
* **Constructor Functions**: this refers to the newly created object instance.
* **Explicit Binding**: You can explicitly set this using call, apply, or bind.
* **Class Context**: this refers to the instance of the class.


#### call, apply, bind
    The call, apply, and bind methods in JavaScript are used to control the value of this when invoking functions.
* `call`: The call method invokes a function with a specified this value and individual arguments passed as separate arguments. It allows you to borrow functions from one object and   invoke them in the context of another.
* `apply`: Similar to call, the apply method invokes a function with a specified this value, but it takes an array or an array-like object as its second argument, allowing you to pass a variable number of arguments to the function.
* `bind`: The bind method creates a new function that, when called, has its this value set to a specific value and prepends any provided arguments to the original function's arguments list. It is often used to create functions with preset contexts or partially applied arguments.


```
One usecase 
const person1 = {
  name: 'Alice',
  greet: function() {
    console.log('Hello, ' + this.name);
  }
};

const person2 = { name: 'Bob' };

// Borrow the greet method from person1 for person2
person1.greet.call(person2);  // Outputs: "Hello, Bob"
```

> _While defining methods inside a class or an object is generally the best practice, call, apply, and bind give you more control over the this context. They are especially useful in scenarios where you need to borrow methods, control context in callbacks, perform partial application, or work within functional programming paradigms._


#### closures
```
function outerFunction() {
  let outerVariable = 'I am from the outer function';

  function innerFunction() {
    console.log(outerVariable); // The inner function has access to the outer function's variable
  }

  return innerFunction;
}

const closureExample = outerFunction();
closureExample(); // Outputs: 'I am from the outer function'
```
A closure in JavaScript is a fundamental concept that allows a function to "remember" the environment in which it was created, even after that function is executed outside of its original scope. In other words, a closure gives you access to an outer function's scope from an inner function.

some usecases include 
* creating private vars 
* Closures allow you to create functions with some pre-filled arguments.
* Maintaining State Across Multiple Function Calls
> Understanding closures is crucial for mastering JavaScript, especially when working with asynchronous code, callbacks, or functional programming techniques.


#### arrow vs regular functions 
Arrow functions are a concise syntax for writing functions in JavaScript, introduced in ES6 (ECMAScript 2015). They provide a shorter syntax and have some differences in behavior compared to regular functions. Here is a comparison table highlighting the key differences:

| Feature                  | Arrow Functions                                  | Regular Functions                               |
|--------------------------|--------------------------------------------------|-------------------------------------------------|
| **Syntax**               | `const func = (param1, param2) => { /* code */ };` | `function func(param1, param2) { /* code */ }` |
| **`this` Binding**       | Does not have its own `this`. Inherits `this` from the surrounding lexical context. | Has its own `this` context, which depends on how the function is called. |
| **`arguments` Object**   | Does not have its own `arguments` object. Use rest parameters (`...args`) instead. | Has its own `arguments` object that holds the passed arguments. |
| **`new` Keyword**        | Cannot be used as a constructor (i.e., cannot be instantiated with `new`). | Can be used as a constructor (i.e., can be instantiated with `new`). |
| **`super` Keyword**      | Cannot use `super` keyword.                     | Can use `super` to call methods from parent classes in class constructors. |
| **Method Definitions**   | Not suited for method definitions in objects or classes because `this` behaves differently. | Commonly used for defining methods in objects and classes, as `this` refers to the object or class instance. |
| **Implicit Return**      | Can omit braces and `return` keyword for single expression returns: `param => expression` | Requires braces and `return` keyword if you want to return a value: `function(param) { return expression; }` |
| **Usage in Methods**     | Not recommended for object methods or class methods due to `this` binding issues. | Suitable for methods in objects and classes. `this` refers to the object or class instance. |

### Examples:

#### Arrow Function
```javascript
const add = (a, b) => a + b;
console.log(add(2, 3)); // 5

const person = {
  name: 'John',
  greet: () => {
    console.log(`Hello, my name is ${this.name}`); // `this` is not bound to `person`
  }
};
person.greet(); // "Hello, my name is undefined"
```

#### Regular Function
```javascript
function add(a, b) {
  return a + b;
}
console.log(add(2, 3)); // 5

const person = {
  name: 'John',
  greet: function() {
    console.log(`Hello, my name is ${this.name}`); // `this` is bound to `person`
  }
};
person.greet(); // "Hello, my name is John"
```

**Summary:**

- **Arrow functions** offer a more concise syntax and inherit `this` from their lexical scope, making them useful for callbacks or functions where the lexical `this` context is desired.
- **Regular functions** provide their own `this` context and are more suitable for object methods, constructors, and scenarios where the function needs to manage its own `this` binding.


#### Reduce 
The reduce() method in JavaScript is used to iterate over an array and accumulate a single result based on the values in the array. It applies a function (reducer function) to each element in the array, resulting in a single output value. The reduce() method takes two arguments: a reducer function and an optional initial value.

```
array.reduce((accumulator, currentValue, currentIndex, array) => {
  // return updated accumulator
}, initialValue);
```

* accumulator: The accumulated result from the previous iteration, or the initial value if provided.
* currentValue: The current element being processed in the array.
* currentIndex (optional): The index of the current element being processed.
* array (optional): The array upon which reduce() was called.
* initialValue (optional): The initial value to start the accumulation. If not provided, the first element of the array will be used as the initial value.

Here are some of my favorite JavaScript interview questions that are commonly asked to software developers:

___

### Core JavaScript
1. **Explain the difference between `var`, `let`, and `const`.**
2. **What is the difference between `==` and `===` in JavaScript?**
3. **What is a closure, and how does it work in JavaScript?**
4. **How does the `this` keyword work in JavaScript?**
5. **Explain the concept of hoisting in JavaScript.**
6. **What are JavaScript promises, and how do they work?**
7. **Can you explain the event loop in JavaScript? How does it handle asynchronous code?**
8. **What is a prototype in JavaScript? How does prototypal inheritance work?**
9. **What are arrow functions, and how do they differ from regular functions?**
10. **Explain how `map()`, `filter()`, and `reduce()` work in JavaScript. Provide examples.**

### Advanced Topics
1. **What are higher-order functions in JavaScript? Can you provide an example?**
2. **What is memoization, and how can it be implemented in JavaScript?**
3. **How does the `async`/`await` syntax work? What are its advantages over using promises directly?**
4. **Explain how JavaScript's garbage collection works.**
5. **What is event delegation, and how does it benefit performance?**
6. **How do you handle errors in JavaScript? Discuss both synchronous and asynchronous error handling.**
7. **What are generators in JavaScript? How do they differ from regular functions?**
8. **Explain the concept of immutability in JavaScript. How can you enforce immutability?**
9. **What are modules in JavaScript, and how are they different from namespaces?**
10. **What is the purpose of JavaScript’s `call()`, `apply()`, and `bind()` methods? Provide use cases.**

### Browser & DOM
1. **How do you prevent event bubbling in the DOM?**
2. **What is the difference between `event.preventDefault()` and `event.stopPropagation()`?**
3. **How does JavaScript handle cookies, local storage, and session storage?**
4. **What is the difference between `innerHTML`, `outerHTML`, and `textContent`?**
5. **How does debouncing and throttling work in JavaScript?**

### ES6 and Beyond
1. **What are destructuring assignments, and how can they be used in JavaScript?**
2. **Explain the concept of rest and spread operators.**
3. **What are JavaScript modules (ES6)? How do you import and export them?**
4. **How does the `Set` and `Map` data structure work in JavaScript?**
5. **What are template literals, and how do they differ from regular strings?**

### Performance Optimization
1. **How would you optimize the performance of a JavaScript application?**
2. **What techniques do you use to reduce load time and improve the rendering of JavaScript-heavy applications?**
3. **Explain the concept of lazy loading in JavaScript. How can it be implemented?**

### Miscellaneous
1. **What are some common memory leaks in JavaScript, and how can they be avoided?**
2. **What are JavaScript design patterns? Can you explain a few commonly used patterns?**
3. **How would you implement a deep copy of an object in JavaScript?**
4. **What is the difference between synchronous and asynchronous code in JavaScript?**
5. **What are web workers, and when would you use them?**

These questions cover a wide range of topics and can help gauge a candidate's understanding of JavaScript, from fundamental concepts to advanced techniques.