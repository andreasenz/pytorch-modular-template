from utils import init_project
import os

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))
init_project(current_directory)


from decorators import *
from decoders import *
from positional_encodings import *
from metrics import *
import torch
import argparse
from loggers import *


parser = argparse.ArgumentParser(description="Choose positional encoding and decoder module")
parser.add_argument('--pos-encoding', type=str, required=False,
                    default=DEFAULT_POS_ENCODING,
                    help=f"Choose the positional encoding technique (PositionalEncoding1, PositionalEncoding2, PositionalEncoding3). Default is {DEFAULT_POS_ENCODING}")
parser.add_argument('--decoder-module', type=str, required=False,
                    default=DEFAULT_DECODER_MODULE,
                    help=f"Choose the decoder module (DecoderModule1, DecoderModule2). Default is {DEFAULT_DECODER_MODULE}")
parser.add_argument('--logger-module', type=str, required=False,
                    default=DEFAULT_LOGGER_MODULE,
                    help=f"Choose the decoder module (DecoderModule1, DecoderModule2). Default is {DEFAULT_LOGGER_MODULE}")

parser.add_argument('--metrics', nargs='+', help='List of metrics to log', required=True)

args = parser.parse_args()


metrics = [(metric,metric_registry[metric]) for metric in args.metrics]
print(metrics)
pos_encoding_class = positional_encoding_registry.get(args.pos_encoding, positional_encoding_registry[DEFAULT_POS_ENCODING])
decoder_class = decoder_registry.get(args.decoder_module, decoder_registry[DEFAULT_DECODER_MODULE])
logger_class = logger_registry.get(args.logger_module, logger_registry[DEFAULT_LOGGER_MODULE])
print(pos_encoding_class)
print(decoder_class)
print(logger_class)

D_MODEL = 768
MAX_LEN = 5000
NUM_LAYERS = 12
NUM_HEADS = 12

@decoder_type(decoder_class, D_MODEL, NUM_LAYERS, NUM_HEADS)
@positional_encoder(pos_encoding_class, D_MODEL, MAX_LEN)
class Transformer(torch.nn.Module):
    def __init__(self):
        super(Transformer, self).__init__()
        #self.positional_encoding = pos_encoding_class(d_model, max_len)
        #self.decoder = decoder_class(d_model,12,12)
        pass

    def forward(self, x):
        x = self.positional_encoding(x)
        x = self.decoder(x)
        return x   
model = Transformer()
print(model)
logger = logger_class()
logger.log("Starting process", "Process ID: 123", metric1=100, metric2=200, metric3="completed")