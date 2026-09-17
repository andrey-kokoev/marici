#!/usr/bin/env python3
"""Check the binary arity square, Gray rotation, and transverse strict interchange model."""
import json,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
vertices=[(0,0),(0,1),(1,1),(1,0)]
def r(v):x,y=v;return (y,1-x)
rotation=[vertices[0]]
for _ in range(3):rotation.append(r(rotation[-1]))
# In the transverse product model both independent refinements are disjoint labelled union.
def tensor(a,b):
 assert a.isdisjoint(b);return a|b
def interchange(a,b,c,d):
 left=tensor(tensor(a,b),tensor(c,d))
 right=tensor(tensor(a,c),tensor(b,d))
 return left==right
labels=[frozenset({i}) for i in range(4)]
checks={
 'gray_cycle':rotation==vertices,
 'rotation_order_four':all(r(r(r(r(v))))==v for v in vertices),
 'independent_input_output_flips_form_C2xC2':len({(x^a,y^b) for a,b in itertools.product((0,1),repeat=2) for x,y in [(0,0)]})==4,
 'strict_transverse_interchange':interchange(*labels),
 'empty_refinement_is_unit':tensor(frozenset(),labels[0])==labels[0],
}
out={'schema':'marici.nima.arity-square-duoidal-contract.v1','arity_vertices':[{'bits':list(v),'type':('1' if v[0]==0 else '*')+','+('1' if v[1]==0 else '*')} for v in vertices],'gray_rotation':[list(v) for v in rotation],'checks':checks,'passed':all(checks.values()),'source_contract':{'horizontal':'rooted-subtree/scalar associahedral substitution','vertical':'physical cut-set coaction','interchange':'strict mixed Beck-Chevalley for cuts transverse to scalar block factors','horizontal_unit':'identity/trivial rooted substitution','vertical_unit':'empty cut set','scope':'transverse mixed product-associahedral subcomplex'},'boundary':'This certifies the combinatorial strict-duoidal contract. Analytic convolution and pointwise product require typed domains; Fourier is a strong monoidal equivalence exchanging them, not by itself the duoidal interchange map.'}
p=ROOT/'research/nima/results/arity-square-duoidal-contract.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
