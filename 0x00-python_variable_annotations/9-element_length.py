#!/usr/bin/env python3
'''
    python module
'''


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
        count the elements of the iterable
    '''
    return [(i, len(i)) for i in lst]
