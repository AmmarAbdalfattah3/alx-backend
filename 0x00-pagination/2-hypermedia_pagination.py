#!/usr/bin/env python3
"""
This module displays the appropriate page of the dataset
"""


import csv
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the range of indexes for pagination.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """This method  find the correct indexes to paginate
           the dataset correctly and return the appropriate
           page of the dataset.
        """
        assert (isinstance(page, int) and
                page > 0), "Page argument must be a positive integer"
        assert (isinstance(page_size, int) and
                page_size > 0), "Page_size argument must be a positive integer"

        data = self.dataset()

        start_index, end_index = index_range(page, page_size)

        if start_index >= len(data):
            return []

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary with pagination details and dataset page."""
        assert (isinstance(page, int) and
                page > 0), "Page argument must be a positive integer"
        assert (isinstance(page_size, int) and
                page_size > 0), "Page_size argument must be a positive integer"

        data = self.dataset()

        total_items = len(data)
        total_pages = math.ceil(total_items / page_size)

        page_data = self.get_page(page, page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
