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


So what is a memory hierarchy and why is it important? Let's answer the second part of that question by looking at the graph below. There are two lines, one for CPU speed and one for memory speed. Over time processor speed has greatly outpaced that of memory. Where it stands now is that a computer's processor can process data many times faster than data can be retrieved from memory. This is known as the processor-memory gap and is the main motivation behind creating a memory hierarchy.

![Performance gap of processors and memory](pm_gap.png)

( Do i want to continue referencing the gardening example here? )

The idea behind a memory hierarchy is for a processor to be able to access data from the fastest possible source, starting with its internal registers. If the data it needs is not in the registers it should go to the next level of memory. For a time the next level was large memory such as DRAM. The increasing performance gap between the CPU and memory motivated another. Giving the CPU access to memory that is faster and smaller in size than DRAM is where cache memory comes in.

Data in a processor's registers is accessed very fast because the registers are 



When a computer processor has all the data it needs it is able to work fast, moving data in and out of registers and relying on a pipeline to get close to one instruction processed per cycle. 

When the processor needs data from memory, just like walking to the shed or going to the garden store, the process slows down a lot. Retrieving data from memory is a very slow process compared to speedy work of a processor. In fact, the speed improvements of processors has drastically outpaced the improvements of memory speed.

![Performance gap of processors and memory](pm_gap.png)

The above chart shows that the rate of performance improvement of processors is much greater than that of memory. This is mostly due to the size of the memory in each case. The memory in a processor is small and local so it should take very little time to access. Computer memory like DRAM continues to grow in size and has always lived far away from the processor. The time for the data to be found and sent back to the processor can only improve so much as memory gets bigger.

The next several exercises are going to introduce Cache memory. This memory unit placed in between the processor and the standard memory to store 

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

Cache is small fast memory located close to the CPU. It is used to hold copies of data from main memery it thinks it may use soon. Instead of taking the time to retrieve the data from main memory, it can retrieve it from the faster cache memory.

Cache is made up of _blocks_ that are fixed in size. 

In order for cache memory help bridge the processor/memory performance gap, certain rules need to exist that ensures useful data is stored with in the memory blocks.
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

### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

## Exercise 5: Cache Hit

### Narrative
- A cache hit is what increases bridges the performance gap.
- Cache entries are checked for needed data, if found that's a cache hit.
  
### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

## Exercise 6: Replacement Policy (Possibly Expand to 2 exercises)

### Narrative
- Cache is only effective when there is data we can use in it. This is helped with a replacement policy.
- Random (or start with the policy implementing in the previous exercise)
- LRU
- FIFO
  
### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

## Exercise 7: Cache Mapping

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

## Exercise 8: Cache Write

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

## Exercise 9: Summary

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

