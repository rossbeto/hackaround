# https://www.hackerrank.com/challenges/queries-with-fixed-length/problem?isFullScreen=true

import math
import os
import re
import random
import sys



def solve(arr, queries):
    # max_a 2d array to contain max value of each query
    # at the end, get min value of each max_a[q] where q is value from queries array
    # first, we can sort and make the array unique

    # queries = list(set(queries))
    # print(queries)

    n = len(arr)
    q = len(queries)
    # print(q)
    # sorted_arr = sorted(arr)
    # print(sorted_arr)
    # print(arr)

    max_a = [[] for i in range(q)]
    # print(max_a)
    for i in range(n):
        for j in range(q):
            d = queries[j]
            if d + i <= n:
                max_di = max(arr[i:i+d])
                max_a[j].append(max_di)
    
    print(max_a)
    result = []
    for i in range(q):
        min_q = min(max_a[i])
        result.append(min_q)
    
    return result

def solve2(arr, queries):
    # the idea is to use the previous MAX calculation to reduce the work load on the next calculation
    # position 0, d =5 : max(0+5) = max(0+4) and arr[5]
    # so to calculate MAX5 we can use MAX4
    # print(f'arr:{arr}')
    sorted_queries = sorted(queries)
    # print(f'sorted_queries:{sorted_queries}')
    n = len(arr)
    q = len(queries)

    max_a_sorted = [[] for i in range(q)]

    if q == 0:
        return []
    d0 = sorted_queries[0]
    for j in range(n):
        if d0 + j <= n:
            max_dj = max(arr[j:j+d0])
            max_a_sorted[0].append(max_dj)
    
    # print(f'max_a_i:{max_a_sorted[0]}')
    
    
    for i in range(1,q):
        prev_d = sorted_queries[i-1]
        d = sorted_queries[i]
        if d == prev_d:
            max_a_sorted[i] = max_a_sorted[i-1]
            # print(f'max_a_i.equal:{max_a_sorted[i]}')
            continue

        # FOR each position_j, we can use the prev_d of the previous iteration
        # and we can also use (position_j-1)
        # MAX(position_j) : MAX(position_j-1) and arr[position_j]
        # if MAX_J == arr[position_j-1]: mean that we have to recalculate MAX_J ( since MAX_j-1 happened to be the max element)
        for j in range(n):
            if d + j <= n:
                if j>0:
                    prev_max_dj = max_a_sorted[i][j-1]
                    # use prev_max_dj to reduce the calculation
                    # however, this is not exact since prev_max_dj include arr[j-1]
                    # if max_dj_temp == arr[j-1] means that we max_dj_temp is not correct, and need to be recalculate
                    # in case max_dj_temp != arr[j-1] means that: we can use this max_dj_temp since the MAX element is not arr[j-1]
                    max_dj_temp = max(prev_max_dj, arr[j+d-1])

                    # this mean we need to recalculate max_dj because arr[j-1] is not the one that should participate in this set ( at position_j)
                    if max_dj_temp != arr[j-1] or arr[j-1] == arr[j+d-1]:
                        max_a_sorted[i].append(max_dj_temp)
                        continue

                # diff = d - sorted_queries[i-1]
                # if we reach here, mean that we cannot use max_dj_temp (because arr[j-1] is the MAX element)
                # so we will use max_a_sorted[i-1][j] -> the previous max calculation at the same position_j ( but with a smaller d query value)
                max_dj = max(arr[j+prev_d-1:j+d])
                # print(f'max_a_sorted[i-1][j]:{max_a_sorted[i-1][j]}|max_dj:{max_dj}')
                max_dj = max(max_a_sorted[i-1][j], max_dj)
                max_a_sorted[i].append(max_dj)
        
        # print(f'max_a_i:{max_a_sorted[i]}')

    result = []
    for i in range(q):
        for j in range(q):
            if queries[i] == sorted_queries[j]:
                min_q = min(max_a_sorted[j])
                result.append(min_q)
                break
    
    return result

    
# d: mean that there is surely d-1 smallest elements will be out
# and maximum : min((d-1)*2, n-1) elements will be out
# why n-1: there is always a Max element ( in an array of n element)
# why (d-1)*2 : an element X, if its position is 'central enough' will participate in [aaaaX] and [Xbbbb] ( X is the Max element in those two set, and 'aaaa' 'bbbb' will be out)
# so the possible elements that will be wipe out are [d-1,min((d-1)*2, n-1)]
# therefore, from sorted_arr, we can check those element in position [d, min((d-1)*2, n-1)]
# for those element in sorted_arr from position [d, min((d-1)*2, n-1)]
# looping through the original arr, if element == sorted_arr[i] => do some calculation
# calculation: go back from [i-d+1] to [i] to i[i+d-1] => check if we should include i

# FOR A specific number at position i
# [i-d+1:i+d-1]: if number[i] is not the max

def read_input(input_file_path):
    input_file = open(input_file_path, "r")

    input_data = input_file.readlines()

    first_multiple_input = input_data[0].rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])
    # print(f'n:{n}|q:{q}')

    arr = list(map(int, input_data[1].rstrip().split()))

    queries = []

    for j in range(q):
        queries_item = int(input_data[j+2].strip())
        queries.append(queries_item)
    # print(f'queries:{queries}')
    input_file.close()

    result = solve2(arr, queries)
    return result

def read_output(output_file_path):
    output_file = open(output_file_path, "r")

    expected_result = []
    output_data = output_file.readlines()
    q = len(output_data)
    for j in range(q):
        r_item = int(output_data[j].rstrip())
        expected_result.append(r_item)

    output_file.close()

    return expected_result

def compare_result(result, expected_result):
    if len(result) != len(expected_result):
        print(f'Wrong.len(result):{len(result)}| len(expected_result):{len(expected_result)}')
        return False
    for i in range(len(result)):
        if result[i] != expected_result[i]:
            print(f'Wrong at:{i}|result[i]:{result[i]}|expected_result[i]:{expected_result[i]}')
            return False

    return True
    

def main():
    arr = [33,11,44,11,55]
    # arr = [33,11,11,44,55]
    queries = [1,2,3,4,5]
    # result = solve(arr, queries)
    # print(result)
    arr = [33,11,44,11,55]
    queries = [1,5,4,2,3,1,1,2]
    # queries = []
    result = solve2(arr, queries)
    print(result)

    # result = read_input('.\\data\\input09.txt')
    # print(result)
    # expected_result = read_output('.\\data\\output09.txt')
    # comp = compare_result(result, expected_result)
    # print(comp)


if __name__ == '__main__':
    main()