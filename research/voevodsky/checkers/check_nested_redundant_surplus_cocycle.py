"""Three weak redundant rows: staged surplus contributions obey additive cocycle."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
base=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
rows=base+(((1,1),3),((2,1),5),((3,1),7))
def image(rs,m,c):return tuple(sum(Q(rs[i][0][j])*m[i] for i in range(len(m))) for j in (0,1)),sum(Q(rs[i][1])*m[i] for i in range(len(m)))+c
def staged(v,c):
 a,x,b,y,z1,z2,z3=map(Q,v);c=Q(c)
 x+=z3;z2+=z3;c+=z3 # R3 -> R2+xhigh+1 surplus
 x+=z2;z1+=z2;c+=z2 # R2 -> R1+xhigh+1 surplus
 x+=z1;y+=z1;c+=z1 # R1 -> xhigh+yhigh+1 surplus
 return (a,x,b,y),c
def direct(v,c):
 a,x,b,y,z1,z2,z3=map(Q,v)
 return (a,x+z1+2*z2+3*z3,b,y+z1+z2+z3),Q(c)+z1+2*z2+3*z3
checks=0
for zs in product((Q(0),Q(1,2),Q(1)),repeat=3):
 v=(Q(0),Q(0),Q(0),Q(0))+zs
 assert staged(v,0)==direct(v,0)
 assert image(rows,v,Q(0))==image(base,*direct(v,0))
 assert min((*direct(v,0)[0],direct(v,0)[1]))>=0
 checks+=1
assert checks==27
unit=(Q(0),)*6+(Q(1),)
assert image(rows,unit,0)==((3,1),Q(7))
assert image(base,(0,3,0,1),0)==((3,1),Q(4))
assert image(base,(0,3,0,1),3)==((3,1),Q(7))
report={'passed':True,'rational_three_row_cases':checks,'nested_surplus':'z1+2*z2+3*z3','direct_surplus':'z1+2*z2+3*z3','naive_no_surplus_R3_wrong_bound':'4 rather than 7','primitive_dependency':'x-high and y-high plus retained R1/R2/R3 derivation chain if proof history replay demanded','scope':'Fixed square, three chosen weaker redundant rows, nonnegative proof multipliers. Packet cocycle not a path 3-cell, canonical selector or owner grant.'}
out=Path(__file__).resolve().parents[1]/'results/nested-redundant-surplus-cocycle.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
