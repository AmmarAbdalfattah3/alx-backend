#!/usr/bin/env python3
"""LRUCache module
"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUCache class inherits from BaseCaching and implements a LRU cache.
    """
    def __init__(self):
        """Initialize the LRUCache
        """
        super().__init__()
        self.cache_data = OrderDict()

    def put(self, key, item):
        """Add an item to the cache.
        """
        if key is None or itme is None:
            return None
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last: True)
        if len(self.cache_data) >= super.MAX_ITEMS:
            self.cache_data.popitem(last=False)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache.
        """
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key, last: True)
        return self.cache_data.get(key, None)
