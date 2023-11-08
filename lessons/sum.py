"""Summing the elements of a list using different loops!"""

__author__ = "730477957"


def w_sum(vals: list[float]) -> float: 
    """Takes a list of floats and returns sum of all elemnts."""
    idx: int = 0 
    sum_1: float = 0.0 
    while idx < len(vals):
        sum_1 += vals[idx]
        idx += 1
    return sum_1
        
        
def f_sum(vals: list[float]) -> float: 
    """Calculates sum of all elements but uses a for... in loop."""
    idx: int = 0
    sum: float = 0.0
    for number in vals: 
        sum += vals[idx]
        idx += 1
    return sum
        

def f_range_sum(vals: list[float]) -> float: 
    """Calculates sum of all elements uses for ... in range loop."""
    idx: int = 0 
    sum: float = 0.0 
    for idx in range(0, len(vals)):
        sum += vals[idx]
        idx += 1
    return sum
    
