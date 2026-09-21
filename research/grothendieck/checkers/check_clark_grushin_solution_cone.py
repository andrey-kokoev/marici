"""Exact contraction of the bordered complex onto the solution observation cone."""
from pathlib import Path
import json
import sympy as s

P=s.Matrix([[2,1,0],[0,3,1],[1,0,2]])
W=s.Matrix([[1,0],[0,1],[1,1]])
O=s.Matrix([[1,2,0],[0,1,1]])
n,k=3,2
D=P.row_join(-W).col_join((-O).row_join(s.zeros(k)))
S=-O*P.inv()*W
im=P.inv()*W
Iminus=im.col_join(s.eye(k))
Izero=s.zeros(n,k).col_join(s.eye(k))
Rminus=s.zeros(k,n).row_join(s.eye(k))
Rzero=(O*P.inv()).row_join(s.eye(k))
H=P.inv().row_join(s.zeros(n,k)).col_join(s.zeros(k,n+k))
assert D*Iminus==Izero*S
assert Rzero*D==S*Rminus
assert Rminus*Iminus==s.eye(k) and Rzero*Izero==s.eye(k)
assert H*D==s.eye(n+k)-Iminus*Rminus
assert D*H==s.eye(n+k)-Izero*Rzero
assert S.det()!=0 and D.det()!=0
assert len(O.nullspace())==1
v=O.nullspace()[0]
assert P*v!=s.zeros(n,1)
# A source-preserving map into the solution cone requires bulk satisfaction.
for j in range(k):
    c=s.eye(k)[:,j]
    x=P.inv()*W*c
    assert P*x-W*c==s.zeros(n,1)
    assert -O*x==S*c
# Different full-domain observations can agree on the source solution graph.
annihilator=im.T.nullspace()[0].T
Delta=s.Matrix([1,2])*annihilator
assert Delta!=s.zeros(k,n) and Delta*im==s.zeros(k,k)
Og=O+Delta
Dg=P.row_join(-W).col_join((-Og).row_join(s.zeros(k)))
shear=s.eye(n).row_join(s.zeros(n,k)).col_join((-Delta*P.inv()).row_join(s.eye(k)))
assert shear*D==Dg and shear.det()==1
# Induced source Gram, retaining a declared positive bulk metric.
G=s.diag(1,2,3)
sourceGram=im.T*G*im
assert sourceGram.det()>0 and sourceGram[0,0]>0
result={'schema':'marici.grothendieck.clark-grushin-solution-cone.v1',
        'passed':True,'bulk_dimension':n,'port_dimension':k,
        'checks':{'inclusion_chain_map':True,'retraction_chain_map':True,
                  'both_deformation_homotopies':True,'solution_graph':True,
                  'unrestricted_observation_cone_has_extra_kernel':True,
                  'source_gram_positive_fixture':True,'source_restricted_observation_shear':True},
        'schur_matrix':[[str(v) for v in S.row(i)] for i in range(k)],
        'scope':'Exact invertible-chart block theorem. Independent analytic input/output incidence identification and seam completion remain separate.'}
p=Path(__file__).resolve().parents[1]/'results/clark-grushin-solution-cone.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
