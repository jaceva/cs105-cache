# CS105 Cache Lesson Outline

## Resources
[Wikipedia: CPU Cache](https://en.wikipedia.org/wiki/CPU_cache)

[Computer Architecture: A Quantitative Approach](https://www.elsevier.com/books/computer-architecture/hennessy/978-0-12-383872-8)

[Essentials of Computer Organization and Hardware](https://www.oreilly.com/library/view/essentials-of-computer/9781284123043/)

[Coursera: Computer Architecture - Motivation for Caches](https://www.coursera.org/learn/comparch/lecture/5girw/motivation-for-caches)

## Lesson Description

The goal of this lesson is to explain the motivation of cache and implement a small processor memory system that reveals the benefits of creating a deeper memory hierarchy. The lesson opens by introducing a real-world analogy to cache. The history of processor vs memory performance will help introduce the motivation for an advanced memory hierarchy. 

The lesson will walk through the implementation of a simple cache class in Python. At the end of the lesson the learner will have a working memory hierarchy that is able to moves data from within the memory using replacement policies and associativity. 

## Lesson Code Description

The goal of the lesson checkpoints is to have the learner implement a cache from scratch within an existing register/memory hierarchy. The initial program will consist of a bank of registers and blocks of main memory. A group of commands will exist that repeatedly request data from memory. The timing of the commands can be output to represent the performance of the commands. As the learner implements the cache they will see timing improve as well as the effects of different policy implementations.

## Things to consider
- Combining ex3: Cache Implementation and ex4: Cache Hit might be good since the implementation of the cache class and cache hits may be one and the same.
- It may also be necessary to expand ex6: Replacement Policy and/or ex7: Cache Mapping.
- It is important to not have the limitations of the code guide the exercise content.
- Keeping the program output simple yet informative will be a balancing act
- I didn't include anything on the Principle of Locality. This could change especially in the replacement policy exercise.

## Exercise Overview

- Intro
- Memory Hierarchy
- Cache Memory
- Cache Hit
- Cache Miss
- Replacement Policy
- Cache Mapping
- Cache Write
- Summary

## Exercises In-Depth
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

###	Cache Memory
- NARRATIVE
  - Cache is made up of blocks
  - Cache entries hold data and memory location
  - For a memory request, the processor will check the cache first and will either result in a cache hit or a cache miss. 
- CHECKPOINTS
  - Create a cache class/subclass with smaller memory but faster processing times
  - Link cache class data blocks to memory class data blocks

### Cache Hit ( this could be combined with previous exercise )
- NARRATIVE
  - Cache entries are checked for needed data, if found that's a cache hit.
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
  - Random (or start with the policy implementing in the previous exercise)
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
  - Set associative can be a happy medium. 
- CHECKPOINTS
  - Implement different associativity.

### Cache Write
- NARRATIVE
  - Writes to memory are not common (Hennessy and Patterson, find the figure, not in my book)
  - Still important to create a write policy
  - Write-through
  - Write-back
- CHECKPOINTS
  - Implement write policies.

### Summary
- NARRATIVE
  - Summarize each topic
- CHECKPOINTS
  - Play with the code
  - Create another cache?