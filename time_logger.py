import datetime


def logger_decorator_factory(file_path):
    def logger_decorator(func):
        def func_with_logging(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_path, 'a+', encoding='utf-8') as f:
                f.write(f"{str(datetime.datetime.now())} - {func.__name__} {args} {kwargs} {result}" + "\n")
            return result
        return func_with_logging
    return logger_decorator
