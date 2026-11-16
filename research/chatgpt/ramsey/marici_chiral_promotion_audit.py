#!/usr/bin/env python3
"""Exact integer audit of chiral comparison-orbit closure on the Marici seed.
All 2-cells are hypothetical admission choices, not native Agda fillers.
"""
import itertools, json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

V = tuple('ABCD')
NATIVE = {'AB','BC','CA','AD','DB','BA'}
CYCLES = [('A','B','C'), ('A','D','B')]
ARCS = [(u,v) for u in V for v in V if u != v]
TRIPLES = list(itertools.permutations(V,3))

def parity(seq, vertices):
    nums = [vertices.index(x) for x in seq]
    return sum(nums[i] > nums[j] for i in range(len(nums)) for j in range(i+1,len(nums))) % 2

def alternating(vertices):
    return [dict(zip(vertices,p)) for p in itertools.permutations(vertices) if parity(p,vertices)==0]

def orbit(seed,group):
    return frozenset(tuple(g[v] for v in seed) for g in group)

def matrices(vertices, arcs, triples):
    d1=sp.zeros(len(vertices),len(arcs))
    for j,(u,v) in enumerate(arcs):
        d1[vertices.index(u),j]=-1
        d1[vertices.index(v),j]=1
    d2=sp.zeros(len(arcs),len(triples))
    for j,(u,v,w) in enumerate(triples):
        for e,c in (((u,v),1),((v,w),1),((u,w),-1)):
            d2[arcs.index(e),j] += c
    assert d1*d2 == sp.zeros(len(vertices),len(triples))
    return d1,d2

def mod2_rank(M):
    rows = [sum((int(M[i,j])&1)<<j for j in range(M.cols)) for i in range(M.rows)]
    rank=0
    for j in range(M.cols):
        i=next((k for k in range(rank,len(rows)) if (rows[k]>>j)&1),None)
        if i is None:continue
        rows[rank],rows[i]=rows[i],rows[rank]
        for k in range(len(rows)):
            if k!=rank and ((rows[k]>>j)&1):rows[k]^=rows[rank]
        rank+=1
    return rank

def info(vertices, arcs, triangles):
    faces=sorted(triangles)
    d1,d2=matrices(vertices,arcs,faces)
    diag=smith_normal_form(d2,domain=ZZ)
    invariants=[abs(int(diag[i,i])) for i in range(min(diag.rows,diag.cols)) if diag[i,i]!=0]
    r1=len(vertices)-1
    r2=len(invariants)
    return dict(vertices=len(vertices),arcs=len(arcs),faces=len(faces),
                rank_boundary1=r1,rank_boundary2=r2,
                boundary2_smith=invariants,
                homology1_free=len(arcs)-r1-r2,
                homology1_torsion=[x for x in invariants if x>1],
                homology2_free=len(faces)-r2), d2

A4=alternating(V)
assert len(A4)==12
SRC=orbit(('A','B','C'),A4)
assert ('A','D','B') in SRC
ALT=frozenset(TRIPLES)-SRC
assert len(SRC)==len(ALT)==12
assert orbit(('C','A','D'),A4)==ALT
shortcuts={
    'AC':'ABC',
    'BD':'BAD',
    'CB':'CAB',
    'DA':'DBA',
    'CD':'CAD',
    'DC':'DBC',
}
assert {u+v for (u,v) in ARCS}-NATIVE == set(shortcuts)
assert all(path[:2] in NATIVE and path[1:] in NATIVE for path in shortcuts.values())
NATIVE_FACES=frozenset(tuple(path) for path in shortcuts.values())
assert len(NATIVE_FACES)==6
chiral_counts={'source':len(NATIVE_FACES & SRC),'opposite':len(NATIVE_FACES & ALT)}
assert chiral_counts=={'source':4,'opposite':2}
assert frozenset().union(*(orbit(t,A4) for t in NATIVE_FACES)) == frozenset(TRIPLES)

native_results,d_native=info(V,ARCS,NATIVE_FACES)
source_results,d_source=info(V,ARCS,SRC)
alt_results,d_alt=info(V,ARCS,ALT)
full_results,d_full=info(V,ARCS,TRIPLES)
assert native_results['homology1_free']==3 and native_results['homology1_torsion']==[]
assert native_results['homology2_free']==0
for q in (source_results,alt_results):
    assert q['homology1_free']==0 and q['homology1_torsion']==[2]
    assert q['homology2_free']==3
assert full_results['homology1_free']==0 and full_results['homology1_torsion']==[]
assert full_results['homology2_free']==15

seam=sp.zeros(len(ARCS),1)
for e in [('A','B'),('B','A')]:seam[ARCS.index(e),0]=1
assert mod2_rank(d_source.row_join(seam)) == mod2_rank(d_source)+1
assert mod2_rank(d_alt.row_join(seam)) == mod2_rank(d_alt)+1
assert mod2_rank(d_full.row_join(seam)) == mod2_rank(d_full)
# Opposite triangle comparison kills the only first-homology torsion class.
for t in ALT:
    info_plus,_=info(V,ARCS,set(SRC)|{t})
    assert info_plus['homology1_free']==0 and info_plus['homology1_torsion']==[]
for t in SRC:
    info_plus,_=info(V,ARCS,set(ALT)|{t})
    assert info_plus['homology1_free']==0 and info_plus['homology1_torsion']==[]

# Nontrivial parity cocycle for the seed-oriented orbit. For each opposite
# pair exactly one arrow evaluates to 1, so it detects any reciprocal seam.
omega_on={'AB','AD','BC','BD','CA','CD'}
assert all((u+v in omega_on)!=(v+u in omega_on) for (u,v) in ARCS)
for u,v,w in SRC:
    assert ((u+v in omega_on)+(v+w in omega_on)-(u+w in omega_on))%2==0
assert ((('AB' in omega_on)+('BA' in omega_on))%2)==1

# On five vertices the alternating group has a single orbit of ordered triples.
V5=tuple('ABCDE')
A5=alternating(V5)
O5=orbit(('A','B','C'),A5)
assert len(A5)==60 and len(O5)==60
assert len(set(itertools.permutations(V5,3)))==60
assert ('A','C','B') in O5
swap={'A':'A','B':'C','C':'B','D':'E','E':'D'}
assert swap in A5
assert tuple(swap[v] for v in ('A','B','C'))==('A','C','B')
A5_arcs=[(u,v) for u in V5 for v in V5 if u!=v]
five_results,_=info(V5,A5_arcs,O5)
assert five_results['homology1_free']==0 and five_results['homology1_torsion']==[]

result={'status':'passed',
        'scope':'formal directed 2-cell complexes; comparison fillers are conditional',
        'native_directed_edges':sorted(NATIVE),
        'missing_incidence_shortcuts':shortcuts,
        'source_orbit_contains_both_original_triangles': True,
        'source_orbit': [''.join(t) for t in sorted(SRC)],
        'opposite_orbit':[''.join(t) for t in sorted(ALT)],
        'native_shortcut_chirality_counts':chiral_counts,
        'native_shortcuts':native_results,
        'source_orbit_comparisons':source_results,
        'opposite_orbit_comparisons':alt_results,
        'all_orbits_comparisons':full_results,
        'seam_is_nonzero_mod2_in_either_chiral_orbit':True,
        'each_single_opposite_face_kills_torsion':True,
        'five_vertex_A5_ordered_triple_orbit_size':len(O5),
        'five_vertex_complete_comparisons':five_results,
        'not_established':['native acceptance of new 2-cell witnesses',
                           'global A4 action on retained path histories',
                           'Ramsey color admissibility']}
with open('/mnt/data/marici_chiral_promotion_audit_results.json','w') as f:
    json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in result.items() if k in ['status','native_shortcut_chirality_counts','native_shortcuts','source_orbit_comparisons','all_orbits_comparisons','five_vertex_A5_ordered_triple_orbit_size','five_vertex_complete_comparisons']},indent=2))
