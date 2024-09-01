
import torch
from decorators.decoder import Decoder



@Decoder
class DecoderModule1(torch.nn.Module):
    def __init__(self, d_model, nhead, num_layers, dim_feedforward=2048):
        super(DecoderModule1, self).__init__()
        self.layers = torch.nn.TransformerDecoderLayer(d_model, nhead, dim_feedforward)
        self.decoder = torch.nn.TransformerDecoder(self.layers, num_layers)
    
    def forward(self, x, memory, tgt_mask=None):
        return self.decoder(x, memory, tgt_mask=tgt_mask)