"""Proof-sensitive sparse selector fails to commute with Farkas composition."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
rows=((-Q(1),Q(0)),(Q(1),Q(0)),(Q(0),-Q(1)),(Q(0),Q(1)))
b=(Q(0),Q(1),Q(0),Q(1))
def dot(x,y):return sum((a*z for a,z in zip(x,y)),Q(0))
def valid(p,normal,bound):return min(p)>=0 and tuple(dot(tuple(r[j] for r in rows),p) for j in (0,1))==normal and dot(b,p)==bound
def key(p):return (sum(z>0 for z in p),tuple(p))
x=((Q(1),Q(2),Q(0),Q(0)),(Q(0),Q(1),Q(1),Q(1)))
y=((Q(0),Q(0),Q(1),Q(2)),(Q(1),Q(1),Q(0),Q(1)))
for p in x:assert valid(p,(1,0),2)
for p in y:assert valid(p,(0,1),2)
local_x=min(x,key=key);local_y=min(y,key=key)
assert local_x==x[0] and local_y==y[0]
compose=lambda u,v,k,l:tuple(k*u[i]+l*v[i] for i in range(4))
staged=compose(local_x,local_y,Q(1),Q(1))
options={(i,j):compose(x[i],y[j],Q(1),Q(1)) for i,j in product(range(2),repeat=2)}
for p in options.values():assert valid(p,(1,1),4)
direct=min(options.values(),key=key)
assert staged==(1,2,1,2) and key(staged)[0]==4
assert direct==(0,1,2,3) and key(direct)[0]==3
assert staged!=direct
# Same four primitive roots support both outputs. The selector itself,
# unlike Farkas addition, is nonlinear and cannot be treated as an affine
# proof bridge or proof-path comparison cell.
report={'passed':True,'local_winners':['x0','y0'],'staged_multipliers':list(map(str,staged)),'staged_support':4,'global_winner':'x1+y0','direct_multipliers':list(map(str,direct)),'direct_support':3,'same_target':'x+y<=4','source_roots':['-x<=0','x<=1','-y<=0','y<=1'],'scope':'Finite candidate sets and support-count/lex tie-break only. Demonstrates nonfunctorial deterministic selector, not that global sparse proof is unique among all Farkas certificates, nor analytic/operational authority.'}
out=Path(__file__).resolve().parents[1]/'results/nonlinear-sparsity-selector.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
