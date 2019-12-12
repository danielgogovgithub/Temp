import time
import random

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("'{}' was running for: {} seconds".format(func.__name__, time.time() - start))
        return result
    return wrapper

@timeit
def time_waster(wait_seconds):
    time.sleep(wait_seconds)
    return "Done"

@timeit
def other_time_waster():
    return

def measured_time_waster():
    print("Start")
    start = time.time()
    time_waster(1)
    print("End", round(time.time()-start, 2))

if __name__ == '__main__':
    measured_time_waster()
    measured_time_waster()