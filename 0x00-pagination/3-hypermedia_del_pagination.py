#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""


import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary with pagination details and dataset page."""
        assert (isinstance(index, int) and
                index >= 0), "Index must be a non-negative integer"
        assert (isinstance(page_size, int) and
                page_size > 0), "Page_size must be a positive integer"

        # Get the indexed dataset
        dataset = self.indexed_dataset()

        # Collect the data
        data = []
        current_index = index

        while len(data) < page_size and current_index in dataset:
            data.append(dataset[current_index])
            current_index += 1

        # Determine next index
        next_index = current_index if len(data) == page_size else None

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
