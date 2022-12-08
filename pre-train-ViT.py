import torch
import torch.nn as nn
from config import cfg
class PreVit(nn.Module):
    def __init__(self):
        self.proj = nn.Linear(cfg.projection_dim,cfg.d_model)
        pass
    def forward(self):
        pass