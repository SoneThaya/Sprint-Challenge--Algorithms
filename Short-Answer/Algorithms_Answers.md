#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
linear time O(n) 

b)
O(n log n) = it loops through all of n, then it has a nested while loop, it doesn't loop through all of n because j is multiplied by 2, it wouldn't be O(n^2)

c)
O(n) linear time - as bunnies grows the amount of recursive calls grows

## Exercise II


***********  answer     ****************************
divide and conquer

find the mid way point of the building. 

drop and egg. if it breaks, go to the down to the middle of the mid way point. drop an egg, if it breaks repeat.

if the egg doesn't break when being dropped, go to the mid way point going up, drop and egg. if it doesn't break repeat process moving up. if it breaks go to mid way point going down then drop.

mid = n // 2
while egg:                # while is not broken, so true
  if drop egg is False:     # if egg breaks
    mid = mid - mid // 2    # go half way down
    drop egg                # keep repeating until egg doesn't break when dropped

  if drop egg is true:      # if egg doesn't break
    mid = mid + mid // 2    # go half way up 
    drop egg                # keep repeating until egg breaks



def binary_search(floors, f):
  low = 0
  high = len(floors) - 1
  mid = 0

  while low <= high:

    mid = (high + low) // 2

    if floor[mid] < f:
       low = mid + 1

    elif floor[mid] > f:
      high = mid - 1

    else:
      return mid

  return -1       # if egg doesn't break at all

run time complexity should be O(log n), splitting the building 