# learn about decorators
import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f"{func.__name__}  Starting time : {end-start}")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(2)



# def debug(func):
#     def wrapper(*args,**kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwarfs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
#         print(f"calling : {func.__name__} with args {args_value} and kwargs : {kwarfs_value}")
#         return func(*args,**kwargs)

#     return wrapper
# @debug
# def hello():
#     print("Hello")


# @debug
# def greet(name,greeting = "Hello"):
#     print(f"{greeting}, {name}")

# hello()
# greet("Chai",greeting="name")



def cache(func):
    cache_value = {}
    print("cache: ",cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper


@cache
def long_runngin_function(a,b):
    time.sleep(4)
    return a+b

print(long_runngin_function(2,3))
print(long_runngin_function(2,3))