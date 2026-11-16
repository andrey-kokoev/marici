#!/usr/bin/env python3
"""Exact, standard-library verification of explicit Ramsey local-obstruction separation witnesses.

For a 6-regular hypothetical R(3,7) counterexample on 23 vertices, fix root v,
S=N(v) (6 independent vertices), and T (16 vertices).
Each T vertex gets its 6-bit support in S; its remaining internal degree is 6-|support|.

Records of class 'five_way_needed' satisfy every degree, triangle and size<=4
support-deficiency clause, but violate at least one size-5 clause.
Records of class 'triangle_needed' satisfy degree and all size<=5 support-
deficiency clauses, but contain a red triangle.

No LP/MILP or graph-isomorphism software used by this verifier.
"""
import json
from itertools import combinations
from pathlib import Path

FILE=Path(__file__).with_name('ramsey_witness_separation.json')

def check(record):
    s=record['supports'];E={tuple(sorted(x)) for x in record['red_edges']}
    assert len(s)==16 and all(1<=m.bit_count()<=3 for m in s)
    assert all(sum((m>>i)&1 for m in s)==5 for i in range(6))
    assert len(E)==33
    assert len(E)==len(record['red_edges'])
    assert all(0<=a<b<16 and not (s[a]&s[b]) for a,b in E)
    for i in range(16):
        assert sum(i in e for e in E)==6-s[i].bit_count()
    triangles=[U for U in combinations(range(16),3)
               if all(e in E for e in combinations(U,2))]
    bad=[]
    for k in range(2,6):
        for U in combinations(range(16),k):
            union=0
            for i in U:union|=s[i]
            if union.bit_count()>=k:continue
            if not any(e in E for e in combinations(U,2)):
                bad.append(U)
    if record['class']=='five_way_needed':
        assert not triangles
        assert bad and all(len(U)==5 for U in bad)
    elif record['class']=='triangle_needed':
        assert not bad
        assert triangles
    else:
        raise ValueError('Unknown class')
    return len(triangles),len(bad)

def main():
    data=json.loads(FILE.read_text())
    assert data['schema']=='ramsey.witness-separation.v1'
    counts={'five_way_needed':0,'triangle_needed':0}
    for record in data['witnesses']:
        tri, bad=check(record)
        counts[record['class']]+=1
        print(record['class'], 'r/index', (record['r'],record['index']),
              'red triangles',tri,'deficient blue witness sets',bad)
    assert counts=={'five_way_needed':6,'triangle_needed':11}
    print('VERIFIED:',counts,'exact integral witnesses, 33 red edges each.')

if __name__=='__main__':main()
