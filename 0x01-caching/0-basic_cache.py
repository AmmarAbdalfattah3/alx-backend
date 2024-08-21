#!/usr/bin/env python3
"""
BasicCache module
"""


BasicCaching = __import__('basic_caching').BasicCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initializes the BasicCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Stores an item in the cache with the specified key.
        """
        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache using the specified key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
