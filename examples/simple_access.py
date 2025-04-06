import argparse
import logging
import numpy as np
import time
from src.cloud.storage import get_cloud_store
from src.core.cache import LRUCache
from src.core.prefetch import SequentialPrefetcher

def main(args):
    store = get_cloud_store(
        args.zarr_path,
        provider=args.cloud_provider,
        anon=args.anonymous
    )

    start_time = time.time()
    zarr_array = store.get_array()
    logging.info(f"Array opened in {time.time() - start_time:.2f}s")
    logging.info(f"Array shape: {zarr_array.shape}, dtype: {zarr_array.dtype}")

    cache = LRUCache(max_size_gb=args.cache_size)
    prefetcher = SequentialPrefetcher(
        fetch_func=lambda key: zarr_array[parse_key(key)],
        cache_func=cache.put,
        lookahead=args.prefetch_lookahead
    ) if args.prefetch else None
    
    # Perform data access operations

