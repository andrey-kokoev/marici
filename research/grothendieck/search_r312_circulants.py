"""Bounded reproducible cyclic search; exact target-size independent-set test."""
import random
from itertools import combinations


def independent(mask, need, adj):
    if not need:
        return True
    while mask.bit_count() >= need:
        b = mask & -mask
        mask ^= b
        if independent(mask & ~adj[b.bit_length()-1], need-1, adj):
            return True
    return False


def search(n, trials):
    rng = random.Random(n)
    seen = set()
    best = n
    for _ in range(trials):
        order = list(range(1, n//2+1))
        rng.shuffle(order)
        s = set()
        for d in order:
            t = s | {d, n-d}
            if not any((x+y)%n in t for x in t for y in t):
                s = t
        key = tuple(sorted(s))
        if key in seen:
            continue
        seen.add(key)
        adj = [sum(1 << ((v+d)%n) for d in s) for v in range(n)]
        # By translation an independent set of maximum size contains 0.
        candidates = ((1 << n)-2) & ~adj[0]
        if independent(candidates, min(best, 13)-1, adj):
            continue
        a = next(k for k in range(1, n) if not independent(candidates,k,adj))
        assert not any(adj[v] & adj[w] for v,w in combinations(range(n),2) if adj[v] >> w & 1)
        best = a
        print(n, 'alpha', a, 'distances', sorted(d for d in s if d<=n//2), flush=True)
    print(n, 'distinct labelled distance sets tested:', len(seen), flush=True)

if __name__ == '__main__':
    for n in (45,46,47,48,49,50,51,52):
        search(n, 150)
