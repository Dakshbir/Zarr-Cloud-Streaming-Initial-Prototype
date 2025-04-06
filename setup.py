from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zarr-cloud-streaming",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Efficient streaming of Zarr data from cloud storage with caching and prefetching",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/zarr-cloud-streaming",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/zarr-cloud-streaming/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "zarr>=2.11.0",
        "s3fs>=2023.1.0",
        "gcsfs>=2023.1.0",
        "azure-storage-blob>=12.14.0",
        "numpy>=1.20.0",
        "torch>=1.10.0",
        "dask>=2022.2.0",
        "fsspec>=2023.1.0",
        "numcodecs>=0.10.0",
        "icechunk>=0.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.1.0",
            "isort>=5.12.0",
            "mypy>=1.0.0",
            "flake8>=6.0.0",
        ],
        "docs": [
            "mkdocs>=1.4.0",
            "mkdocs-material>=9.0.0",
            "mkdocstrings>=0.20.0",
        ],
        "benchmark": [
            "matplotlib>=3.5.0",
            "seaborn>=0.12.0",
            "pandas>=1.5.0",
            "tqdm>=4.64.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "zarr-benchmark=src.benchmark.cli:main",
        ],
    },
)
