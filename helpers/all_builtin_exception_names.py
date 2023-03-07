import builtins
import functools


@functools.cache
def all_builtin_exception_names() -> set[str]:
    return set(name for name, value in builtins.__dict__.items()
               if isinstance(value, type) and issubclass(value, BaseException))
