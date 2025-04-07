**Hierarchy: Broker - Topic - Partition - Consumer**

The hierarchy is as follows:

1. **Broker:** A Kafka broker is a single Kafka server.  A Kafka cluster consists of one or more brokers.  Brokers store the data for Kafka topics and partitions.

2. **Topic:** A topic is a category or feed name to which messages are published.  It's a logical grouping of related messages.

3. **Partition:** A topic is divided into one or more partitions.  Each partition is an ordered sequence of messages.  Partitions are the fundamental units of parallelism and distribution in Kafka.

4. **Consumer:** Consumers subscribe to topics.  Consumers within the same consumer group cooperate to consume messages from the partitions of a topic.  Each consumer in a group is assigned one or more partitions, and each partition is consumed by only one consumer in a group.

**Visual Representation**

```
Kafka Cluster (multiple brokers)
  └── Broker 1
      └── Topic A
          ├── Partition 1
          └── Partition 2
      └── Topic B
          └── Partition 1
  └── Broker 2
      └── Topic A
          ├── Partition 3
          └── Partition 4
      └── Topic C
          └── Partition 1

Consumer Group 1
  └── Consumer 1 (consumes from Topic A - Partition 1 & 2)
  └── Consumer 2 (consumes from Topic A - Partition 3 & 4)

Consumer Group 2
  └── Consumer 3 (consumes from Topic B - Partition 1)
```

**Key Points to Remember**

* **Ordering:** Messages are only guaranteed to be ordered *within* a partition.  There's no guarantee of ordering across partitions within a topic.
* **Parallelism:** Partitions are the unit of parallelism.  More partitions allow for more consumers to process messages concurrently.
* **Scalability:** Distributing a topic across multiple partitions allows Kafka to scale horizontally by adding more brokers and consumers.
* **Consumer Groups:** Consumers within the same group share the responsibility of consuming messages from the partitions of a topic.
