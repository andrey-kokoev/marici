"""Coordinate lex choice fails row reorder; named-root lex survives transport."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
names=('x-low','x-high','y-low','y-high')
B=(Q(1),Q(2),Q(0),Q(1));C=(Q(0),Q(1),Q(1),Q(2))
assert min((B,C))==C
order=(2,3,0,1);scale=(Q(2),Q(3),Q(1,2),Q(4))
def move(v):return tuple(v[i]/s for i,s in zip(order,scale))
b,c=move(B),move(C)
assert min((b,c))==b and move(min((B,C)))==c and b!=c
labelled=lambda v,old_names:tuple(v[old_names.index(label)] for label in sorted(names))
assert min((B,C),key=lambda v:labelled(v,names))==C
new_names=tuple(names[i] for i in order)
# Convert transported multipliers to invariant source-row contributions:
# new scale * new multiplier recovers original value at the named row.
def rooted(v):return tuple(scale[new_names.index(label)]*v[new_names.index(label)] for label in sorted(names))
assert rooted(b)==labelled(B,names) and rooted(c)==labelled(C,names)
assert min((b,c),key=rooted)==c
checks=0
for s in product((Q(1,2),Q(1),Q(2)),repeat=4):
 x=tuple(B[i]/s[i] for i in range(4));y=tuple(C[i]/s[i] for i in range(4))
 assert min((x,y))==y # fixed row order and positive scales preserve raw lex
 checks+=1
assert checks==81
report={'passed':True,'raw_lex_original':'C','raw_lex_after_reorder':'B','transported_original_choice':'C','raw_lex_naturality_fails':True,'root_named_contribution_lex_stable':True,'fixed_order_positive_scale_cases':checks,'scope':'Frozen two zero-surplus candidate proofs of x+y<=3 and identified row roots. Named-root policy presupposes retained name bijection; neither policy is composition-functorial or an owner-granted selector.'}
out=Path(__file__).resolve().parents[1]/'results/square-lex-policy-naturality.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
