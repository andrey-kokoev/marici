"""Classify every XOR pair-equality pattern for eight fixed 3-bit profiles.
Affine functions added to extra bits do not change equality for pairs with equal
base XOR. Normalize extra Boolean functions to vanish on the affine basis 0,1,2,4.
A pair collision then means a four-column affine plane has zero lifted parity.
"""
from itertools import combinations
from collections import Counter
import json
from pathlib import Path

def audit():
    pairs=list(combinations(range(8),2));planes=[t for t in combinations(range(8),4) if t[0]^t[1]^t[2]^t[3]==0];assert len(planes)==14
    free=(3,5,6,7); patterns={0:()};base=Path(__file__).parent
    for extra in range(4):
        shapes={}
        for fs in combinations(range(1,16),extra):
            labels=[j+8*sum(((f>>free.index(j))&1)<<i for i,f in enumerate(fs)) if j in free else j for j in range(8)]
            flat=tuple(t for t in planes if not(labels[t[0]]^labels[t[1]]^labels[t[2]]^labels[t[3]]));shape=len({labels[a]^labels[b] for a,b in pairs});shapes[flat]=shape
        # At most this many extra bits; repeated bits or zero add no restrictions.
        if extra:shapes.update(old)
        old=shapes.copy();print('width',extra+3,'distinct pair partitions by number of pair labels:',sorted(Counter(shapes.values()).items()))
        for bits in (4,5,6):
            path=base/f'ramsey_38_cell_{bits}bit_{25 if bits==4 else 26}.json';rows=json.loads(path.read_text())['rows'];bad=set()
            for t in planes:
                for a,b in combinations(t,2):
                    c,d=sorted(set(t)-{a,b});
                    if any((rows[8*i+a]>>(8*j+b)^rows[8*i+c]>>(8*j+d))&1 for i in range(3) for j in range(3)):bad.add(t);break
            # Same-column and swapped-column readings must also match independent of the lift.
            for i,j in combinations(range(3),2):
                assert len({rows[8*i+a]>>(8*j+a)&1 for a in range(8)})==1
                assert all(not ((rows[8*i+a]>>(8*j+b)^rows[8*i+b]>>(8*j+a))&1) for a,b in pairs)
            print('witness',bits,'compatible partitions',sum(not bad.intersection(flat) for flat in shapes),'forbidden planes',len(bad))
if __name__=='__main__':audit()
