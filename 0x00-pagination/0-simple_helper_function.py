#!/usr/bin/env python3
"""
This module return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters.
"""


from typing import Tuple


def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
    first_page = page - 1
    return first_page, page_size
