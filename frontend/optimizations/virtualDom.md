When React (or a similar framework) talks about a “virtual DOM,” what it really means is:

1. **In-memory Data Structure**

   * The virtual DOM is just a tree of JavaScript objects—plain data structures—kept in your page’s **JS heap**.
   * “In-memory” here means “held in the browser’s JavaScript memory,” not on the screen. It’s like a lightweight mirror of what the actual DOM should look like.

2. **Why That’s Faster for Updates**

   * **Real DOM operations** (inserting, removing, updating nodes or styles) are relatively slow because each change can trigger:

     1. **Reflow (layout)** – recalculating sizes/positions
     2. **Repaint** – redrawing pixels
     3. **Composite** – merging layers into the final screen
   * By contrast, **mutating plain JS objects** in memory is extremely cheap—no layout or paint is triggered.

3. **Diff & Batch vs. Direct Mutation**

   * When you update state in React, you don’t poke the real DOM immediately. You change the virtual-DOM objects.
   * React then **diffs** (compares) the new virtual tree against the previous one to figure out the smallest set of real-DOM changes needed.
   * Finally, it applies **only** those minimal changes in a single, efficient batch to the real DOM—greatly reducing wasted reflows and repaints.

4. **Real DOM vs. Virtual DOM**

   | Aspect          | Real DOM                                        | Virtual DOM                                             |
   | --------------- | ----------------------------------------------- | ------------------------------------------------------- |
   | Representation  | Browser’s internal HTML tree + layout info      | Plain JS objects—just your data/model                   |
   | Mutation cost   | High (may trigger reflow/repaint)               | Very low (object property updates)                      |
   | Update strategy | You call methods (`appendChild`, etc.) directly | You update state; framework diffs & batches updates     |
   | Location        | Managed by browser engine, tied to rendering    | Managed by your JS runtime, disconnected from rendering |

---

### TL;DR

By keeping a lightweight copy of the UI in JavaScript memory (the “virtual DOM”), frameworks can compute exactly what needs to change and then make **just those changes** to the real DOM all at once—so you get the power of declarative UI updates without the performance hit of hammering the DOM on every little change.


Virtual DOM -- Reconcilliation + Fibre Tree 
Internal Working of virtual DOM
https://www.youtube.com/watch?v=61R7Py0szPs
