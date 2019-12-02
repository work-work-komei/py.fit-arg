import inspect


def ignore_longer(func):
    spec = inspect.getfullargspec(func)
    arg_len = len(spec.args)
    if hasattr(func, "__self__"):
        arg_len -= 1

    return lambda *args, **kwargs: func(*args[:min(arg_len, len(args))], **kwargs)


def ignore_unknown(func):
    spec = inspect.getfullargspec(func)
    known = 
