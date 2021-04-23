# CS105 Cache Lesson Outline
- Intro
- Memory Hierarchy
- Cache Implementation
- Cache Hit
- Cache Miss
- Replacement Policy
- Cache Mapping
- Cache Write
- Summary

## Lesson Description

The goal of this lesson is to explain the motivation of cache and implement a small processor memory system that reveals the benefits of creating a memory hierarchy. The lesson opens by introducing a real-world analogy to cache. The history of processor speed vs memory speed will help introduce the need to create a memory hierarchy. 

The lesson will walk through the implementation of a simple memory class in Python. This class will be able to represent memory types like registers, all levels of cache and main memory. The class will define a data limit, processing time and possibly a way to display processing time during memory reads and writes.

At the end of the lesson the learner will have a working memory hierarchy that is able to moves data from within the memory using replacement policies and mapping tables. 

## Lesson Code Description

The goal of the lesson is to have the learner implement a cache from scratch to complete an existing register/memory hierarchy. The initial program will consist of a bank of registers and a block of main memory. A group of commands will exist that repeatedly request data from memory. The timing of the commands will measure performance. As the learner implements the cache they will see timing improve as well as the effects of different policy implementations.

## Exercises
### Intro
- NARRATIVE
  - Introduce analogy
    - food analogy (counter/pantry/supermarket)
    - tool analogy (hand/work bench/tool chest) from book
  - Introduce cache using analogy
  - Summarize lesson/exercises
- Instructions
  - Move to the next exercise to get started with Caches

### Memory Hierarchy
- NARRATIVE
  - Processor/memory gap
  - Big memory slow, small memory fast
  - Registers -> Fast but small – Memory -> big but slow
  - Let’s put something in between
- CHECKPOINTS
  1. Explain base code and output, then run code 

###	Cache Description
- NARRATIVE
  - Cache is made up of blocks
  - Cache entries hold data and memory location
  - For a memory request the processor will check the cache first, this will either result in a cache hit or a cache miss. 
- CHECKPOINTS
  - Create a cache class/subclass with smaller memory but faster processing times
  - Link cache class data "blocks" to memory class data "blocks"
### Cache Hit ( this could be combined with previous exercise: i.e. Cache Description with Cache hit )
- NARRATIVE
  - Cache entries are checked for needed data, if found that's a cache hit.
  - 
- CHECKPOINTS
  - Implement a cache hit and transfer data back to register class.
## Cache Miss
- NARRATIVE
  - When the data isn't in the cache it is a cache miss.
  - A new entry is created and the data and memory address are collected
  - Hint at replacement policy by saying for now the cache entries will be replaced using either FIFO or random.
- CHECKPOINTS
  - Implement cache miss functionality in cache class
## Replacement policy
- NARRATIVE
  - Cache is only effective when there is data we can use in it. This is helped with a replacement policy.
  - Random (or whatever was programed in the previous exercise)
  - LRU
  - FIFO
- CHECKPOINTS
  - Implement different replacement policies and compare performance.
### Cache Mapping
- NARRATIVE
  - Deciding where in the cache to store memory locations can affect performance.
  - Fully associative
  - Direct-Mapped
  - Compare and contrast the 2 
  - Set associative
- CHECKPOINTS
  - Implement different association mapping.
### Cache Write
- NARRATIVE
  - Writes to memory are not common (Hennesy and Patterson, find the figure, not in my book)
  - Still important to create a write policy
  - Write-through
  - Write-back
- CHECKPOINTS
### Summary
- NARRATIVE
  - Summarize each topic
- CHECKPOINTS
  - Play with the code
  - Create another cache?
