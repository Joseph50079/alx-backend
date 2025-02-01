#!/usr/bin/env python3

"""
1-simple_pagination.py
"""

import csv
import math
from typing import List


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
        """get the page of index """

        if not isinstance(page, int) or not isinstance(page_size, int):
            raise AssertionError
        assert page >= 0 and page_size > 0
        tup = index_range(page, page_size)
        if tup[0] >= len(self.dataset()) or tup[1] >= len(self.dataset()):
            return []
        paginate = self.dataset()[tup[0]: tup[1]]
        return paginate


def index_range(page: int, page_size: int) -> tuple:
    """index_range for pagination """

    if page == 1:
        first = 0

    else:
        first = page_size * (page - 1)
    last = first + page_size

    return first, last
