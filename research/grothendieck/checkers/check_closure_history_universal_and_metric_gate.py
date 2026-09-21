"""Exact truncated-history universal evaluation and terminal-metric obstruction."""
import importlib.util
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('history',ROOT/'research/grothendieck/theta_interval_signature.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
zero=lambda:tuple({} for _ in range(5))
def add(a,b,scale=1):
    out=tuple(dict(x) for x in a)
    for i,row in enumerate(b):
        for k,v in row.items():out[i][k]=out[i].get(k,0)+scale*v
    return tuple({k:v for k,v in row.items() if v} for row in out)
def power(a,n):
    out=h.unit()
    for _ in range(n):out=h.concatenate(out,a)
    return out

def inverse(a):
    aug=add(a,h.unit(),-1)
    out=h.unit()
    for k in range(1,5):out=add(out,power(aug,k),(-1)**k)
    assert h.concatenate(a,out)==h.unit()==h.concatenate(out,a)
    return out

left=h.observe_route((0,1));right=h.observe_route((1,0))
r=h.concatenate(inverse(left),right)
d=add(r,h.unit(),-1)
assert not d[0] and not d[1] and d[2]
assert power(d,2)[4] and power(d,3)==zero()
assert h.concatenate(left,r)==right
# On span(1,d,d^2), right multiplication by r is an actual Jordan block.
U=s.Matrix([[1,0,0],[1,1,0],[0,1,1]])
assert (U-s.eye(3))**3==s.zeros(3) and (U-s.eye(3))**2!=s.zeros(3)
a,b,c,e,f,g=s.symbols('a b c e f g', real=True)
G=s.Matrix([[a,b,c],[b,e,f],[c,f,g]])
solutions=s.linsolve(list(U.T*G*U-G),(a,b,c,e,f,g))
solution=next(iter(solutions))
assert s.simplify(solution[-1])==0
# This is enough for Hermitian metrics too: real part restricted to real vectors
# would be a positive definite real symmetric invariant matrix.
# Universal evaluation in a concrete nilpotent algebra: 5x5 strict upper triangles.
letters={j:s.zeros(5) for j in range(15)}
for j in range(15):
    for k in range(4):letters[j][k,k+1]=s.Integer((j+2*k)%5-2)

def evaluate(poly):
    out=s.zeros(5)
    for row in poly:
        for word,coefficient in row.items():
            term=s.eye(5)
            for j in word:term=term*letters[j]
            out+=coefficient*term
    return out
assert evaluate(h.concatenate(left,right))==evaluate(left)*evaluate(right)
assert evaluate(inverse(left))*evaluate(left)==s.eye(5)
# Full source route versus product of independently calculated event factors.
route=(0,2,1,3);mask=0;product=s.eye(5)
for j in route:
    target=mask|1<<j
    v=sum((letters[k] for k in range(h.POSITION[mask],h.POSITION[target])),s.zeros(5))
    product=product*(s.eye(5)+v);mask=target
assert evaluate(h.observe_route(route))==product
result={'schema':'marici.grothendieck.closure-history-universal-metric.v1','passed':True,
        'checks':{'nilpotent_algebra_evaluation':True,'source_event_factorization':True,
                  'two_order_comparison_exact':True,'comparison_leading_degree_two':True,
                  'actual_three_dimensional_jordan_subspace':True,
                  'invariant_positive_metric_obstructed':True},
        'jordan_matrix':U.tolist(),
        'symmetric_invariant_metric_solution':[str(x) for x in solution],
        'scope':'Universal property conditional on linear event increments and nilpotent truncation; obstruction to a single positive metric invariant under the same-terminal comparison.'}
# Sympy integers converted through JSON default.
p=ROOT/'research/grothendieck/results/closure-history-universal-metric.json'
p.write_text(json.dumps(result,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2,default=str))
