# Cache - Lesson Draft 

## Exercise 1: Introduction
### Narrative
- Introduce analogy
  - food analogy (counter/pantry/supermarket)
  - tool analogy (hand/work bench/tool chest) from book
  - garden (supplies at garden/supplies in shed/supplies from gardener)
- Introduce cache using analogy
- Summarize lesson/exercises

Its a nice day out today and you are going to work in your garden. You have with you a pair of work gloves, a shovel and flowers in pots. You mark out the perfect spots for each flower and start to dig the holes. 

After digging a couple holes you realize you have special fertilizer for these flowers in your shed. You stop what you're doing, put your shovel down and walk to the shed to get the fertilizer. It's not a long walk to the shed but you are excited about getting the flowers in the ground and want to get back to gardening. 

You get the fertilizer, walk back to the garden and begin digging again. When digging the third hole you hit an old root from a tree and can no longer dig. In order to plant the flower in that spot you'll need a large pruner to remove the root. You don't have the tool with you or in your shed so decide to go to your local gardening store. 

This takes a longer than walking to the shed since the store is all the way on the other side of town and you have to take the bus. Once you get there you buy the tool and some more fertilizer in case you need more. You head home, remove the root, and continue with the gardening.

This is a lesson on CPU Cache memory so why are we gardening. The supplies, their locations and what it means to spend time to retrieve them can be directly mapped to common computer processor memory hierarchies. Creating a balance between having what we can store to complete a process and spending the least amount of time to retrieve the rest what we will explore in this lesson.

### Instructions
**CP1**
Move to the next exercise to get started with Caches

## Exercise 2: Memory Hierarchy

### Narrative
- Processor/memory gap
- Big memory slow, small memory fast
- Registers -> Fast but small – Memory -> big but slow
- Let’s put something in between
### Checkpoints
**CP1**
- Explain the code to be used for the lesson.
- Ask the learner to configure the architecture to use main memory.
- Run the code

**Hint**

**CP2**

- Call the architecture `read_code()` method with `"code.txt"` as the argument.
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

