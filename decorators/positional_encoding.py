
positional_encoding_registry = {}
DEFAULT_POS_ENCODING = "PositionalEncoding1"

def PositionalEncoding(cls):
    positional_encoding_registry[cls.__name__] = cls
    return cls
