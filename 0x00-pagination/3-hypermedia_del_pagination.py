#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get_hyper_index of pagination """

        if not isinstance(index, int):
            raise AssertionError
        if index == None:
            index = 0

        assert index <= len(self.indexed_dataset().values()) + page_size

        hypermedia = dict()
        hypermedia['index'] = index
        x = index

        hypermedia['data'] = list(self.indexed_dataset().values())[index : page_size + x]
        hypermedia['page_size'] = page_size
        hypermedia['next_index'] =  list(self.indexed_dataset().keys())[index : page_size + x][-1] + 1

        return hypermedia
