Here’s a set of “go-to” quick-notes for mastering React’s core hooks—**useState**, **useRef**, **useEffect**, **useMemo**, and **useCallback**. Keep this as your pocket reference when coding or revising.

---

## 1. useState

**Purpose**: Add local state to function components.
**Signature**:

```ts
const [state, setState] = useState<S>(initialState: S | () => S);
```

**Key Points**

* **Lazy init**: pass a function if computing initial value is expensive.
* **Updater form**: `setState(prev => newVal)` for safe updates.
* **Batched**: multiple `setState` calls in same event are merged.

**Common Pitfalls**

* Mutating state directly (always produce new object/array).
* Forgetting dependency in effects when using state inside useEffect.

**Example**

```jsx
const [count, setCount] = useState(0);
const increment = () => setCount(c => c + 1);
```

---

## 2. useRef

**Purpose**:

1. Hold a mutable value that persists across renders (like instance fields).
2. Access DOM elements directly.

**Signature**:

```ts
const ref = useRef<T>(initialValue: T);
```

**Key Points**

* `.current` is mutable—updating it does **not** trigger a re-render.
* Good for timers, previous values, form fields.

**Common Pitfalls**

* Overusing for state—you rarely need to read `.current` in JSX.
* Forgetting to attach `ref` to an element: `<div ref={myRef}>`.

**Example**

```jsx
const inputRef = useRef<HTMLInputElement>(null);
useEffect(() => {
  inputRef.current?.focus();
}, []);
return <input ref={inputRef} />;
```

---

## 3. useEffect

**Purpose**: Run side-effects after render—data fetching, subscriptions, manual DOM.
**Signature**:

```ts
useEffect(effect: () => (void | () => void), deps?: any[]);
```

**Key Points**

* **Runs after paint**.
* **Cleanup**: return a function to tear down (e.g. unsubscribe).
* **Deps array**:

  * `[]` → run once on mount; cleanup on unmount.
  * Omitted → run after *every* render (rarely recommended).
  * `[a, b]` → run when `a` or `b` change.

**Common Pitfalls**

* Missing dependencies → stale closures / bugs.
* Over-running effects → infinite loops (e.g. updating state inside without proper guard).
* Doing heavy work in effect without throttling.

**Example**

```jsx
useEffect(() => {
  const id = setInterval(() => setTime(Date.now()), 1000);
  return () => clearInterval(id);
}, []);  // once
```

---

## 4. useMemo

**Purpose**: Memoize an **expensive** computed value between renders.
**Signature**:

```ts
const memoVal = useMemo(() => compute(a, b), [a, b]);
```

**Key Points**

* Only re-computes when dependencies change.
* Avoids wasteful recalculation **or** prevents child re-renders when passing objects/arrays.

**Common Pitfalls**

* Overuse: if compute is cheap, overhead of memo can hurt.
* Wrong deps array → stale values or needless recompute.

**Example**

```jsx
const sorted = useMemo(() => items.sort(compareFn), [items]);
```

---

## 5. useCallback

**Purpose**: Memoize a **function** instance so that its reference stays stable across renders.
**Signature**:

```ts
const memoFn = useCallback(() => doSomething(x), [x]);
```

**Key Points**

* Helpful when passing callbacks to optimized children (`React.memo`) to avoid re-renders.
* Similar cost/benefit tradeoff as `useMemo`.

**Common Pitfalls**

* Wrapping every function by default—only use when child receives the function as prop and cares about identity.
* Missing deps → callback closing over stale values.

**Example**

```jsx
const handleClick = useCallback(() => {
  console.log(count);
}, [count]);
return <Button onClick={handleClick} />;
```

---

## 6. Quick Rules & Conventions

1. **Hook Names & Placement**

   * Always start with `use`
   * Call only at top level (no loops/conditions).

2. **Deps Arrays**

   * Treat them like API: list *all* external values used in your effect/memo/callback.
   * Use ESLint plugin (`eslint-plugin-react-hooks`) to auto-lint.

3. **Performance**

   * Only memoize when you have:

     * **Expensive compute** (`useMemo`)
     * **Referential equality** matters (`useMemo`/`useCallback`)

4. **Cleanup Effects**

   * Always clear subscriptions/listeners in cleanup.
   * If effect returns nothing, no cleanup is applied.

5. **State Updates**

   * Prefer updater form when new state depends on previous: `setVal(v => v+1)`.

---

### 7. Cheat-Sheet Table

| Hook            | Use When…                                          | Returns                    |
| --------------- | -------------------------------------------------- | -------------------------- |
| **useState**    | you need local component state                     | `[state, setState]`        |
| **useRef**      | you need mutable “instance” value or DOM access    | `{ current }`              |
| **useEffect**   | you need side-effects (fetch, subscribe, DOM ops)  | *nothing* / **cleanup fn** |
| **useMemo**     | you need to cache expensive value or stable object | `memoizedValue`            |
| **useCallback** | you need to cache function identity across renders | `memoizedFunction`         |

Keep this at hand, and you’ll confidently wield React hooks in all your components!

---

_To keep your components predictable, readable, and performant, a common “hooks ordering” convention is:_

1. Context hooks       (e.g. const theme = useTheme();)
2. State hooks         (useState, useReducer)
3. Ref hooks           (useRef, useImperativeHandle)
4. Effect hooks        (useEffect, useLayoutEffect)
5. Memo hooks          (useMemo)
6. Callback hooks      (useCallback)
7. Custom hooks        (that wrap the above, in their own logical spot)
