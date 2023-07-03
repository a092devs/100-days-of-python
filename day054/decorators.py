import time

def speed_calc_decorator(function):
    def wrapper_fucntion():
        start_time = time.time()
        function()
        end_time = time.time()
        duration = end_time - start_time
        function_name = function.__name__
        print(f"{function_name} took {duration:.2f} seconds")
    return wrapper_fucntion

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator     
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()