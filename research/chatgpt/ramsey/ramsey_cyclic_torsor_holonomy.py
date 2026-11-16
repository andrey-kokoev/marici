#!/usr/bin/env python3
"""Exact five-vertex cyclic-torsor / six-vertex descent audit.

Mathematical model: undirected support edges, with unordered complementary
C5 factors. This is a conditional interface, not a native Marici filler law.
No external dependencies.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
import json

V = tuple(range(6))

def edge(a, b):
    assert a != b
    return tuple(sorted((a, b)))

def all_edges(W):
    return frozenset(edge(a,b) for a,b in combinations(W,2))

def cycle_group(cycle):
    W=tuple(sorted(cycle))
    pos={v:i for i,v in enumerate(cycle)}
    return frozenset(tuple(cycle[(pos[v]+k)%len(cycle)] for v in W)
                     for k in range(len(cycle)))

def cyclic_factors(W):
    W=tuple(sorted(W)); assert len(W)==5
    out={}
    for tail in permutations(W[1:]):
        cyc=(W[0],)+tail
        group=cycle_group(cyc)
        red=frozenset(edge(cyc[j],cyc[(j+1)%5]) for j in range(5))
        blue=all_edges(W)-red
        assert len(red)==len(blue)==5 and not red.intersection(blue)
        out[group]=frozenset((red,blue))
    assert len(out)==6
    assert len(set(out.values()))==6
    for fac in out.values():
        for triple in combinations(W,3):
            te=set(all_edges(triple))
            assert all(0 < len(te.intersection(E)) < 3 for E in fac)
    return tuple(sorted(out.items(),key=lambda el:tuple(sorted(el[0]))))

def restrict(factors,U):
    U=set(U)
    return frozenset(frozenset(e for e in F if set(e).issubset(U)) for F in factors)

def component_is_path(F,U):
    deg={v:0 for v in U}
    for a,b in F:
        deg[a]+=1;deg[b]+=1
    return sorted(deg.values())==[1,1,2,2] and len(F)==3

def rename_group(group,W,substitution):
    """Relabel permutations by a bijection W -> W'; do not identify histories."""
    W=tuple(sorted(W)); dest=tuple(sorted(substitution.get(v,v) for v in W))
    sigma=lambda v:substitution.get(v,v)
    sigma_inv={sigma(v):v for v in W}
    group2=set()
    for perm in group:
        f=dict(zip(W,perm))
        group2.add(tuple(sigma(f[sigma_inv[v]]) for v in dest))
    return frozenset(group2)

families={i:cyclic_factors(tuple(v for v in V if v!=i)) for i in V}
for i,items in families.items():
    for j in V:
        if i==j:continue
        U=tuple(v for v in V if v not in (i,j))
        restrictions=[restrict(fac,U) for group,fac in items]
        assert len(set(restrictions))==6
        assert all(all(component_is_path(F,U) for F in pair) for pair in restrictions)

# Each W_i -> W_j transports a group by substituting its missing old vertex j
# with the new vertex i, keeping four common vertices fixed.
transport={}
for i,j in permutations(V,2):
    Wi=tuple(v for v in V if v!=i)
    Wj=tuple(v for v in V if v!=j)
    U=tuple(v for v in V if v not in (i,j))
    fi=families[i]; fj=families[j]
    mapping={}
    for a,(grp_a, fac_a) in enumerate(fi):
        choices=[b for b,(grp_b,fac_b) in enumerate(fj)
                 if restrict(fac_a,U)==restrict(fac_b,U)]
        assert len(choices)==1
        b=choices[0]
        assert rename_group(grp_a,Wi,{j:i})==fj[b][0]
        mapping[a]=b
    assert len(set(mapping.values()))==6
    transport[i,j]=mapping

def go(i,j,k,idx):
    return transport[k,i][transport[j,k][transport[i,j][idx]]]

def perm_cycle_type(mapping):
    visited=set(); lengths=[]
    for i in mapping:
        if i in visited: continue
        p=i; count=0
        while p not in visited:
            visited.add(p);count+=1;p=mapping[p]
        lengths.append(count)
    return tuple(sorted(lengths))

triangular_holonomies={}
for i,j,k in combinations(V,3):
    Wi=tuple(v for v in V if v!=i)
    hol={a:go(i,j,k,a) for a in range(6)}
    assert perm_cycle_type(hol)==(2,2,2)
    for a,(group,fac) in enumerate(families[i]):
        assert families[i][hol[a]][0]==rename_group(group,Wi,{j:k,k:j})
    # Common three-vertex boundary has three possible nonconstant partitions,
    # each with exactly two five-vertex cyclic lifts. Holonomy flips the lifts.
    U3=tuple(v for v in V if v not in (i,j,k))
    fibers=defaultdict(list)
    for a,(group,fac) in enumerate(families[i]):
        fibers[restrict(fac,U3)].append(a)
    assert len(fibers)==3 and sorted(map(len,fibers.values()))==[2,2,2]
    for states in fibers.values():
        assert hol[states[0]]==states[1] and hol[states[1]]==states[0]
    triangular_holonomies[f"{i},{j},{k}"]=hol

# Four-facet Bianchi/pasting identity: composing two triangle holonomies
# equals the other two, after transport to a common base. This is formal
# associativity; it does NOT flatten any triangle holonomy.
quadruple_bianchi_checks=0
for i,j,k,l in permutations(V,4):
    for a in range(6):
        lhs=go(i,k,l, go(i,j,k,a))
        t_ij=transport[i,j][a]
        transported=transport[j,i][go(j,k,l,t_ij)]
        rhs=go(i,j,l,transported)
        assert lhs==rhs
        quadruple_bianchi_checks+=1
assert quadruple_bianchi_checks==6*6*5*4*3

# Count pairwise compatible simultaneous five-facet structures. At three
# facets the first obstruction occurs, despite every pair being compatible.
compat_count={}
for nfaces in range(1,7):
    counts=[]
    for chosen in combinations(V,nfaces):
        n=0
        for states in product(range(6),repeat=nfaces):
            if all(transport[a,b][states[pos_a]]==states[pos_b]
                   for pos_a,pos_b in combinations(range(nfaces),2)
                   for a,b in [(chosen[pos_a],chosen[pos_b])]):
                n+=1
        counts.append(n)
    assert len(set(counts))==1
    compat_count[nfaces]=counts[0]
assert compat_count=={1:6,2:6,3:0,4:0,5:0,6:0}

# Six unordered K4 decompositions = 3 split-opposite-edge matchings x 2.
U4=tuple(range(4))
first_family=families[5]  # W_5={0,1,2,3,4}; restriction to 0..3
D4=tuple(restrict(fac,U4) for group,fac in first_family)
assert len(set(D4))==6
matchings=(frozenset((edge(0,1),edge(2,3))),
           frozenset((edge(0,2),edge(1,3))),
           frozenset((edge(0,3),edge(1,2))))
split_count=Counter()
for F in D4:
    splits=[m for m in matchings
            if sorted(len(m.intersection(part)) for part in F)==[1,1]]
    assert len(splits)==1
    split_count[str(sorted(splits[0]))]+=1
assert sorted(split_count.values())==[2,2,2]

# Independent all-coloring audit: 5 vertices have 12 oriented triangle-free
# red/blue edge colorings, 6 unordered pairs. 6 vertices have none.
def triangle_free_colorings(W):
    E=tuple(combinations(W,2)); edges_count=len(E)
    triangles=tuple(combinations(W,3)); out=[]
    for bits in range(1<<edges_count):
        cmap={e:(bits>>j)&1 for j,e in enumerate(E)}
        if all(len({cmap[edge(u,v)] for u,v in combinations(tri,2)})==2
               for tri in triangles):
            out.append(bits)
    return out
assert len(triangle_free_colorings(tuple(range(5))))==12
assert len(triangle_free_colorings(V))==0

# Stronger finite consequence: the minimum number of monochromatic triangles
# in a coloring of K6 is 2, consistent with triple-facet obstruction.
K6edges=tuple(combinations(V,2)); triangles=tuple(combinations(V,3))
hist=Counter()
for bits in range(1<<15):
    cm={e:(bits>>j)&1 for j,e in enumerate(K6edges)}
    mono=sum(1 for tri in triangles if len({cm[edge(a,b)]
                                          for a,b in combinations(tri,2)})==1)
    hist[mono]+=1
assert min(hist)==2 and hist[2]==1760

# Native comparison countermodel: choose one frame tau_v sending distinguished
# root 0 to v, and let e_{uv}=tau_v o tau_u^{-1}. Every compositional triangle
# has consistent transport at every finite n (without conflating occurrence IDs).
def flat_comparison_check(n):
    vals=tuple(range(n))
    def tau(v):
        return tuple(v if k==0 else 0 if k==v else k for k in vals) if v else vals
    frames={v:tau(v) for v in vals}
    def compose(a,b):return tuple(a[b[v]] for v in vals) # a after b
    def inverse(p):return tuple(p.index(v) for v in vals)
    e={(u,v):compose(frames[v],inverse(frames[u])) for u in vals for v in vals}
    assert all(e[u,v][u]==v for u,v in e)
    assert all(compose(e[v,w],e[u,v])==e[u,w]
               for u,v,w in product(vals,repeat=3))
    return True
assert all(flat_comparison_check(n) for n in range(2,8))

report={
    "scope":"Conditional cyclic-torsor local completion, not native Marici admissibility",
    "five_vertex_cyclic_groups":6,
    "four_vertex_unordered_complementary_path_decompositions":6,
    "matching_splits_per_matching":sorted(split_count.values()),
    "five_facet_pairwise_transport_is_unique":True,
    "six_vertex_triangular_facet_loops":len(triangular_holonomies),
    "holonomy_type_all_triples":"(2,2,2)",
    "holonomy_example_0_1_2":triangular_holonomies["0,1,2"],
    "holonomy_equals_transposition_j_k":True,
    "ordered_tetrahedral_bianchi_checks":quadruple_bianchi_checks,
    "common_three_vertex_boundary_values":3,
    "lifts_per_three_vertex_boundary":2,
    "compatible_assignments_by_number_of_five_facets":compat_count,
    "triangle_free_K5_oriented_colorings":12,
    "triangle_free_K6_oriented_colorings":0,
    "minimum_monochromatic_triangles_K6":2,
    "K6_colorings_with_exactly_two_mono_triangles":hist[2],
    "uniform_flat_native_style_comparison_exists_up_to_n7":True
}
if __name__=='__main__':
    target='/mnt/data/ramsey_cyclic_torsor_holonomy_results.json'
    with open(target,'w') as f:json.dump(report,f,indent=2)
    print(json.dumps(report,indent=2))
