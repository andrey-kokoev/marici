#!/usr/bin/env python3
"""Exact group-action bridge: A4/<s> and 6 complementary K4 path pairs.

This constructs a 6-element SOURCE GROUP SET without input colors, but it is
not an actual free-path WG execution/filled comparison operation.
"""
from itertools import permutations,combinations
from collections import Counter
from pathlib import Path
import json
V='ABCD'
ID=dict(zip(V,V))
g={'A':'B','B':'C','C':'A','D':'D'}
h={'A':'D','D':'B','B':'A','C':'C'}
s={'A':'B','B':'A','C':'D','D':'C'}
j={'A':'C','C':'B','B':'D','D':'A'}
def product(p,q):return {v:p[q[v]] for v in V}
def key(p):return tuple(p[v] for v in V)
def power(p,n):
    a=ID
    for i in range(n):a=product(p,a)
    return a
assert power(j,2)==s and power(j,4)==ID
G={key(ID):ID};todo=[ID]
while todo:
    a=todo.pop()
    for t in (g,h):
        b=product(t,a)
        if key(b) not in G:G[key(b)]=b;todo.append(b)
assert len(G)==12
S4=[dict(zip(V,p)) for p in permutations(V)]
assert len(S4)==24
H={key(ID),key(s)}
J4={key(power(j,n)) for n in range(4)}
assert H==J4.intersection(G)

edges={frozenset(e) for e in combinations(V,2)}
def norm_path(p):return min(p,p[::-1])
paths={norm_path(p):frozenset(frozenset(e) for e in zip(p,p[1:])) for p in permutations(V)}
lookup={v:k for k,v in paths.items()}
D=set()
for path,sup in paths.items():
    alt=lookup.get(frozenset(edges-sup))
    if alt is not None:D.add(tuple(sorted((path,alt))))
assert len(D)==6

def action(p,d):
    return tuple(sorted(norm_path(tuple(p[v] for v in chain)) for chain in d))

def stab(d,group):return {key(p) for p in group if action(p,d)==d}
fixH={d for d in D if action(s,d)==d}
fixJ={d for d in D if action(j,d)==d}
assert fixH==fixJ and len(fixJ)==2
for d in fixH:
    assert stab(d,G.values())==H
    assert stab(d,S4)==J4

# Equivariant bijections are in bijection with the two H-fixed path pairs.
# For each d, the map aH -> a*d is well-defined and bijective.
cosets=[]
for a in G.values():
    c=frozenset((key(a),key(product(a,s))))
    if c not in cosets:cosets.append(c)
assert len(cosets)==6
bijections=[]
for d in fixH:
    cmap={c:action(G[next(iter(c))],d) for c in cosets}
    assert len(set(cmap.values()))==6
    bijections.append(cmap)
assert len(bijections)==2
assert all(bijections[0][c] != bijections[1][c] for c in cosets)

# The H-normalizer in A4 has four elements, and the quotient H-normalizer/H
# acts simply transitively on the two identifications.
normalizer={key(a) for a in G.values() if key(product(product(a,s),{v:next(w for w in V if a[w]==v) for v in V}))==key(s)}
assert len(normalizer)==4

results={'A4_order':12,'S4_order':24,'seed_reflection':'(A B)(C D)',
 'geometric_quarter_turn':'(A C B D)','quarter_turn_square_is_seed_reflection':True,
 'H_order':2,'quarter_turn_subgroup_order':4,'A4_cosets_mod_seed_reflection':len(cosets),
 'unordered_complementary_P4_pair_count':len(D),
 'H_fixed_path_pair_count':len(fixH),'H_fixed_path_pairs':[list(map(''.join,d)) for d in sorted(fixH)],
 'each_H_fixed_pair_stabilizer_in_A4_size':2,
 'each_H_fixed_pair_stabilizer_in_S4_size':4,
 'H_normalizer_in_A4_size':len(normalizer),
 'equivariant_bijections_A4_cosets_to_path_pairs':2,
 'scope':'abstract generated vertex permutation group, not native pointed occurrence transport'}
Path('/mnt/data/marici_six_state_coset_bridge_results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
