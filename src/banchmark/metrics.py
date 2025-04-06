import time
import json
import logging
import os
import numpy as np
from typing import Dict, Any, Optional
from datetime import datetime

class BenchmarkTracker:
    """Track and analyze performance metrics during training/evaluation"""
    def __init__(self, log_dir: str, experiment_name: str):
        self.log_dir = log_dir
        self.experiment_name = experiment_name

        os.makedirs(log_dir, exist_ok=True)

        self.metrics = {
            'data_load_time': [],
            'training_time': [],
            'throughput': [],
            'memory_usage': [],
            'bandwidth_utilization': [],
            'batch_sizes': [],
            'batch_times': []
        }
        
        self.start_times = {}
        self.counters = {}

        self.start_time = time.time()
