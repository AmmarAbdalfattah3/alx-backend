#!/usr/bin/env python3
"""
This module return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters.
"""


from typing import Tuple


def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
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
