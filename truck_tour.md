<h1 align="center"> Truck Tour </h1>

### Problem statement

Suppose there is a circle. There are `N`  petrol pumps on that circle. Petrol pumps are numbered `0` to (`N-1`)  (both inclusive). You have two pieces of information corresponding to each of the petrol pump: (1) the amount of petrol that particular petrol pump will give, and (2) the distance from that petrol pump to the next petrol pump.

Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps. Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps. The truck will move one kilometer for each litre of the petrol.

## Input Format
The first line will contain the value of `N`.
The next `N`  lines will contain a pair of integers each, i.e. the amount of petrol that petrol pump will give and the distance between that petrol pump and the next petrol pump.

## Constraints:

$1 \le N \le 10^5$

$1 \le amount\ of\ petrol,\ distance \le 10^9$

## Output format
An integer which will be the smallest index of the petrol pump from which we can start the tour.

## Sample input
```
3
1 5
10 3
3 4
```

## Sample output

```
1
```

## Explaination
We can start the tour from the second petrol pump.


### How to

## Restatement
You need to look for the smallest starting index where the truck can travel a full round.

In order for the truck to move to the next pump, it need to have more amount of petrol then the distance between the two.

## Solution
The solution is simple, just move, collect petrol and check with the distance. If the truck is able to move, then move it, else the truck have to start again with another index.
Let say the Truck choose to start at index I, and is able to move on until index J. At this point (index J), if the Truck is not able to move next, J will be the breaking point and it will be the next point to be considered. There is no use to start from (I+1)

The code is in [petrol_pumps.py](petrol_pumps.py) 




