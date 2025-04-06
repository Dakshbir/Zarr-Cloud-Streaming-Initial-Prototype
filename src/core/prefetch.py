import threading
import logging
import queue
import time
from typing import List, Dict, Any, Callable

class PrefetchWorker:
    """Worker thread for prefetching Zarr chunks"""
    def __init__(self, fetch_func: Callable, cache_func: Callable):
        self.fetch_func = fetch_func
        self.cache_func = cache_func
        self.queue = queue.Queue()
        self.running = False
        self.thread = None
        self.metrics = {
            'prefetched': 0, 'failures': 0, 'total_fetch_time': 0
        }
    
    def start(self):
        """Start the prefetch worker thread"""
        if self.running:
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._worker_loop, daemon=True)
        self.thread.start()
    
    def queue_keys(self, keys: List[str]):
        """Queue keys for prefetching"""
        for key in keys:
            self.queue.put(key)
    
    def _worker_loop(self):
        """Main worker loop"""
        while self.running:
            try:
                key = self.queue.get(timeout=0.1)

                start_time = time.time()
                try:
                    data = self.fetch_func(key)
                    self.cache_func(key, data)
                    self.metrics['prefetched'] += 1
                except Exception as e:
                    logging.warning(f"Failed to prefetch key {key}: {e}")
                    self.metrics['failures'] += 1
                
                self.metrics['total_fetch_time'] += time.time() - start_time
                
                self.queue.task_done()
            
            except queue.Empty:
                continue
