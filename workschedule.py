
# range(1,3): 1, 2 ( 3 is exclusive)


def findSchedules(work_hours, day_hours, pattern):
    #1. input sanitize
    work_days = get_must_work_days(pattern)
    # print(work_days)
    current_work_hours = get_current_work_hours(pattern)
    # print(current_work_hours)
    remaining_work_hours = work_hours - current_work_hours
    # print(remaining_work_hours)
    number_of_work_days = len(work_days)
    # print(f'number_of_work_days:{number_of_work_days}')

    max_work_outs = day_hours * len(work_days)
    # print(max_work_outs)
    # if max_work_outs == remaining_work_hours:
    #     print('only one possible distribution')
    #     pass

    #2. initial data
    index = 0
    min_work_hours = get_min_work_hours_per_index(
                index=0, 
                number_of_work_days=number_of_work_days, 
                already_distributed_work_hours=0, 
                remaining_work_hours=remaining_work_hours, 
                day_hours=day_hours)
    # print(min_work_hours)

    # min_work_hours = get_min_work_hours_per_index(0, number_of_work_days, 0, 4, day_hours)
    # print(min_work_hours)

    # for i in range(min_work_hours, number_of_work_days):
    #     print(i)

    # test()
    # return

    result = list()
    distribute(
        index=0,
        number_of_work_days=number_of_work_days,
        min_work_hours=min_work_hours,
        remaining_work_hours=remaining_work_hours,
        day_hours=day_hours,
        result=result
    )

    pass

def test():
    print('est')
    for i in range(1,4):
        print(i)

def distribute(index, number_of_work_days, min_work_hours, remaining_work_hours, day_hours, result):
    # print(f'index:{index}')
    min_top = min(remaining_work_hours, day_hours)
    # print(f'min_top:{min_top}| remaining_work_hours:{remaining_work_hours}')
    for wh in range(min_work_hours, min_top+1):
        new_result = result.copy()
        new_result.append(wh)
        # print(f'new_result:{new_result}')
        # 4.1 print the result
        if (index+1 == number_of_work_days):
            # print result
            print(new_result)
            return
        else:
            #4.2 recalculate the new constraints
            new_index = index + 1
            already_distributed_work_hours = sum(new_result)
            new_remaining_work_hours = remaining_work_hours - wh
            new_min_work_hours = get_min_work_hours_per_index(
                index=new_index, 
                number_of_work_days=number_of_work_days, 
                already_distributed_work_hours=already_distributed_work_hours, 
                remaining_work_hours=new_remaining_work_hours, 
                day_hours=day_hours)
            # print(f'new_min_work_hours:{new_min_work_hours}')

            distribute(
                index=new_index, 
                number_of_work_days=number_of_work_days, 
                min_work_hours=new_min_work_hours,
                remaining_work_hours=new_remaining_work_hours,
                day_hours=day_hours,
                result=new_result)


def get_must_work_days(pattern):
    work_days = []
    for i, c in enumerate(pattern):
        if c == '?':
            work_days.append(i)
    return work_days


def get_current_work_hours(pattern):
    current_work_hours = 0
    for i, w in enumerate(pattern):
        if w != '?':
            current_work_hours += int(w)
    return current_work_hours


# index is zero base
def get_min_work_hours_per_index(index, number_of_work_days, already_distributed_work_hours, remaining_work_hours, day_hours):
    left_over = remaining_work_hours - already_distributed_work_hours
    # print(left_over)
    max_possible_work_hours = (number_of_work_days - index - 1) * day_hours
    # print(max_possible_work_hours)
    if remaining_work_hours >= max_possible_work_hours:
        min_work_hours = remaining_work_hours - max_possible_work_hours
    else:
        min_work_hours = 0

    return min_work_hours

def get_max_work_hours_per_index(index, number_of_work_days, already_distributed_work_hours, remaining_work_hours, day_hours):
    pass


def main():
    work_hours = 24
    day_hours = 4
    pattern = '08??840'
# [0, 4]
# [1, 3]
# [2, 2]
# [3, 1]
# [4, 0]
    # work_hours = 56
    # day_hours = 8
    # pattern = '???8???'

    findSchedules(work_hours, day_hours, pattern)
    

if __name__ == '__main__':
    main()