"""Enumerate a certified finite rational proof envelope, not all proofs."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
new=old+(((1,1),3),)
grid=tuple(Q(k,2) for k in range(5)) # 0,1/2,1,3/2,2
bound=Q(3);normal=(Q(1),Q(1))
def image(rs,m):return (sum(rs[i][0][0]*m[i] for i in range(len(m))),sum(rs[i][0][1]*m[i] for i in range(len(m)))),sum(rs[i][1]*m[i] for i in range(len(m)))
def enumerate_packets(rs):
 out=[]
 for m in product(grid,repeat=len(rs)):
  n,b=image(rs,m);c=bound-b
  if n==normal and c in grid:out.append((m,c))
 return tuple(out)
o=enumerate_packets(old);n=enumerate_packets(new)
assert o and n
assert all((m+(Q(0),),c) in n for m,c in o)
assert ((Q(0),Q(1),Q(0),Q(1)),Q(1)) in o
assert ((Q(1),Q(2),Q(0),Q(1)),Q(0)) in o
assert ((Q(0),Q(0),Q(0),Q(0),Q(1)),Q(0)) in n
assert min(n,key=lambda p:(p[0][4],p[1],p[0]))[0][4]==0
outside=(Q(2),Q(3),Q(0),Q(1))
assert image(old,outside)==((1,1),Q(4)) and max(outside)>max(grid)
def covered(m,c):return len(m) in (4,5) and all(x in grid for x in (*m,c))
assert not covered(outside,Q(1))
report={'passed':True,'root_sets':['four ordered old square roots','same four plus weak row x+y<=3'],'grid':'{0,1/2,1,3/2,2} for each multiplier and surplus','target':'normal (1,1), bound 3','old_candidates':len(o),'new_candidates':len(n),'every_old_candidate_in_new_with_zero_new_row':True,'outside_witness':'old proof (2,3,0,1;c1) targets bound5, rejected by cap2','noncoverage_policy':'OUT_OF_ENVELOPE, not proof nonexistence','scope':'Exhaustive only for explicitly specified finite rational grid and target; no global proof completeness or source issuer authorization.'}
out=Path(__file__).resolve().parents[1]/'results/finite-square-proof-envelope.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
