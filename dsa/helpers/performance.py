"""A set of wrapper functions to measure the performance of base functions."""
from time import time


def run_time(function):
    """Measures base function runtime."""
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        finish = time()
        print(f"{function.__name__} took {finish - start} seconds")
        return result
    return wrapper
