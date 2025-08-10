from functools import wraps
from time import perf_counter
from typing import Callable, Any

def benchmark(func: Callable) -> Callable:
    """Decorator to measure function execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        self = args[0] if args and hasattr(args[0], '_stats') else None
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        
        if self:
            self._stats['parse_time'] += elapsed
            self._stats['parse_count'] += 1
            
        return result
    return wrapper

def memoize(func: Callable) -> Callable:
    """Simple memoization decorator"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args) -> Any:
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper