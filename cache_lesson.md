# Cache - Lesson Draft 

## Exercise 1: Introduction
### Narrative
- Introduce analogy
  - food analogy (counter/pantry/supermarket)
  - tool analogy (hand/work bench/tool chest) from book
  - garden (supplies at garden/supplies in shed/supplies from gardener)
- Introduce cache using analogy
- Summarize lesson/exercises

It's a nice day out today and you have decided to work in your garden. You have with you a pair of gloves, a shovel and flowers in pots. You mark out the perfect spots for each flower and start to dig the holes. After digging the holes you realize you want to use a special fertilizer for the garden. You don't have the fertilizer so you go to the garden store to pick some up. 

Getting the fertilizer from the store takes some time since you have to take the bus then find the fertilizer in the many aisles in the store. Once you find the fertilizer in the store you decide to buy extra to keep in your backyard shed. This way if you need fertilizer for your next project you'll have it and only have to get it from the shed. When you get back to your garden you use the fertilizer plant the flowers and enjoy a job well done.

This is a lesson on CPU Cache memory so why are you gardening. The fertilizer, its location and what it means to spend time to retrieve and store it in the shed is a good example of how a computer accesses memory. In the following exercises we will explore how minimize the delay in processing when access data from memory by introducing you to _Cache memory_. Just like the shed in our gardening example Cache memory is a place we can keep something we need to retrieve faster. By introducing cache in between the cpu and main memory, we are creating what is known as a _memory hierarchy_.

### Instructions
**CP1**
Move to the next exercise to get started with Caches

## Exercise 2: Memory Hierarchy

### Narrative
- Processor/memory gap
- Big memory slow, small memory fast
- Registers -> Fast but small – Memory -> big but slow
- Let’s put something in between


So what is a memory hierarchy and why is it important? Let's answer the second part of that question by looking at the graph below. 

![Performance gap of processors and memory](pm_gap.png)

There are two lines, one for processor performance and one for memory performance. As time passes, processor performance increases at a much higher rate than that of memory. This results in a computer that can process data much faster than it can retrieve data from memory. This is known as the processor-memory performance gap and is the motivation behind creating a memory hierarchy.

The gardening example from the previous exercise had you working in your garden until you needed to stop to get fertilizer from the store. The garden and the few tools you have are equivalent to the processor and data in the registers. Retrieving the fertilizer from the store is the same as retrieving data from memory. It's a slow process, but everything you need is there and you can get to both by bus ;-).

![Simple Memory Hierarchy](mem_hier.png)

The image above represents a simple memory hierarchy. At the top is the processor (your garden) with the best performance but can only hold a small amount of data. At the bottom is memory (the garden store) with the decrease performance but increased size. This memory is the DRAM/SDRAM/DDR memory used widely in computers today. Throughout this lesson we will refer to it as main memory. 

The middle section of the memory hierarchy is cache and is equivalent to your storage shed where the extra fertilizer you brought home is stored. Cache memory is what we will cover for the rest of this lesson by showing how it helps bridge the processor memory performance gap.

### Checkpoints
**CP1**


- Explain the code to be used for the lesson.
- Run the code, notice the memory can't be found.

Throughout this lesson you will be working with a small memory hierarchy that outputs a string by bringing characters from memory. 


**Hint**

**CP2**

- 
- Ask the learner to configure the architecture to use main memory.
- (NO?)Call the architecture `read_code()` method with `"code.txt"` as the argument.
- Run code, explain output.

## Exercise 3: Cache Memory

### Narrative
- Cache is made up of blocks
- Cache entries hold data and memory location
- For a memory request, the processor will check the cache first and will either result in a cache hit or a cache miss.
- A cache hit is what increases bridges the performance gap.
- Cache entries are checked for needed data, if found that's a cache hit.

Cache memory can hold more data than the processor but less than main memory. Its size means data retrieval is slower than within the processor but is faster than from main memory. Cache memory performance and size is a compromise between the processor and main memory. But this isn't what helps bridge the performance gap. The structure and the behavior of cache is what leads to increased data retrieval.

Cache is made up of _blocks_ equal in size. Each block stores a copy of data from main memory. Unlike memory, cache blocks are not assigned addresses. When a piece of data is stored in cache, it is paired with a _tag_ which is equal to the address of the data in main memory. This simplifies retrieval since the processor uses the same address when accessing data from cache and main memory.

![A cache with 2 blocks filled](cache.png)

The diagram above represents a small cache with 4 blocks. The cache has two elements of data from main memory: the character `'Q'` with a tag `15` and the character `'c'` with a tag `2`. Remember the tag is the main memory address of the data. When the processor requests data from a main memory address it will first search for that address in the cache. If any of the blocks has a tag with the requested address a _cache hit_ occurs.

![A cache hit](cache_hit_gif.png)

In the animation there is a processor, main memory with a cache in the middle. The processor requests the data located at main memory address `2`. The address is found inside the cache so a cache hit occurs. The character `'c'` will be returned from cache and the main memory is never accessed. The goal of the memory hierarchy is to get as many cache hits when requesting data from memory.

### Checkpoints
**CP1**
- Introduce Cache class (already implemented with `MainMemory` as next tier and `size` set)
- Learner will add the memory block variable(s)

**Hint**

**CP2**
- Create a class function `read()`.
- Inside the function call the parent class `read()` function using `super()` and place the return value in a variable called `byte`.
- return byte 

**Hint**

**CP3**

- In **app.py** create an instance of `Cache()` and put it in the variable `cache_memory` 
- Change memory of architecture to `cache_memory`

Run the code. Out put will be the same since `Cache()` is just a pass through for now.

**Hint**


## Exercise 4: Cache Miss

### Narrative
- When the data isn't in the cache it is a cache miss.
- A new entry is created and the data and memory address are collected
- Hint at replacement policy by saying for now the cache entries will be replaced using either FIFO or random.

When the data requested from the processor isn't in cache, a _cache miss_ occurs. 

![A cache miss](cache_miss_gif.png)

In the above animation of a cache miss, the data request first goes to the cache. A cache mis occurs and the request goes to main memory. The memory address and retrieved data will then be placed in cache. Finally, the processor will finish the request by retrieving the data from the cache.

A cache miss is what populates data in the cache. But since cache has a quicker access time than main memory a cache hit is preferable to a cache miss. The goal of the cache is to keep the data that will result in the most cache hits and limit the cache misses.

### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

## Exercise 5: Replacement Policy (Possibly Expand to 2 exercises)

### Narrative
- Cache is only effective when there is data we can use in it. This is helped with a replacement policy.
- Random (or start with the policy implementing in the previous exercise)
- LRU
- FIFO

In the previous exercise, we looked at a half empty cache and added entries to that. But what happens when the cache is full and a cache miss occurs? The incoming data will need to replace an existing data entry in the cache, but which data entry?

The decision about which populated entry will be replaced with new data is made by the cache's _replacement policy_. A replacement policy might use information about each cache entry in order decide which to replace. This approach comes at a cost of collecting and processing the information on each entry. Here are some examples of replacement policies:
- First In First Out (FIFO): known also as round robin, this policy replaces the entries in the order that they came in to the cache. An index is maintained that points to the next entry to be replaced. After replacement, the index is incremented or set back to the first entry if the last entry was just replaced.
- Least Recently Used (LRU): this policy replaces the with the most time passed since it was last accessed. This requires that each entry have a way to keep track of when it was last accessed compared to the other entries. 
- Random Replacement: this policy chooses a cache entry at random. While there is some work involved in this policy the cost tends to be less than both the FIFO and LRU policies.

The correct replacement policy is key to increasing the number of cache hits a processor has. The random replacement policy is simple to implement but might cause more cache hits than the other 2 policies. The LRU policy is more complicated but does a better job at keeping data in the cache that will be used again. In fact, the LRU policy has been expanded to multiple policies that look at an entries "age" as a way to decide which one to replace. 
  
### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

## Exercise 6: Cache Mapping

### Narrative
- Deciding where in the cache to store memory locations can affect performance.
- Fully associative
- Direct-Mapped
- Compare and contrast the 2 
- Set associative can be a happy medium. 



### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

## Exercise 7: Cache Write

### Narrative
- Writes to memory are not common (Hennessy and Patterson, find the figure, not in my book)
- Still important to create a write policy
- Write-through
- Write-back
  
### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

## Exercise 8: Summary

### Narrative
- Summarize each topic

### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

