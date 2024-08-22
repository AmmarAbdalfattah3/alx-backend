#!/usr/bin/env python3
"""LFUCache module
"""


from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """Initialize the LFUCache."""
        super().__init__()
        self.cache_data = {}
        self.freq = defaultdict(int)
        self.order = defaultdict(OrderedDict)
        self.min_freq = 1

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self._update_frequency(key)
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict()
            self.cache_data[key] = item
            self.freq[key] = 1
            self.order[1][key] = None
            self.min_freq = 1

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is None or key not in self.cache_data:
            return None

        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """Update the frequency and access order of a key."""
        freq = self.freq[key]
        del self.order[freq][key]
        if not self.order[freq]:
            del self.order[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.freq[key] += 1
        self.order[self.freq[key]][key] = None

    def _evict(self):
        """Evict the least frequently used item, using LRU if necessary."""
        lfu_keys = self.order[self.min_freq]
        lru_key, _ = lfu_keys.popitem(last=False)
        del self.cache_data[lru_key]
        del self.freq[lru_key]
        if not lfu_keys:
            del self.order[self.min_freq]

    def print_cache(self):
        """Print the current state of the cache."""
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")
