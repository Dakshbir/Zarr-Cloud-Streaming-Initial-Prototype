# examples/ml_training.py
from src.data.dataset import ZarrCloudDataset
from src.data.loader import AdaptiveCloudDataLoader
from src.benchmark.metrics import BenchmarkTracker
from src.benchmark.visualize import BenchmarkVisualizer

def main(args):
    device = torch.device("cuda" if torch.cuda.is_available() and not args.no_cuda else "cpu")

    tracker = BenchmarkTracker(
        log_dir=args.output_dir,
        experiment_name=args.experiment_name
    )

    dataset = ZarrCloudDataset(
        zarr_path=args.zarr_path,
        cloud_provider=args.cloud_provider,
        cache_size_gb=args.cache_size,
        prefetch_method=args.prefetch_method,
        prefetch_lookahead=args.prefetch_lookahead
    )

    loader = AdaptiveCloudDataLoader(
        dataset=dataset,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=args.num_workers,
        adaptive_batching=args.adaptive_batching
    )
    
    # Create and train model
