"""Exact finite obstruction audit for the Marici 4->5 pentagon bridge.
Only the hard-coded six seed endpoints come from Marici. The complementarity
and pentagon completion tests are explicit *extra* combinatorial predicates;
this program does not claim a native proof or source-generated Ramsey color.
"""
import json
from itertools import combinations, permutations, product
from collections import Counter

V=('A','B','C','D')
W=V+('E',)
SEED={'AB':('A','B'),'BC':('B','C'),'CA':('C','A'),
      'AD':('A','D'),'DB':('D','B'),'BA':('B','A')}
# These are composites, not primitive directed occurrences.
SHORTCUTS={'CD':('C','D'),'DC':('D','C')}
DIR={**SEED,**SHORTCUTS}
edge=lambda u,v:frozenset((u,v))
all_edges=lambda verts:frozenset(edge(u,v) for u,v in combinations(verts,2))
path_edges=lambda path:frozenset(edge(u,v) for u,v in zip(path,path[1:]))
canonpath=lambda path:min(path,tuple(reversed(path)))
path_by_support={path_edges(p):canonpath(p) for p in permutations(V)}
assert len(path_by_support)==12
E4=all_edges(V)
D={frozenset((P,E4-P)) for P in path_by_support if E4-P in path_by_support}
assert len(D)==6

def dname(d):
    return [''.join(path_by_support[p]) for p in sorted(d,key=lambda x: ''.join(path_by_support[x]))]

def act_d(d,p):
    return frozenset(frozenset(frozenset(p[v] for v in e) for e in path) for path in d)

s=dict(zip(V,'BADC'))
g={'A':'B','B':'C','C':'A','D':'D'}
h_triangle={'A':'D','D':'B','B':'A','C':'C'}
perms4=[dict(zip(V,p)) for p in permutations(V)]
ident=dict(zip(V,V))
def mul(p,q): return {v:p[q[v]] for v in p}
def order(p):
    r=ident
    for k in range(1,25):
        r=mul(p,r)
        if r==ident:return k
    raise AssertionError('order >24')

autos=[p for p in perms4 if {(p[u],p[v]) for u,v in SEED.values()}==set(SEED.values())]
assert autos==[ident,s]
base=min(D,key=lambda d:tuple(dname(d)))
stab4=[p for p in perms4 if act_d(base,p)==base]
assert sorted(order(p) for p in stab4)==[1,2,4,4]

poss=[p for p in permutations(V) if all((u,v) in DIR.values() for u,v in zip(p,p[1:]))]
assert len(poss)==8
feasible={frozenset((path_edges(p),path_edges(q))) for p,q in combinations(poss,2)
          if path_edges(p)|path_edges(q)==E4 and not path_edges(p)&path_edges(q)}
assert len(feasible)==4
fixed={d for d in D if act_d(d,s)==d}
assert len(fixed)==2 and feasible==D-fixed
assert not(any(act_d(d,s)==d for d in feasible))
assert any(act_d(d,g) not in feasible for d in feasible)
assert any(act_d(d,h_triangle) not in feasible for d in feasible)
# transpositions in S4 have no fixed decomposition
transpositions4=[p for p in perms4 if sum(p[v]!=v for v in V)==2]
assert len(transpositions4)==6
assert all(act_d(d,p)!=d for d in D for p in transpositions4)
assert {act_d(d,p) for d in feasible for p in perms4}==D

# A4 is sharply transitive on the twelve ordered distinct vertex pairs.
a4=[p for p in perms4 if
    sum(tuple(p[v] for v in V)[i]>tuple(p[v] for v in V)[j]
        for i in range(4) for j in range(i+1,4))%2==0]
assert len(a4)==12
all_arcs={(u,v) for u in V for v in V if u!=v}
assert { (p['A'],p['B']) for p in a4 } == all_arcs
orbit_seed={(p[u],p[v]) for p in a4 for u,v in SEED.values()}
assert orbit_seed==all_arcs
missing_arcs={u+v for u,v in all_arcs-set(SEED.values())}
assert missing_arcs=={'AC','BD','CB','DA','CD','DC'}
# Every stabilizer of an unordered complementary path pair is C4;
# there are three distinct C4 subgroups, each fixing exactly two pairs.
stabilizer_to_pairs={}
for d in D:
    stabilizer=frozenset(tuple(p[v] for v in V) for p in perms4 if act_d(d,p)==d)
    stabilizer_to_pairs.setdefault(stabilizer,[]).append(d)
assert len(stabilizer_to_pairs)==3
assert sorted(len(ds) for ds in stabilizer_to_pairs.values())==[2,2,2]

def min_reverse(d):
    paths=[path_by_support[e] for e in sorted(d,key=lambda e: ''.join(path_by_support[e]))]
    tests=[]
    for bits in product((0,1),repeat=2):
        dirs=[tuple(reversed(path)) if reverse else path for path,reverse in zip(paths,bits)]
        missing=[u+v for path in dirs for u,v in zip(path,path[1:])
                 if (u,v) not in DIR.values()]
        tests.append((len(missing), [''.join(p) for p in dirs], missing))
    return min(tests)
assert sorted(min_reverse(d)[0] for d in D)==[0,0,0,0,2,2]

# A declared K4 support shortcut is NOT history-disjoint from the other
# complementary path: its only two-step witness uses the other path's edges.
shortcut_required={'CD':frozenset((edge('C','A'),edge('A','D'))),
                   'DC':frozenset((edge('D','B'),edge('B','C')))}
for d in feasible:
    feasible_orientations=[]
    paths=[path_by_support[e] for e in d]
    for bits in product((0,1),repeat=2):
        oriented=[tuple(reversed(p)) if bit else p for p,bit in zip(paths,bits)]
        if all((u,v) in DIR.values() for p in oriented for u,v in zip(p,p[1:])):
            feasible_orientations.append(oriented)
    assert feasible_orientations
    for oriented in feasible_orientations:
        matches=[(i,name) for i,p in enumerate(oriented) for name,ends in SHORTCUTS.items()
                 if ends in tuple(zip(p,p[1:]))]
        assert len(matches)==1
        index,name=matches[0]
        assert shortcut_required[name].issubset(path_edges(oriented[1-index]))

# Minimal additional individual inverse *views*, not native executed arrows.
# Exact incidence requirements for supporting all six unordered partitions.
reverse_types={v+u for u,v in SEED.values() if (v,u) not in SEED.values()}
assert reverse_types=={'AC','BD','CB','DA'}
def supports_all(additions):
    legal=set(DIR.values())|{tuple(t) for t in additions}
    oriented=[p for p in permutations(V) if all((u,v) in legal for u,v in zip(p,p[1:]))]
    allowed={frozenset((path_edges(p),path_edges(q))) for p,q in combinations(oriented,2)
             if path_edges(p)|path_edges(q)==E4 and not path_edges(p)&path_edges(q)}
    return allowed==D
valid_added=[]
for size in range(5):
    for add in combinations(sorted(reverse_types),size):
        if supports_all(add):valid_added.append(frozenset(add))
min_number=min(map(len,valid_added))
minimal_added={a for a in valid_added if len(a)==min_number}
assert min_number==2
assert minimal_added=={frozenset(x) for x in product(('AC','BD'),('CB','DA'))}
def act_arc(arc,p):return p[arc[0]]+p[arc[1]]
invariant_added=[a for a in valid_added if {act_arc(t,s) for t in a}==set(a)]
assert invariant_added==[frozenset(reverse_types)]

# Given z, close each P4 by its endpoints. This *adds* new incident edges:
# not an output of free composition on the existing four vertices.
def pentagon_close(d,z='E'):
    cycles=[]
    for path in d:
        p=path_by_support[path]
        cycles.append(frozenset(set(path)|{edge(z,p[0]),edge(z,p[-1])}))
    assert cycles[0].isdisjoint(cycles[1])
    return frozenset(cycles)
H={pentagon_close(d) for d in D}
assert len(H)==6
# Enumerate all pentagon-pair decompositions on an arbitrary 5-set.
def cycle_pairs(verts):
    verts=tuple(sorted(verts));first=verts[0];allE=all_edges(verts)
    ans=set()
    for suffix in permutations(verts[1:]):
        cyc=(first,)+suffix
        red=frozenset(edge(cyc[i],cyc[(i+1)%5]) for i in range(5))
        blue=allE-red
        if all(sum(v in e for e in blue)==2 for v in verts):
            ans.add(frozenset((red,blue)))
    assert len(ans)==6
    return frozenset(ans)
assert H==set(cycle_pairs(W))

def act_h(H,p):
    return frozenset(frozenset(frozenset(p[v] for v in e) for e in cyc) for cyc in H)

perms5=[dict(zip(W,p)) for p in permutations(W)]
h0=next(iter(H))
stab5=[p for p in perms5 if act_h(h0,p)==h0]
stab5_fixed_z=[p for p in stab5 if p['E']=='E']
assert len(stab5)==20 and len(stab5_fixed_z)==4
assert sorted(order({v:p[v] for v in V}) for p in stab5_fixed_z)==[1,2,4,4]
transpositions5=[p for p in perms5 if sum(p[v]!=v for v in W)==2]
assert len(transpositions5)==10
assert all(act_h(a,p)!=a for a in H for p in transpositions5)

# Recompute the full restriction/extension transport on 6 overlapping 5-facets,
# and verify that all 20 triangle holonomies have cycle type 2+2+2.
S=tuple(range(6))
facets={i:tuple(v for v in S if v!=i) for i in S}
local_H={i:cycle_pairs(facets[i]) for i in S}
def restrict_h(h,verts):
    avail=all_edges(tuple(verts))
    return frozenset(frozenset(cyc&avail) for cyc in h)
transports={}
for i,j in permutations(S,2):
    overlap=set(facets[i])&set(facets[j]);table={}
    for h in local_H[i]:
        match=[cand for cand in local_H[j] if restrict_h(cand,overlap)==restrict_h(h,overlap)]
        assert len(match)==1
        table[h]=match[0]
    assert len(set(table.values()))==6
    transports[i,j]=table
holonomy_count=0
for i,j,k in combinations(S,3):
    hol={h:transports[k,i][transports[j,k][transports[i,j][h]]] for h in local_H[i]}
    assert not any(a==b for a,b in hol.items())
    assert all(hol[hol[h]]==h for h in hol)
    holonomy_count+=1
assert holonomy_count==20

report={
 'seed_occurrences':SEED,'automorphism_group_size':len(autos),
 'complementary_K4_path_pairs':len(D),'native_direction_realizable_pairs':len(feasible),
 'fixed_pairs_under_seed_reflection':len(fixed),
 'native_equals_non_fixed_pairs':feasible==D-fixed,
 'decompositions':[{ 'paths':dname(d), 'native_directed':d in feasible,
                    'reflection_fixed':d in fixed,
                    'minimum_reversed_incidence_steps':min_reverse(d)[0]}
                   for d in sorted(D,key=lambda d:tuple(dname(d)))],
 'S4_stabilizer_of_decomposition':{'size':len(stab4),'element_orders':sorted(order(p) for p in stab4)},
 'S4_transpositions_fixed_point_free':True,
 'A4_triangle_generator_g_preserves_native_four':{act_d(d,g) for d in feasible}==feasible,
 'A4_triangle_generator_h_preserves_native_four':{act_d(d,h_triangle) for d in feasible}==feasible,
 'all_six_generated_by_vertex_permutation_orbit':True,
 'every_native_feasible_shortcut_reuses_two_occurrences_of_opposite_path':True,
 'minimum_individual_inverse_views_to_complete_D':min_number,
 'four_minimal_inverse_view_choices':[sorted(a) for a in sorted(minimal_added,key=lambda x:sorted(x))],
 'minimum_reflection_equivariant_inverse_view_set':sorted(invariant_added[0]),
 'A4_ordered_arc_orbit_size':len(orbit_seed),
 'additional_directed_arc_types_for_A4_invariance':sorted(missing_arcs),
 'number_of_C4_stabilizers':len(stabilizer_to_pairs),
 'pairs_per_C4_stabilizer':sorted(len(ds) for ds in stabilizer_to_pairs.values()),
 'K5_pentagon_pair_completions':len(H),
 'K5_pairs_from_native_four':len({pentagon_close(d) for d in feasible}),
 'S5_stabilizer_of_pentagon_pair':{'size':len(stab5),
            'point_stabilizer_size':len(stab5_fixed_z),
            'point_stabilizer_orders':sorted(order({v:p[v] for v in V}) for p in stab5_fixed_z)},
 'S5_transpositions_fixed_point_free':True,
 'all_20_triangular_facet_holonomies_fixed_point_free':holonomy_count,
 'native_lift_status':'strict g,h action on seed path-category impossible: directed quiver automorphism group size two',
 'required_extra_axioms':['admit edge-disjoint complementary covering path bundles',
                        'admit a new vertex and endpoint-closing occurrences',
                        'impose compatibility of local bundles on overlaps']
}
if __name__=='__main__':
    print(json.dumps(report,indent=2))
