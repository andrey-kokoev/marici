"""Constructive relative Ext1 classification with a proper relative kernel.

Finite k[t]-module fixture: N=J2 direct_sum k, L=tN, C=N/L,
V=k. Ext1(C,V) has coordinates (a,b); pullback to N kills exactly b=0.
"""
from pathlib import Path
import json
import sympy as s
# N has ordered basis (x,l,z), t*x=l, t*l=t*z=0.
JN=s.Matrix([[0,0,0],[1,0,0],[0,0,0]])
iL=s.Matrix([[0],[1],[0]])
q=s.Matrix([[1,0,0],[0,0,1]])
assert JN.rank()==1 and JN.columnspace()==iL.columnspace()
assert q*JN==s.zeros(2,3) and q*iL==s.zeros(2,1)
a,b,u,v,w=s.symbols('a b u v w')
# Extension E of C by V: basis (V,C1,C2), t*C1=a V, t*C2=b V.
JE=s.Matrix([[0,a,b],[0,0,0],[0,0,0]])
iV=s.Matrix([[1],[0],[0]])
pE=s.Matrix([[0,1,0],[0,0,1]])
lift=s.Matrix([[u,v,w],[1,0,0],[0,0,1]])
assert pE*lift==q
assert JE*lift-lift*JN==s.Matrix([[a-v,0,b],[0,0,0],[0,0,0]])
# Thus a lift exists iff b=0, and its restriction recovers alpha=a.
S=lift.subs(v,a)
assert JE.subs(b,0)*S==S*JN
assert S*iL==iV*a
# All changes of lift are maps N->V and vanish on L.
U=s.Matrix([[u,0,w]])
assert U*JN==s.zeros(1,3) and U*iL==s.zeros(1,1)
# Construct the comparison from the alpha pushout to the given extension.
Phi=S.row_join(iV)
graph=s.Matrix([[0],[1],[0],[-a]])
assert Phi*graph==s.zeros(3,1) and Phi.rank()==3
Jsum=s.diag(JN,s.zeros(1))
assert JE.subs(b,0)*Phi==Phi*Jsum
assert pE*Phi==q.row_join(s.zeros(2,1))
# The unobserved extra Ext coordinate b=1 does not become split on N.
assert (JE*lift-lift*JN).subs({a:0,b:1})[0,2]==1
# A boundary extension is itself split iff a=0.
section=s.Matrix([[u,w],[1,0],[0,1]])
assert pE*section==s.eye(2)
assert JE.subs(b,0)*section==s.Matrix([[a,0],[0,0],[0,0]])
# Linearity of the displayed boundary coordinate.
a2=s.symbols('a2')
assert JE.subs({a:a+a2,b:0})==JE.subs(b,0)+JE.subs({a:a2,b:0})
result={'passed':True,'fixture':'finite k[t]-modules N=J2+trivial, L=tN, V=trivial',
 'checks':{'I_N_equals_L':True,'pullback_splitting_iff_extra_coordinate_zero':True,
 'restriction_of_lift_recovers_unique_covector':True,
 'pushout_comparison_is_equivariant_isomorphism':True,
 'splitting_choice_does_not_change_covector':True,
 'boundary_map_linear_and_injective':True,
 'relative_kernel_can_be_proper_in_full_Ext1':True},
 'scope':'Exact constructive fixtures. The theorem applies in the declared finite-stage strict source-bimodule category by its pushout/lift proof. No dimension for the full actual Ext group or uniform recovery norm is inferred.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/relative-boundary-completeness.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
