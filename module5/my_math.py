import statistics


def calc_min(lst):
    min_count = min(lst)
    return print(min_count)


def calc_max(lst):
    max_count = max(lst)
    return print(max_count)


def calc_middle(lst):
    count_min = statistics.mean(lst)
    return print(count_min)


def cal_median(lst):
    count_median = statistics.median(lst)
    return print(count_median)


def cal_pstdev(lst):
    count_pstdev = statistics.pstdev(lst)
    return print(count_pstdev)
