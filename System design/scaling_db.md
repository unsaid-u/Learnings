Scaling a PostgreSQL database to handle a large number of requests in a short time frame without changing backend code involves optimizing the database performance and infrastructure. Here are some strategies you can consider:

### 1. **Vertical Scaling (Scaling Up)**
- **Upgrade Hardware:** Increase the CPU, memory, and storage resources of the database server.
- **Use Faster Storage:** Switch to SSDs if you're using HDDs, as SSDs provide much faster read/write speeds.

### 2. **Horizontal Scaling (Scaling Out)**
- **Read Replicas:** Set up read replicas to distribute read requests. This can significantly reduce the load on the primary database.
- **Load Balancing:** Use a load balancer to distribute requests between the primary database and read replicas.

### 3. **Database Configuration Tuning**
- **Connection Pooling:** Use a connection pooling tool like PgBouncer to manage database connections efficiently.
- **Adjust Configuration Parameters:** Tune PostgreSQL configuration parameters such as `shared_buffers`, `work_mem`, `maintenance_work_mem`, `checkpoint_segments`, and `effective_cache_size`.

### 4. **Indexing**
- **Create Indexes:** Ensure that proper indexes are in place for frequently queried columns. This can significantly speed up query execution.
- **Optimize Existing Indexes:** Review and optimize existing indexes to ensure they are being used efficiently.

### 5. **Caching**
- **In-Memory Caching:** Use in-memory caching solutions like Redis or Memcached to cache frequently accessed data and reduce the number of database queries.
- **Application-Level Caching:** Implement caching at the application level to reduce the database load.

### 6. **Partitioning**
- **Table Partitioning:** Partition large tables to improve query performance and maintenance tasks. PostgreSQL supports range, list, and hash partitioning.
- **Sharding:** Distribute data across multiple databases or servers to balance the load.

### 7. **Monitoring and Optimization**
- **Monitor Performance:** Use monitoring tools like pg_stat_statements, pgBadger, or Datadog to monitor database performance and identify bottlenecks.
- **Analyze Queries:** Regularly analyze slow queries and optimize them using the `EXPLAIN` command.

### 8. **Managed Database Services**
- **Cloud Databases:** Consider using managed database services provided by cloud providers like AWS RDS, Google Cloud SQL, or Azure Database for PostgreSQL. These services offer automatic scaling, backups, and maintenance.

### 9. **Clustering**
- **PostgreSQL Clustering:** Set up a PostgreSQL cluster using tools like Patroni, Citus, or pgpool-II for high availability and load distribution.

Implementing these strategies can help handle the increased load on your PostgreSQL database and improve its performance without requiring changes to your backend code.