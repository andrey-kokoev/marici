#!/usr/bin/env python3
"""Exact source-geodesic comparison defects, full cycle basis, and 4-way cocycle.

Diagnostics use the FORMAL groupoid completion (signed inverse occurrences),
not Marici's executable reverse traversal or newly admitted 2-cells.
"""
from itertools import permutations, combinations
from collections import Counter
from pathlib import Path
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
import json
V='ABCD'
E={'AB':('A','B'),'BC':('B','C'),'CA':('C','A'),
   'AD':('A','D'),'DB':('D','B'),'BA':('B','A')}
out={u:[e for e,(a,b) in E.items() if a==u] for u in V}

def all_paths(s,t,n):
    if n==0:
        if s==t:yield ()
    else:
        for e in out[s]:
            for q in all_paths(E[e][1],t,n-1):yield (e,)+q

def geodesic(u,v):
    if u==v:return ()
    for n in (1,2,3,4,5):
        xs=list(all_paths(u,v,n))
        if xs:
            assert len(xs)==1, (u,v,xs)
            return xs[0]
    raise AssertionError('disconnected')
p={(u,v):geodesic(u,v) for u in V for v in V}
assert len({x for x in p.values() if len(x)==1})==6
assert len({x for x in p.values() if len(x)==2})==6

def inv(word):return tuple((e,-sgn) for e,sgn in word[::-1])
def pos(word):return tuple((e,1) for e in word)
def reduced(word):
    stack=[]
    for e,sgn in word:
        if stack and stack[-1]==(e,-sgn):stack.pop()
        else:stack.append((e,sgn))
    return tuple(stack)
def concatenate(*ws):return reduced(sum(ws,()))
def curvature(u,v,w):
    return concatenate(pos(p[(u,v)]),pos(p[(v,w)]),inv(pos(p[(u,w)])))

def chordvec(u,v,w):
    a=p[u,v]+p[v,w];b=p[u,w]
    return tuple(a.count(k)-b.count(k) for k in ('BC','DB','BA'))

strict=[];nontrivial=[]
for u,v,w in permutations(V,3):
    q=curvature(u,v,w)
    if q:nontrivial.append(''.join((u,v,w)))
    else:strict.append(''.join((u,v,w)))
assert len(strict)==6 and len(nontrivial)==18
assert len(set(chordvec(*q) for q in nontrivial))==5

# Exhibit integral basis corresponding to three original independently
# generated fundamental cycles (oriented spanning tree AB, AD, reverse CA).
D={triple:chordvec(*triple) for triple in nontrivial}
basis=('ABD','ACB','ADB')
B=Matrix.hstack(*[Matrix(D[t]) for t in basis])
assert abs(B.det())==1
allmat=Matrix.hstack(*[Matrix(D[t]) for t in nontrivial])
assert allmat.rank()==3
snf=smith_normal_form(allmat,domain=ZZ)
assert [snf[i,i] for i in range(3)]==[1,1,1]

# The three based nonabelian loops (including inverse of AB as a FORMAL
# inverse, not a supplied BA occurrence) are exactly a free graph basis:
#   ABD = AB BA
#   ACB = AB BC CA
#   ADB = AD DB (AB)^-1.
assert curvature(*'ABD')==pos(('AB','BA'))
assert curvature(*'ACB')==pos(('AB','BC','CA'))
assert curvature(*'ADB')==(('AD',1),('DB',1),('AB',-1))

# Nonabelian 2-cocycle / tetrahedral pasting identity:
# d_uvw d_uwx = (p_uv d_vwx p_uv^-1) d_uvx.
for u,v,w,x in permutations(V,4):
    left=concatenate(curvature(u,v,w),curvature(u,w,x))
    right=concatenate(pos(p[u,v]),curvature(v,w,x),inv(pos(p[u,v])),curvature(u,v,x))
    assert left==right,(u,v,w,x,left,right)

# s-equivariance of unique minimal path dictionary, including its
# non-identity based defects.
s={'A':'B','B':'A','C':'D','D':'C'}
e_by_pair={vv:k for k,vv in E.items()}
def move_word(word):return tuple(e_by_pair[(s[E[e][0]],s[E[e][1]])] for e in word)
for u,v in permutations(V,2):
    assert move_word(p[u,v])==p[s[u],s[v]]

result={
 'source':list(E),'objects':list(V),'source_homology_rank':3,
 'unique_shortest_macro_arrows':12,
 'ordered_distinct_triangle_requests':24,'strict_flat_triangles':len(strict),
 'nontrivial_defect_triangles':len(nontrivial), 'strict_triangles':strict,
 'defect_cycle_coordinate_basis':{'coordinate_tree_edges':['AB','AD','CA'],
    'free_chords':['BC','DB','BA'],
    'based_defects':{
        'ABD':'AB BA', 'ACB':'AB BC CA', 'ADB':'AD DB (AB)^(-1)'},
    'chord_matrix':[[int(B[i,j]) for j in range(3)] for i in range(3)],
    'determinant':int(B.det())},
 'all_nontrivial_defects_smith_invariants':[1,1,1],
 'ordered_four_vertex_cocycle_pastings_verified':24,
 'nonabelian_cocycle_identity':'d_uvw*d_uwx = p_uv*d_vwx*p_uv^-1*d_uvx',
 'source_reflection_preserves_shortest_paths':True,
 'scope':'defects are in formal groupoid/chain diagnostics; no native 2-cell or reverse execution is inferred'
}
Path('/mnt/data/marici_geodesic_curvature_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
