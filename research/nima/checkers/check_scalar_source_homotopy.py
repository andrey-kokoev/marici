"""Polarized equation recursion from the scalar action; exact tree comparison."""
import json,runpy
from functools import lru_cache
from itertools import product
from collections import Counter
from pathlib import Path
from sympy import symbols,diff,expand
z=runpy.run_path('research/nima/checkers/check_quartic_contact_source.py')
g,h=z['g'],z['h'];x,K=symbols('x K')
S=K*x*x/2-g*x**3/6-h*x**4/24
assert expand(diff(S,x)-(K*x-g*x*x/2-h*x**3/6))==0
# Unordered partitions account for cancellation of k! in polarized b_k/k!.
def partitions(items):
    if not items:yield ();return
    a,*tail=items
    for p in partitions(tail):
        yield ((a,),)+p
        for j in range(len(p)):
            yield p[:j]+((a,)+p[j],)+p[j+1:]
@lru_cache(None)
def trees(items):
    if len(items)==1:return ((frozenset(),0,0),)
    ans=[]
    for p in partitions(list(items)):
        if len(p) not in (2,3):continue
        for children in product(*(trees(tuple(sorted(q))) for q in p)):
            edges=set();v3=int(len(p)==2);v4=int(len(p)==3)
            for q,(es,a,b) in zip(p,children):
                edges.update(es);v3+=a;v4+=b
                if len(q)>1:edges.add(tuple(sorted(q)))
            ans.append((frozenset(edges),v3,v4))
    assert len(ans)==len(set(ans))
    return tuple(ans)
records={}
for n in (4,6):
    alltrees=trees(tuple(range(n-1)))
    planar=[t for t in alltrees if all(tuple(range(min(e),max(e)+1))==e for e in t[0])]
    records[n]={'full_counts':{str(k):v for k,v in Counter((a,b) for E,a,b in alltrees).items()},'planar_counts':{str(k):v for k,v in Counter((a,b) for E,a,b in planar).items()}}
    if n==4:
        assert Counter((a,b) for E,a,b in alltrees)=={(2,0):3,(0,1):1}
    if n==6:
        mapped={frozenset((min(e),max(e)+1) for e in E):g**a*h**b for E,a,b in planar}
        assert mapped==z['weights']
assert records[6]['full_counts']=={'(4, 0)':105,'(2, 1)':105,'(0, 2)':10}
assert any(r['nonzero'] for r in z['residuals'])
out={'status':'passed','source_derivative_checked':True,'tree_comparison':records,'six_point_planar_graph_and_coupling_equality':True,'triangle_quadric_defect_persists':True,'scope':'Formal off-pole propagator recursion; shifted two-term brackets and vanishing nested compositions are proved in packet. No global contraction on on-shell distributions or residual-to-boundary map asserted.'}
Path('research/nima/results/scalar_source_homotopy.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
