
metric_registry = {}
DEFAULT_METRIC_MODULE = "Accuracy"

def Metric(cls):
    metric_registry[cls.__name__] = cls
    return cls
