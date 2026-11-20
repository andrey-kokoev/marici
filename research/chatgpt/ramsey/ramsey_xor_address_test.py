"""Exact two-address XOR test and minimum expression size in the full linear span."""
from itertools import combinations
from ramsey_delayed_address_move import moves, build


def main():
    n = 20
    rows = [r & ((1 << n) - 1) for r in build()[:n]]
    legal = set(moves(rows)[2]); assert len(legal) == 5
    pairs = [(i,j) for i,j in combinations(range(n),2) if rows[i]^rows[j] in legal]
    print('legal two-address expressions:', pairs)
    best = {}; span = set(); value = mask = 0
    for step in range(1 << n):
        if step:
            flip = step & -step
            mask ^= flip; value ^= rows[flip.bit_length()-1]
        span.add(value)
        if value in legal and (value not in best or mask.bit_count() < best[value].bit_count()):best[value] = mask
    print('rank:',len(span).bit_length()-1)
    ids = lambda m:[i for i in range(n) if m>>i&1]
    for col in sorted(legal):print(ids(col),'minimum XOR expression:',ids(best[col]) if col in best else None)

if __name__=='__main__':main()
