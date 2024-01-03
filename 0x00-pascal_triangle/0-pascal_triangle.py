#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    result = []
    
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    
    return result
