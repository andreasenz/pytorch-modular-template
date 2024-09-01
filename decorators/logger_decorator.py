
logger_registry = {}
DEFAULT_LOGGER_MODULE = "TerminalLogger"

def Logger(cls):
    logger_registry[cls.__name__] = cls
    return cls
