#!/usr/bin/env python3
"""Exact incidence/chain audit for the six-arrow Marici seed.

Scope: directed 12-edge macro completion, six uniquely shortest primitive
macro histories, their definitional 2-cells, and A4 vertex relabeling.
No assertion of native filler admissibility or exact history-level A4 action.
"""
from itertools import permutations, combinations
from collections import Counter
import json
from pathlib import Path
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

V='ABCD'
primitive=('AB','BC','CA','AD','DB','BA')
edges=tuple(a+b for a in V for b in V if a!=b)
missing=tuple(e for e in edges if e not in primitive)
paths={}
for e in edges:
    if e in primitive:
        paths[e]=(e,)
    else:
        a,b=e
        choices=[(a+v,v+b) for v in V if v not in (a,b) and a+v in primitive and v+b in primitive]
        assert len(choices)==1,(e,choices)
        paths[e]=choices[0]

g=dict(zip(V,'BCAD'))
h=dict(zip(V,'DACB'))
s=dict(zip(V,'BADC'))
def compose(f,k):
    return {v:f[k[v]] for v in V}
G={tuple(V):dict(zip(V,V))}
queue=[G[tuple(V)]]
while queue:
    p=queue.pop()
    for generator in (g,h):
        q=compose(p,generator)
        key=tuple(q[v] for v in V)
        if key not in G:
            G[key]=q
            queue.append(q)
assert len(G)==12
assert any(p==s for p in G.values())

def tau_of(e):
    a,b=e
    return (a,paths[e][0][1],b)
initial_triangles=tuple(tau_of(e) for e in missing)
all_transported=sorted({tuple(perm[v] for v in t)
                        for perm in G.values() for t in initial_triangles})
assert len(all_transported)==24

def orbit(t):
    return frozenset(tuple(perm[v] for v in t) for perm in G.values())
orbits={orbit(t) for t in all_transported}
assert len(orbits)==2 and all(len(o)==12 for o in orbits)
seed_orbit=orbit(tuple('ABC'))
opposite_orbit=next(o for o in orbits if o!=seed_orbit)
assert Counter('seed' if t in seed_orbit else 'opposite' for t in initial_triangles)=={'seed':4,'opposite':2}

def b(t):
    a,mid,c=t
    return Matrix([int(e==a+mid)+int(e==mid+c)-int(e==a+c) for e in edges])
M6=Matrix.hstack(*(b(t) for t in initial_triangles))
M12=Matrix.hstack(*(b(t) for t in sorted(seed_orbit)))
M24=Matrix.hstack(*(b(t) for t in all_transported))

def smith(M):
    S=smith_normal_form(M,domain=ZZ)
    return [abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0]
assert M6.rank()==6 and smith(M6)==[1]*6
assert M12.rank()==9 and smith(M12)==[1]*8+[2]
assert M24.rank()==9 and smith(M24)==[1]*9
# Reading occurrences of BC through each edge's canonical shortest history
lam={e:paths[e].count('BC') for e in edges}
assert all((sum(lam[x] for x in paths[e])-lam[e])==0 for e in missing)
F_AC=('A','B','C')
g_F_AC=tuple(g[v] for v in F_AC)
assert g_F_AC==('B','C','A')
assert (b(g_F_AC).T*Matrix([lam[e] for e in edges]))[0]==1
assert Matrix.hstack(M6,b(g_F_AC)).rank()==7
# A4-invariant closure kills the full integral cycle lattice.
# rank(d1)=3, rank(M24)=9, all Smith invariants 1.
assert len(edges)-3-M6.rank()==3
assert len(edges)-3-M24.rank()==0
assert len(all_transported)-M24.rank()==15

# Macro path expansion is nonfaithful in precisely two oriented Hamilton paths.
# These are the two cuts of the first seam-inserted C->D history and their
# reflected D->C analogues.
expansion_fibers={}
for t in permutations(V):
    word=''.join(t)
    expansion=tuple(primitive_event for i in range(3)
                    for primitive_event in paths[word[i:i+2]])
    expansion_fibers.setdefault(expansion,[]).append(word)
collisions={tuple(v):[list(expansion),list(v)] for expansion,v in expansion_fibers.items() if len(v)>1}
assert len(expansion_fibers)==22
assert set(collisions)=={('CABD','CBAD'),('DABC','DBAC')},collisions
assert expansion_fibers[('CA','AB','BA','AD')]==['CABD','CBAD']
assert expansion_fibers[('DB','BA','AB','BC')]==['DABC','DBAC']

# The A4-equivariant coset correspondence has two possible bases.
K4=frozenset(''.join(sorted(pair)) for pair in combinations(V,2))
path_edges={}
for t in permutations(V):
    support=frozenset(''.join(sorted(t[i:i+2])) for i in range(3))
    path_edges.setdefault(support,[]).append(''.join(t))
assert len(path_edges)==12
Ds={frozenset((e,K4-e)) for e in path_edges if K4-e in path_edges}
assert len(Ds)==6

def actD(D,perm):
    return frozenset(frozenset(''.join(sorted((perm[e[0]],perm[e[1]]))) for e in part) for part in D)
fixed=[D for D in Ds if actD(D,s)==D]
assert len(fixed)==2
assert all(len([p for p in G.values() if actD(D,p)==D])==2 for D in fixed)
assert all(set(actD(D,p) for p in G.values())==Ds for D in fixed)

# The two s-fixed choices have the same C->D primitive path, but distinct
# B->A complementary words.  Their discrepancy is second-order (nonabelian).
CD_plus='CABD'
CD_minus='CBAD'
BA_plus='BCDA'
BA_minus='BDCA'  # independently directed B->A presentation of D_minus's other path

def expand_string(t):
    return tuple(z for i in range(3) for z in paths[t[i:i+2]])
common_cd=expand_string(CD_plus)
assert common_cd==expand_string(CD_minus)==('CA','AB','BA','AD')
other_plus=expand_string(BA_plus)
other_minus=expand_string(BA_minus)
assert other_plus==('BC','CA','AD','DB','BA')
assert other_minus==('BA','AD','DB','BC','CA')
assert Counter(other_plus)==Counter(other_minus)
assert other_plus!=other_minus
# Choose the spanning tree BA, BC, DB, rooted at B. The chord coordinates
# are AB=X, CA=Y, AD=Z. For a B->A word append BA^{-1} to close it;
# the tree collapse then gives exactly the following free-group words.
chord={'AB':'X','CA':'Y','AD':'Z'}
free_plus=tuple(chord[e] for e in other_plus if e in chord)
free_minus=tuple(chord[e] for e in other_minus if e in chord)
assert free_plus==('Y','Z') and free_minus==('Z','Y')
free_commutator=('Y','Z','Y^-1','Z^-1')
assert free_commutator!=()
# WG generated-fragment comparison is an equivalence between current
# attachment carriers (the outgoing edges at the source of last step).
# For the chosen B->A paths, the final edges are BA (source B) and
# CA (source C); appending AB to both makes both final sources A.
outs={v:tuple(e for e in primitive if e[0]==v) for v in V}
assert outs=={'A':('AB','AD'),'B':('BC','BA'),'C':('CA',),'D':('DB',)}
def terminal_reader_image(word):
    assert word
    return frozenset(e[1] for e in outs[word[-1][0]])
assert terminal_reader_image(other_plus)==frozenset({'A','C'})
assert terminal_reader_image(other_minus)==frozenset({'A'})
assert terminal_reader_image(other_plus)!=terminal_reader_image(other_minus)
assert terminal_reader_image(other_plus+('AB',))==terminal_reader_image(other_minus+('AB',))==frozenset({'B','D'})
# The groupoid discrepancy is unchanged by appending the identical suffix:
# (beta+ e)(beta- e)^(-1) = beta+ beta-^(-1), so the commutator remains.
assert free_plus+('X',)==('Y','Z','X')
assert free_minus+('X',)==('Z','Y','X')
# Canonical degree-two word signature: additive occurrence inventory plus
# ALL ordered pairs.  It is source-covariant and has a non-additive cross term.
def sig1(word): return Counter(word)
def sig2(word): return Counter((word[i],word[j]) for i in range(len(word)) for j in range(i+1,len(word)))
def tensor(a,b):return Counter({(e,f):u*v for e,u in a.items() for f,v in b.items()})
for left,right in ((other_plus,other_minus),(('AB','BC'),('CA','AD')), (other_plus,('AB',))):
    want=sig2(left)+sig2(right)+tensor(sig1(left),sig1(right))
    assert sig2(left+right)==want
assert sig1(other_plus)==sig1(other_minus)
assert sig2(other_plus)!=sig2(other_minus)
assert sig2(other_plus+('AB',))-sig2(other_minus+('AB',))==sig2(other_plus)-sig2(other_minus)
assert sig2(other_plus)[('CA','AD')]==1 and sig2(other_minus)[('CA','AD')]==0
# For any seed automorphism relabeling individual primitive tokens commutes
# with the entire ordered-pair signature.
def relabel(word,perm):return tuple(perm[e[0]]+perm[e[1]] for e in word)
assert sig2(relabel(other_plus,s))==Counter({(s[e[0]]+s[e[1]],s[f[0]]+s[f[1]]):num for (e,f),num in sig2(other_plus).items()})

# In gamma_2 F_3 / gamma_3 F_3 ~= Lambda^2 Z^3,
# this commutator is the primitive wedge Y ^ Z.

# Both base decompositions require reuse of primitive occurrence TYPES after
# each macro-incidence is expanded into its unique shortest primitive word.
def expand_path(t):
    return tuple(z for i in range(3) for z in paths[t[i:i+2]])
base=[]
for D in fixed:
    parts=tuple(D)
    variants=[(a,b,tuple(sorted(set(expand_path(a)) & set(expand_path(b)))))
              for a in path_edges[parts[0]] for b in path_edges[parts[1]]]
    assert set(len(v[2]) for v in variants)=={3}
    base.append({'paths':sorted([sorted(path_edges[part]) for part in parts]),
                 'minimum_shared_primitive_labels':min(len(v[2]) for v in variants),
                 'one_overlap':variants[0][2]})

result={
    'source_occurrences':list(primitive),
    'missing_edges':list(missing),
    'unique_shortest_histories':{e:list(paths[e]) for e in missing},
    'triangle_action_group_size':len(G),
    'geodesic_comparison_triples':[''.join(t) for t in initial_triangles],
    'initial_orbit_counts':{'seed':4,'opposite':2},
    'closure_ordered_triangle_faces':len(all_transported),
    'witness_first_failed_image':{'initial':'AB+BC-AC',
        'mapped_by_g':'BC+CA-BA', 'lambda':'count of primitive BC in shortest expansion',
        'evaluation':1},
    'initial_6_face_complex':{'boundary_rank':M6.rank(),'smith':smith(M6),
                              'H1':'Z^3','H2':'0'},
    'single_chiral_orbit_12_face_complex':{'boundary_rank':M12.rank(),'smith':smith(M12),
                              'H1':'Z/2','H2':'Z^3'},
    'A4_closure_24_face_complex':{'boundary_rank':M24.rank(),'smith':smith(M24),
                              'H1':'0','H2':'Z^15'},
    'ordered_pair_signature':{'same_additive_counts':True,'changed_ordered_pairs':8,'CA_before_AD_plus':1,'CA_before_AD_minus':0,'after_common_AB_difference_preserved':True},
    'WG_vs_free_groupoid':{'before_common_continuation':{'plus_image':['A','C'],'minus_image':['A'],'WG_filler':'empty'},'after_AB_continuation':{'common_image':['B','D'],'WG_filler':'contractible','free_groupoid_defect':'[Y,Z] nontrivial'}},
    'two_coset_identifications_second_order':{'shared_C_to_D_primitive_history':list(common_cd),'different_B_to_A_words':{'plus':list(other_plus),'minus':list(other_minus)},'same_primitive_occurrence_counts':True,'free_group_tree_chord_images':{'plus':list(free_plus),'minus':list(free_minus)},'nonabelian_defect':list(free_commutator),'class2_graded_defect':'Y wedge Z'},
    'hamilton_path_expansion':{'oriented_hamilton_paths':24,'distinct_primitive_expansions':len(expansion_fibers),'collisions':{' '.join(expansion):pair for expansion,pair in expansion_fibers.items() if len(pair)>1}},
    'six_coset_identifications':{'unordered_complementary_paths':len(Ds),
                                  's_fixed_base_decompositions':base},
    'scope':'Cellular relation closure under incidence-level A4; does NOT prove native fillability or full-history action'
}
out=Path('/mnt/data/marici_equivariant_shortcut_obstruction_results.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print('PASS:',out)
print('six shortcuts:',missing)
print('initial boundary rank:',M6.rank(),'full A4-closed rank:',M24.rank())
print('first missing comparison: BC CA => BA; BC-occurrence detector = 1')
print('s-fixed equivariant bases: 2; each shortest-ancestry primitive overlap = 3')
print('24 Hamilton paths expand to 22 primitive words; 2 collisions at seam-inserted histories')
print('two s-fixed complements differ by free commutator [Y,Z]; additive edge counts equal')
print('WG: refusal before common AB, unique package comparison after; commutator survives')
print('canonical degree-two signature detects 8 changed pair orders; survives common suffix AB')
