"""
Shared runtime utilities. 

Seed reproducibility and device selection.
"""

import os
import random

import numpy as np
import torch


def set_seed(seed: int) -> None:
    """ Set deterministic seeds for Python, NumPy, and PyTorch """

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

        # torch.backends.cudnn.benchmark = False  # uses the inbuilt cudnn auto-tuner to find the fastest convolution algorithms
        # torch.backends.cudnn.enabled   = False
    
    return True

def get_device() -> str:
    """ Return available PyTorch device """

    return "cuda" if torch.cuda.is_available() else "cpu"

def is_hpc() -> bool:
    """ Return True when running on the VSC HPC environment """

    return Path("/scratch/antwerpen/grp/ap_vliz_research").exists()