MongoDB primarily uses **B-trees**, specifically a variant called **B+ trees**, to implement its indexes. These indexes are designed to optimize query performance, especially for range queries, and to efficiently handle large datasets.

Here’s a more detailed look at MongoDB’s indexing approach:

### 1. **B+ Trees in MongoDB**
   - MongoDB's indexes, including the default **_id** index, are implemented using **B+ trees**. This structure allows for efficient lookups, inserts, updates, and deletions, all while keeping the tree balanced.
   - In a B+ tree, internal nodes only store keys, and the leaf nodes store both the keys and pointers to the actual document or record. This design is optimized for disk access, as MongoDB can quickly traverse the tree to find or insert records.
   
   **Why B+ trees?**
   - **Range Queries**: B+ trees are particularly useful for range queries. For example, if you query MongoDB with a range condition, such as `age > 20 AND age < 30`, the B+ tree allows for efficient traversal through contiguous leaf nodes.
   - **Ordered Storage**: Because B+ trees store keys in sorted order, they also support efficient sorting operations, which is useful for MongoDB’s query execution when the query includes `ORDER BY`.
   - **Balancing**: B+ trees are self-balancing, meaning they maintain their structure automatically as inserts, updates, or deletes happen, which ensures that lookups remain fast over time.

### 2. **Hash Indexes in MongoDB?**
   - MongoDB **does not** use hash tables by default for its general-purpose indexes. However, starting from version 2.0, MongoDB introduced a **hashed index** type, but this is only for **specific use cases**.
   - **Hashed Indexes**: These are useful for exact-match queries but are not suitable for range queries (since hashing destroys the order of the keys). You can create a hashed index in MongoDB when you need efficient lookups based on equality conditions (like searching by unique IDs).
     - Example of creating a hashed index: 
       ```js
       db.collection.createIndex({ field: "hashed" })
       ```
   - While hashed indexes can improve performance for exact lookups (e.g., `field = value`), they do not support range queries like `field > value` or `field < value` since the hash function doesn't preserve key order.

### Summary
- **MongoDB** predominantly uses **B+ trees** for its indexes, which supports both exact-match and range queries efficiently. This structure is well-suited for handling the large, dynamic datasets that MongoDB typically stores.
- **Hash indexes** are available in MongoDB but are only used for specific cases where exact-match lookups are required and not for range queries.

___

Let's walk through how **indexes** would be created, stored, and accessed in MongoDB based on the example you provided, where a collection (table) has the following fields:

- **name** (string)
- **age** (integer)
- **section** (string)
- **score** (integer)

If we create indexes on a few columns, MongoDB will build a data structure (typically a **B+ tree**) that allows for faster lookup of records. I'll explain how it stores these indexes and how lookups work.

### Example: Creating Indexes
Assume you create the following indexes:
1. An index on **`age`**.
2. A compound index on **`section`** and **`score`**.

```js
// Create an index on age
db.students.createIndex({ age: 1 })

// Create a compound index on section and score
db.students.createIndex({ section: 1, score: -1 })
```

### 1. **Index on `age`:**
   When you create an index on `age`, MongoDB will build a **B+ tree** where the keys are the `age` values, and the values are references to the actual documents (or records).

   - **Storage:** 
     The **B+ tree** will be built with `age` values as the keys. Each leaf node of the tree will store the `age` and a reference (pointer) to the document where this `age` value exists. The pointer typically refers to the document's location (its ObjectID or its physical storage location on disk).

     For example, the tree might look something like this:
     ```
     age: 18 → Document ID 1
     age: 20 → Document ID 2
     age: 21 → Document ID 3
     age: 25 → Document ID 4
     ```

   - **Lookup Process:**
     - When a query like `db.students.find({ age: 20 })` is executed, MongoDB uses the **B+ tree index** to traverse the tree and quickly locate the key `20`. It then follows the pointer stored in the leaf node to fetch the actual document (e.g., Document ID 2).
     - Range queries such as `db.students.find({ age: { $gt: 18 } })` are efficient because MongoDB can traverse the tree starting from the key `18` and scan through subsequent keys (e.g., 20, 21, 25, etc.) in the leaf nodes, fetching the matching documents.

### 2. **Compound Index on `section` and `score`:**
   - When you create a compound index on `section` and `score`, MongoDB builds another **B+ tree**, but this time with a composite key consisting of both `section` and `score`. MongoDB first sorts by `section`, and within each section, it sorts by `score` (in descending order because we specified `-1` for score).
   
   - **Storage:**
     The compound index stores keys as pairs of `section` and `score`. For example, if the data looks like this:
     ```
     { name: "John", age: 18, section: "A", score: 85 }
     { name: "Alice", age: 19, section: "A", score: 90 }
     { name: "Bob", age: 20, section: "B", score: 70 }
     { name: "Charlie", age: 21, section: "B", score: 95 }
     ```

     The **B+ tree** might look like:
     ```
     section: A, score: 90 → Document ID 2 (Alice)
     section: A, score: 85 → Document ID 1 (John)
     section: B, score: 95 → Document ID 4 (Charlie)
     section: B, score: 70 → Document ID 3 (Bob)
     ```

   - **Lookup Process:**
     - For a query like `db.students.find({ section: "A", score: { $gte: 85 } })`, MongoDB will traverse the tree to find the `section: A` key, then look within that section to find all documents with a `score` greater than or equal to 85. It will return Document ID 1 and Document ID 2.
     - The **ordering** of keys matters. This index is optimal for queries where `section` is included because MongoDB can use the first part of the index (`section`) to narrow down results. If the query were to filter only by `score` (e.g., `db.students.find({ score: 85 })`), the index might not be used efficiently because the first part of the index (`section`) is missing.

### 3. **How Documents are Stored and Accessed:**
   - Each index stores **keys** based on the indexed fields and **pointers** to the actual documents. These pointers are typically **document references** (such as the ObjectID or internal pointers to the storage location on disk).
   - When MongoDB looks up a value in the index, it does not directly retrieve the entire document. Instead, it first retrieves the pointer from the index and then uses that pointer to fetch the actual document from the collection (storage).

### Example Lookup Scenarios:
- **Single-Field Index (age):**
  ```js
  db.students.find({ age: 20 })
  ```
  MongoDB will:
   1. Traverse the **B+ tree** for the `age` index to find the key `20`.
   2. Retrieve the document pointer (e.g., Document ID 2).
   3. Fetch the actual document from the collection.

- **Compound Index (section and score):**
  ```js
  db.students.find({ section: "B", score: { $gte: 70 } })
  ```
  MongoDB will:
   1. Traverse the **B+ tree** for the `section` and `score` compound index.
   2. Find all keys where `section = "B"` and `score >= 70` (Document IDs 3 and 4).
   3. Fetch the corresponding documents.

### Summary:
- **Indexes in MongoDB** are typically stored using **B+ trees**, where each indexed field (or combination of fields in compound indexes) serves as the key in the tree.
- The tree nodes contain **keys** (the indexed field values) and **pointers** to the actual documents.
- **Lookups** use the index to quickly find the relevant keys and follow the pointers to fetch the actual documents from storage.
- Compound indexes work by sorting first by the first field (e.g., `section`), then by the second field (e.g., `score`), and are most efficient when the query includes the left-most part of the index.


___

NoSQL databases (TTL feature): Automatically delete keys after a predefined time using TTL (best for Redis, MongoDB).

db.url_shortener.createIndex( { "createdAt": 1 }, { expireAfterSeconds: 3600 } )

In **MongoDB**, **TTL (Time to Live)** is a feature that allows you to automatically remove documents from a collection after a certain amount of time. This is particularly useful for managing data that is time-sensitive, such as session data, logs, or in your case, expired URLs in a URL shortening service.

MongoDB’s TTL feature works by creating a **TTL index** on a field that stores a date or timestamp value. Once the specified amount of time has passed since the value in that field, MongoDB automatically deletes the document from the collection.

### How TTL Works in MongoDB:

1. **TTL Index Creation**: You create a TTL index on a date field in a MongoDB document.
2. **Expiration Time**: When documents in the collection reach the specified expiration time (based on the timestamp in the indexed field), they are automatically deleted.
3. **Background Process**: MongoDB runs a background task every **60 seconds** that checks for expired documents and deletes them. There may be a slight delay in the actual deletion due to this background check, but it happens within a minute after the expiration time is reached.

### Steps to Use TTL in MongoDB:

#### 1. Add a Timestamp Field to Your Document
To use TTL, you must have a field in your MongoDB document that holds a **date** or **timestamp** value. For example, when you insert a new document (such as a shortened URL), you can store the creation time or an expiration time in the document.

**Example Document:**
```json
{
  "_id": "abc123",
  "original_url": "https://www.example.com",
  "short_url": "https://short.ly/abc123",
  "createdAt": ISODate("2024-10-14T12:00:00Z")
}
```

In this example, `createdAt` is a field that holds the creation timestamp of the shortened URL.

#### 2. Create a TTL Index on the Timestamp Field
Next, create a **TTL index** on the `createdAt` field, and specify the number of seconds after which the documents should expire. MongoDB will automatically delete documents once they reach this age.

**Example Command to Create a TTL Index:**
```javascript
db.url_shortener.createIndex(
   { "createdAt": 1 },
   { expireAfterSeconds: 3600 }
)
```

Here:
- `createdAt`: The field that contains the document's creation timestamp.
- `expireAfterSeconds: 3600`: This means that MongoDB will delete the document **3600 seconds** (or **1 hour**) after the `createdAt` timestamp.

#### 3. MongoDB Background Process
Once you create the TTL index, MongoDB's background process runs every minute to check for documents that have "expired" (i.e., where `createdAt` is older than the expiration time). Expired documents are then deleted automatically.

### Example Use Case for a URL Shortener
If you're building a URL shortener and want URLs to expire after 7 days, you could use a TTL index as follows:

1. Store the **creation timestamp** (`createdAt`) when a URL is shortened.
2. Set the **TTL index** to expire the documents after 7 days (7 * 24 * 60 * 60 = 604800 seconds).

**MongoDB Command:**
```javascript
db.url_shortener.createIndex(
   { "createdAt": 1 },
   { expireAfterSeconds: 604800 }  // 7 days
)
```

With this setup, any URL document older than 7 days will be automatically deleted by MongoDB, without needing to manually handle cleanup.

### Key Details about MongoDB TTL:
- **Time-based Deletion**: TTL is based on the value of the date field and the configured `expireAfterSeconds`. It counts from the timestamp in that field and deletes documents once that time has passed.
  
- **Precision**: TTL expiration happens in the background, and there is a slight delay since MongoDB checks every 60 seconds. This means documents might not be deleted exactly when they expire but within a minute after.

- **TTL Index Field Must Be a Date**: The field on which you create the TTL index must contain a **Date** type value (e.g., `ISODate`), not other types like `String` or `Number`.

- **Non-Configurable Frequency**: MongoDB checks for expired documents once every minute, and this interval is not configurable.

- **Non-Recoverable Deletion**: Once a document is deleted by the TTL mechanism, it cannot be recovered unless you have backups in place.

### Considerations:
- **Expiration based on Creation Time or Expiry Time**: You can decide whether to use the document’s creation time (`createdAt`) or store a specific expiration time (`expireAt`). For instance, you could add an `expireAt` field instead of `createdAt` if you want more control over when documents should expire.
  
- **TTL Indexes Can’t Be Compound**: TTL indexes must be **single-field** indexes. MongoDB does not support TTL indexes as part of a compound index.

In this case, MongoDB will delete the document exactly at the `expireAt` time specified.

---

### Summary
- **TTL in MongoDB** allows automatic deletion of expired documents based on a timestamp field.
- You set the expiration using a **TTL index** on a date field.
- MongoDB’s background process checks for expired documents every minute and removes them.
- This feature is perfect for expiring time-sensitive data such as sessions, logs, or shortened URLs without manually handling cleanup.

This approach helps you efficiently manage the lifecycle of URLs and reduce database bloat, without constant manual intervention.