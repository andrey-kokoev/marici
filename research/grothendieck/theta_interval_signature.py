"""Event-segmented interval signatures, before route aggregation.

Coefficients refer to the fifteen arithmetic interval atoms, not sampled theta
values. Physical realization uses the separately established theta synthesis H.
"""
from itertools import product
from math import prod

PRIMES = (2, 3, 5, 7)
LABELS = {m: 2*prod(PRIMES[j] for j in range(4) if m >> j & 1)
          for m in range(16)}
POSITION = {m: i for i, m in enumerate(sorted(LABELS, key=LABELS.get))}


def unit():
    return ({(): 1}, {}, {}, {}, {})


def concatenate(left, right):
    """Truncated tensor product; chronological order, including scalar mass."""
    if len(left) != 5 or len(right) != 5:
        raise ValueError('Expected degrees zero through four')
    out = tuple({} for _ in range(5))
    for degree in range(5):
        for k in range(degree+1):
            for u, a in left[k].items():
                for v, b in right[degree-k].items():
                    key = u+v
                    out[degree][key] = out[degree].get(key, 0)+a*b
    return tuple({k:v for k,v in d.items() if v != 0} for d in out)


def observe_route(word, start=0):
    if not isinstance(start, int) or not 0 <= start < 16:
        raise ValueError('Invalid start vertex')
    result, mask = unit(), start
    for j in word:
        if not isinstance(j, int) or not 0 <= j < 4 or mask & (1 << j):
            raise ValueError('A route must add an unused prime')
        target = mask | (1 << j)
        event = ({(): 1}, {(a,): 1 for a in range(POSITION[mask], POSITION[target])}, {}, {}, {})
        result = concatenate(result, event)
        mask = target
    return result


def observe_mixture(routes):
    """Items (coefficient, start, word); observe before linear aggregation."""
    out = tuple({} for _ in range(5))
    for coefficient, start, word in routes:
        for degree, channel in enumerate(observe_route(word, start)):
            for key, value in channel.items():
                out[degree][key] = out[degree].get(key, 0)+coefficient*value
    return tuple({k:v for k,v in d.items() if v != 0} for d in out)
