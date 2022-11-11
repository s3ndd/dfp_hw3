"""
Homework 3 Team 7:

Name: Yuling Shi
Andrew ID: yulings
Email: yulings@andrew.cmu.edu

Name: Sheldon Shi
Andrew ID: lijuns
Email: lijuns@andrew.cmu.edu
"""
from typing import List, Tuple
import numpy as np


# File: mystats.py

def is_iter(v):
    """
    check the given parameter v is iterable or not
    :param v: the variable to be checked
    :return: True if the variable is iterable, otherwise, return false
    """
    v_is_iter = True
    try:
        iter(v)
    except:
        v_is_iter = False
    return v_is_iter


def retrieve_arg(*args) -> List:
    """
    retrieve_arg parses the args and combines the args to a list of numbers
    :param args: arguments
    :return: a list of numbers
    """
    numbers = []
    for item in args:
        if is_iter(item):
            numbers.extend([num for num in item])
        else:
            numbers.append(item)

    return numbers


# define the mean function here
def mean(*args) -> float:
    """
    Return the mean of the given data
    If ``args`` is empty, RuntimeError will be raised.
    """
    numbers = retrieve_arg(*args)
    if len(numbers) == 0:
        raise RuntimeError('mean requires at least one number')
    return sum(numbers) / len(numbers)


# define the stddev function here
def stddev(*args) -> float:
    """
    Return the square root of the given data variance.
    If the count of the given data is less than two, RuntimeError will be raised.
    """
    numbers = retrieve_arg(*args)
    if len(numbers) < 2:
        raise RuntimeError('stddev requires at least two numbers')

    _mean = mean(*args)
    _sum = sum([(num - _mean) ** 2 for num in numbers])

    return (_sum / (len(numbers) - 1)) ** 0.5


# define the median function here
def median(*args):
    """
    Return the median (middle value) of the given data.
    In the case of an odd number of args, return the middle point.
    In the case of an odd number of args, the median is interpolated by taking the average of the two middle values:
    If ``args`` is empty, RuntimeError will be raised.
    """
    numbers = retrieve_arg(*args)
    if len(numbers) == 0:
        raise RuntimeError('no median for empty data')

    numbers.sort()
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]


# define the mode function here
def mode(*args) -> Tuple:
    """
    Return the most common number from the given data.
    If *args* is empty, ``mode``, raises RuntimeError.
    """
    numbers = retrieve_arg(*args)
    if len(numbers) == 0:
        raise RuntimeError('no mode for empty data')

    count_dict = dict()
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1

    max_count = max(count_dict.values())
    _mode = tuple([key for key, value in count_dict.items() if value == max_count])

    return _mode


# part 3, b
if __name__ == '__main__':
    # part (a)
    print('The current module is:', __name__)
    # The current module is: __main__

    # part (b)
    print('mean(1) should be 1.0, and is:', mean(1))
    print('mean(1,2,3,4) should be 2.5, and is:', mean(1, 2, 3, 4))
    print('mean(2.4,3.1) should be 2.75, and is:', mean(2.4, 3.1))
    # print('mean() should FAIL:', mean())

    # part (c)
    print('mean([1,1,1,2]) should be 1.25, and is:', mean([1, 1, 1, 2]))
    print('mean((1,), 2, 3, [4,6]) should be 3.2,' +
          'and is:', mean((1,), 2, 3, [4, 6]))

    # part (d)
    for i in range(10):
        print("Draw", i, "from Norm(0,1):", np.random.randn())

    ls50 = [np.random.randn() for i in range(50)]
    print("Mean of", len(ls50), "values from Norm(0,1):", mean(ls50))

    ls10000 = [np.random.randn() for i in range(10000)]
    print("Mean of", len(ls10000), "values from Norm(0,1):", mean(ls10000))

    # part (e)
    seed = 0
    np.random.seed(seed)
    a1 = np.random.randn(10)
    print("a1:", a1)

    print("the mean of a1 is:", mean(a1))

    # part (f)
    print("the stddev of a1 is:", stddev(a1))

    # part (g)
    print("the median of a1 is:", median(a1))
    print("median(3, 1, 5, 9, 2):", median(3, 1, 5, 9, 2))

    # part (h)
    print("mode(1, 2, (1, 3), 3, [1, 3, 4]) is:", mode(1, 2, (1, 3), 3, [1, 3, 4]))
