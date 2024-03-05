def AsyncExecutionTime(task_name):
    """
    A decorator that prints the execution time of the function it decorates.
    """
    from functools import wraps
    import time

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            result = await func(*args, **kwargs)
            end_time = time.time()
            print(f"[{task_name}] Execution time: {end_time - start_time:.2f} s")
            return result

        return wrapper

    return decorator

def ExecutionTime(task_name):
    """
    A decorator that prints the execution time of the function it decorates.
    """
    from functools import wraps
    import time

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Execution time of {task_name} : {end_time - start_time:.2f} s")
            return result

        return wrapper

    return decorator