"""Cut maps descend through four-event product relations in source coordinates."""
from pathlib import Path
from itertools import permutations, product, combinations
import contextlib
import io
import json
import runpy
ROOT = Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    s = runpy.run_path(str(ROOT/'research/grothendieck/checkers/check_six_prime_derived_block_associativity.py'))
D, record, multiply, relation = (s[k] for k in ('derivative','record','multiply','relation'))

def tensor(a,b):
    return {(x,y):c*d for x,c in a.items() for y,d in b.items() if c*d}

def cut(column, start, side):
    out = {}
    for (word, marks), coefficient in column.items():
        mid = start | sum(1 << p for p in word[:2])
        first, last = {(word[:2],marks[:2]):1}, {(word[2:],marks[2:]):1}
        if side == 'left':
            value = tensor(D(first,start),record(word[2:],marks[2:],mid))
        else:
            value = tensor(record(word[:2],marks[:2],start),D(last,mid))
        for key,c in value.items():
            label = (mid,key)
            out[label] = out.get(label,0)+coefficient*c
    return {k:c for k,c in out.items() if c}

killed = comparisons = 0
for items in combinations(range(6),4):
    outside = tuple(p for p in range(6) if p not in items)
    for start in (0,sum(1 << p for p in outside)):
        for col in s['power_basis'](items).values():
            for side in ('left','right'):
                assert not cut(col,start,side)
                killed += 1
        for first,last in s['blocks'](items):
            mid = start | sum(1 << p for p in first)
            for kind in (0,1):
                for word in permutations(last):
                    for marks in product((False,True),repeat=2):
                        a = relation(first,kind)
                        w = {(word,marks):1}
                        expected = {(mid,k):v for k,v in tensor(D(a,start),record(word,marks,mid)).items()}
                        assert cut(multiply(a,w),start,'left') == expected
                        comparisons += 1
                for word in permutations(first):
                    for marks in product((False,True),repeat=2):
                        w = {(word,marks):1}
                        c = relation(last,kind)
                        expected = {(mid,k):v for k,v in tensor(record(word,marks,start),D(c,mid)).items()}
                        assert cut(multiply(w,c),start,'right') == expected
                        comparisons += 1
print(json.dumps({'passed':True,'product_basis_cut_vanishings':killed,
 'coarse_restriction_comparisons':comparisons,
 'scope':'Actual cut formulas in finite source coordinates. Does not identify inherited coarse Green forms with refined tensor forms.'},indent=2))
