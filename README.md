# ☁️ Zarr Cloud Streaming

A modular, production-ready prototype for **streaming Zarr data from cloud storage** using **Ice Chunk** and **Zarr 3**. This implementation supports **efficient data access**, **caching**, **intelligent prefetching**, and **PyTorch integration** — enabling scalable machine learning workflows on large cloud-hosted datasets.

---

## 🚀 Features

- ✅ **Pluggable Cloud Storage**: Supports AWS S3, GCS, and more via `s3fs` and `gcsfs`.
- ⚡ **LRU Caching**: Minimizes redundant I/O with a memory-aware Least Recently Used cache.
- 🤖 **Intelligent Prefetching**: Pattern-based and sequential chunk preloading for optimized throughput.
- 🔁 **PyTorch Dataset Wrapper**: Seamless integration with `torch.utils.data.Dataset`.
- 🔄 **Adaptive DataLoader**: Adjusts batch size based on performance metrics.
- 📊 **Benchmarking Tools**: Measure data access latency, throughput, memory, and bandwidth utilization.

---

## 📁 Project Structure

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

## 🛠️ Installation

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

## 🧪 Quickstart

### 📦 Simple Cloud Access

```bash
python examples/simple_access.py \
  --zarr_path "s3://your-bucket/data.zarr" \
  --cloud_provider s3 \
  --anonymous False \
  --cache_size 2.0 \
  --prefetch
```

### 🤖 ML Training with Adaptive Loader

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

## 🧠 Usage Highlights

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

## 🤝 Contributing

Contributions are welcome! Please open issues, PRs, or suggestions.

### Setup for Development

```bash
# Run tests
pytest tests/

# Linting
flake8 src/ tests/
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Dakshbir Singh**  
🔗 [GitHub](https://github.com/Dakshbir)  
🔗 [LinkedIn](https://www.linkedin.com/in/dakshbir-singh-kapoor-26210b286/)  
✉️ [dakshbirkapoor@gmail.com](mailto:dakshbirkapoor@gmail.com)

---

## 🌐 Acknowledgements

- [Zarr 3](https://zarr.readthedocs.io/en/stable/)
- [Ice Chunk](https://github.com/zarr-developers/icechunk)
- [PyTorch](https://pytorch.org/)
