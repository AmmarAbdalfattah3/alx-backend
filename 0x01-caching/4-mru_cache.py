#!/usr/bin/env python3
"""MRUCache module
"""


from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and implements
    a Least Recently Used (MRU) caching system.
    """

    def __init__(self):
        """
        Initialize the MRUCache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add or update an item in the cache.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
