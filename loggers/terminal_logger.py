import torch
from decorators import Logger

@Logger
class TerminalLogger():
    def __init__(self):
        pass

    def log(self, *args, **kwargs):
        # Convert positional arguments to a string
        args_str = ' '.join(map(str, args))
        
        # Convert keyword arguments to a string
        kwargs_str = ', '.join(f"{key}={value}" for key, value in kwargs.items())
        
        # Combine both parts into a single log line
        log_message = args_str
        if kwargs_str:
            if args_str:
                log_message += ' | '
            log_message += kwargs_str
        
        # Print the log message (or handle it however you need)
        print(log_message)