"""Exact all-vacuum comparison of the two raw coarse ordinary forms."""
from pathlib import Path
import contextlib
import io
import json
import runpy

ROOT = Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    src = runpy.run_path(str(ROOT/'research/grothendieck/checkers/check_six_prime_derived_block_associativity.py'))
D, relation, multiply = (src[k] for k in ('derivative','relation','multiply'))

def tensor(a, b):
    return {(x,y):c*d for x,c in a.items() for y,d in b.items() if c*d}

def observe(first, middle, last, grouping):
    a, c = relation(first,0), relation(last,0)
    w = {(middle,(False,False)):1}
    if grouping == 'left':
        cut = sum(1 << p for p in first+middle)
        image = tensor(D(multiply(a,w),0),D(c,cut))
    else:
        cut = sum(1 << p for p in first)
        image = tensor(D(a,0),D(multiply(w,c),cut))
    return {(cut,key):coefficient for key,coefficient in image.items()}

def pairing(a,b):
    # Only vacuum histories and Omega seam letters occur, all of unit norm.
    for cut,(x,y) in set(a) | set(b):
        for edge in (x,y):
            source,target,left,letter,right = edge
            assert left == right == () and letter == 0
    return sum(c*b.get(key,0) for key,c in a.items())

u = ((0,1),(2,3),(4,5))
v = ((0,2),(1,3),(4,5))
# The source comparison certificate already includes these ordinary columns.
forms = {}
for grouping in ('left','right'):
    images = [observe(*p,grouping) for p in (u,v)]
    forms[grouping] = [[pairing(a,b) for b in images] for a in images]
assert forms['left'] == [[16,4],[4,16]]
assert forms['right'] == [[16,0],[0,16]]
# Diagonal-only checks on individual basis vectors miss the difference.
assert sum(map(sum,forms['left'])) == 40
assert sum(map(sum,forms['right'])) == 32
print(json.dumps({
    'passed':True,
    'left_raw_coarse_gram':forms['left'],
    'right_raw_coarse_gram':forms['right'],
    'sum_vector_squared_forms':{'left':40,'right':32},
    'scope':'Two actual forgotten ordinary common-cell vectors. Raw derivative forms with orthogonal coarse-cut labels and unit vacuum/Omega; root factor omitted identically. Not a claim about a differently prescribed coarse assembly.'
},indent=2))
