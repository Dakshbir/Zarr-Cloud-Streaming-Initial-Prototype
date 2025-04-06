# Zarr Cloud Streaming

This is a modular, initial prototype for **streaming Zarr data from cloud storage** using **Ice Chunk** and **Zarr 3**. This implementation supports **efficient data access**, **caching**, **intelligent prefetching**, and **PyTorch integration** — enabling scalable machine learning workflows on large cloud-hosted datasets.

---

## Features

- **Pluggable Cloud Storage**: Supports AWS S3, GCS, and more via `s3fs` and `gcsfs`.
- **LRU Caching**: Minimizes redundant I/O with a memory-aware Least Recently Used cache.
- **Intelligent Prefetching**: Pattern-based and sequential chunk preloading for optimized throughput.
- **PyTorch Dataset Wrapper**: Seamless integration with `torch.utils.data.Dataset`.
- **Adaptive DataLoader**: Adjusts batch size based on performance metrics.
- **Benchmarking Tools**: Measure data access latency, throughput, memory, and bandwidth utilization.

---

## Project Structure- Initial 

```
zarr-cloud-streaming/
│
├── src/
│   ├── cloud/             # Cloud storage interfaces (S3, GCS, etc.)
│   ├── core/              # Caching, prefetching, chunking logic
│   ├── data/              # PyTorch dataset and adaptive dataloader
│   └── benchmark/         # Performance metrics and tracking
│
├── examples/              # Example scripts (simple access, ML training)
├── tests/                 # Unit and integration tests
├── requirements.txt       # Python dependencies
├── setup.py               # Package installation
└── README.md              # Project documentation
```

---

## Project Structure- Final (At the end of the project)

```
zarr-cloud-streaming/
│
├── src/
│   ├── cloud/                       # Cloud storage interfaces
│   │   ├── __init__.py
│   │   ├── storage.py               # Base storage implementations
│   │   ├── s3_store.py              # AWS S3 specific implementation
│   │   ├── gcs_store.py             # Google Cloud Storage implementation 
│   │   └── azure_store.py           # Azure Blob Storage implementation
│   │
│   ├── core/                        # Core functionality
│   │   ├── __init__.py
│   │   ├── cache.py                 # LRU caching system
│   │   ├── prefetch.py              # Intelligent prefetching
│   │   ├── config.py                # Configuration management
│   │   └── utils.py                 # Common utilities
│   │
│   ├── data/                        # PyTorch integration
│   │   ├── __init__.py
│   │   ├── dataset.py               # PyTorch Dataset implementation
│   │   ├── loader.py                # Custom DataLoader for cloud streaming
│   │   ├── transforms.py            # Data transformation utilities
│   │   └── samplers.py              # Custom sampling strategies
│   │
│   └── benchmark/                   # Performance tracking
│       ├── __init__.py
│       ├── metrics.py               # Performance metrics collection
│       ├── visualize.py             # Results visualization 
│       ├── analyze.py               # Analysis utilities
│       └── comparison.py            # Benchmark comparison tools
│
├── examples/                        # Usage examples
│   ├── __init__.py
│   ├── simple_access.py             # Basic data access example
│   ├── ml_training.py               # Machine learning training example
│   ├── caching_strategies.py        # Caching strategy examples
│   ├── prefetch_patterns.py         # Prefetching pattern examples
│   └── cloud_comparison.py          # Cloud provider comparison
│
├── tests/                           # Test cases
│   ├── __init__.py
│   ├── conftest.py                  # Test configuration
│   ├── test_cloud/                  # Storage backend tests
│   │   ├── __init__.py
│   │   ├── test_s3.py
│   │   ├── test_gcs.py
│   │   └── test_azure.py
│   ├── test_core/                   # Core functionality tests
│   │   ├── __init__.py
│   │   ├── test_cache.py
│   │   └── test_prefetch.py
│   ├── test_data/                   # Dataset and loader tests
│   │   ├── __init__.py
│   │   ├── test_dataset.py
│   │   └── test_loader.py
│   └── test_benchmark/              # Benchmark tests
│       ├── __init__.py
│       └── test_metrics.py
│
├── notebooks/                       # Jupyter notebooks
│   ├── quickstart.ipynb             # Getting started tutorial
│   ├── benchmark_analysis.ipynb     # Performance analysis
│   ├── cloud_comparison.ipynb       # Cloud provider comparison
│   └── advanced_usage.ipynb         # Advanced usage patterns
│
├── docs/                            # Documentation
│   ├── index.md                     # Main documentation page
│   ├── installation.md              # Installation instructions
│   ├── quickstart.md                # Getting started guide
│   ├── api/                         # API documentation
│   │   ├── cloud.md                 # Cloud storage API docs
│   │   ├── core.md                  # Core functionality docs
│   │   ├── data.md                  # Data loading API docs
│   │   └── benchmark.md             # Benchmarking API docs
│   ├── examples/                    # Example documentation
│   │   ├── basic.md                 # Basic usage examples
│   │   └── advanced.md              # Advanced usage examples
│   └── performance/                 # Performance documentation
│       ├── benchmarks.md            # Benchmark results
│       └── optimization.md          # Optimization strategies
│
├── scripts/                         # Utility scripts
│   ├── benchmark.py                 # Run benchmarks
│   ├── convert_to_zarr.py           # Convert datasets to Zarr format
│   └── deploy_cloud.py              # Deploy to cloud environments
│
├── .github/                         # GitHub configuration
│   ├── workflows/                   # CI/CD workflows
│   │   ├── tests.yml                # Run tests
│   │   ├── lint.yml                 # Run linting
│   │   └── publish.yml              # Publish package
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
│
├── requirements.txt                 # Basic requirements
├── requirements-dev.txt             # Development requirements
├── setup.py                         # Package setup
├── setup.cfg                        # Package configuration
├── pyproject.toml                   # Build system requirements
├── LICENSE                          # License file
├── CHANGELOG.md                     # Version changes
├── CONTRIBUTING.md                  # Contribution guidelines
└── README.md                        # Project overview
```

---

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/<your-username>/zarr-cloud-streaming.git
cd zarr-cloud-streaming
pip install -r requirements.txt
```

Optionally, install in editable mode:

```bash
pip install -e .
```

---

## Quickstart

### Simple Cloud Access

```bash
python examples/simple_access.py \
  --zarr_path "s3://your-bucket/data.zarr" \
  --cloud_provider s3 \
  --anonymous False \
  --cache_size 2.0 \
  --prefetch
```

### ML Training with Adaptive Loader

```bash
python examples/ml_training.py \
  --zarr_path "s3://your-bucket/data.zarr" \
  --cloud_provider s3 \
  --batch_size 64 \
  --prefetch_method pattern \
  --prefetch_lookahead 3 \
  --adaptive_batching \
  --output_dir logs/
```

---

## Usage Highlights

### 🔹 Cloud Storage Access

```python
from src.cloud.storage import get_cloud_store
store = get_cloud_store("s3://my-bucket/data.zarr", provider="s3")
zarr_array = store.get_array()
```

### 🔹 LRU Caching

```python
from src.core.cache import LRUCache
cache = LRUCache(max_size_gb=2.0)
cache.put("chunk-key", data_chunk)
```

### 🔹 Prefetching

```python
from src.core.prefetch import SequentialPrefetcher
prefetcher = SequentialPrefetcher(fetch_func, cache.put, lookahead=5)
prefetcher.queue_keys(["key1", "key2", "key3"])
```

### 🔹 PyTorch Dataset

```python
from src.data.dataset import ZarrCloudDataset
dataset = ZarrCloudDataset("s3://...", cloud_provider="s3", prefetch_method="pattern")
```

---

## 📊 Benchmarking

Track training time, data throughput, bandwidth utilization, and more:

```python
from src.benchmark.metrics import BenchmarkTracker
tracker = BenchmarkTracker(log_dir="logs/", experiment_name="run1")
tracker.log_metric("data_load_time", 0.18)
tracker.save()
```

---

## ✅ TODOs

- [ ] Add support for Azure Blob Storage
- [ ] Improve multi-threaded caching
- [ ] Add visualizations for benchmarking results
- [ ] CI/CD and code coverage

---

### Setup for Development

```bash
# Run tests
pytest tests/

# Linting
flake8 src/ tests/
```

---

## License

---

## Author

**Dakshbir Singh**  
🔗 [GitHub](https://github.com/Dakshbir)  
🔗 [LinkedIn](https://www.linkedin.com/in/dakshbir-singh-kapoor-26210b286/)  
✉️ [dakshbirkapoor@gmail.com](mailto:dakshbirkapoor@gmail.com)

---

## 🌐 Acknowledgements
