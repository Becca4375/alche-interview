#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n: int) -> int:
    """Minimum Operations needed to get n H characters"""
    if not isinstance(n, int) or n <= 1:
        return 0

    clipboard = 1
    current_len = 1
    op = 0

    while current_len < n:
        if n % current_len == 0:
            op += 2
            clipboard = current_len
            current_len += current_len
        else:
            op += 1
            current_len += clipboard

    if current_len != n:
        return 0
    return op
