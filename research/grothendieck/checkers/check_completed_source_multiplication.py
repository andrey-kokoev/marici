"""Exact scale-loss inequality, source vacuum hostile, and shift transport.

No source quotient norm is inferred from an analytical Gram matrix.
"""
from pathlib import Path
from collections import defaultdict
from math import comb
from fractions import Fraction
import json
ROOT=Path(__file__).resolve().parents[3]

def scale_bound(n,m,r,t):
    # Graph factorial ratio and path-length ratio, with input radii 2s,2b.
    return comb(r+t,r)*(1+n+m)**(r+t) <= 2**(r+t+n+m)*(1+n)**r*(1+m)**t
count=0
for n in range(2,25):
    for m in range(2,25):
        for r in range(1,n//2+1):
            for t in range(1,m//2+1):
                assert scale_bound(n,m,r,t);count+=1
unequal=((1024,2,1,1),(2,1024,1,1),(512,2,256,1),(2,512,1,256),(40,400,20,200))
for n,m,r,t in unequal:assert scale_bound(n,m,r,t)
# Removing the actual minimum-event hypothesis would invalidate this estimate.
assert not scale_bound(2,100,100,1)

def clean(x):return {k:v for k,v in x.items() if v}
def multiply(a,b):
    out=defaultdict(int)
    for u,c in a.items():
        for v,d in b.items():out[u+v]+=c*d
    return clean(out)
def forgotten_derivative(a,start):
    out=defaultdict(int)
    for word,c in a.items():
        vertex=start
        for p in word:
            end=vertex|1<<p
            out[vertex,end]+=c;vertex=end
    return clean(out)

hostiles=[]
for n in range(2,65):
    # A local relation with a long forgotten suffix, followed by a new diamond.
    a={tuple(range(n)):1,(1,0)+tuple(range(2,n)):-1}
    b={(n,n+1):1,(n+1,n):-1}
    da=forgotten_derivative(a,0)
    db=forgotten_derivative(b,(1<<n)-1)
    assert len(da)==len(db)==4
    joint={(e,f):c*d for e,c in da.items() for f,d in db.items()}
    selected=((0,1),((1<<n)-1,(1<<(n+1))-1))
    assert joint[selected]==1 and len(joint)==16
    assert not forgotten_derivative(multiply(a,b),0)
    # The coefficient functional has norm <=1/W_2(n+2) on presentations.
    # Input classes have norms <=2W_1(n),2W_1(2), giving this lower ratio.
    ratio=Fraction((n+3)**2,6*(n+1))
    assert ratio==Fraction(n+5,6)+Fraction(2,3*(n+1))
    assert ratio>=Fraction(n,6)
    hostiles.append({'path_lengths':[n,2],'same_scale_product_lower_ratio':str(ratio)})

def phase(r):return (-1)**(r*(r-1)//2)
phase_checks=0
for r in range(13):
    for t in range(13):
        assert phase(r+t)==phase(r)*phase(t)*(-1)**(r*t)
        for u in range(9):
            assert ((-1)**(r*t+(r+t)*u))==((-1)**(t*u+r*(t+u)))
            phase_checks+=1
result={'schema':'marici.grothendieck.completed-source-multiplication.v1','passed':True,
        'exact_weight_inequalities':count,'unequal_length_depth_cases':len(unequal),
        'forgotten_suffix_hostiles':len(hostiles),'shift_transport_checks':phase_checks,
        'first_hostile':hostiles[0],'last_hostile':hostiles[-1],
        'checks':{'scale_2s_2b_to_s_b_bound':True,'minimum_event_hypothesis_required':True,
                  'source_product_selected_coefficient_survives':True,
                  'same_scale_multiplication_unbounded_family':True,
                  'normalized_tensor_phase_coherent':True},
        'scope':'Finite exact inequalities and actual source coefficient witnesses. Completion, quotient descent and multiplicative analytical comparison are proved in the companion note, not inferred from these finite tests.'}
p=ROOT/'research/grothendieck/results/completed-source-multiplication.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
