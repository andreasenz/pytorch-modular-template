import torch
from decorators.positional_encoding import PositionalEncoding

@PositionalEncoding
class PositionalEncoding3(torch.nn.Module):
    def __init__(self, d_model, max_len=5000):
        super(PositionalEncoding3, self).__init__()
        # Implementation for Positional Encoding Technique 1

    def forward(self, x):
        return x