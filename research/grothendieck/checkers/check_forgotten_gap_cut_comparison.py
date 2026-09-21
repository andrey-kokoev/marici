"""Exact marked-cut localization, multicut coherence, and multiplicity checks."""
from itertools import combinations_with_replacement, combinations
from collections import defaultdict, Counter
from math import comb
from pathlib import Path
import json

def masks(n):
    for k in range(n+1):yield from combinations(range(1,n+1),k)

def rank(mask,j):return sum(i<=j for i in mask)
def low(mask,r):return 0 if r==0 else mask[r-1]
def high(n,mask,r):return n if r==len(mask) else mask[r]-1

def pieces(mask,record_cuts):
    ends=(0,)+tuple(record_cuts)+(len(mask),)
    return tuple(mask[a:b] for a,b in zip(ends,ends[1:]))

fiber_count=0;tuple_count=0;nested_count=0
for n in range(7):
    for mask in masks(n):
        for q in range(4):
            fibers=defaultdict(list)
            raw=Counter()
            for js in combinations_with_replacement(range(n+1),q):
                rs=tuple(rank(mask,j) for j in js)
                fibers[rs].append(js)
                raw[pieces(mask,rs)]+=1
                tuple_count+=1
                # Forgetting a cut and repeating a cut commute with projection.
                for a in range(q):
                    assert tuple(rank(mask,j) for j in js[:a]+js[a+1:])==rs[:a]+rs[a+1:]
                    assert tuple(rank(mask,j) for j in js[:a]+(js[a],)+js[a:])==rs[:a]+(rs[a],)+rs[a:]
            corrected=Counter()
            for rs,js_list in fibers.items():
                lo=tuple(low(mask,r) for r in rs)
                hi=tuple(high(n,mask,r) for r in rs)
                assert lo in js_list and hi in js_list
                assert all(all(a<=b<=c for a,b,c in zip(lo,js,hi)) for js in js_list)
                # The pointwise-order fiber has initial and terminal objects.
                # Its nerve is contractible, so its Euler weight is one.
                corrected[pieces(mask,rs)]+=1
                fiber_count+=1
            expected=Counter(pieces(mask,rs) for rs in combinations_with_replacement(range(len(mask)+1),q))
            assert corrected==expected
            assert sum(raw.values())==comb(n+q,q)
            assert sum(corrected.values())==comb(len(mask)+q,q)
        # Further forgetting commutes with rank and both contraction sections.
        for subindex in masks(len(mask)):
            smaller=tuple(mask[i-1] for i in subindex)
            for j in range(n+1):
                assert rank(smaller,j)==rank(subindex,rank(mask,j))
            for r in range(len(smaller)+1):
                assert low(mask,low(subindex,r))==low(smaller,r)
                assert high(n,mask,high(len(mask),subindex,r))==high(n,smaller,r)
            nested_count+=1
# The most elementary coalgebra failure: forgotten single event gives two cuts.
n=1;mask=()
assert len(list(range(n+1)))==2 and len({rank(mask,j) for j in range(n+1)})==1
# A visible internal gap, not just a vacuum/end effect.
assert [j for j in range(4) if rank((1,3),j)==1]==[1,2]
result={'schema':'marici.grothendieck.forgotten-gap-cut-comparison.v1',
        'passed':True,'max_source_events':6,'max_simultaneous_cuts':3,
        'cut_tuples_checked':tuple_count,'contractible_fibers_checked':fiber_count,
        'nested_masks_checked':nested_count,
        'checks':{'fiber_initial_and_terminal_objects':True,
                  'cut_deletion_and_repetition':True,'nested_forgetting_sections':True,
                  'corrected_cut_sum_equals_record_deconcatenation':True,
                  'raw_source_cut_multiplicity_is_different':True},
        'scope':'Marked-path localization and record coefficient cuts. Does not identify distinct arithmetic endpoint objects or assert the original source cut functor is an equivalence.'}
p=Path(__file__).resolve().parents[1]/'results/forgotten-gap-cut-comparison.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
