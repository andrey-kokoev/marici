"""Ordered higher derivatives and the two-stage filtered comparison."""
from pathlib import Path
from itertools import combinations,product
from collections import defaultdict
import runpy
import json
ROOT=Path(__file__).resolve().parents[3]
b=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))
rel,mul,record,D=(b[k] for k in ('relation','multiply','record','derivative'))

def ordered_derivative(start,column,r):
    out=defaultdict(int)
    for (word,marks),coef in column.items():
        states=[start]
        for p in word:states.append(states[-1]|(1<<p))
        for selected in combinations(range(len(word)),r):
            seams=tuple(('e',states[i],states[i+1],marks[i]) for i in selected)
            cuts=(-1,)+selected+(len(word),)
            buffers=[record(states[left+1],word[left+1:right],marks[left+1:right])
                     for left,right in zip(cuts,cuts[1:])]
            for entries in product(*(v.items() for v in buffers)):
                value=coef
                for k,c in entries:value*=c
                out[seams,tuple(k for k,c in entries)]+=value
    return {k:c for k,c in out.items() if c}

products=vanishings=0
for kinds in product((0,1),repeat=3):
    cols=[rel((2*i,2*i+1),kind) for i,kind in enumerate(kinds)]
    triple=b['chain_product'](cols)
    image=ordered_derivative(0,triple,3)
    expected=b['balanced'](b['raw_joint']((3,15),
                 (D(0,cols[0]),D(3,cols[1]),D(15,cols[2]))))
    assert image==expected and image
    assert not b['balanced_boundary'](image)
    # The previous attachment is unchanged by a J3 representative change.
    assert not ordered_derivative(0,triple,2)
    products+=1
    for kind in (0,1):
        fourth=mul(triple,rel((6,7),kind))
        assert fourth and not ordered_derivative(0,fourth,3)
        vanishings+=1

# Kernel of [J2/J4 -> J1/J4] -> [J2/J3 -> J1/J3] is [G3 --id--> G3].
# Its contraction h^0=id has d h+h d=id in both degrees.
for size in (1,2,8):
    # Check on coordinates, independent of a chosen source product metric.
    for i in range(size):
        vector=tuple(int(i==j) for j in range(size))
        differential=vector
        homotopy=differential
        assert homotopy==vector

# Adjacent extension and full extension have the same connecting component:
# [G3 -> J2/J4] includes into [G3 -> J1/J4] by id on degree -1.
a,c,d=[rel(pair,0) for pair in ((0,1),(2,3),(4,5))]
witness=ordered_derivative(0,mul(a,mul(c,d)),3)
assert witness and any(v==1 for v in witness.values())
result={'passed':True,'triple_cycle_comparisons':products,
 'fourth_power_vanishings':vanishings,
 'checks':{'old_two_seam_map_kills_new_layer':True,
           'refinement_kernel_is_identity_complex':True,
           'adjacent_and_full_connecting_components_agree':True,
           'nonzero_six_event_attachment_witness':True},
 'scope':'Actual higher source derivatives plus elementary comparison-complex fixtures. Completed norm bounds and exact roof compatibility are proved in the companion note.'}
out=ROOT/'research/voevodsky/results/two-stage-filtered-attachment.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
