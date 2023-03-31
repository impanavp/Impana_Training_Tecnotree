# Write a Python program that defines a decorator to measure the time taken by a function to execute. 

import time

def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print("Time taken by fibonacci: " , end_time - start_time , " seconds")
        return result
    return wrapper

@timer_decorator
def fibonacci():
    n1, n2 = 0, 1
    count = 0
    while count < 40:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

fibonacci()
