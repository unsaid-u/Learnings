When RAM (Random Access Memory) gets full, the system may experience performance degradation, and the operating system takes several measures to handle the situation:

### 1. **Increased Use of Swap Space (Virtual Memory)**

When the RAM is full, the operating system starts using the **swap space** (on disk) to move inactive pages (data) from RAM to disk, freeing up space in RAM for more immediate tasks.

- **Swap space (or page file)** is part of the hard drive or SSD that is used as an extension of the RAM. Although it helps avoid running out of memory, reading from and writing to disk is much slower than using RAM.
- **Paging**: The system swaps parts of memory (pages) between RAM and disk storage to manage the memory load. Active processes stay in RAM, while inactive data or processes are moved to disk.

As a result, when RAM is full, the system relies heavily on swap space, which causes significant performance slowdowns because disk access speeds are far slower than RAM.

### 2. **System Slowdowns**

If more memory is needed than is available in RAM and swap space, the system starts spending more time moving data between RAM and disk (a process called **thrashing**). This can slow down the system, making it unresponsive as it tries to keep up with the memory demands.

Symptoms include:
- **Slow application performance**: Apps take longer to respond or load.
- **System freezing**: The OS may become unresponsive, making it difficult to switch between tasks or open new applications.
- **High disk I/O activity**: The disk light may stay on as the system continuously reads from and writes to the swap file.

### 3. **Out-of-Memory (OOM) Errors and Crashes**

If the system runs out of both RAM and swap space, the operating system may begin to terminate processes to free up memory. This is especially true for Linux systems, where the **OOM killer** process is invoked to kill memory-hogging processes.

- **OOM Killer**: On systems like Linux, when the system is critically low on memory, the OOM killer selects and terminates processes that are using large amounts of memory to recover resources.
- **Crashes**: In extreme cases, applications or even the entire system may crash due to insufficient memory to perform required operations.

### 4. **Application-Level Consequences**

Applications running on the system may experience the following effects:

- **Unresponsive or crashing applications**: Some programs may not handle memory shortages well and can become unresponsive or crash.
- **Data loss**: If an application crashes due to memory shortages, unsaved work may be lost.
- **Memory errors**: Some applications may throw specific memory-related errors, like "out of memory" exceptions, if they cannot allocate the necessary resources to function.

### 5. **Preventive Measures by the OS**

Modern operating systems take various preventive measures to avoid such scenarios:

- **Memory compression**: Some operating systems like macOS and Linux use memory compression techniques to reduce the amount of physical memory used by compressing inactive pages.
- **Low-memory warnings**: Some systems notify users when memory is running low, encouraging them to close unused applications.
- **Task management**: Operating systems like Windows and Linux allow users to manually kill processes through task managers (e.g., Task Manager in Windows, `top` or `htop` in Linux).

### 6. **How to Mitigate Full RAM Issues**

To mitigate the effects of full RAM, users can:

- **Close unused applications**: Free up RAM by closing background apps or tabs in a browser.
- **Increase RAM**: Physically upgrading the amount of RAM in the system helps handle larger workloads.
- **Use lighter applications**: Opt for less memory-intensive applications when working with large datasets.
- **Optimize software**: Developers can optimize applications to use less memory or release unused memory back to the system.

### Summary

When RAM gets full:
1. **Swap space** (disk-based virtual memory) is used, but it is much slower than RAM.
2. **Performance declines** due to increased paging and disk I/O.
3. **System slowdowns and unresponsiveness** can occur.
4. The system may invoke the **OOM killer** to terminate processes, or applications may crash.
5. To mitigate these issues, users can upgrade RAM, optimize applications, or close unused processes.