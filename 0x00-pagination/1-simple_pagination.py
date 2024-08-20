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
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        data = self.dataset()

        first_index, end_index = index_range(page, page_size)

        if first_index >= len(data):
            return []

        return [first_index:end_index]
