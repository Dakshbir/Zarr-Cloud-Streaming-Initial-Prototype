import logging
import time
import numpy as np
import torch
from torch.utils.data import Dataset
from typing import Optional, Tuple, Dict, Any, List, Callable, Union

class ZarrCloudDataset(Dataset):
    """PyTorch Dataset for accessing Zarr arrays from cloud storage"""
    def __init__(self, 
                 zarr_path: str,
                 cloud_provider: str = 'auto',
                 cache_size_gb: float = 2.0,
                 prefetch_method: str = 'pattern',
                 prefetch_lookahead: int = 3,
                 transform: Optional[Callable] = None,
                 **kwargs):

        self.cloud_store = get_cloud_store(zarr_path, provider=cloud_provider, **kwargs)

        self.array = self.cloud_store.get_array()
        self.shape = self.array.shape
        self.ndim = len(self.shape)
        self.dtype = self.array.dtype

        self.cache = LRUCache(max_size_gb=cache_size_gb)

        self.prefetch_method = prefetch_method
        if prefetch_method == 'sequential':
            self.prefetcher = SequentialPrefetcher(
                fetch_func=self._fetch_chunk,
                cache_func=self.cache.put,
                lookahead=prefetch_lookahead
            )
        elif prefetch_method == 'pattern':
            self.prefetcher = PatternPrefetcher(
                fetch_func=self._fetch_chunk,
                cache_func=self.cache.put,
                lookahead=prefetch_lookahead
            )
        else:
            self.prefetcher = None

        self.transform = transform

        self.metrics = {
            'get_calls': 0, 'cache_hits': 0, 'fetch_time': []
        }
