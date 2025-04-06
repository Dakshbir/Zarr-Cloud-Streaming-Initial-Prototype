# Zarr Cloud Streaming

[![PyPI version](https://badge.fury.io/py/zarr-cloud-streaming.svg)](https://badge.fury.io/py/zarr-cloud-streaming)

[![Tests](https://github.com/yourusername/zarr-cloud-streaming/actions/workflows/tests.yml/badge.svg)](https://github.com/yourusername/zarr-cloud-streaming/actions/workflows/tests.yml)

[![Documentation Status](https://readthedocs.org/projects/zarr-cloud-streaming/badge/?version=latest)](https://zarr-cloud-streaming.readthedocs.io/en/latest/?badge=latest)

Efficiently stream Zarr data from cloud storage with intelligent caching and prefetching for machine learning applications.

## Features

- **Efficient cloud access**: Optimized storage backends for AWS S3, Google Cloud Storage, and Azure Blob Storage
- **Intelligent caching**: LRU cache with configurable size to minimize cloud requests
- **Advanced prefetching**: Pattern-based and sequential prefetching strategies
- **PyTorch integration**: Seamless integration with PyTorch training pipelines
- **Adaptive batch sizing**: Dynamic adjustment based on data loading performance
- **Comprehensive benchmarking**: Detailed performance metrics and visualizations

## Installation

pip install zarr-cloud-streaming


### For development installation:

git clone https://github.com/yourusername/zarr-cloud-streaming.git
cd zarr-cloud-streaming
pip install -e ".[dev]"


## Quick Start

    from zarr_cloud_streaming.cloud import get_cloud_store
    from zarr_cloud_streaming.core import LRUCache

    store = get_cloud_store(
    "s3://mybucket/dataset.zarr",
    provider="s3",
    anon=False
    )

    zarr_array = store.get_array()
    print(f"Array shape: {zarr_array.shape}, dtype: {zarr_array.dtype}")

    data_slice = zarr_array[10:20, 10:20]

    from zarr_cloud_streaming.data import ZarrCloudDataset, AdaptiveCloudDataLoader
    import torch

    dataset = ZarrCloudDataset(
    zarr_path="s3://mybucket/dataset.zarr",
    cloud_provider="s3",
    cache_size_gb=4.0,
    prefetch_method="pattern",
    prefetch_lookahead=3
    )

    loader = AdaptiveCloudDataLoader(
    dataset=dataset,
    batch_size=32,
    shuffle=True,
    num_workers=4,
    adaptive_batching=True
    )

    model = YourModel()
    optimizer = torch.optim.Adam(model.parameters())

    for epoch in range(10):
    for batch_idx, (data, target) in enumerate(loader):

    # Forward pass
    output = model(data)
    loss = torch.nn.functional.cross_entropy(output, target)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if batch_idx % 10 == 0:
        print(f"Epoch: {epoch}, Batch: {batch_idx}, Loss: {loss.item()}")


## Advanced Features

from zarr_cloud_streaming.benchmark import BenchmarkTracker, BenchmarkVisualizer

tracker = BenchmarkTracker(
log_dir="./benchmark_results",
experiment_name="s3_vs_local"
)
tracker.start_timer("data_loading")

#... your data loading code ...
load_time = tracker.end_timer("data_loading")

stats = tracker.generate_report()
print(f"Average loading time: {stats['data_loading']['mean']:.4f}s")

visualizer = BenchmarkVisualizer(tracker)
visualizer.create_comparison_plots()


## Documentation

For full documentation, visit [zarr-cloud-streaming.readthedocs.io](https://zarr-cloud-streaming.readthedocs.io/).


### Development setup

### Install development dependencies
pip install -e ".[dev,docs,benchmark]"

### Run tests
pytest

### Run linting
flake8 src tests
black src tests

## License


## Acknowledgments

