#!/usr/bin/env python
"""FIFOCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """FIFOCache class inherits from BaseCaching and implements a FIFO cache.
    """
    def __init__(self):
        """Initialize the FIFOCache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > super().MAX_ITEMS:
                oldest_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(oldest_key))

    def get(self, key):
        """Retrieve an item from the cache.
        """
        return self.cache_data.get(key, None)
