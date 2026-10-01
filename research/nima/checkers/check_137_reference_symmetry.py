"""Exact reference-preserving symmetry audit for 137 comparison weights.

Two independent four-state carriers, each with directed reference (0,1).
Admissible local permutations fix both reference endpoints, so form S2.
All slot weights below are trial measures, not measured coupling inputs.
"""
from itertools import permutations, product
from fractions import Fraction as F
from collections import defaultdict, Counter

V = tuple(range(4))
reference = (0,1)
perms = [p for p in permutations(V) if (p[0],p[1]) == reference]
edges = [(a,b) for a,b in product(V,repeat=2) if a != b and (a,b) != reference]
slots = [('arrow',e,f) for e,f in product(edges,repeat=2)]
slots += [('state',a,b) for a,b in product(V,repeat=2)]


def act(slot,p,q):
    kind,a,b = slot
    if kind == 'arrow':
        return kind,tuple(p[x] for x in a),tuple(q[x] for x in b)
    return kind,p[a],q[b]


orbits = {}
for slot in slots:
    orbit = frozenset(act(slot,p,q) for p,q in product(perms,repeat=2))
    orbits.setdefault(orbit,[]).append(slot)
assert len(orbits) == 45
assert Counter(next(iter(o))[0] for o in orbits) == {'arrow':36,'state':9}
assert all(set(members) == set(o) for o,members in orbits.items())
# Two normalized invariant measures with genuinely different responses.
uniform = {slot:F(1,137) for slot in slots}
equal_orbits = {slot:F(1,45*len(o)) for o in orbits for slot in o}
equal_blocks = {slot:F(1,242) if slot[0]=='arrow' else F(1,32) for slot in slots}
for weights in (uniform,equal_orbits,equal_blocks):
    assert sum(weights.values()) == 1
    assert all(weights[slot] == weights[act(slot,p,q)]
               for slot in slots for p,q in product(perms,repeat=2))
    # Reindexing preserves the response if group weights are pushed forward.
    groups = defaultdict(list)
    for slot in slots:
        kind,a,b = slot
        key = (kind,a[0],b[0]) if kind=='arrow' else slot
        groups[key].append(slot)
    response = {slot:F(slot[0]=='state') for slot in slots}
    direct = sum(weights[s]*response[s] for s in slots)
    grouped = F(0)
    for members in groups.values():
        mass = sum(weights[s] for s in members)
        conditional = sum(weights[s]*response[s] for s in members)/mass
        grouped += mass*conditional
    assert direct == grouped
assert uniform != equal_orbits != equal_blocks

# Isolate a primitive leg change at unit scalar maps. It affects all slots
# with that left leg. Choose the reverse-reference arrow and source state0.
arrow_leg = (1,0)
for name, weights in [('uniform slots',uniform),('equal orbit masses',equal_orbits),('equal block masses',equal_blocks)]:
    block = sum(w for s,w in weights.items() if s[0]=='arrow')
    ga = sum(w for s,w in weights.items() if s[0]=='arrow' and s[1]==arrow_leg)
    gs = sum(w for s,w in weights.items() if s[0]=='state' and s[1]==0)
    print(f'{name}: arrow block={block}; chosen arrow-leg gain={ga}; chosen state-leg gain={gs}')
print('Reference stabilizer S2 x S2: 36 arrow orbits + 9 state orbits = 45.')
print('Invariant normalized slot measures have 44 free orbit-mass parameters.')
print('All three distinct trial measures preserve reference symmetry and grouped readout.')
print('Even assuming uniformity within each block leaves one free arrow/state block weight.')
