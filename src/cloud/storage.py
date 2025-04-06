import zarr
import s3fs
import gcsfs
import time
import logging
from typing import Dict, Any, Optional, Union

class CloudStore:
    """Base class for cloud storage backends"""
    def __init__(self, path: str, **kwargs):
        self.path = path
        self.metrics = {
            'hits': 0, 'misses': 0, 'bytes_read': 0, 'read_time': []
        }
    
    def get_store(self):
        """Return the store object for zarr"""
        raise NotImplementedError
    
    def get_array(self, path: Optional[str] = None):
        """Open a zarr array from the store"""
        store = self.get_store()
        return zarr.open(store)

class S3Store(CloudStore):
    """AWS S3 storage backend for Zarr"""
    def __init__(self, path: str, anon: bool = False, **kwargs):
        super().__init__(path, **kwargs)
        self.anon = anon
        self.region = kwargs.get('region', None)
        self._initialize()
    
    def _initialize(self):
        """Initialize the S3 filesystem"""
        client_kwargs = {}
        if self.region:
            client_kwargs['region_name'] = self.region
            
        self.s3fs = s3fs.S3FileSystem(
            anon=self.anon,
            client_kwargs=client_kwargs
        )
        self.store = self.s3fs.get_mapper(self.path)
    
    def get_store(self):
        """Return the S3 store mapper"""
        return self.store
