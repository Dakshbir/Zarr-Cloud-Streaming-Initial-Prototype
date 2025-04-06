import time
import logging
import numpy as np
import torch
from torch.utils.data import DataLoader
from typing import Dict, Any

class AdaptiveCloudDataLoader:
    """DataLoader with adaptive batch sizing for cloud-based datasets"""
    def __init__(self, 
                 dataset,
                 batch_size: int = 32,
                 shuffle: bool = True,
                 num_workers: int = 4,
                 prefetch_factor: int = 2,
                 adaptive_batching: bool = True,
                 min_batch_size: int = 1,
                 max_batch_size: int = 128,
                 batch_adjustment_factor: float = 0.8,
                 target_batch_time: float = 0.1,
                 monitoring_window: int = 5,
                 **kwargs):
        
        self.dataset = dataset
        self.base_batch_size = batch_size
        self.current_batch_size = batch_size
        self.shuffle = shuffle
        self.num_workers = num_workers
        self.prefetch_factor = prefetch_factor
        self.kwargs = kwargs
        

        self.adaptive_batching = adaptive_batching
        self.min_batch_size = min_batch_size
        self.max_batch_size = max_batch_size
        self.batch_adjustment_factor = batch_adjustment_factor
        self.target_batch_time = target_batch_time
        self.monitoring_window = monitoring_window

        self.batch_times = []
        self.batch_sizes = []

        self.dataloader = self._create_dataloader()
