<h1 align="center"> Simple Text Editor </h1>

### Problem statement
https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

### Solution
Each layer of the input two-dimentional matrix can be peeled off and converted into a single-dimentional matrix.
The task is to move all those single-dimentional matrixes in an anti-clock wise direction, at each movement, the elements will be shifted one step ahead.
The main point will be to identify all elements that belong to the same virtual single-dimentional matrix ( from the two-dimentional matrix) then make the movement.
For each virtual single-dimentional matrix, let say the size of it is `n`, after `n` movements all the elements of the matrix will be the same as before. It means that given a `distance`, the real movement that we need to calculate is just `distance mod n`.

Implementation is in [matrix_rotation_algo](matrix_rotation_algo.py)