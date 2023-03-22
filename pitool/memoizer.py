import shelve
import functools
import os

__all__ = ["memoize"]


def _cache_path():
    """Get the path to the cache directory."""
    return os.environ.get("PITOOL_CACHE", "pitool_cache")


def memoize(func):
    """Persistently memoize a function."""
    cache_path = _cache_path()
    cache = shelve.open(cache_path)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper
