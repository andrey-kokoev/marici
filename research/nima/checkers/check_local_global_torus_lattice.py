"""Six-point integral lattice audit for the local/global torus quotient."""
import json
from pathlib import Path
from math import gcd, lcm, prod
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
source=json.loads(Path('research/nima/results/triangle_recovery.json').read_text())
assert source['status']=='passed'
T=[frozenset(tuple(e) for e in t) for t in source['triangulations']]
channels=sorted(set().union(*T))
A=Matrix([[int(c in t) for c in channels] for t in T])
def primitive(v):
    d=lcm(*(int(x.q) for x in v));r=[int(d*x) for x in v];g=gcd(*r)
    return [x//g for x in r]
def smith(m):
    d=smith_normal_form(m,domain=ZZ)
    return [abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]]
G=Matrix([primitive(v) for v in A.T.nullspace()])
local=[]
for c in channels:
    inside=set(range(c[0],c[1]+1));cells={}
    for k,t in enumerate(T):
        if c in t:
            left=frozenset(e for e in t-{c} if set(e)<=inside)
            cells[left,(t-{c})-left]=k
    ls=sorted({a for a,b in cells},key=repr);rs=sorted({b for a,b in cells},key=repr)
    for a in ls[1:]:
        for b in rs[1:]:
            row=[0]*14
            for pair,s in [((a,b),1),((ls[0],rs[0]),1),((a,rs[0]),-1),((ls[0],b),-1)]:row[cells[pair]]+=s
            local.append(row)
R=Matrix(local)
assert R.rank()==3 and G.rank()==5
assert R*A==Matrix.zeros(3,9) and G*A==Matrix.zeros(5,9)
rows=list(local);complement=[]
for raw in G.tolist():
    row=list(map(int,raw))
    if Matrix(rows+[row]).rank()>len(rows):rows.append(row);complement.append(row)
S=Matrix(rows)
assert len(complement)==2 and S.rank()==5
assert smith(G)==[1]*5 and smith(R)==[1]*3
result={'status':'passed','global_smith':smith(G),'local_smith':smith(R),'combined_smith':smith(S),'combined_index_in_saturation':prod(smith(S)), 'complement':complement,'triangulations':source['triangulations'], 'scope':'Integral six-point lattice test; Smith factors distinguish rational independence from a character-lattice basis.'}
Path('research/nima/results/local_global_torus_lattice.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='triangulations'}))
