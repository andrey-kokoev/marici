"""Search valid edge-deleted order-39 parents for a counterexample to the six-set test."""
import csv
import itertools
from pathlib import Path
import random

path = Path(__file__).resolve().parents[2] / 'chatgpt/ramsey/ramsey_3_10_witness_39.csv'
with path.open() as f:
    base = [sum(int(x) << i for i, x in enumerate(r)) for r in csv.reader(f) if r]
full = (1 << len(base)) - 1

def independent(A, m, k):
    if not k:
        return True
    while m.bit_count() >= k:
        b = m & -m
        m ^= b
        if independent(A, m & ~A[b.bit_length()-1], k-1):
            return True
    return False

def six(A):
    for s in itertools.combinations([i for i,v in enumerate(A) if v.bit_count()==9],6):
        mask = sum(1 << i for i in s)
        neighbors = 0
        for i in s:
            neighbors |= A[i]
        if not neighbors & mask and (full & ~(mask | neighbors)).bit_count() >= 8:
            return s
    return None

if __name__ == '__main__':
    # The envelope need not be valid. Its degree-nine vertices lose no edge
    # under ANY valid deletion: a forbidden independent set survives deletions.
    envelope = base.copy()
    for i in range(len(base)):
        for j in range(i):
            if base[i] >> j & 1 and not independent(base, full & ~(base[i]|base[j]), 8):
                envelope[i] ^= 1 << j; envelope[j] ^= 1 << i
    permanent = six(envelope)
    assert permanent and all(envelope[i] == base[i] for i in permanent)
    print('permanent six-set', permanent)
    for seed in range(100):
        A = base.copy(); removed = []
        edges = [(i,j) for i in range(len(A)) for j in range(i) if A[i] >> j & 1]
        random.Random(seed).shuffle(edges)
        for i,j in edges:
            if not independent(A, full & ~(A[i]|A[j]), 8):
                A[i] ^= 1 << j; A[j] ^= 1 << i; removed.append((i,j))
        if six(A) is None:
            assert not independent(A, full, 10)
            assert all(not (A[i]&A[j]) for i,j in edges if A[i] >> j & 1)
            print('seed',seed,'removed',removed,'degree 9',sum(a.bit_count()==9 for a in A)); break
    else:
        print('No counterexample in 100 trials')
