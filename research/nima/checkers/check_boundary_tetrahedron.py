"""Bounded tetrahedral audit. Standard library; never runs supplier main()."""
from __future__ import annotations
import ast
import hashlib
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

SOURCE=Path('research/chatgpt/coefficient-marked-boundary/check_coefficient_marked_boundary.py')
raw=SOURCE.read_bytes()
# Only the inspected local matrix constructors and their helpers are executed.
wanted={'check','pm','normalized','crosses','faces','subsets','add','apply','degree','project','Loaded'}
tree=ast.parse(raw)
selected=[n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name in wanted]
assert {n.name for n in selected}==wanted
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0)]+selected,type_ignores=[])
ns={'COUNTS':Counter(),'combinations':combinations}
exec(compile(ast.fix_missing_locations(module),str(SOURCE),'exec'),ns)
Loaded,apply,add,project,crosses,normalized=[ns[n] for n in ('Loaded','apply','add','project','crosses','normalized')]
empty=((),())
ds=tuple((i,j) for i in range(8) for j in range(i+1,8) if j-i not in (1,7))
cuts=tuple(sorted({normalized(i,i+3) for i in range(8)}))
edges=tuple(e for e in combinations(cuts,2) if not crosses(*e))
charts={c:Loaded(tuple(d for d in ds if d!=c and not crosses(d,c))) for c in cuts}
overlaps={e:Loaded(tuple(d for d in ds if d not in e and all(not crosses(d,c) for c in e))) for e in edges}
assert len(charts)==8 and len(overlaps)==12
assert all(len(c.cells)==1075 for c in charts.values())
assert all(len(c.cells)==125 for c in overlaps.values())
for c in list(charts.values())+list(overlaps.values()):c.audit()
counts=Counter();wrong_face_detected=0
for e,B in overlaps.items():
    for cut in e:
        A=charts[cut]
        # Vertices (A,B,B,Z); edges P, P, eps_A, i_B eps_B, eps_B, eps_B.
        # f01=P, f02=P, f03=eps_A, f12=i eps, f13=eps, f23=eps.
        # delta Hijk=fjk fij-fik. H012=-H_B P; other three faces zero.
        assert project(A.unit,B.cellset)==B.unit
        assert B.unit.get(empty)==1
        for x in A.cells:
            v={x:1};p=project(v,B.cellset)
            assert project(A.d[x],B.cellset)==apply(B.d,p)
            hp=apply(B.H,p)
            assert project(A.H[x],B.cellset)==hp
            h=add({},hp,-1)
            dh=add(apply(B.d,h),add({},apply(B.H,project(A.d[x],B.cellset)),-1))
            reduced={c:a*p.get(empty,0) for c,a in B.unit.items() if a*p.get(empty,0)}
            defect=add(reduced,p,-1)
            assert dh==defect
            # Remaining faces: eps P=eps_A and eps i eps=eps.
            assert p.get(empty,0)==int(x==empty)
            assert reduced.get(empty,0)==p.get(empty,0)
            # R=H013+H123 f01-H023-f23 H012. All but last zero.
            residual=-h.get(empty,0)
            assert residual==0  # explicit K=0 satisfies delta K=R
            counts['generator_face_and_filler_tests']+=1
            if defect:
                # Reverse the sign of the nonzero face: fails its stated boundary.
                assert add({},dh,-1)!=defect
                wrong_face_detected+=1
        counts['typed_tetrahedra']+=1
assert counts['typed_tetrahedra']==24 and wrong_face_detected>0
# Genuine nonfiller control: V=Z in degrees -1 and 0, d=0; every edge id.
# H012 sends degree 0 basis to degree -1 basis; all other faces zero.
# Every face satisfies delta H=0. R=-H012 is nonzero, while Hom^-2(V,V)=0.
H=((0,1),(0,0))  # basis order (-1,0)
R=tuple(tuple(-a for a in row) for row in H)
assert any(a for row in R for a in row)
assert not any(target==source-2 for source in (-1,0) for target in (-1,0))
# Readout collision in the constant-source-variable subfamily of conductor pairs.
pair_a=((1,),(1,));pair_b=((1,1),(1,))
def conductor(p):
    assert p[0][0]==p[1][0]
    return p[0][0]
assert pair_a!=pair_b and conductor(pair_a)==conductor(pair_b)==1
# In the stated unshifted nonnegative conductor model there are no degree -1
# cochains whose boundary could identify these degree-zero cocycles.
result={'status':'passed','source_sha256':hashlib.sha256(raw).hexdigest(),
'counts':dict(counts),'supplier_local_checks':dict(ns['COUNTS']),
'wrong_face_sign_detected_generators':wrong_face_detected,
'filler':'K=0; the single nonzero face is killed by epsilon H=0',
'nonfiller_control':'Four valid faces on V=Z[-degree1] plus Z[degree0], d=0; nonzero R and zero Hom^-2',
'encoding_collision':{'a':'(1,1)','b':'(1+z_plus,1)','common_readout':1,'lost_coordinate':'positive branch polynomial; distinct pi0 markings'},
'scope':'24 local primitive tetrahedra, not an encoding of the entire pyramid; supplier geometric provenance and physical elimination of branch modes unverified'}
out=Path('research/nima/results/boundary_tetrahedron.json')
assert not out.exists(), 'Do not overwrite an existing run result'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
