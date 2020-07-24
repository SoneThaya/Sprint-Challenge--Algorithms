# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
linear time O(n) - as n gets larger time is linear

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
O(n log n) = it loops through all of n, then it has a nested while loop, it doesn't loop through all of n because j is multiplied by 2, it wouldn't be O(n^2)

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
O(n) linear time - as bunnies grows the amount of recursive calls grows

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

***********  answer     ****************************
divide and conquer

find the mid way point of the building. 

drop and egg. if it breaks, go to the down to the middle of the mid way point. drop an egg, if it breaks repeat.

if the egg doesn't break when being dropped, go to the mid way point going up, drop and egg. if it doesn't break repeat process moving up. if it breaks go to mid way point going down then drop.



run time complexity should be O(log n), splitting the building 