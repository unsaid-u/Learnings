
Asynchornous processing
Concurrency 
Multithreading

    Definitions
    Usecase
    How they can be achieved (implementation) 
    Overheads 


**Asynchronous processing** refers to the execution of tasks in a non-blocking manner, where the program can continue to perform other operations while waiting for the completion of the task.

**Concurrency** refers to the ability of a program to handle multiple tasks at the same time. It allows for different tasks to make progress even if one of them is busy or waiting.
    -> Concurrency can come into picture when we have single core cpu and multiple tasks (all) need execution at a level of a time
     -> Here, job context switching comes into picture, which has some overhead of saving state of each job 

**Parallelism** refers to the execution of multiple tasks simultaneously, typically across multiple processors or cores. 
Tasks are divided into smaller sub-tasks and executed in parallel to improve performance. This may involve dividing a task into smaller components that can be executed concurrently, 
or assigning separate tasks to different processors or cores.g refers to the execution of multiple tasks simultaneously, typically across multiple processors or cores. Tasks are divided into smaller sub-tasks and executed in parallel to improve performance. This may involve dividing a task into smaller components that can be executed concurrently, or assigning separate tasks to different processors or cores.

**Multithreading** is a specific type of concurrency in which different parts of a program can run concurrently and independently of each other, allowing for more efficient use of resourcesand improved performance. 
It involves creating multiple threads within a single process, each handling a different task.



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
