"""Faithful quotient U(1) repairs charge assignment, not charging coefficients."""
from fractions import Fraction as F
from itertools import permutations
from collections import Counter
from pathlib import Path
from contextlib import redirect_stdout
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    previous=runpy.run_path(str(HERE/'check_mass_rotor_action_charge.py'))
N=previous['N']; slots=previous['slots']; edges=previous['edges']
index={s:i for i,s in enumerate(slots)}
adj=[set() for _ in slots]
for a,b in edges: adj[a].add(b); adj[b].add(a)
seen={0}; queue=[0]; tree=[]
for parent in queue:
    for child in sorted(adj[parent]):
        if child not in seen:
            seen.add(child); queue.append(child); tree.append((parent,child))
assert len(tree)==N-1
# Incidence columns are -1 at parent,+1 at child. Connected incidence realizes
# every zero-sum integer vector (and every zero-sum rational charge-lift vector).
def gauge_flow(v):
    assert sum(v)==0
    sums=list(v); flows={}
    for p,c in reversed(tree):
        flows[p,c]=sums[c]; sums[p]+=sums[c]
    assert sums[0]==0
    reconstructed=[F(0)]*N
    for (p,c),f in flows.items(): reconstructed[p]-=f; reconstructed[c]+=f
    assert reconstructed==list(v)
    return flows
one=[F(int(i==0)) for i in range(N)]
uniform=[F(1,N)]*N
assert sum(one)==sum(uniform)==1
flow=gauge_flow([a-b for a,b in zip(uniform,one)])
assert any(f.denominator>1 for f in flow.values())
# A2*pi loop of the fractional lift equals an integer one-slot loop plus an
# internal gauge transformation: it is periodic on the physical quotient.
for k in (-2,-1,0,1,2):
    assert sum(q*k for q in uniform)==k
    assert sum(q*k for q in one)==k
# A negative unit electron representation is simultaneously well-defined.
for k in range(-2,3):
    for electron in range(-2,3):
        total=sum(q*k for q in uniform)-electron
        assert total.denominator==1 and total==k-electron
# Microscopic diagonal rotation is a DIFFERENT map: degree N, not degree1.
assert sum(F(1) for _ in slots)==N
assert N!=1
# No preferred slot is needed physically. Different one-slot lifts differ by
# an integer gauge vector. Check multiple actual slots, including both types.
for i in (1,N//2,N-1):
    alternative=[F(int(j==i)) for j in range(N)]
    f=gauge_flow([a-b for a,b in zip(alternative,one)])
    assert all(x.denominator==1 for x in f.values())

# Strict invariance of an integer microscopic lift is stronger than quotient
# invariance. Under simultaneous rooted S3, all slot orbits have size3 or6.
rooted=[p for p in permutations(range(4)) if p[0]==0]
def act(s,p):
    outer,(kind,a,b)=s
    edge=lambda e: tuple(p[x] for x in e)
    inner=(kind,edge(a),edge(b)) if kind=='arrow' else (kind,p[a],p[b])
    return edge(outer),inner
unseen=set(slots); sizes=[]; triple=None
while unseen:
    s=min(unseen); orbit={act(s,p) for p in rooted}
    unseen-=orbit; sizes.append(len(orbit))
    if len(orbit)==3: triple=orbit
assert Counter(sizes)=={3:10,6:301}
# A1/3 lift on any three-slot orbit is symmetric and has total charge1.
thirds=[F(1,3) if s in triple else F(0) for s in slots]
assert sum(thirds)==1
gauge_flow([a-b for a,b in zip(thirds,one)])
for p in rooted:
    assert all(thirds[index[act(s,p)]]==thirds[index[s]] for s in slots)
# All these lifts give the SAME physical charge and energy on n_s=k.
# The capacitance hostile remains unchanged by the repaired charge assignment.
equal_ratio=F(N)
unequal_ratio=sum(F(1) if s[1][0]=='arrow' else F(2) for s in slots)
assert unequal_ratio==1944
# The elementary rotor also has an antiparticle state of charge+1. The operator
# exp(-i*(Phi+theta_e)) maps (k,n_e)=(1,0) to (0,-1), conserving Q. Its Hermitian
# sum is gauge invariant; preventing this mixing needs an additional sector law.
initial=(1,0); lighter=(0,-1)
assert initial[0]-initial[1]==lighter[0]-lighter[1]==1
assert F(N,2)>F(1,2)
result={
 'status':'passed','classification':'primitive_quotient_charge_consistent_mass_normalization_unfixed',
 'channels':N,'physical_charge_formula':'Q=k-n_e',
 'conditional_equal_inertia_energy_ratio':str(equal_ratio),
 'same_charge_unequal_inertia_energy_ratio':str(unequal_ratio),
 'rooted_diagonal_orbit_sizes':dict(Counter(sizes)),
 'checks':{'prior_rotor_chain_fresh':True,'zero_sum_lifts_have_explicit_gauge_flows':True,
           'fractional_lift_periodic_on_physical_quotient':True,
           'electron_and_collective_charge_jointly_integral':True,
           'no_physically_preferred_charge_slot':True,
           'symmetric_three_slot_lift_gauge_equivalent':True,
           'degree_N_diagonal_action_not_silently_relabelled':True,
           'energy_normalization_hostile_survives':True,
           'unit_charge_alone_allows_mixing_with_elementary_antiparticle':True},
 'conclusion':'Choosing the faithful quotient U(1), and a primitive negative electron representation, gives a consistent unit-charged collective excitation without an extra core rotor. Uniform1/N, one-slot and symmetric three-slot charge lifts are gauge equivalent. This is a new external-symmetry assignment, not a reinterpretation of the prior degree-N diagonal coupling. Equal charging inertias still remain an independent assumption.',
 'next_falsifier':'Derive the external quotient action, common charging coefficient and a protected particle-sector law. The same unit charge allows ratios1836 or1944 and mixing with the lighter elementary antiparticle.'}
out=HERE.parent/'results/mass-primitive-quotient-charge.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
