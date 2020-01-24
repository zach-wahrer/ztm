from time import time

times = []


def performance(function):
    def wrapper(*args, **kwargs):
        start = time()
        run = function(*args, **kwargs)
        finish = time()
        times.append(f"{function.__name__} took {(finish - start):.10f}")
        return run
    return wrapper


@performance
def fib(to_index_number):
    yield 0
    yield 1
    if to_index_number > 1:
        f0 = 0
        f1 = 1
    for i in range(1, to_index_number):
        yield f0 + f1
        temp = f1 + f0
        f0 = f1
        f1 = temp


fib(1000000)


@performance
def fib_to_list(to_index_number):
    fib_list = [0]
    f0 = 0
    f1 = 1
    for i in range(1, to_index_number):
        fib_list.append(f0 + f1)
        temp = f1 + f0
        f0 = f1
        f1 = temp
    return fib_list


fib_to_list(100000)

for result in times:
    print(result)
