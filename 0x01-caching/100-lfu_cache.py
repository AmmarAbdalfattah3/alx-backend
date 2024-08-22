#!/usr/bin/env python3
"""LFUCache module
"""


from collections import defaultdict, OrderedDict
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """LFUCache class inherits from BaseCaching and implements a Least Frequently Used (LFU) cache."""

    def __init__(self):
        """Initialize the LFUCache."""
        super().__init__()
        self.cache_data = {}
        self.freq = defaultdict(int)  # To track the frequency of access
        self.order = defaultdict(OrderedDict)  # To track the order of access per frequency level
        self.min_freq = 1  # To track the minimum frequency

    def put(self, key, item):
        """Add an item to the cache.

        If the cache exceeds BaseCaching.MAX_ITEMS, discard the least frequently used item.
        If multiple items have the same frequency, discard the least recently used one.

        Args:
            key (str): The key to store the item under.
            item (str): The value to store in the cache.

        If `key` or `item` is None, this method does nothing.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the existing item
            self._update_frequency(key)
            self.cache_data[key] = item
        else:
            # Add a new item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict()

            self.cache_data[key] = item
            self.freq[key] = 1
            self.order[1][key] = None
            self.min_freq = 1

    def get(self, key):
        """Retrieve an item from the cache.

        Updates the frequency and order of the item.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            str: The value associated with the key.
        """
        if key is None or key not in self.cache_data:
            return None

        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """Update the frequency and order of the given key."""
        freq = self.freq[key]
        # Remove the key from the current frequency level
        del self.order[freq][key]
        if not self.order[freq]:
            del self.order[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Update frequency and add to the new frequency level
        self.freq[key] += 1
        new_freq = self.freq[key]
        self.order[new_freq][key] = None

    def _evict(self):
        """Evict the least frequently used item."""
        # Get the least frequently used level
        lfu_keys = self.order[self.min_freq]
        # Remove the least recently used item from the least frequent level
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

