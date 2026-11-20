"""Enumerate segment contribution profiles at the two proposed endpoints."""
from itertools import combinations_with_replacement
from collections import Counter
from ramsey_interface_union_test import contributions


def profiles(target):
    return [Counter(p) for n in range(1,min(target)+1)
            for p in combinations_with_replacement(sorted(contributions),n)
            if tuple(map(sum,zip(*p)))==target]

if __name__=='__main__':
    for t in [(3,6,6),(8,6,6)]:
        p=profiles(t);assert len(p)==1;print(t,p[0])
