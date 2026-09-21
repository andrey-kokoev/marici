"""Exact source-length nilpotence and nonuniqueness of event refinements."""
from itertools import permutations
from pathlib import Path
import json
import sympy as s
# Free path category of the four-prime cube: source is part of its type.
paths=[]
for start in range(16):
    unused=[j for j in range(4) if not start>>j&1]
    for length in range(len(unused)+1):
        paths += [(start,w) for w in permutations(unused,length)]
assert len(paths)==168
assert max(len(w) for _,w in paths)==4
# Radical powers spanned by paths with at least k steps.
dimensions=[sum(len(w)>=k for _,w in paths) for k in range(6)]
assert dimensions[-1]==0 and dimensions[-2]>0
# Closure identity on a nonzero four-step flag remains nonnilpotent.
Id=s.eye(4)
assert Id**5==Id!=s.zeros(4)
# Same finite nilpotent target and same first-order generator, different updates.
N=s.zeros(5)
for j in range(4):N[j,j+1]=1
assert N**5==s.zeros(5) and N**4!=s.zeros(5)
U= s.eye(5)+N
V= s.eye(5)+N+N**2/2+N**3/6+N**4/24
assert U!=V and U.det()==V.det()==1
# Both prescriptions induce coherent reference changes by multiplication.
for reference in ((s.eye(5),U,U*U),(s.eye(5),V,V*V)):
    a,b,c=reference
    assert (a.inv()*b)*(b.inv()*c)==a.inv()*c
# Linearity in the individual event selects the degree-one insertion.
f=lambda a:s.eye(5)+a*N
exp=lambda a:s.eye(5)+a*N+a*a*N**2/2+a**3*N**3/6+a**4*N**4/24
assert f(3)-s.eye(5)==3*(f(1)-s.eye(5))
assert exp(3)-s.eye(5)!=3*(exp(1)-s.eye(5))
# Rational scaling: a natural linear degree-r event component must vanish for r>1.
assert all(2**r-2!=0 for r in (2,3,4))
result={'schema':'marici.grothendieck.closure-history-requirements.v1',
        'passed':True,'free_path_algebra_dimension':len(paths),
        'positive_length_ideal_power_dimensions':dimensions,
        'checks':{'typed_path_ideal_fifth_power_zero':True,
                  'four_step_flag_does_not_make_all_maps_nilpotent':True,
                  'two_coherent_same_first_order_event_rules':True,
                  'linearity_selects_squarefree_event_insertion':True},
        'scope':'Algebraic consequences and countermodels for the specified finite source; not a derivation of a unique scalar field or a unique completion from polymorphic cofiber laws.'}
p=Path(__file__).resolve().parents[1]/'results/closure-history-requirements.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
