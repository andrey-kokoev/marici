"""Minimum worst-case coordinate probes to decide one boundary, given exactly three reds."""
from functools import cache
from itertools import combinations

words = [sum(1 << i for i in a) for a in combinations(range(10), 3)]
full = (1 << len(words)) - 1
ok = sum(1 << j for j,w in enumerate(words) if ((w ^ (w >> 1)) & 511).bit_count() == 1)
cols = [sum(1 << j for j,w in enumerate(words) if w >> i & 1) for i in range(10)]
@cache
def depth(states):
    if not states & ok or not states & (full ^ ok): return 0
    return min(1 + max(depth(states & c), depth(states & ~c)) for c in cols if states & c and states & ~c)
print('accepted:', ok.bit_count(), 'depth:', depth(full), 'depth by first column:', [1 + max(depth(c),depth(full ^ c)) for c in cols]); assert depth(full)==4
