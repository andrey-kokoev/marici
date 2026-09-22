"""Exact module/complex fixtures for consistency versus depth extensions.

The nonsplit fixture is k[t]/(t^2) -> k, not a replacement for the actual
source proof. Frame changes are nonidentity compatible scalar transports.
"""
from pathlib import Path
import json
import sympy as s
F=4
weights=list(map(s.Rational,range(1,F+1)))
i=s.Matrix(weights);r=s.zeros(1,F);r[0,0]=1
D=s.zeros(F-1,F);h=s.zeros(F,F-1)
for f in range(1,F):
    D[f-1,0]=-1;D[f-1,f]=1/weights[f]
    h[f,f-1]=weights[f]
assert r*i==s.eye(1)
assert D*i==s.zeros(F-1,1)
assert D*h==s.eye(F-1)
assert r*h==s.zeros(1,F-1)
assert i*r+h*D==s.eye(F)
A=r.col_join(D);B=i.row_join(h)
assert A*B==s.eye(F) and B*A==s.eye(F)
# A nonsplit depth extension: p maps [top,bottom] to top, t(top)=bottom.
p=s.Matrix([[1,0]]);j=s.Matrix([[0],[1]])
J=j*p
assert p*j==s.zeros(1,1) and J*J==s.zeros(2)
# Any section u would satisfy p*u=1 and J*u=0, but J*u=j*p*u=j!=0.
assert J==j*p and j.rank()==1
# Exact incompatible linear equations for that module section.
constraints=p.col_join(J);rhs=s.Matrix([1,0,0])
assert constraints.rank()<constraints.row_join(rhs).rank()
# Horizontal maps at the middle of the extension; all commute with t.
i2=s.kronecker_product(i,s.eye(2));r2=s.kronecker_product(r,s.eye(2))
D2=s.kronecker_product(D,s.eye(2));h2=s.kronecker_product(h,s.eye(2))
P=s.kronecker_product(s.eye(F),p)
PD=s.kronecker_product(s.eye(F-1),p)
assert D*P==PD*D2
assert r*P==p*r2
assert P*i2==i*p
assert P*h2==h*PD
Jall=s.kronecker_product(s.eye(F),J)
JD=s.kronecker_product(s.eye(F-1),J)
assert D2*Jall==JD*D2
assert Jall*i2==i2*J
assert Jall*h2==h2*JD
assert i2*r2+h2*D2==s.eye(2*F)
# Decomposition into synchronized and discrepancy depth extensions.
A2=s.kronecker_product(A,s.eye(2))
assert A*P==P*A2
jD=s.kronecker_product(s.eye(F-1),j)
assert JD==jD*PD and jD.rank()==F-1
# Compatible horizontal homotopy: Dh=id and hD=id-ir at both rungs.
assert D2*h2==s.eye(2*(F-1))
assert h2*D2==s.eye(2*F)-i2*r2
result={'passed':True,'frames':F,'checks':{
 'nonidentity_frame_transports':True,'horizontal_source_equivariant_deformation_retraction':True,
 'homotopy_and_splittings_commute_with_depth':True,
 'synchronized_kernel_inclusion_has_retraction':True,
 'discrepancy_annihilates_synchronized_kernel':True,
 'single_depth_extension_is_nonsplit':True,
 'discrepancy_depth_extension_is_F_minus_1_nonsplit_copies':True},
 'scope':'Exact algebraic fixtures and signs. Corrected source nonsplitting is proved separately by its actual fully observed initial corner and positive higher witness; no global completed projectivity or source realization is inferred.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/consistency-tower-extension-transport.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
