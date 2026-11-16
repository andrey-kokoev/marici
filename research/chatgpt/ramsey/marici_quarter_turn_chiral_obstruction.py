#!/usr/bin/env python3
"""Exact quarter-turn/chiral-comparison obstruction and minimal two-sheet repair.

Sources: research/realization-tower/cellulation-white-clone.mjs and
research/nima/binary-tetrahedral-spinor-bridge.md (tetrahedron coordinates).
The twelve chiral comparison fillers are CONDITIONAL and not native-generated.
No physical realization or Ramsey forcing law is asserted.
"""
from itertools import permutations
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

vnames='ABCD'
positions={'A':s.Matrix([1,1,1]),'B':s.Matrix([1,-1,-1]),
           'C':s.Matrix([-1,1,-1]),'D':s.Matrix([-1,-1,1])}
J=s.Matrix([[-1,0,0],[0,0,1],[0,-1,0]])
assert J.det()==-1 and J**4==s.eye(3)
lookup={tuple(x):v for v,x in positions.items()}
j={v:lookup[tuple(J*x)] for v,x in positions.items()}
assert j==dict(zip(vnames,'CDBA'))
swap={v:j[j[v]] for v in vnames}
assert swap==dict(zip(vnames,'BADC'))
assert all(j[j[j[j[v]]]]==v for v in vnames)

G=dict(zip(vnames,'BCAD'))
H=dict(zip(vnames,'DACB'))
idmap={v:v for v in vnames}
def mul(p,q):return {v:p[q[v]] for v in vnames}
A4={tuple(idmap.values()):idmap}; queue=[idmap]
while queue:
    p=queue.pop()
    for g in (G,H):
        q=mul(p,g);k=tuple(q[v] for v in vnames)
        if k not in A4:A4[k]=q;queue.append(q)
assert len(A4)==12
plus={''.join(p[v] for v in 'ABC') for p in A4.values()}
all_tri={''.join(t) for t in permutations(vnames,3)}
minus=all_tri-plus
assert len(plus)==len(minus)==12
assert 'ABC' in plus and 'ADB' in plus
assert {''.join(j[v] for v in t) for t in plus}==minus
assert {''.join(j[v] for v in t) for t in minus}==plus
assert {''.join(swap[v] for v in t) for t in plus}==plus

edges={a+b for a in vnames for b in vnames if a!=b}
orig={'AB','BC','CA','AD','DB','BA'}
assert {''.join(j[v] for v in e) for e in orig}=={'CD','DB','BC','CA','AD','DC'}

# Z4 cocycle vanishes on the 12 admitted chiral 2-cell boundaries.
def weights(a,b):
  m={'AB':a,'BA':a,'AD':b,'BC':b,'CA':a-b,'DB':a-b,
     'AC':a+b,'BD':a+b,'CB':2*a-b,'DA':2*a-b,
     'CD':-a,'DC':-a}
  return {e:x%4 for e,x in m.items()}
w=weights(1,3)
def curvature(t):
    u,v,z=t
    return (w[u+v]+w[v+z]-w[u+z])%4
assert all(curvature(t)==0 for t in plus)
assert all(curvature(t)==2 for t in minus)
assert curvature('ABC')==0 and curvature('CDB')==2
assert (w['AB']+w['BA'])%4==2

# One chiral sheet, its opposite, their graph-identified union, and a
# vertex-only glued double (distinct occurrences retained on each sheet).
def homology(which):
    if which=='chiral':
        sheets=['']; es=[('',e) for e in sorted(edges)]
        fs=[('',t) for t in sorted(plus)]
    elif which=='both_on_same_edges':
        es=[('',e) for e in sorted(edges)]
        fs=[('',t) for t in sorted(all_tri)]
    elif which=='shared_vertices_separate_edges':
        es=[(name,e) for name in ('+','-') for e in sorted(edges)]
        fs=[('+',t) for t in sorted(plus)]+[('-',t) for t in sorted(minus)]
    else:raise ValueError(which)
    idx={e:i for i,e in enumerate(es)}
    B=s.zeros(len(es),len(fs))
    for col,(name,t) in enumerate(fs):
        a,b,c=t
        for edge,sign in [(a+b,1),(b+c,1),(a+c,-1)]:
            B[idx[name,edge],col]+=sign
    # Spanning-tree edges of the first sheet. Projection onto complement
    # identifies integer graph H1 with Z^(E-V+1) via a unimodular basis.
    sheet=es[0][0]
    tree={idx[sheet,e] for e in ['AB','BC','AD']}
    restricted=B[[i for i in range(len(es)) if i not in tree],:]
    D=smith_normal_form(restricted,domain=ZZ)
    nz=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]!=0]
    rk=len(nz)
    return {'V':4,'E':len(es),'F':len(fs),'rank_boundary2':rk,
            'H1_free_rank':len(es)-3-rk,
            'H1_torsion_invariants':[x for x in nz if x>1],
            'H2_free_rank':len(fs)-rk}

h={k:homology(k) for k in ['chiral','both_on_same_edges','shared_vertices_separate_edges']}
assert (h['chiral']['H1_torsion_invariants'],h['chiral']['H2_free_rank'])==([2],3)
assert (h['both_on_same_edges']['H1_torsion_invariants'],h['both_on_same_edges']['H2_free_rank'])==([],15)
assert (h['shared_vertices_separate_edges']['H1_free_rank'],h['shared_vertices_separate_edges']['H1_torsion_invariants'],h['shared_vertices_separate_edges']['H2_free_rank'])==(3,[2,2],6)

# Two-sheet C4 action. On each sheet flip plus/minus and act by j on labels.
def act_sheet(sheet,word):
    return ('-' if sheet=='+' else '+',''.join(j[v] for v in word))
for sheet,ts in [('+',plus),('-',minus)]:
    for t in ts:
        s2,t2=act_sheet(sheet,t)
        assert t2 in (plus if s2=='+' else minus)
        s3,t3=act_sheet(s2,t2)
        assert s3==sheet and t3==''.join(swap[v] for v in t)
        z=(sheet,t)
        for _ in range(4):z=act_sheet(*z)
        assert z==(sheet,t)

report={
    'status':'verified',
    'quarter_turn_vertex_permutation':j,
    'square_seed_reflection':swap,
    'spatial_determinant':int(J.det()),
    'maps_ABC_to':'CDB',
    'maps_original_AB_to':'CD',
    'chiral_orbits':{'admitted':len(plus),'opposite':len(minus)},
    'chiral_curvature_Z4':0,
    'opposite_curvature_Z4':2,
    'no_chain_map_lift_reason':'j sends admitted face boundary to nonzero class in H1(Z/2)',
    'homology':h,
    'two_sheet_action':'strict C4; j exchanges chirality sheets, j^2 acts as seed reflection',
    'scope':'conditional chiral 2-cell admission; sheets are a constructed extension, not source-generated'
}
Path('/mnt/data/marici_quarter_turn_chiral_obstruction_results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
