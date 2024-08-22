#!/usr/bin/python3
""" LFU Caching module

This module contains the LFUCache class, which implements a caching system
using the Least Frequently Used (LFU) caching algorithm. In case of a tie
in the frequency count, the Least Recently Used (LRU) strategy is used to
break ties.

The LFUCache inherits from the BaseCaching class and implements the required
methods: put and get.
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict

class LFUCache(BaseCaching):
    """ LFUCache class

    This class implements a caching system using the LFU (Least Frequently Used)
    algorithm. It maintains the frequency of access for each cache item and
    evicts the least frequently used item when the cache exceeds the maximum
    allowed size. In case of a tie, it uses LRU (Least Recently Used) to
    determine which item to discard.

    Attributes:
        freq (defaultdict): A dictionary that maps cache keys to their access frequencies.
        order (OrderedDict): An ordered dictionary that tracks the order of cache accesses.
        min_freq (int): The minimum frequency count of items currently in the cache.
    """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.freq = defaultdict(int)
        self.order = OrderedDict()
        self.min_freq = 1

    def put(self, key, item):
        """ Add an item to the cache

        If the cache is full, it will discard the least frequently used item.
        If there is a tie, the least recently used item among the least
        frequently used ones will be discarded.

        Args:
            key (str): The key of the item.
            item (any): The item to be stored in the cache.

        If the key or item is None, this method does nothing.
        """
        if key and item:
            if key in self.cache_data:
                # Update the item and its frequency
                self.cache_data[key] = item
                self.freq[key] += 1
                self.order.move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find the LFU items
                    min_freq_keys = [k for k, v in self.freq.items() if v == self.min_freq]
                    if min_freq_keys:
                        # Break tie using LRU
                        lru_key = min(min_freq_keys, key=lambda k: self.order[k])
                        self.cache_data.pop(lru_key)
                        self.freq.pop(lru_key)
                        self.order.pop(lru_key)
                        print(f"DISCARD: {lru_key}")

                # Add the new item
                self.cache_data[key] = item
                self.freq[key] = 1
                self.order[key] = item
                self.min_freq = 1

    def get(self, key):
        """ Retrieve an item from the cache

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if the key does not
            exist in the cache.
        """
        if key in self.cache_data:
            # Update frequency and order
            self.freq[key] += 1
            self.order.move_to_end(key)
            self.min_freq = min(self.freq.values())
            return self.cache_data[key]
        return None
