<h1 align="center"> Simple Text Editor </h1>

### Problem statement

Consider an $n$-integer sequence, $A=\{a_0, a_1,..,a_{n-1}\}$. We perform a query on $A$ using an integer $d$ to calculate the result of the following expression:

$$\begin{align*}
\huge min\     (max\ a_j)\\
\small 0 \le i \le {n-d}\qquad  i \le j \le {i+d}
\end{align*}$$

In other words, if we let $m_i=max{(a_i, a_{i+1}, a_{i+2},..,a_{i+d-1})}$, then you need to calculate $min(m_0,m_1,...,m_{n-d})$.

Given $arr$ and $q$ queries, return a list of answers to each query.

## Example
$arr=[2,3,4,5,6]$

$queries=[2,3]$

The first query uses all the subarrays of length 2:$[2,3],[3,4],[4,5],[5,6]$. The maxima of the subarrays are $[3,4,5,6]$. The minimum of these is $3$.

The second query uses all the subarrays of length 3:$[2,3,4],[3,4,5],[4,5,6]$. The maxima of the subarrays are $[4,5,6]$. The minimum of these is $4$.

Return $[4,5]$

## Function description
Complete the solve function below.

solve has the following parameters:
- int arr[n]: an array of integers
- int queries[q]: the lengths of subarrays to query

## Returns
- int[q]: the answers to each query

## Input format
The first line consists of two space-separated integers,$n$ and $q$ .
The second line consists of $n$ space-separated integers, the elements of $arr$.
Each of the $q$ subsequent lines contains a single integer denoting the value of $d$ for that query.

## Constraints
- $1 \le n \le 10^5$
- $0 \le arr[i] \lt 10^6$
- $1 \le q \le 100$
- $1 \le d \le n$

## Sample Input 0
```
5 5
33 11 44 11 55
1
2
3
4
5
```

## Sample Output 0
```
11
33
44
44
55
```

## Sample Input 1
```
5 5
1 2 3 4 5
1
2
3
4
5
```

## Sample Output 1
```
1
2
3
4
5
```

### Solution
The gist of an efficient solution is to use the smaller Maxima to reduce the calculation time of the bigger Maxima.

For example 
- Max4 = Max (1,3,2,4)
- Max5 = Max (1,3,2,4,6) = Max (Max4, 6)

The implementation is describled as the following steps
1. Sort the $queries$ input ascending, so we can utilize the `smaller Maxima` to calculate `bigger Maxima`
2. Calculate the first smallest query, result will be stored in `max_arr[0]`. The array `max_arr` will be used to store subsequent maxima value according to each query.

Move on to the subsequent query in step `#3`
3. For each query `q`, we try to use the previous smaller query to calculate the equivalent maxima.
4. The we draw the answer from the `max_arr` which contains all the max value of each query.

The implementation is in [query_fixed_length](query_fixed_length.py)