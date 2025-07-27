React’s Context API provides a way to share values (like themes, user info, settings) “globally” across a component tree, without having to thread props through every intermediate level. Here’s a crash-course plus best practices.

---

## 1. Core Concepts

### 1.1. Creating a Context

```jsx
import { createContext } from 'react';

export const AuthContext = createContext(/* defaultValue */);
```

* **`defaultValue`** is used only if a component consumes the context without a matching Provider above it.

### 1.2. Providing a Value

```jsx
import { AuthContext } from './AuthContext';

function App() {
  const [user, setUser] = useState(null);

  return (
    <AuthContext.Provider value={{ user, setUser }}>
      <YourRoutesOrApp />
    </AuthContext.Provider>
  );
}
```

* Wrap the part of your tree that needs access.
* Any time the `value` prop changes, consumers will re-render.

### 1.3. Consuming Context

#### 1.3.1. Via Hook

```jsx
import { useContext } from 'react';
import { AuthContext } from './AuthContext';

function Header() {
  const { user, setUser } = useContext(AuthContext);
  return <div>Welcome, {user?.name ?? 'guest'}</div>;
}
```

#### 1.3.2. Via `<Context.Consumer>`

```jsx
<AuthContext.Consumer>
  {({ user }) => <div>Hi, {user?.name}</div>}
</AuthContext.Consumer>
```

> In function components you’ll almost always prefer `useContext`.

---

## 2. Common Patterns & Practices

### 2.1. Split Contexts by Concern

* Don’t lump all state in one giant context.
* E.g. have separate `ThemeContext`, `AuthContext`, `SettingsContext`—this minimizes unnecessary re-renders when unrelated values change.

### 2.2. Memoize Provider Value

Because objects/arrays get new references every render, wrap your `value` in `useMemo`:

```jsx
const authValue = useMemo(() => ({ user, setUser }), [user, setUser]);
return <AuthContext.Provider value={authValue}>…</AuthContext.Provider>;
```

### 2.3. Encapsulate in a Custom Hook

Bundle `useContext` logic and default-value checks:

```jsx
function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be inside AuthProvider');
  return ctx;
}

// then in components:
const { user } = useAuth();
```

### 2.4. Provider Composition

If you have multiple contexts:

```jsx
function AppProviders({ children }) {
  return (
    <AuthProvider>
      <SettingsProvider>
        <ThemeProvider>
          {children}
        </ThemeProvider>
      </SettingsProvider>
    </AuthProvider>
  );
}
```

—keeps `index.js` or `App.js` tidy.

### 2.5. Keep Context “Stable” & Minimal

* Only include what truly needs global scope.
* Avoid frequent changes (e.g. high-frequency timers) in context values—those will cascade updates everywhere.

---

## 3. Performance Tips

1. **Provider Placement**

   * Wrap as narrowly as possible. E.g. if only a sidebar needs theme, don’t wrap the whole app.

2. **Avoid Passing Large Objects**

   * If you need multiple pieces of state, consider creating multiple contexts rather than one big object.

3. **Selective Rendering**

   * If only one part of the context changes often, isolate it in its own context so other consumers don’t re-render.

4. **React.memo for Consumers**

   ```jsx
   const UserProfile = React.memo(function UserProfile({ /* props */ }) { … });
   ```

   —prevents extra re-renders even if parent context updates with unrelated keys.

---

## 4. When *Not* to Use Context

* For **local** state that’s only used by a couple of siblings, plain prop-drilling is often simpler.
* For very **large** or **complex** global state, a dedicated state-management library (Redux, MobX, Zustand) may be a better fit.

---

### 5. Putting It All Together

```jsx
// AuthContext.js
const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const value = useMemo(() => ({ user, setUser }), [user]);
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within AuthProvider');
  return ctx;
}

// App.js
function App() {
  return (
    <AuthProvider>
      <AppRoutes />
    </AuthProvider>
  );
}

// SomeComponent.js
function SomeComponent() {
  const { user } = useAuth();
  return <div>Hello, {user?.name}</div>;
}
```

With these patterns, Context becomes a powerful, predictable tool for sharing state—while staying performant and maintainable.

---

```js
// routes.js
export const routes = [
  {
    path: "/",
    element: <MainLayout />,
    children: [
      { index: true, element: <Home /> },
      { path: "about", element: <About /> },
      {
        path: "dashboard",
        element: <RequireAuth><DashboardLayout/></RequireAuth>,
        children: [
          { index: true, element: <Overview /> },
          { path: "users/:id", element: <UserProfile /> },
          { path: "*", element: <DashboardNotFound /> }
        ]
      }
    ]
  },
  { path: "*", element: <GlobalNotFound /> }
];

// App.js
import { useRoutes } from 'react-router-dom';
import { routes } from './routes';

function App() {
  const element = useRoutes(routes);
  return element;
}

```