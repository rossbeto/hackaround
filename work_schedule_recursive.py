

class WorkScheduleRecursive:
    def __init__(self, work_hours, day_hours, pattern):
        self.input_work_hours = work_hours
        self.input_day_hours = day_hours
        self.input_pattern = pattern
    
    @property
    def work_days(self):
        work_days = []
        for i, c in enumerate(self.input_pattern):
            if c == '?':
                work_days.append(i)
        return work_days
    
    @property
    def current_work_hours(self):
        current_work_hours = 0
        for i, w in enumerate(self.input_pattern):
            if w != '?':
                current_work_hours += int(w)
        return current_work_hours
    
    @property
    def remaining_work_hours(self):
        return self.input_work_hours - self.current_work_hours
    
    @property
    def number_of_work_days(self):
        return len(self.work_days)
    
    def print_schedule(self, result):
        schedule = ''
        i = 0
        for c in self.input_pattern:
            if c == '?':
                schedule += str(result[i])
                i += 1
            else:
                schedule += c
        print(schedule)

    def get_min_work_hours_per_index(self, index, already_distributed_work_hours, remaining_work_hours):
        max_possible_work_hours = (self.number_of_work_days - index - 1) * self.input_day_hours
        # print(max_possible_work_hours)
        if remaining_work_hours >= max_possible_work_hours:
            min_work_hours = remaining_work_hours - max_possible_work_hours
        else:
            min_work_hours = 0

        return min_work_hours
    
    # note: dynamic recursive method
    # at each step, adjust the range(min_work_hours, min_top+1) base on the : number_of_day that have not been assigned a value
    # and the remaining_work_hours( that have not been distributed)
    # for each schedule, at the last number(index+1==number_of_work_days), 
    # remaining_work_hours must be <= input_day_hours ( mean that the number of hours that will be distributed to the last position should fit in that day)
    def distribute(self, index, min_work_hours, remaining_work_hours, result):
        # print(f'index:{index}')
        min_top = min(remaining_work_hours, self.input_day_hours)
        # print(f'min_top:{min_top}| remaining_work_hours:{remaining_work_hours}')
        for wh in range(min_work_hours, min_top+1):
            new_result = result.copy()
            new_result.append(wh)
            # print(f'new_result:{new_result}')
            if (index+1 == self.number_of_work_days):
                # print result
                self.print_schedule(new_result)
                return
            else:
                new_index = index + 1
                already_distributed_work_hours = sum(new_result)
                new_remaining_work_hours = remaining_work_hours - wh
                new_min_work_hours = self.get_min_work_hours_per_index(
                    index=new_index, 
                    already_distributed_work_hours=already_distributed_work_hours, 
                    remaining_work_hours=new_remaining_work_hours)
                # print(f'new_min_work_hours:{new_min_work_hours}')

                self.distribute(
                    index=new_index, 
                    min_work_hours=new_min_work_hours,
                    remaining_work_hours=new_remaining_work_hours,
                    result=new_result)



def findSchedules(work_hours, day_hours, pattern):
    work_schedule = WorkScheduleRecursive(work_hours, day_hours, pattern)
    remaining_work_hours = work_schedule.remaining_work_hours
    min_work_hours = work_schedule.get_min_work_hours_per_index(
        index=0, 
        already_distributed_work_hours=0, 
        remaining_work_hours=remaining_work_hours
    )
    result = list()
    work_schedule.distribute(
        index=0,
        min_work_hours=min_work_hours,
        remaining_work_hours=remaining_work_hours,
        result=result
    )


def test_data():
    return [
        # (24, 4, '08??840'),
        # (56, 8, '???8???'),
        (24, 4, '4????84')
    ]

def main():
    for suite in test_data():
        work_hours, day_hours, pattern = suite
        print(f'---{work_hours}-{day_hours}-{pattern}---')
        findSchedules(work_hours, day_hours, pattern)
        print('--------------')

    # work_hours = 24
    # day_hours = 4
    # pattern = '08??840'
# [0, 4]
# [1, 3]
# [2, 2]
# [3, 1]
# [4, 0]
    # work_hours = 56
    # day_hours = 8
    # pattern = '???8???'

    # findSchedules(work_hours, day_hours, pattern)
    

if __name__ == '__main__':
    main()