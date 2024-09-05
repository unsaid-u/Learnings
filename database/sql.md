### Important SQL Queries with Joins

1. **Simple Select Query:**
   ```sql
   SELECT * FROM employees;
   ```

2. **Filtering with WHERE Clause:**
   ```sql
   SELECT * FROM employees WHERE department = 'Sales';
   ```

3. **Using `JOIN` (INNER JOIN):**
   Joins two tables and returns rows that have matching values in both tables.
   ```sql
   SELECT employees.name, departments.department_name
   FROM employees
   INNER JOIN departments ON employees.department_id = departments.id;
   ```

4. **LEFT JOIN:**
   Returns all rows from the left table, and the matched rows from the right table. If no match, NULL values are returned for columns from the right table.
   ```sql
   SELECT employees.name, departments.department_name
   FROM employees
   LEFT JOIN departments ON employees.department_id = departments.id;
   ```

5. **RIGHT JOIN:**
   Returns all rows from the right table, and the matched rows from the left table. If no match, NULL values are returned for columns from the left table.
   ```sql
   SELECT employees.name, departments.department_name
   FROM employees
   RIGHT JOIN departments ON employees.department_id = departments.id;
   ```

6. **FULL OUTER JOIN:**
   Returns all rows when there is a match in either left or right table. If there is no match, the result is NULL on the side that does not have a match.
   ```sql
   SELECT employees.name, departments.department_name
   FROM employees
   FULL OUTER JOIN departments ON employees.department_id = departments.id;
   ```

7. **CROSS JOIN:**
   Returns the Cartesian product of both tables (i.e., all possible combinations of rows).
   ```sql
   SELECT employees.name, projects.project_name
   FROM employees
   CROSS JOIN projects;
   ```

8. **GROUP BY with Aggregation:**
   Groups rows that have the same values into summary rows, like "find the number of employees in each department".
   ```sql
   SELECT department, COUNT(*)
   FROM employees
   GROUP BY department;
   ```

9. **HAVING Clause (used with GROUP BY):**
   Filters groups after aggregation.
   ```sql
   SELECT department, COUNT(*)
   FROM employees
   GROUP BY department
   HAVING COUNT(*) > 5;
   ```

10. **ORDER BY Clause:**
    Orders the result set of a query by one or more columns.
    ```sql
    SELECT name, salary
    FROM employees
    ORDER BY salary DESC;
    ```

11. **Subquery (Nested Query):**
    A query within another query.
    ```sql
    SELECT name
    FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees);
    ```

12. **UNION Operator:**
    Combines the result-set of two or more SELECT statements.
    ```sql
    SELECT name FROM employees
    UNION
    SELECT name FROM clients;
    ```

### Important SQL Query Interview Questions

1. **What is the difference between `INNER JOIN` and `OUTER JOIN`? Provide examples.**

2. **How do you find the second highest salary from the "employees" table?**
   ```sql
   SELECT MAX(salary) AS SecondHighestSalary
   FROM employees
   WHERE salary < (SELECT MAX(salary) FROM employees);
   ```

3. **Write a query to retrieve all employees who have the same department as 'John'.**
   ```sql
   SELECT e1.name
   FROM employees e1
   JOIN employees e2 ON e1.department_id = e2.department_id
   WHERE e2.name = 'John';
   ```
   a subquery approach would also work, and is more efficient than join
   ```
    SELECT name
    FROM employees
    WHERE department_id = (
        SELECT department_id
        FROM employees
        WHERE name = 'John'
    );
    ```

4. **What is a self-join? Write a query using a self-join.**
   A self-join is a regular join but the table is joined with itself.
   ```sql
   SELECT e1.name AS Employee, e2.name AS Manager
   FROM employees e1
   JOIN employees e2 ON e1.manager_id = e2.id;
   ```

5. **How do you find the number of employees in each department, including departments with no employees?**
   ```sql
   SELECT d.department_name, COUNT(e.id) AS num_employees
   FROM departments d
   LEFT JOIN employees e ON d.id = e.department_id
   GROUP BY d.department_name;
   ```

6. **Write a SQL query to delete duplicate rows from a table.**
   ```sql
   DELETE FROM employees
   WHERE id NOT IN (
       SELECT MIN(id)
       FROM employees
       GROUP BY name, department_id
   );
   ```

7. **Explain the difference between `WHERE` and `HAVING` clauses.**

8. **How would you optimize a slow-running query?**
   - Use indexes on the columns that are being queried often.
   - Avoid using `SELECT *`; instead, specify the needed columns.
   - Ensure proper indexing on columns used in joins and filtering.
   - Consider denormalizing data if necessary for read-heavy systems.
   - Use EXPLAIN to analyze the query execution plan.

9. **What are the differences between a clustered index and a non-clustered index?**

10. **Write a query to find the top N records by a specific field.**
    ```sql
    SELECT *
    FROM employees
    ORDER BY salary DESC
    LIMIT 5;
    ```

These queries and questions are commonly encountered in interviews for SQL-related roles. They test a candidate's ability to handle common SQL tasks and understand important concepts related to database management and optimization.

___

### Normalization

**Normalization** is a database design technique that organizes tables to reduce redundancy and improve data integrity. The goal is to minimize duplication of information and to ensure that data dependencies are logical and stored efficiently. 

Normalization is achieved through a series of steps known as **normal forms**. Each normal form addresses specific issues, and a database that satisfies higher normal forms is considered more normalized.

#### Normal Forms

1. **First Normal Form (1NF)**:
   - **Rule**: Each table cell should contain only a single value (atomic values), and each record needs to be unique.
   - **Example**: A table with columns like `ID`, `Name`, `PhoneNumbers` would be non-1NF if `PhoneNumbers` contains multiple phone numbers. To convert it to 1NF, each phone number should be in a separate row.

2. **Second Normal Form (2NF)**:
   - **Rule**: It must be in 1NF, and all non-key attributes must be fully functional dependent on the primary key. This means that there should be no partial dependency of any column on the primary key.
   - **Example**: In a table with columns `StudentID`, `CourseID`, and `CourseName`, if `CourseName` is dependent only on `CourseID`, not on `StudentID`, it violates 2NF. `CourseName` should be in a separate table.

3. **Third Normal Form (3NF)**:
   - **Rule**: It must be in 2NF, and there should be no transitive dependency (i.e., non-key attributes should not depend on other non-key attributes).
   - **Example**: In a table with `StudentID`, `CourseID`, `CourseName`, and `InstructorName`, if `InstructorName` is dependent on `CourseID` (and `CourseID` is dependent on `StudentID`), this is a transitive dependency. `InstructorName` should be moved to another table where `CourseID` is the key.

4. **Boyce-Codd Normal Form (BCNF)**:
   - A stricter version of 3NF where every determinant must be a candidate key.

### Denormalization

**Denormalization** is the process of combining normalized tables into larger, more complex tables. It involves merging tables or adding redundant data to improve read performance, even at the cost of some redundancy and potential anomalies.

#### Key Points:

- **Purpose**: To optimize read performance, denormalization allows retrieving all required information with fewer joins, making data retrieval faster.
- **Trade-Off**: While it improves read performance, it can lead to data redundancy, which may increase the storage requirements and complicate data updates and inserts.

#### Example:

- In a normalized design, you might have separate `Customers` and `Orders` tables with a foreign key relationship. In a denormalized version, customer details could be included in the `Orders` table directly, reducing the need for joins when reading customer order information.

### Consider Denormalizing Data If Necessary for Read-Heavy Systems

**Context Explanation**:

- **Read-Heavy Systems**: These are systems where the majority of operations involve reading data rather than writing or updating it. Examples include reporting systems, data warehouses, or web applications with high read-to-write ratios.

- **Why Consider Denormalization?**
  - **Performance Optimization**: In read-heavy systems, frequent joins can slow down performance. By denormalizing data, you reduce the need for complex joins, thereby speeding up read operations.
  - **Simplified Querying**: Fewer joins make the SQL queries simpler and faster. This can be particularly beneficial in real-time data processing or when running complex analytical queries.
  - **Caching Efficiency**: Denormalized data is easier to cache because all required information is often contained within a single table. This can significantly enhance performance for repeated read operations.

- **Potential Downsides**:
  - **Data Redundancy**: Denormalization introduces redundancy, which can lead to inconsistencies and increased storage costs. Changes need to be replicated across multiple rows or tables, increasing the complexity of updates.
  - **Data Integrity**: It becomes harder to maintain integrity when the same data is stored in multiple places. Updates need careful handling to prevent anomalies.

#### Example Scenario:

Imagine an e-commerce platform where the order details need to be fetched frequently for displaying on the user dashboard. Instead of having separate normalized tables for `Orders`, `Customers`, and `Products`, a denormalized table could store all order-related information, including customer details and product specifications. This would allow for quicker retrieval of order details since all information can be fetched from a single table.

### Conclusion

- **Normalization** is essential for maintaining data integrity and minimizing redundancy, making it ideal for transactional systems with frequent updates.
- **Denormalization** is useful for improving read performance in scenarios where reading data is more common than writing, such as in reporting or read-heavy applications. The trade-off is increased complexity in maintaining data consistency.
- The decision to normalize or denormalize depends on the specific use case, data access patterns, and performance requirements. Both approaches have their place in database design and should be evaluated carefully when designing a database schema.