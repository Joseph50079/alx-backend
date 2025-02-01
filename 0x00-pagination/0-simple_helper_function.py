#!/usr/bin/env python3

"""
0-simple_helper_function.py
"""


def index_range(page: int, page_size: int) -> tuple:
    if page == 1:
        first = 0

    else:
        first = page * 10
    last = first + page_size

    return first, last
