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


___

### SQL Commands: DDL, DML, DCL, TCL, and DQL

In SQL (Structured Query Language), commands are classified into different types based on their purpose and functionality. These types are:

1. **DDL (Data Definition Language)**
2. **DML (Data Manipulation Language)**
3. **DCL (Data Control Language)**
4. **TCL (Transaction Control Language)**
5. **DQL (Data Query Language)**

Each type is used to interact with the database in different ways, such as defining the structure of the database, manipulating data within it, controlling access, and more.

---

### 1. **DDL (Data Definition Language)**

DDL commands are used to **define** and **modify** the structure of a database (tables, schemas, indices, etc.). DDL statements generally **do not manipulate data** but instead work with the schema or metadata of the database.

Some key **DDL commands**:

- **`CREATE`**: Creates objects in the database, such as tables, views, schemas, or indices.
  
    ```sql
    CREATE TABLE Employees (
      EmployeeID INT PRIMARY KEY,
      Name VARCHAR(50),
      Age INT,
      Department VARCHAR(50)
    );
    ```

- **`ALTER`**: Alters the structure of an existing object (like adding, modifying, or dropping columns from a table).
  
    ```sql
    ALTER TABLE Employees
    ADD Email VARCHAR(100);
    ```

- **`DROP`**: Deletes an object (like a table or view) from the database.

    ```sql
    DROP TABLE Employees;
    ```

- **`TRUNCATE`**: Removes all records from a table, but the table itself remains.
  
    ```sql
    TRUNCATE TABLE Employees;
    ```

---

### 2. **DML (Data Manipulation Language)**

DML commands are used to **manipulate data** in the database. These commands operate on the data stored in tables, allowing you to insert, update, delete, and retrieve data.

Some key **DML commands**:

- **`INSERT`**: Adds new records to a table.

    ```sql
    INSERT INTO Employees (EmployeeID, Name, Age, Department)
    VALUES (1, 'John', 30, 'HR');
    ```

- **`UPDATE`**: Modifies existing data in a table.
  
    ```sql
    UPDATE Employees
    SET Age = 31
    WHERE EmployeeID = 1;
    ```

- **`DELETE`**: Deletes records from a table.

    ```sql
    DELETE FROM Employees
    WHERE EmployeeID = 1;
    ```

---

### 3. **DCL (Data Control Language)**

DCL commands are used to **control access** to the data and the database. These commands manage permissions and enforce security by granting or revoking privileges to users.

Some key **DCL commands**:

- **`GRANT`**: Gives specific privileges to users or roles.
  
    ```sql
    GRANT SELECT, INSERT ON Employees TO 'username';
    ```

- **`REVOKE`**: Removes privileges from users or roles.
  
    ```sql
    REVOKE SELECT, INSERT ON Employees FROM 'username';
    ```

---

### 4. **TCL (Transaction Control Language)**

TCL commands are used to **manage transactions** in the database. A transaction is a group of SQL commands that are executed together as a single unit. TCL commands allow you to control whether the transaction is completed (committed) or undone (rolled back).

Some key **TCL commands**:

- **`COMMIT`**: Saves the changes made in the transaction permanently to the database.
  
    ```sql
    COMMIT;
    ```

- **`ROLLBACK`**: Undoes the changes made in the current transaction.
  
    ```sql
    ROLLBACK;
    ```

- **`SAVEPOINT`**: Sets a point within a transaction to which you can later roll back.

    ```sql
    SAVEPOINT savepoint_name;
    ```

- **`RELEASE SAVEPOINT`**: Deletes a previously set savepoint, but does not affect the transaction itself.

    ```sql
    RELEASE SAVEPOINT savepoint_name;
    ```

---

### 5. **DQL (Data Query Language)**

DQL is used to **retrieve data** from the database. Although **`SELECT`** is often included under DML, it's also frequently categorized as a separate DQL since its purpose is to **query** data rather than modify it.

Key **DQL command**:

- **`SELECT`**: Fetches data from the database based on given conditions.

    ```sql
    SELECT Name, Age
    FROM Employees
    WHERE Department = 'HR';
    ```

---

### **Normalization vs. Denormalization in Context of Read-Heavy Systems**

1. **Normalization**:
    - **Normalization** is a database design technique that organizes tables to reduce data redundancy and improve data integrity. It involves breaking down larger tables into smaller, related tables and establishing relationships between them.
    - This process follows normal forms (1NF, 2NF, 3NF, etc.), and its goal is to minimize duplication of data and avoid anomalies in data operations (inserts, updates, deletes).

    **Example of Normalization**:
    - Suppose we have a table combining employees and departments:
      
      | EmployeeID | EmployeeName | DepartmentID | DepartmentName |
      |------------|--------------|--------------|----------------|
      | 1          | John          | 101          | HR             |
      | 2          | Alice         | 102          | IT             |

      In normalization, we split this into two tables:
      
      **Employees**:
      | EmployeeID | EmployeeName | DepartmentID |
      |------------|--------------|--------------|
      | 1          | John          | 101          |
      | 2          | Alice         | 102          |

      **Departments**:
      | DepartmentID | DepartmentName |
      |--------------|----------------|
      | 101          | HR             |
      | 102          | IT             |

2. **Denormalization**:
    - **Denormalization** is the process of merging tables to **reduce the number of joins**, often to improve **query performance** in read-heavy systems.
    - In read-heavy systems, where data is accessed more frequently than it is updated, joins can become expensive in terms of performance, so denormalizing (i.e., intentionally introducing some data redundancy) can help improve **query speed**.

    **Example of Denormalization**:
    - In a denormalized design, you might merge the **Employees** and **Departments** tables back into one larger table, so the system doesn't have to perform a `JOIN` operation every time it needs to retrieve department names along with employee data.
  
    **Consideration for Denormalization in Read-Heavy Systems**:
    - **Read-heavy systems** are those where the frequency of reading data is much higher than updating it (e.g., reporting systems, search systems).
    - In such cases, **denormalization** can help optimize performance by reducing complex `JOIN` operations, which can slow down queries. However, denormalization comes with a trade-off: data redundancy increases, and maintaining data consistency can become more challenging during updates.

---

### Key Points:
- **Normalization** is about reducing redundancy and improving data integrity but can lead to complex joins and slower read performance.
- **Denormalization** introduces redundancy for the sake of **improving query performance** in read-heavy systems, at the cost of more challenging data updates.

In the context of **read-heavy systems**, **denormalization** can make sense because the performance boost in querying outweighs the potential drawbacks of maintaining duplicate data.

___

SELECT upper(FIRST_NAME) as STUDENT_NAME from Student;

SELECT DISTINCT MAJOR from STUDENT;    --- unique values of a column


SELECT SUBSTRING(FIRST_NAME, 1, 3)  FROM Student;       --- substring 
SELECT CONCAT(FIRST_NAME, ' ', LAST_NAME) AS COMPLETE_NAME FROM Student;
SELECT REPLACE(FIRST_NAME, 'a', 'A') FROM Student;



SELECT MAJOR,LENGTH(MAJOR) FROM Student GROUP BY(MAJOR);                                                         
or                                                                                                                                                                                                                 
SELECT DISTINCT MAJOR, LENGTH(MAJOR) FROM Student;

SELECT * FROM Student ORDER BY FIRST_NAME , MAJOR DESC;


SELECT * from Student WHERE FIRST_NAME IN ('Prem' , 'Shivansh');
                                    NOT IN


SELECT * FROM Student WHERE FIRST_NAME LIKE '%a';           ---- ends with 'a', starts with 'a%'
SELECT * FROM Student WHERE FIRST_NAME LIKE '_____a';       ---  five characters and ends with 'a'
SELECT * FROM Student WHERE GPA BETWEEN 9.00 AND 9.99;



SELECT Major, COUNT(*) as TOTAL_COUNT FROM Student WHERE MAJOR = 'Computer Science';

SELECT MAJOR, COUNT(MAJOR) from Student group by MAJOR order by COUNT(MAJOR) DESC;



SELECT 
    Student.FIRST_NAME,
    Student.LAST_NAME,
    Scholarship.SCHOLARSHIP_AMOUNT,
    Scholarship.SCHOLARSHIP_DATE
FROM 
    Student
INNER JOIN 
    Scholarship ON Student.STUDENT_ID = Scholarship.STUDENT_REF_ID;



--- List all students and their scholarship amounts if they have received any. If a student has not received a scholarship, display NULL for the scholarship details.

SELECT 
    Student.FIRST_NAME,
    Student.LAST_NAME,
    Scholarship.SCHOLARSHIP_AMOUNT,
    Scholarship.SCHOLARSHIP_DATE
FROM 
    Student
LEFT JOIN 
    Scholarship ON Student.STUDENT_ID = Scholarship.STUDENT_REF_ID;



SELECT * from Student ORDER BY GPA DESC LIMIT 5;    --- top 5 records 

SELECT * FROM Student ORDER BY GPA DESC LIMIT 5, 1;         --- determine the nth (say n=5) highest GPA from a table.
                                                            --- LIMIT 5, 1 is saying: skip the first 5 rows and then return exactly 1 row after that.
SELECT GPA                  ---- i think this is correct
FROM Student 
ORDER BY GPA DESC 
LIMIT 1 OFFSET 4;



--- Write an SQL query to fetch the list of Students with the same GPA.
SELECT s1.* FROM Student s1, Student s2 WHERE s1.GPA = s2.GPA AND s1.Student_id != s2.Student_id;
-- using explicit self join
SELECT s1.* 
FROM Student s1
JOIN Student s2 
  ON s1.GPA = s2.GPA 
  AND s1.Student_id != s2.Student_id;


-- to list STUDENT_ID who does not get Scholarship.
SELECT STUDENT_ID FROM Student 
WHERE STUDENT_ID NOT IN (SELECT STUDENT_REF_ID FROM Scholarship);



-- to fetch three max GPA from a table using co-related subquery.
SELECT DISTINCT GPA FROM Student S1 
WHERE 3 >= (SELECT COUNT(DISTINCT GPA) FROM Student S2 WHERE S1.GPA <= S2.GPA) ORDER BY S1.GPA DESC;


-- to fetch MAJOR subjects along with the max GPA in each of these MAJOR subjects.
SELECT MAJOR, MAX(GPA) as MAXGPA FROM Student GROUP BY MAJOR;



-- to fetch the names of Students who has highest GPA.
SELECT FIRST_NAME, GPA FROM Student WHERE GPA = (SELECT MAX(GPA) FROM Student);
SELECT MAJOR, AVG(GPA) AS AVERAGE_GPA FROM Student GROUP BY MAJOR;      --- avg gpa 
