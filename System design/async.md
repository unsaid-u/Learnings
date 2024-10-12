
Asynchornous processing
Concurrency 
Multithreading
Parallelism

Parallelism can only be achived via a multicore design

    Definitions
    Usecase
    How they can be achieved (implementation) 
    Overheads 


**Asynchronous processing** refers to the execution of tasks in a non-blocking manner, where the program can continue to perform other operations while waiting for the completion of the task.

**Concurrency** refers to the ability of a program to handle multiple tasks at the same time. It allows for different tasks to make progress even if one of them is busy or waiting.
    -> Concurrency can come into picture when we have single core cpu and multiple tasks (all) need execution at a level of a time
     -> Here, job context switching comes into picture, which has some overhead of saving state of each job 

- single core - CPU jumps between tasks frequently between jobs, giving illusion of running concurrently - *increases the CPU context switch overhead*. CPU does some chunks of a job 1, then save the state and then starts job2 - switch, save state, context reuse till 1 is complete. and so on
     
**Parallelism** refers to the execution of multiple tasks simultaneously, typically across multiple processors or cores. 
Tasks are divided into smaller sub-tasks and executed in parallel to improve performance. This may involve dividing a task into smaller components that can be executed concurrently, 
or assigning separate tasks to different processors or cores.g refers to the execution of multiple tasks simultaneously, typically across multiple processors or cores. Tasks are divided into smaller sub-tasks and executed in parallel to improve performance. This may involve dividing a task into smaller components that can be executed concurrently, or assigning separate tasks to different processors or cores.

**Multithreading** is a specific type of concurrency in which different parts of a program can run concurrently and independently of each other, allowing for more efficient use of resourcesand improved performance. 
It involves creating multiple threads within a single process, each handling a different task, each handling a single independant task.
- Its is generally easier to switch context between threads than processes


## Async and concurrency are related concepts, but they have some key differences:

**Concurrency:**

* **Focuses on managing multiple tasks that appear to be running at the same time.** It doesn't necessarily guarantee true parallel execution, but it gives the illusion of it.
* **Can be achieved with various techniques:**
    * **Multithreading:** Running multiple threads of execution within a single process. This allows true parallel execution on systems with multiple cores.
    * **Process-based:** Running multiple independent processes to handle tasks concurrently.
* **Complexity:** Managing concurrent tasks can be complex due to potential race conditions and the need for synchronization mechanisms to avoid data corruption.

**Async:**

* **Focuses on avoiding blocking the main thread while waiting for long-running tasks to complete.** This improves application responsiveness and allows the program to continue executing other tasks.
* **Doesn't necessarily imply true parallel execution.** The asynchronous operation might still run on the same thread as the main program.
* **Achieved through mechanisms like callbacks, promises, or async/await (depending on the programming language).** These techniques allow the program to continue execution and be notified when the asynchronous operation finishes.
* **Complexity:**  While simpler than full concurrency with multithreading, dealing with callbacks and managing asynchronous flow can still introduce some complexity.

**Here's an analogy:**

* **Imagine you're a chef (main thread).** You have to prepare multiple dishes (tasks).
* **Concurrency:** You hire multiple assistants (threads) to help you cook different dishes simultaneously (parallel execution). This can be very efficient, but you need to coordinate carefully to avoid mistakes (e.g., not using the same oven at the same time).
* **Async:** You place orders (start long-running tasks) for ingredients (data) at the grocery store (server) and the butcher (another server). While you wait for the deliveries (asynchronous operations), you can prep other dishes (continue executing other tasks). Once the deliveries arrive (tasks finish), you'll be notified (through callbacks or promises) and can resume those specific tasks.

**In summary:**

* **Concurrency** allows managing multiple tasks that appear to run simultaneously, while **async** avoids blocking the main thread during long-running operations.
* **Concurrency** can be more complex due to potential synchronization issues, while **async** is simpler but still requires managing asynchronous flow.
* **They can be used together:** Async operations can be employed within a concurrent program to maintain responsiveness.


![concurrency vs paralleism](<../flow dialgrams/Screenshot 2024-09-10 at 7.30.25 AM.png>)

___

### Multithreading - single core vs multi-core:

Multithreading is a concept where multiple threads are created within a single process to perform tasks concurrently. Each thread represents a separate path of execution, allowing a program to perform multiple tasks at the same time, or at least appear to do so. 

#### **Multithreading on a Single-Core System**

On a single-core system, the CPU can only execute one instruction at a time, which means true parallelism is impossible. However, **multithreading** allows **concurrency** by making use of the CPU's ability to quickly switch between threads. This is achieved through **context switching**, where the CPU shifts its attention from one thread to another, giving the appearance of multiple threads running simultaneously. Here's how multithreading achieves concurrency on a single-core system:

##### Key Concepts:
- **Concurrency**: This is when two or more tasks are making progress over the same period of time. Even though the CPU is executing one task at a time, it switches between tasks so quickly that it seems like they're running in parallel.
- **Thread Switching**: On a single-core system, the operating system uses a scheduler to determine which thread should be running at any given time. The CPU switches between threads frequently, usually hundreds or thousands of times per second. This switching is what gives the illusion of parallelism.
- **Blocking I/O**: One of the biggest advantages of multithreading is the ability to deal with I/O-bound tasks. When a thread is waiting for an I/O operation (e.g., reading a file or waiting for a network request), other threads can continue to run, which improves responsiveness and efficiency.

##### Benefits of Multithreading on Single-Core Systems:
1. **Improved Responsiveness**: While one thread is blocked (e.g., waiting for I/O), other threads can continue executing.
2. **Concurrency in I/O-bound Tasks**: Tasks that involve waiting (such as network requests or file reading) can benefit from multithreading, as threads can perform computation while others are waiting.
3. **Task Prioritization**: The scheduler can prioritize more important threads over less critical ones, optimizing CPU time usage.

##### Limitations on a Single-Core System:
- **No Real Parallelism**: Only one thread can be executed at any point in time, so multithreading cannot truly speed up CPU-bound tasks.
- **Context Switching Overhead**: Switching between threads incurs some overhead, as the CPU must save and restore the state of each thread, which can lead to performance degradation if not managed efficiently.

---

#### **Multithreading on a Multi-Core System**

In a multi-core system, multiple CPU cores are available, each capable of executing its own thread. This allows **true parallelism**, where threads can be executed simultaneously on different cores, unlike a single-core system that only simulates parallelism.

##### Key Concepts:
- **Parallelism**: This is the simultaneous execution of multiple threads. In a multi-core system, each core can run a thread independently, achieving real parallel processing.
- **Load Balancing**: The operating system's scheduler attempts to distribute threads across multiple cores efficiently, balancing the workload to prevent any core from being overworked.
- **CPU-Bound Tasks**: In multi-core systems, CPU-bound tasks (tasks that require heavy computation) benefit greatly from multithreading because the workload can be divided among different cores, thereby reducing overall execution time.

##### Benefits of Multithreading on Multi-Core Systems:
1. **True Parallelism**: Multiple threads can execute at the same time on different cores, speeding up CPU-bound tasks (e.g., mathematical computations, simulations).
2. **Scalability**: As the number of CPU cores increases, more threads can run in parallel, improving the overall performance of multi-threaded applications.
3. **Improved Performance for CPU-Intensive Applications**: Tasks like scientific computations, image processing, and simulations benefit greatly as they can be split into multiple threads that run on different cores.
4. **Concurrent Task Execution**: Both I/O-bound and CPU-bound tasks can benefit from multithreading in a multi-core system, as some cores handle computation while others handle I/O-bound threads.

##### Limitations and Considerations:
- **Thread Synchronization**: When multiple threads are accessing shared resources, synchronization issues like race conditions, deadlocks, and data inconsistencies can arise. Proper synchronization mechanisms (e.g., mutexes, semaphores) are required to prevent these problems.
- **Thread Overhead**: Although multi-core systems can execute threads in parallel, too many threads can lead to excessive context switching and resource contention, which may reduce performance.
- **Scalability Limits**: Not all tasks can be parallelized easily. Some tasks might have dependencies that require one thread to wait for another, reducing the benefit of parallelism.

##### Example: Performance Impact
For example, if a task can be broken down into independent subtasks, on a multi-core system:
- A **single-core system** may take 10 seconds to complete, as it runs each subtask sequentially by switching between threads.
- A **multi-core system** with 4 cores can divide the task into 4 threads, one for each core, and complete the job in approximately 2.5 seconds, assuming there’s no significant overhead.

---

#### Conclusion:
- **Single-Core System**: Multithreading provides **concurrency**, allowing tasks to progress by context switching between threads, though there is no real parallelism. It's most beneficial for I/O-bound applications.
  
- **Multi-Core System**: Multithreading provides both **concurrency** and **parallelism**, enabling true simultaneous execution of threads across multiple cores. This is especially beneficial for CPU-bound tasks, where splitting work across cores can significantly speed up performance.

_**Good article on concurreny and race conditions, in Node.js**_
[Mastering Node.js Concurrency: 🚦Race Condition Detection and Prevention](https://medium.com/@zuyufmanna/mastering-node-js-concurrency-race-condition-detection-and-prevention-3e0cfb3ccb07)

![threads](<../flow dialgrams/threads.png>)

