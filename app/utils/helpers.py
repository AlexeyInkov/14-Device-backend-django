from loguru import logger


def logging(message: str):
    def decorator(func):
        def wrapper(*args, **kwargs):

            context_logger = logger.bind(
                user="someone", action="", func_name=func.__name__
            )
            context_logger.info(message, action="start")
            result = func(*args, **kwargs)
            context_logger.info(message, action="end")
            return result

        return wrapper

    return decorator
