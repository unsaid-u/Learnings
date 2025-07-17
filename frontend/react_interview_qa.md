# React Interview Questions and Answers

## Beginner Level Questions

### 1. What is React?
**Answer:** React is a JavaScript library developed by Facebook for building user interfaces, particularly web applications. It allows developers to create reusable UI components and efficiently update the DOM using a virtual DOM approach. React follows a component-based architecture and uses a declarative programming paradigm.

### 2. What is JSX?
**Answer:** JSX (JavaScript XML) is a syntax extension for JavaScript that allows you to write HTML-like code within JavaScript. It makes React code more readable and easier to write. JSX gets transpiled to regular JavaScript function calls.

```jsx
// JSX
const element = <h1>Hello, World!</h1>;

// Transpiled JavaScript
const element = React.createElement('h1', null, 'Hello, World!');
```

### 3. What are React components?
**Answer:** React components are reusable pieces of code that return JSX elements to be rendered to the page. There are two types:
- **Functional Components**: JavaScript functions that return JSX
- **Class Components**: ES6 classes that extend React.Component

```jsx
// Functional Component
function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

// Class Component
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}
```

### 4. What is the Virtual DOM?
**Answer:** The Virtual DOM is a JavaScript representation of the actual DOM (Document Object Model). React creates a virtual copy of the real DOM in memory. When state changes occur, React:
1. Creates a new virtual DOM tree
2. Compares it with the previous virtual DOM tree (diffing)
3. Updates only the parts of the real DOM that changed (reconciliation)

This process is much faster than directly manipulating the real DOM.

### 5. What are props in React?
**Answer:** Props (short for properties) are read-only attributes passed from parent components to child components. They allow data to flow down the component tree and make components reusable.

```jsx
function Greeting(props) {
  return <h1>Hello, {props.name}!</h1>;
}

// Usage
<Greeting name="Alice" />
```

## Intermediate Level Questions

### 6. What is state in React?
**Answer:** State is a built-in React object that stores data that can change over time. Unlike props, state is mutable and belongs to the component that declares it. When state changes, the component re-renders.

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### 7. What are React Hooks?
**Answer:** Hooks are functions that allow you to use state and other React features in functional components. They were introduced in React 16.8. Common hooks include:
- `useState`: Manages component state
- `useEffect`: Handles side effects
- `useContext`: Accesses React context
- `useReducer`: Manages complex state logic
- `useMemo`: Memoizes expensive calculations
- `useCallback`: Memoizes functions

### 8. Explain the useEffect hook.
**Answer:** `useEffect` is a hook that lets you perform side effects in functional components. It serves the same purpose as `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` combined.

```jsx
import { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    // Side effect: fetch user data
    fetchUser(userId).then(setUser);
    
    // Cleanup function (optional)
    return () => {
      // Cleanup code here
    };
  }, [userId]); // Dependency array
  
  return user ? <div>{user.name}</div> : <div>Loading...</div>;
}
```

### 9. What is the difference between controlled and uncontrolled components?
**Answer:** 
- **Controlled Components**: Form elements whose value is controlled by React state. The component's state is the single source of truth.
- **Uncontrolled Components**: Form elements that maintain their own internal state. You use refs to access their values.

```jsx
// Controlled Component
function ControlledInput() {
  const [value, setValue] = useState('');
  
  return (
    <input 
      value={value} 
      onChange={(e) => setValue(e.target.value)} 
    />
  );
}

// Uncontrolled Component
function UncontrolledInput() {
  const inputRef = useRef();
  
  const handleSubmit = () => {
    alert(inputRef.current.value);
  };
  
  return (
    <input ref={inputRef} />
  );
}
```

### 10. What is lifting state up?
**Answer:** Lifting state up is a pattern where you move state from child components to their common parent component. This allows multiple components to share the same state and stay in sync.

```jsx
function Parent() {
  const [sharedState, setSharedState] = useState('');
  
  return (
    <div>
      <ChildA value={sharedState} onChange={setSharedState} />
      <ChildB value={sharedState} />
    </div>
  );
}
```

## Advanced Level Questions

### 11. What is React Context?
**Answer:** React Context provides a way to pass data through the component tree without having to pass props down manually at every level. It's useful for globally shared data like themes, user authentication, or language preferences.

```jsx
const ThemeContext = createContext('light');

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <MainContent />
    </ThemeContext.Provider>
  );
}

function MainContent() {
  const theme = useContext(ThemeContext);
  return <div className={theme}>Content</div>;
}
```

### 12. What is the useReducer hook?
**Answer:** `useReducer` is a hook that provides an alternative to `useState` for managing complex state logic. It's particularly useful when state updates depend on previous state or when you have complex state objects.

```jsx
const initialState = { count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      throw new Error();
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);
  
  return (
    <div>
      Count: {state.count}
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
    </div>
  );
}
```

### 13. What are React.memo, useMemo, and useCallback?
**Answer:** These are optimization techniques to prevent unnecessary re-renders:

- **React.memo**: Higher-order component that memoizes the component result
- **useMemo**: Memoizes expensive calculations
- **useCallback**: Memoizes functions

```jsx
// React.memo
const ExpensiveComponent = React.memo(({ data }) => {
  return <div>{/* expensive rendering */}</div>;
});

// useMemo
function ExpensiveCalculation({ items }) {
  const expensiveValue = useMemo(() => {
    return items.reduce((sum, item) => sum + item.value, 0);
  }, [items]);
  
  return <div>{expensiveValue}</div>;
}

// useCallback
function Parent() {
  const [count, setCount] = useState(0);
  
  const handleClick = useCallback(() => {
    setCount(c => c + 1);
  }, []);
  
  return <Child onClick={handleClick} />;
}
```

### 14. What is the difference between useMemo and useCallback?
**Answer:**
- **useMemo**: Memoizes the result of a calculation/computation
- **useCallback**: Memoizes the function itself

```jsx
// useMemo - memoizes the computed value
const expensiveValue = useMemo(() => {
  return computeExpensiveValue(data);
}, [data]);

// useCallback - memoizes the function
const handleClick = useCallback(() => {
  doSomething(data);
}, [data]);
```

### 15. What are Error Boundaries?
**Answer:** Error Boundaries are React components that catch JavaScript errors anywhere in their child component tree, log those errors, and display a fallback UI. They only work in class components.

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }
  
  static getDerivedStateFromError(error) {
    return { hasError: true };
  }
  
  componentDidCatch(error, errorInfo) {
    console.log('Error caught:', error, errorInfo);
  }
  
  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}
```

## Performance and Best Practices

### 16. How do you optimize React application performance?
**Answer:** Several techniques can optimize React performance:

1. **Use React.memo** for functional components
2. **Implement useMemo and useCallback** for expensive calculations and functions
3. **Code splitting** with React.lazy and Suspense
4. **Avoid creating objects/functions in render**
5. **Use proper key props** in lists
6. **Implement virtualization** for long lists
7. **Profile with React DevTools**

### 17. What is code splitting in React?
**Answer:** Code splitting is a technique to split your code into smaller chunks that can be loaded on demand. React supports this through React.lazy and Suspense.

```jsx
import { lazy, Suspense } from 'react';

const LazyComponent = lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

### 18. What are the rules of hooks?
**Answer:** React hooks have two main rules:
1. **Only call hooks at the top level** - Don't call hooks inside loops, conditions, or nested functions
2. **Only call hooks from React functions** - Call hooks from React functional components or custom hooks

```jsx
// ❌ Wrong - conditional hook
function MyComponent() {
  if (someCondition) {
    const [state, setState] = useState(); // Don't do this
  }
}

// ✅ Correct
function MyComponent() {
  const [state, setState] = useState();
  
  if (someCondition) {
    // Use state here
  }
}
```

### 19. What is the difference between createElement and cloneElement?
**Answer:**
- **createElement**: Creates a new React element
- **cloneElement**: Clones an existing element and returns a new element

```jsx
// createElement
const element = React.createElement('div', { className: 'my-class' }, 'Hello');

// cloneElement
const clonedElement = React.cloneElement(element, { id: 'my-id' });
```

### 20. What are portals in React?
**Answer:** Portals provide a way to render children into a DOM node that exists outside the parent component's DOM hierarchy. They're useful for modals, tooltips, and dropdowns.

```jsx
import { createPortal } from 'react-dom';

function Modal({ children }) {
  return createPortal(
    <div className="modal">
      {children}
    </div>,
    document.getElementById('modal-root')
  );
}
```

## Common Coding Challenges

### 21. How would you implement a custom hook?
**Answer:** Custom hooks are JavaScript functions that start with "use" and can call other hooks.

```jsx
// Custom hook for fetching data
function useApi(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);
        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, [url]);
  
  return { data, loading, error };
}

// Usage
function MyComponent() {
  const { data, loading, error } = useApi('/api/users');
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  return <div>{JSON.stringify(data)}</div>;
}
```

### 22. How do you handle forms in React?
**Answer:** Forms can be handled using controlled components with state management:

```jsx
function ContactForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  });
  
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', formData);
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input
        name="name"
        value={formData.name}
        onChange={handleChange}
        placeholder="Name"
      />
      <input
        name="email"
        value={formData.email}
        onChange={handleChange}
        placeholder="Email"
      />
      <textarea
        name="message"
        value={formData.message}
        onChange={handleChange}
        placeholder="Message"
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

These questions cover the fundamental concepts and common scenarios you'll encounter in React interviews. Practice implementing these concepts and understanding the underlying principles to succeed in your interview.