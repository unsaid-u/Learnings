// debounce(func, delay) // after the function is called

// The primary purpose of a debounce function is to limit the rate at which a function is called. It ensures that a function is executed only after a specific period of inactivity (the delay) has passed since its last invocation.

function debounce(func, delay) {
  let id;

  return function (...args) {
    clearTimeout(id);
    id = setTimeout(() => {
      func.apply(this, args);
    }, delay);
  };
}
// here using an arrow function inside a setTimeout works, because it has access to its scope's 'this' which the context with which my debounce() method was called

function throttle(func, limit) {
  let inThrottle = false;

  return function (...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;

      setTimeout(() => {
        inThrottle = false;
      }, limit);
    }
  };
}

// With throttle(func, 200):

// The function runs immediately on the first call
// It will then ignore further calls for the next 200ms
// After 200ms, it’s eligible to run again

// | Feature   | Debounce                        | Throttle                          |
// | --------- | ------------------------------- | --------------------------------- |
// | Purpose   | Wait until user **stops** doing | Limit calls to once every X ms    |
// | Execution | Runs **after** final trigger    | Runs **every X ms**, continuously |
// | Use case  | Search input, resizing          | Scroll, resize, drag, mouse move  |
