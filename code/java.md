#### Reversing a string in java
In java string are immutable 
Thus we can use a  `StringBuilder` object
```
String reversed = new StringBuilder(s).reverse().toString();
```

#### Ordered Sets and Maps in Java
`TreeSet` and `TreeMap` for sorted orders
`LinkedHashSet` and `LinkedHashMap` for maitain insertion order

```
Set<String> treeSet = new TreeSet<>();
    treeSet.add("banana");
    treeSet.add("apple");
    treeSet.add("cherry");

Map<String, Integer> treeMap = new TreeMap<>();
    treeMap.put("banana", 2);
    treeMap.put("apple", 1);
    treeMap.put("cherry", 3);

Set<String> linkedHashSet = new LinkedHashSet<>();
Map<String, Integer> linkedHashMap = new LinkedHashMap<>();
```

#### PriorityQueue in Java 
Min and max heap in java can be used via PirorityQueue 
`PriorityQueue<Integer> pq = new PriorityQueue<>();` - min heap by default
`PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());` - max heap 
Here are the commonly used methods of PriorityQueue:

* `add(E e)`: Inserts the specified element into this priority queue.
* `offer(E e)`: Inserts the specified element into this priority queue.
* `poll()`: Retrieves and removes the head of the queue (smallest or highest priority element).
* `peek()`: Retrieves, but does not remove, the head of the queue.
* `isEmpty()`: Returns true if the queue contains no elements.
* `size()`: Returns the number of elements in the queue.


#### Stack 
``` Stack<Integer> stack = new Stack<>();
    stack.push(1);
    stack.isEmpty()
    stack.pop();

    stack.peek(); // returns the top element without removing it
    stack.clear();
    stack.clone();
```


Here’s a concise **ArrayList cheatsheet** to help you get started with basic operations in Java:

### **Initialization**
```java
// Create an ArrayList of Strings
ArrayList<String> list = new ArrayList<>();

// With initial capacity
ArrayList<Integer> numbers = new ArrayList<>(10);

// From another collection
ArrayList<Integer> copyList = new ArrayList<>(Arrays.asList(1, 2, 3));
```

### **Basic Operations**
```java
// Add elements
list.add("apple");
list.add("banana");

// Add element at specific index
list.add(1, "orange");

// Get element by index
String fruit = list.get(0);  // returns "apple"

// Set element at specific index
list.set(1, "kiwi");  // replaces "banana" with "kiwi"

// Remove element by index or value
list.remove(0);       // removes "apple"
list.remove("kiwi");  // removes "kiwi"

// Check if element exists
boolean hasBanana = list.contains("banana");

// Get size of the list
int size = list.size();

// Clear the list
list.clear();

// Check if list is empty
boolean isEmpty = list.isEmpty();
```

### **Iteration**
```java
// Using for-each loop
for (String item : list) {
    System.out.println(item);
}

// Using for loop with index
for (int i = 0; i < list.size(); i++) {
    System.out.println(list.get(i));
}

// Using iterator
Iterator<String> iterator = list.iterator();
while (iterator.hasNext()) {
    System.out.println(iterator.next());
}
```

### **Sorting**
```java
Collections.sort(list);  // Sorts in natural order
Collections.sort(list, Collections.reverseOrder());  // Sorts in reverse order
```

### **Other Useful Methods**
```java
// Check index of an element
int index = list.indexOf("banana");  // returns -1 if not found

// Check last index of an element (useful if duplicates exist)
int lastIndex = list.lastIndexOf("banana");

// Convert to Array
String[] array = list.toArray(new String[0]);

// Add all elements from another collection
list.addAll(Arrays.asList("cherry", "mango"));
```

### **ArrayList Capacity and Performance**
- **Initial Capacity**: You can specify the initial capacity to avoid resizing the internal array when elements are added frequently.
  ```java
  ArrayList<Integer> numbers = new ArrayList<>(20);  // Initial capacity set to 20
  ```

- **Resize Mechanism**: The ArrayList increases its size by 50% when it runs out of space.
  
### **Thread Safety**
`ArrayList` is **not thread-safe**. To make it thread-safe, you can wrap it with `Collections.synchronizedList()`:
```java
List<String> synchronizedList = Collections.synchronizedList(new ArrayList<>());
```

### **Conversion between Array and ArrayList**
```java
// Convert ArrayList to Array
String[] arr = list.toArray(new String[0]);

// Convert Array to ArrayList
String[] fruits = {"apple", "banana", "cherry"};
ArrayList<String> fruitList = new ArrayList<>(Arrays.asList(fruits));
```

### **Copying**
```java
// Create a shallow copy of ArrayList
ArrayList<String> copy = (ArrayList<String>) list.clone();
```

This covers the essentials of working with **`ArrayList`** in Java.