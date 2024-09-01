# Description: Decorators for composing modules
def decoder_type(decoder_class, d_model, num_heads, num_layers):
    def decorator(cls):
        original_init = cls.__init__

        def __init__(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            self.decoder = decoder_class( d_model, num_heads, num_layers)
            self.add_module('decoder', self.decoder)  # Register as submodule

        cls.__init__ = __init__
        return cls
    return decorator

def positional_encoder(encoder_class, d_model, max_len):
    def decorator(cls):
        original_init = cls.__init__

        def __init__(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            self.positional_encoder = encoder_class(d_model, max_len)
            self.add_module('positional_encoder', self.positional_encoder)  # Register as submodule

        cls.__init__ = __init__
        return cls
    return decorator