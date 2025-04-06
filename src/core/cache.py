import time
import threading
import logging
import numpy as np
from typing import Dict, Any, Optional, Tuple

class LRUCache:
    """LRU (Least Recently Used) cache for Zarr chunks"""
    def __init__(self, max_size_gb: float = 2):
        self.max_size_bytes = int(max_size_gb * 1024**3)
        self.current_size_bytes = 0
        self.cache: Dict[str, Tuple[np.ndarray, float]] = {}  
        self.lock = threading.RLock()
        self.metrics = {
            'hits': 0, 'misses': 0, 'evictions': 0
        }
    
    def __contains__(self, key: str) -> bool:
        """Check if a key is in the cache"""
        return key in self.cache
    
    def get(self, key: str) -> Optional[np.ndarray]:
        """Get a value from the cache, returns None if not found"""
        with self.lock:
            if key in self.cache:
                data, _ = self.cache[key]
                self.cache[key] = (data, time.time())
                self.metrics['hits'] += 1
                return data
            
            self.metrics['misses'] += 1
            return None
