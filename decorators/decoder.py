decoder_registry = {}
DEFAULT_DECODER_MODULE = "DecoderModule1"

def Decoder(cls):
    decoder_registry[cls.__name__] = cls
    return cls