### What is Indexing?

**Indexing** is a technique used in databases to improve the speed and efficiency of data retrieval operations. An index is a data structure that allows the database to quickly locate and access the rows of a table that correspond to a particular search condition without scanning the entire table.

**Analogy:** Think of an index in a book. Instead of scanning the entire book to find a topic, you can look at the index, which tells you the exact page numbers where the topic is discussed. Similarly, in a database, an index helps quickly locate data without scanning the entire table.

### How Indexing Works

- **Data Structure:** Indexes are typically implemented using data structures like B-trees, B+ trees, or hash tables. B-trees and B+ trees are commonly used because they maintain sorted order and allow for efficient searching, insertion, and deletion.
- **Indexed Columns:** An index is created on one or more columns of a table. When you query the database using these columns, the index helps in quickly locating the rows that match the query condition.
- **Primary vs. Secondary Index:** 
  - **Primary Index:** Automatically created on the primary key of a table. It ensures that each key is unique and helps in the fast retrieval of records based on the primary key.
  - **Secondary Index:** Created on non-primary key columns to speed up queries involving those columns.

### Types of Indexes

1. **Single-Column Index:**
   - An index on a single column of a table.
   - Useful for queries that filter or sort based on that column.
   - Example: `CREATE INDEX idx_name ON employees (last_name);`

2. **Composite (Multi-Column) Index:**
   - An index on multiple columns of a table.
   - Useful for queries that filter or sort based on multiple columns in a specific order.
   - Example: `CREATE INDEX idx_name_dept ON employees (last_name, department_id);`
   - **Note:** The order of columns in a composite index matters; it’s optimized for queries that filter based on the first column or both columns.

3. **Unique Index:**
   - Ensures that the indexed column(s) contain unique values.
   - Example: `CREATE UNIQUE INDEX idx_email ON users (email);`

4. **Full-Text Index:**
   - Used for full-text searches, typically in text-heavy fields.
   - Example: Searching for keywords within a blog post content.

5. **Bitmap Index:**
   - Stores a bitmap for each possible value of an indexed column.
   - Efficient for columns with a low cardinality (few unique values).
   - Often used in data warehousing for complex queries involving multiple columns.

6. **Clustered vs. Non-Clustered Index:**
   - **Clustered Index:** Alters the physical order of the table. A table can have only one clustered index, usually on the primary key.
   - **Non-Clustered Index:** Does not alter the physical order. A table can have multiple non-clustered indexes.

### How to Approach Indexing as Part of Database Design

1. **Understand the Query Patterns:**
   - Analyze the most common queries your application will run.
   - Identify which columns are frequently used in `WHERE`, `JOIN`, `ORDER BY`, and `GROUP BY` clauses.

2. **Index Selective Columns:**
   - Index columns that have high selectivity, meaning they have a large number of unique values.
   - Avoid indexing columns with low cardinality (few unique values), as the performance gain might not justify the overhead.

3. **Use Composite Indexes for Multi-Column Queries:**
   - If a query often filters or sorts by multiple columns, consider creating a composite index that covers those columns.
   - Ensure that the order of columns in the index matches the query patterns.

4. **Limit the Number of Indexes:**
   - While indexes improve read performance, they add overhead to write operations (INSERT, UPDATE, DELETE).
   - Avoid over-indexing; only create indexes that will significantly improve query performance.

5. **Consider the Data Modification Impact:**
   - Indexes slow down write operations because they need to be updated every time data is inserted, updated, or deleted.
   - Balance the need for fast reads with the potential impact on write performance.

6. **Use Covering Indexes:**
   - A covering index is one where all the columns used in a query are included in the index. This allows the database to satisfy the query entirely from the index without accessing the actual table.

7. **Monitor and Tune Indexes:**
   - Regularly analyze the performance of your queries and indexes.
   - Use database tools to identify unused indexes and remove them.
   - Rebuild or reorganize indexes periodically to maintain performance.

### Indexing in the Context of Query Optimization

- **Faster Query Execution:**
  - Indexes significantly speed up query execution by reducing the amount of data the database needs to scan.
  - For example, a query that searches for a specific record by ID can directly locate the record using an index rather than scanning the entire table.

- **Reducing Disk I/O:**
  - Indexes reduce the number of disk I/O operations needed to retrieve data, which is a common bottleneck in query performance.
  - This is especially important in large databases where full table scans can be prohibitively expensive.

- **Avoiding Full Table Scans:**
  - Without an index, the database might perform a full table scan, which is slow, especially for large tables. An index allows the database to jump directly to the relevant rows.
  
- **Optimizing Complex Queries:**
  - Complex queries with multiple joins, conditions, and aggregations benefit greatly from well-designed indexes.
  - For example, creating an index on the columns used in join conditions can drastically reduce the time required to execute the query.

- **Improving Sorting and Grouping:**
  - Indexes can speed up operations like `ORDER BY` and `GROUP BY` because the data is already sorted in the index.
  
- **Covering Indexes:**
  - If an index contains all the columns needed for a query, the database can retrieve results directly from the index without accessing the table, which is known as a covering index.

### Example

Consider a table `employees` with columns `employee_id`, `first_name`, `last_name`, `department_id`, and `salary`.

- **Query:** `SELECT * FROM employees WHERE last_name = 'Smith';`
  - **Index:** Creating an index on `last_name` (`CREATE INDEX idx_lastname ON employees(last_name);`) will significantly speed up this query by allowing the database to locate all rows with `last_name = 'Smith'` quickly.

- **Query:** `SELECT * FROM employees WHERE department_id = 5 ORDER BY salary DESC;`
  - **Index:** A composite index on `department_id` and `salary` (`CREATE INDEX idx_dept_salary ON employees(department_id, salary DESC);`) will optimize both the filtering and sorting operations.

In summary, indexing is a crucial aspect of database design and query optimization. By carefully selecting which columns to index and understanding your query patterns, you can significantly improve the performance and efficiency of your database.

___

In SQL databases, indexes are used to speed up the retrieval of data by providing quick access to rows in a table. There are two primary types of indexes: **Clustered** and **Non-Clustered**. Understanding the differences between them is crucial for database design and performance optimization.

### Clustered Index

- **Definition**: A clustered index determines the physical order of data in the table. Essentially, it sorts and stores the data rows of the table based on the index key. Because of this, a table can have only one clustered index since the data rows can only be sorted in one way.

- **Characteristics**:
  - The table itself is organized around the clustered index. The index and the table data are stored together.
  - When you create a clustered index, the rows in the table are sorted according to the index.
  - Fast retrieval of data when the search involves the columns included in the clustered index, because the data is physically stored in order.
  - Suitable for range queries (e.g., finding records between certain dates).

- **Example**: A primary key constraint automatically creates a clustered index. If you create a table with a primary key, the primary key column is by default a clustered index.
  ```sql
  CREATE TABLE Employees (
      EmployeeID INT PRIMARY KEY, -- This creates a clustered index on EmployeeID
      Name VARCHAR(100),
      DepartmentID INT
  );
  ```

### Non-Clustered Index

- **Definition**: A non-clustered index creates a separate structure from the table data, which contains pointers (or references) to the location of the actual data rows. It does not affect the physical order of data in the table.

- **Characteristics**:
  - A table can have multiple non-clustered indexes.
  - The index stores a sorted list of values for the specified columns, along with pointers to the corresponding rows in the table.
  - Non-clustered indexes are useful for queries that filter on columns not included in the clustered index, and for quickly locating rows without scanning the entire table.
  - Non-clustered indexes can improve performance for lookups, but might require additional space to store pointers.

- **Example**: Creating a non-clustered index on the `Name` column of the `Employees` table.
  ```sql
  CREATE NONCLUSTERED INDEX idx_EmployeeName
  ON Employees(Name);
  ```

### Key Differences

1. **Physical vs. Logical Sorting**:
   - **Clustered Index**: Physically arranges and sorts the table data based on the indexed column(s).
   - **Non-Clustered Index**: Maintains a logical order for the indexed column(s) and includes pointers to the actual data rows.

2. **Number per Table**:
   - **Clustered Index**: Only one per table, as it defines the physical layout.
   - **Non-Clustered Index**: Multiple non-clustered indexes can be created per table.

3. **Storage**:
   - **Clustered Index**: The data rows are stored directly in the order of the clustered index.
   - **Non-Clustered Index**: The index and the data rows are stored separately; the index contains pointers to the actual data locations.

4. **Use Cases**:
   - **Clustered Index**: Ideal for columns frequently used in range queries or where data is often retrieved in sorted order.
   - **Non-Clustered Index**: Ideal for columns used in search queries or frequently joined columns, not necessarily involving sorting.

### Summary

- Use a **Clustered Index** when you need data to be physically sorted for performance, such as for primary keys or frequently searched columns that benefit from sorting.
- Use a **Non-Clustered Index** when you need to quickly find data based on a specific column or set of columns without requiring the physical order to be changed.

Choosing the correct type of index depends on the specific use cases and query patterns of your database, and both types of indexes can be used effectively to improve query performance.


___

Index - data structures 
   - usually b-tree/ b+tree, hashtables 
   - primary index - made on primary key - already present in most dbs
   - secondary index - can be made on non-primary key columns to speed up search
      - Single Field Index: Created on one field.
      - Compound Index: Created on multiple fields (used for multi-field queries).


**Limitations in MongoDB**
- Index Size: Indexes must fit in RAM to be efficient. If the index size exceeds available memory, MongoDB performance may degrade as it will have to read indexes from disk.
- Index Overhead: Indexes add storage overhead. More indexes mean more disk usage and slower writes due to the need to maintain the indexes.
- Write Latency: For every write operation (inserts, updates, deletes), MongoDB must update all relevant indexes, which can introduce write latency.
- Inefficient for High Cardinality Queries: If the indexed field has high cardinality (many distinct values), performance may degrade as MongoDB has to traverse a large index.
- Single Field Index for Sharding: Only one index can be used as the shard key, limiting the flexibility of how data is partitioned across multiple nodes