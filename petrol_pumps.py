
# https://www.hackerrank.com/challenges/truck-tour/problem?isFullScreen=true
def truckTour(petrolpumps):
    n = len(petrolpumps)
    acc_arr = [0]*len(petrolpumps)

    # print(f'n={n}')
    # print(f'petrolpumps={petrolpumps}')

    prev_starting_point = -1
    i = 0
    while i < n:
        # print(f'round_i:{i}')
        row = petrolpumps[i]
        amount = row[0]
        distance = row[1]

        # look for a possible starting point
        if amount >= distance:
            # first starting point or a new starting point

            # if there is a previously starting point, try to calculate the new one base on the previous one
            # if prev_starting_point != -1:
            #     prev_balance = 0
            #     if i>0:
            #         prev_balance = acc_arr[i-1]

            #     acc_arr[prev_breaking_point] += (amount - distance) - prev_balance
            #     j = prev_breaking_point + 1
            # else:
            #     acc_arr[i] = amount - distance
            #     j = i + 1
            
            acc_arr[i] = amount - distance
            j = i + 1
            while j < n + i:
                real_j = get_real_index(j, n)
                row_j = petrolpumps[real_j]
                amount = row_j[0]
                distance = row_j[1]
                acc_arr[real_j] = acc_arr[real_j-1] + (amount - distance)
                if acc_arr[real_j] < 0:
                    # cannot move on - starting from i is not a good choice
                    # prev_starting_point = i
                    prev_breaking_point = real_j
                    i = real_j
                    # print('break here')
                    # break out of the inner loop(while j < n+1) => then increase i = i +1 to continue the next loop
                    # why: because real_j is the point that will surely break if i < real_j - and this is also the place to boost performance ( skip unncessary loop)
                    break
                j += 1
            
            # found solution - i
            # print(f'j:{j}|i:{i}')
            if j == n + i:
                return i

        i += 1


def get_real_index(index, n):
    return (index) % n

def main():
    petrolpumps = [
        [1,5],
        [10,3],
        [3,4]
    ]

    petrolpumps = [
        [1,5],
        [1,4],
        [3,3],
        [20,4]
    ]

    i = truckTour(petrolpumps)
    print(i)


if __name__ == '__main__':
    main()