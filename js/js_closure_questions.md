# Tricky JavaScript Closure Interview Questions

## Question 1: Classic Loop Closure Problem
```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i);
  }, 1000);
}

// What does this output after 1 second?
```

## Question 2: Function Factory Pattern
```javascript
function createCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}

const counter1 = createCounter();
const counter2 = createCounter();

console.log(counter1()); // What does this output?
console.log(counter1()); // What does this output?
console.log(counter2()); // What does this output?
```

## Question 3: Closure with Parameters
```javascript
function multiplier(factor) {
  return function(number) {
    return number * factor;
  };
}

const double = multiplier(2);
const triple = multiplier(3);

console.log(double(5)); // What does this output?
console.log(triple(5)); // What does this output?

// Now the tricky part:
const functions = [];
for (var i = 1; i <= 3; i++) {
  functions.push(multiplier(i));
}

console.log(functions[0](10)); // What does this output?
console.log(functions[2](10)); // What does this output?
```

## Question 4: Closure Memory Leak Scenario
```javascript
function attachListener() {
  const largeData = new Array(1000000).fill('data');
  
  document.getElementById('button').addEventListener('click', function() {
    console.log('Button clicked');
  });
  
  return function() {
    console.log('Cleanup function');
  };
}

const cleanup = attachListener();
// What happens to largeData? Is it garbage collected?
```

## Question 5: Nested Closures
```javascript
function outer(x) {
  return function middle(y) {
    return function inner(z) {
      return x + y + z;
    };
  };
}

const result1 = outer(1)(2)(3);
const result2 = outer(1)(2);
const result3 = result2(3);

console.log(result1); // What does this output?
console.log(result3); // What does this output?

// Now what about this?
const partialOuter = outer(5);
const partialMiddle = partialOuter(10);
console.log(partialMiddle(15)); // What does this output?
```

## Question 6: Closure with Object Mutation
```javascript
function createUser(name) {
  const user = { name: name, age: 0 };
  
  return {
    getName: function() {
      return user.name;
    },
    getAge: function() {
      return user.age;
    },
    setAge: function(newAge) {
      user.age = newAge;
    }
  };
}

const user1 = createUser('Alice');
const user2 = createUser('Bob');

user1.setAge(25);
user2.setAge(30);

console.log(user1.getName(), user1.getAge()); // What does this output?
console.log(user2.getName(), user2.getAge()); // What does this output?

// Tricky part:
const getName = user1.getName;
console.log(getName()); // What does this output?
```

## Question 7: Module Pattern with Closure
```javascript
const myModule = (function() {
  let privateVar = 0;
  
  function privateFunction() {
    console.log('Private function called');
  }
  
  return {
    publicMethod: function() {
      privateVar++;
      privateFunction();
      return privateVar;
    },
    getPrivateVar: function() {
      return privateVar;
    }
  };
})();

console.log(myModule.publicMethod()); // What does this output?
console.log(myModule.publicMethod()); // What does this output?
console.log(myModule.privateVar);     // What does this output?

// What happens if we try this?
const { publicMethod } = myModule;
console.log(publicMethod()); // What does this output?
```

## Question 8: Closure with Array Methods
```javascript
function createFunctions() {
  const functions = [];
  
  for (var i = 0; i < 3; i++) {
    functions.push(function() {
      return i;
    });
  }
  
  return functions;
}

const funcs = createFunctions();
console.log(funcs[0]()); // What does this output?
console.log(funcs[1]()); // What does this output?
console.log(funcs[2]()); // What does this output?

// How would you fix this to return 0, 1, 2 respectively?
```

## Question 9: Closure with setTimeout and Parameters
```javascript
function processData(data) {
  for (var i = 0; i < data.length; i++) {
    setTimeout(function() {
      console.log('Processing:', data[i]);
    }, i * 1000);
  }
}

processData(['A', 'B', 'C']);
// What does this output and when?
```

## Question 10: Closure Scope Chain
```javascript
let globalVar = 'global';

function outer() {
  let outerVar = 'outer';
  
  function middle() {
    let middleVar = 'middle';
    
    function inner() {
      let innerVar = 'inner';
      console.log(globalVar, outerVar, middleVar, innerVar);
    }
    
    return inner;
  }
  
  return middle;
}

const innerFunc = outer()();
innerFunc(); // What does this output?

// Now what about this scenario?
function createFunction() {
  let x = 1;
  
  if (true) {
    let x = 2;
    return function() {
      console.log(x);
    };
  }
}

const func = createFunction();
func(); // What does this output?
```

## Question 11: Closure with Function Hoisting
```javascript
function mystery() {
  var funcs = [];
  
  for (var i = 0; i < 3; i++) {
    funcs.push(createFunc);
  }
  
  function createFunc() {
    return i;
  }
  
  return funcs;
}

const result = mystery();
console.log(result[0]()); // What does this output?
console.log(result[1]()); // What does this output?
```

## Question 12: Closure with Async/Await
```javascript
function createAsyncCounter() {
  let count = 0;
  
  return async function() {
    await new Promise(resolve => setTimeout(resolve, 100));
    count++;
    return count;
  };
}

const asyncCounter = createAsyncCounter();

asyncCounter().then(console.log); // What does this output?
asyncCounter().then(console.log); // What does this output?
asyncCounter().then(console.log); // What does this output?

// Are these executed sequentially or in parallel?
```

## Question 13: Closure Memory Reference
```javascript
function createClosures() {
  const obj = { value: 1 };
  
  const closure1 = function() {
    return obj.value;
  };
  
  const closure2 = function() {
    obj.value++;
    return obj.value;
  };
  
  return [closure1, closure2];
}

const [getter, incrementer] = createClosures();

console.log(getter());      // What does this output?
console.log(incrementer()); // What does this output?
console.log(getter());      // What does this output?
```

## Question 14: Closure with Function Arguments
```javascript
function createLogger(prefix) {
  return function(...args) {
    console.log(prefix + ':', ...args);
  };
}

const errorLogger = createLogger('ERROR');
const infoLogger = createLogger('INFO');

errorLogger('Something went wrong'); // What does this output?
infoLogger('Process completed');     // What does this output?

// Now the tricky part:
function createMultiLogger() {
  const loggers = [];
  const prefixes = ['DEBUG', 'INFO', 'WARN', 'ERROR'];
  
  for (var i = 0; i < prefixes.length; i++) {
    loggers.push(function(message) {
      console.log(prefixes[i] + ':', message);
    });
  }
  
  return loggers;
}

const [debug, info, warn, error] = createMultiLogger();
debug('Test message'); // What does this output?
```

## Question 15: Advanced Closure Pattern
```javascript
function createSecureCounter(initialValue, maxValue) {
  let count = initialValue;
  let isLocked = false;
  
  return {
    increment: function() {
      if (isLocked) return 'Counter is locked';
      if (count >= maxValue) {
        isLocked = true;
        return 'Max value reached, counter locked';
      }
      count++;
      return count;
    },
    
    decrement: function() {
      if (isLocked) return 'Counter is locked';
      count--;
      return count;
    },
    
    getValue: function() {
      return count;
    },
    
    reset: function(newInitial) {
      count = newInitial || initialValue;
      isLocked = false;
      return 'Counter reset';
    }
  };
}

const counter = createSecureCounter(0, 3);

console.log(counter.increment()); // What does this output?
console.log(counter.increment()); // What does this output?
console.log(counter.increment()); // What does this output?
console.log(counter.increment()); // What does this output?
console.log(counter.decrement()); // What does this output?
```

---

## Answers and Explanations

### Answer 1:
**Output:** `3` (printed three times)

**Explanation:** By the time the setTimeout callbacks execute, the loop has finished and `i` is 3. All three functions close over the same variable `i`.

**Fix:**
```javascript
// Using let
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 1000);
}

// Using IIFE
for (var i = 0; i < 3; i++) {
  (function(j) {
    setTimeout(() => console.log(j), 1000);
  })(i);
}
```

### Answer 2:
**Output:** `1`, `2`, `1`

**Explanation:** Each call to `createCounter()` creates a new closure with its own `count` variable. `counter1` and `counter2` have separate counters.

### Answer 3:
**Output:** `10`, `15`, `10`, `30`

**Explanation:** Each multiplier function closes over its own `factor` value. The loop creates separate closures for each iteration because `multiplier` is called immediately.

### Answer 4:
**Answer:** `largeData` is NOT garbage collected

**Explanation:** The event listener function creates a closure that has access to the entire scope of `attachListener`, including `largeData`, even though it doesn't use it. This creates a memory leak.

**Fix:**
```javascript
function attachListener() {
  const largeData = new Array(1000000).fill('data');
  
  const handler = function() {
    console.log('Button clicked');
  };
  
  document.getElementById('button').addEventListener('click', handler);
  
  return function() {
    document.getElementById('button').removeEventListener('click', handler);
    console.log('Cleanup function');
  };
}
```

### Answer 5:
**Output:** `6`, `6`, `30`

**Explanation:** Each function level creates a closure over the parameters from outer scopes. Partial application works because closures maintain access to all outer variables.

### Answer 6:
**Output:** `Alice 25`, `Bob 30`, `Alice`

**Explanation:** Each `createUser` call creates a separate closure with its own `user` object. The extracted `getName` function still has access to its closure even when called without context.

### Answer 7:
**Output:** `Private function called\n1`, `Private function called\n2`, `undefined`, `Private function called\n3`

**Explanation:** The IIFE creates a closure preserving `privateVar` and `privateFunction`. Destructured methods still maintain their closure. `privateVar` is undefined because it's not exposed publicly.

### Answer 8:
**Output:** `3`, `3`, `3`

**Explanation:** Same issue as Question 1. All functions close over the same `i` variable.

**Fix:**
```javascript
function createFunctions() {
  const functions = [];
  
  for (let i = 0; i < 3; i++) { // Use let instead of var
    functions.push(function() {
      return i;
    });
  }
  
  return functions;
}
```

### Answer 9:
**Output:** `Processing: undefined` (printed three times at 0s, 1s, 2s)

**Explanation:** By the time setTimeout executes, `i` is 3, so `data[3]` is undefined.

### Answer 10:
**Output:** `global outer middle inner`, `2`

**Explanation:** Closures have access to the entire scope chain. Block-scoped `let` creates a new binding in the block scope.

### Answer 11:
**Output:** `3`, `3`

**Explanation:** Function declarations are hoisted, but they still close over the variable `i` from the loop scope, which is 3 by the time functions are called.

### Answer 12:
**Output:** `1`, `2`, `3` (but timing depends on when promises resolve)

**Explanation:** Each call to `asyncCounter` creates a new promise, but they all share the same `count` variable through closure. They may execute in parallel.

### Answer 13:
**Output:** `1`, `2`, `2`

**Explanation:** Both closures reference the same `obj`. When `closure2` modifies `obj.value`, `closure1` sees the change because they share the same reference.

### Answer 14:
**Output:** `ERROR : Something went wrong`, `INFO : Process completed`, `undefined : Test message`

**Explanation:** The multi-logger has the same closure issue - all functions reference the same `i` variable, which is 4 after the loop completes.

### Answer 15:
**Output:** `1`, `2`, `3`, `Max value reached, counter locked`, `Counter is locked`

**Explanation:** The closure maintains private state (`count`, `isLocked`) and enforces business rules through the closure scope.

## Key Closure Concepts for Interviews:

1. **Variable Capture**: Closures capture variables by reference, not value
2. **Scope Chain**: Closures have access to entire scope chain at creation time
3. **Memory Management**: Closures can prevent garbage collection
4. **Loop Issues**: `var` in loops creates closure problems; `let` solves them
5. **Module Pattern**: Closures enable private variables and methods
6. **Factory Functions**: Closures allow creating multiple instances with private state
7. **Partial Application**: Closures enable functional programming patterns

## Pro Interview Tips:
- Always trace the scope chain when analyzing closures
- Identify whether variables are captured by reference or value
- Consider the timing of when closures are created vs. executed
- Understand the difference between `var`, `let`, and `const` in closure contexts
- Know common patterns: Module, Factory, Partial Application
- Be able to identify and fix memory leaks caused by closures