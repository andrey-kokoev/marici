"""Two positive-bound syzygies yield different zero-surplus Farkas proofs."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
rows=(Q(-1),Q(1),Q(1));bounds=(Q(0),Q(1),Q(1))
d1=(Q(1),Q(1),Q(0));d2=(Q(1),Q(0),Q(1))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))
def valid(m,c,target,limit):return min(m)>=0 and c>=0 and dot(rows,m)==target and dot(bounds,m)+c==limit
def norm(m,c,d,target,limit):
 assert valid(m,c,target,limit) and min(d)>=0 and dot(rows,d)==0 and dot(bounds,d)>0
 lam=c/dot(bounds,d);out=tuple(x+lam*y for x,y in zip(m,d))
 assert valid(out,Q(0),target,limit);return out
checks=0
for cap,b in product((Q(1),Q(3,2),Q(2),Q(3)),(Q(1),Q(3,2),Q(2))):
 if b>cap:continue
 m=(b-1,b,Q(0));c=cap-b;assert valid(m,c,Q(1),cap)
 n1=norm(m,c,d1,Q(1),cap);n2=norm(m,c,d2,Q(1),cap)
 assert valid(n1,0,Q(1),cap) and valid(n2,0,Q(1),cap)
 if c>0:assert n1!=n2
 checks+=1
start=(Q(0),Q(1),Q(0));n1=norm(start,Q(1),d1,Q(1),Q(2));n2=norm(start,Q(1),d2,Q(1),Q(2))
assert n1==(Q(1),Q(2),Q(0)) and n2==(Q(1),Q(1),Q(1))
k=tuple(y-x for x,y in zip(d1,d2));assert k==(Q(0),Q(-1),Q(1)) and dot(rows,k)==dot(bounds,k)==0
assert tuple(n1[i]+k[i] for i in range(3))==n2
# The signed zero-bound direction does not permit unrestricted movement:
assert min(tuple(n1[i]+3*k[i] for i in range(3)))<0
assert n1!=n2 # retaining primitive row identities distinguishes proof replay
report={'passed':True,'cases_checked':checks,'start':['0','1','0','c=1'],'normal_d1':['1','2','0','c=0'],'normal_d2':['1','1','1','c=0'],'zero_bound_signed_transfer':['0','-1','1'],'transfer_after_three_unit_steps_refused_by_nonnegativity':True,'scope':'Duplicated but separately rooted primitive upper inequalities on [0,1]. Competing proof multipliers, same semantic inclusion and bound; candidate redistribution is not an admitted proof 2-cell, source-row identity quotient, or analytic authority.'}
out=Path(__file__).resolve().parents[1]/'results/competing-source-syzygies.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
