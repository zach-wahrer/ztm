from time import time


def performance(function):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        finish_time = time()
        print(f'Function took {finish_time - start_time} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(10**8):
        i * 5


long_time()
