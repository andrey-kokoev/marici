#!/usr/bin/env python3
"""Exact finite audit: native directed K4 bundles versus K6 pentagon-pair holonomy.

The six directed source edges are from Marici's ActualSeedEndpointTable.agda.
CD/DC promotion, Hamiltonian-path partition, and pentagon-pair completion are
EXPLICIT CONDITIONAL interpretations, not native WG laws.
"""
from itertools import combinations, permutations
from collections import deque
import json

V4 = tuple('ABCD')
E0 = {('A','B'), ('B','C'), ('C','A'), ('A','D'), ('D','B'), ('B','A')}
J = dict(zip('ABCD','CDBA'))  # A->C, B->D, C->B, D->A
assert {a: J[J[a]] for a in V4} == dict(zip('ABCD','BADC'))

def graph_edges(U):
    return frozenset(frozenset(e) for e in combinations(sorted(U),2))

def path_edges(p):
    return frozenset(frozenset((p[i],p[i+1])) for i in range(len(p)-1))

def canon_path(p):
    q = tuple(p)
    return min(q,tuple(reversed(q)))

def path_decompositions(U):
    U = tuple(sorted(U))
    by_edges = {path_edges(p): canon_path(p) for p in permutations(U)}
    all_edges = graph_edges(U)
    assert len(by_edges)==12
    return frozenset(frozenset((e,all_edges-e)) for e in by_edges if all_edges-e in by_edges)

def directed_path_representable(edges,allowed):
    # Both orientations of each Hamilton path are considered.
    by_edges = {}
    for p in permutations(V4):
        pp=path_edges(p)
        if all(e in allowed for e in zip(p,p[1:])):
            by_edges[pp]=True
    return bool(by_edges.get(edges))

D4=path_decompositions(V4)
assert len(D4)==6
E8=E0|{('C','D'),('D','C')}
D8=frozenset(d for d in D4 if all(directed_path_representable(e,E8) for e in d))
assert len(E8)==8 and len(D8)==4
missing_arcs={(a,b) for a in V4 for b in V4 if a!=b}-E8
assert missing_arcs=={('A','C'),('C','B'),('B','D'),('D','A')}
missing_orbit=[]
x=('A','C')
for _ in range(4):
    missing_orbit.append(x)
    x=(J[x[0]],J[x[1]])
assert x==('A','C') and set(missing_orbit)==missing_arcs

def permute_bundle(d, perm):
    return frozenset(
        frozenset(frozenset(perm.get(v,v) for v in edge) for edge in path)
        for path in d)

assert all(permute_bundle(d,J) in D8 for d in D8)
assert {permute_bundle(d,J) for d in D8}==set(D8)
assert all(permute_bundle(d,J)==d for d in D4-D8)
assert all(permute_bundle(permute_bundle(permute_bundle(permute_bundle(d,J),J),J),J)==d for d in D4)
assert all(permute_bundle(d,J)!=d for d in D8)
# No <4 primitive additions can simultaneously preserve the J-action and
# realize all six decompositions: the remaining four directed arcs are one J-orbit.
minimal_unmarked=[]
for arcs in combinations(sorted(missing_arcs),2):
    candidate=E8|set(arcs)
    if all(all(directed_path_representable(p,candidate) for p in d) for d in D4):
        minimal_unmarked.append(tuple(''.join(e) for e in arcs))
assert len(minimal_unmarked)==4
assert not any(all(all(directed_path_representable(p,E8|{e}) for p in d) for d in D4) for e in missing_arcs)

V6=tuple(range(6))
def pentagon_pairs(U):
    U=tuple(sorted(U))
    first=U[0]
    def cycle(p):
        return frozenset(frozenset((p[i],p[(i+1)%5])) for i in range(5))
    all_edges=graph_edges(U)
    cycles={cycle((first,)+q) for q in permutations(U[1:])}
    assert len(cycles)==12
    out=frozenset(frozenset((C,all_edges-C)) for C in cycles)
    assert len(out)==6
    return out

H={i:pentagon_pairs(set(V6)-{i}) for i in V6}
def restrict(bundle, U):
    return frozenset(frozenset(e for e in path if e.issubset(U)) for path in bundle)

restrictions={}
for i,j in combinations(V6,2):
    U=set(V6)-{i,j}
    for v in (i,j):
        lookup={restrict(b,U):b for b in H[v]}
        assert len(lookup)==6 and set(lookup)==set(path_decompositions(U))
        restrictions[(v,i,j)] = lookup

def transport(i,j,b):
    if i==j:return b
    a,z=sorted((i,j))
    return restrictions[(j,a,z)][restrict(b,set(V6)-{i,j})]

def triangle(i,j,k,b):
    return transport(k,i,transport(j,k,transport(i,j,b)))

# Every one of the 20 unordered triples has (2,2,2) holonomy.
for i,j,k in combinations(V6,3):
    for base,mid,next_ in ((i,j,k),(j,k,i),(k,i,j)):
        s={mid:next_,next_:mid}
        domain=H[base]
        assert all(triangle(base,mid,next_,b)==permute_bundle(b,s) for b in domain)
        img={b:triangle(base,mid,next_,b) for b in domain}
        assert len(set(img.values()))==6
        assert all(img[b]!=b and img[img[b]]==b for b in domain)

# Choose one original four-set U={2,3,4,5}, with A,B,C,D -> 2,3,4,5.
# Its four directed decompositions are extended uniquely to W0={1,2,3,4,5}.
base=0
U=set(V6)-{0,1}
rename=dict(zip(V4,sorted(U)))
D8_renamed=frozenset(permute_bundle(d,rename) for d in D8)
lookup=restrictions[(0,0,1)]
selected=frozenset(lookup[d] for d in D8_renamed)
assert len(selected)==4
missing=H[base]-selected
assert len(missing)==2

preserving=[]; expanding=[]
for j,k in combinations(range(1,6),2):
    shifted=frozenset(triangle(base,j,k,b) for b in selected)
    if shifted==selected:
        preserving.append((j,k))
    else:
        expanding.append((j,k))
        assert len(selected|shifted)==6
assert preserving==[(2,3),(4,5)]
assert len(expanding)==8

# The triangular transpositions generate S5 and act transitively on the 6
# structures. Thus their only invariant subsets are empty/full.
label=lambda b:tuple(sorted(tuple(sorted(tuple(sorted(e)) for e in path)) for path in b))
states=sorted(H[base],key=label)
index={b:i for i,b in enumerate(states)}
transpositions=[]
for j,k in combinations(range(1,6),2):
    transpositions.append(tuple(index[permute_bundle(b,{j:k,k:j})] for b in states))
def permcompose(p,q): return tuple(p[q[i]] for i in range(6))
identity=tuple(range(6))
seen={identity}
q=deque([identity])
while q:
    g=q.popleft()
    for h in transpositions:
        k=permcompose(g,h)
        if k not in seen:
            seen.add(k);q.append(k)
assert len(seen)==120
assert all(set(g[i] for g in seen)==set(range(6)) for i in range(6))
assert all(set(g[i] for i in range(6))==set(range(6)) for g in seen)

report={
  'scope':'conditional incidence-promotion + path-partition + pentagon completion; no native Ramsey forcing',
  'seed_edges':[''.join(e) for e in sorted(E0)],
  'quarter_turn':J,
  'four_node_unordered_path_pairs':len(D4),
  'after_CD_DC_promotion':{'directed_edges':len(E8),'directed_path_pairs':len(D8),'unrealized_pairs':len(D4-D8)},
  'quarter_turn_orbits_of_path_pairs':[4,1,1],
  'missing_arcs_quarter_turn_orbit':[''.join(e) for e in missing_orbit],
  'minimum_non_equivariant_extra_arcs_to_realize_six':minimal_unmarked,
  'minimum_quarter_turn_equivariant_extra_arcs':4,
  'five_node_pentagon_pair_count_each_window':6,
  'four_vertex_restriction_is_bijective':True,
  'six_vertex_unordered_triangular_loops_checked':20,
  'all_holonomy_cycle_types':[2,2,2],
  'base_window_local_four_family_count':len(selected),
  'base_window_triangles_preserving_four':preserving,
  'base_window_triangles_forcing_six':expanding,
  'single_nonpreserving_triangle_closure_size':6,
  'base_window_holonomy_group_order':len(seen),
  'base_window_holonomy_orbits_on_six':[6],
  'holonomy_invariant_subsets':'only empty and all six',
  'all_six_admit_global_section':False
}
with open('/mnt/data/marici_wg_boundary_indexed_monodromy_results.json','w') as f:
    json.dump(report,f,indent=2)
    f.write('\n')
print('PASS: directed 4/6 closure, two-stage minimality, 20 fixed-point-free holonomies, full S5 (order 120).')
print('Preserving triangles:',preserving,'Expanding triangles:',expanding)
