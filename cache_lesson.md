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

This is a lesson on CPU Cache memory so why are you gardening. The fertilizer, its location and what it means to spend time to retrieve and store it in the shed is a good example of a computer memory hierarchy. In the following exercises we will explore how minimize the delay in processing when access data from memory by introducing you to _Cache memory_. Just like the shed in our gardening example. Cache memory is a place we can keep data to access faster, so we don't have to wait for the main memory.

### Instructions
**CP1**
Move to the next exercise to get started with Caches

## Exercise 2: Memory Hierarchy

### Narrative
- Processor/memory gap
- Big memory slow, small memory fast
- Registers -> Fast but small – Memory -> big but slow
- Let’s put something in between

EDIT: Reference hierarchy of garden shed store.

So what is a memory hierarchy? To answer this lets first look at why we need a memory hierarchy. The graph below shows the progression of the CPU-Memory performance gap or the rate of increase in CPU performance is much bigger than that of computer memory. What this means is that modern day processors are much faster than memory.

![Performance gap of processors and memory](pm_gap.png)

In the gardening example work was smooth when you were digging the holes because you had everything you needed. The work only slowed down when you needed to go to the shed or gardening store for supplies you don't have. 

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

## Exercise

### Narrative

### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

## Exercise

### Narrative

### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

## Exercise

### Narrative

### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

## Exercise

### Narrative

### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

## Exercise

### Narrative

### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

## Exercise

### Narrative

### Checkpoints
**CP1**

**Hint**

**CP2**

**Hint**

**CP3**

**Hint**

**CP4**

**Hint**

