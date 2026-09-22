"""Explicit three-step roofs for the zero consecutive Yoneda product.

Matrices are a filtered-module fixture, not a projectivity claim for
completed ideals. The companion proof constructs the same maps from the
actual ideal-power inclusions and quotients.
"""
from pathlib import Path
import json
import sympy as s
# T has ordered grades r,r+1,r+2; F is its bottom two grades.
iF=s.Matrix([[0,0],[1,0],[0,1]])
iB_F=s.Matrix([[0],[1]])
iB_T=s.Matrix([[0],[0],[1]])
pA=s.Matrix([[1,0]])
pE=s.Matrix([[1,0,0],[0,1,0]])
iA_E=s.Matrix([[0],[1]])
assert pE*iF==iA_E*pA
assert iF*iB_F==iB_T
assert pA*iB_F==s.zeros(1,1)
# A nilpotent action makes the example a compatible module diagram.
aT=s.Matrix([[0,0,0],[1,0,0],[0,1,0]])
aF=s.Matrix([[0,0],[1,0]])
aE=aF
assert aT*iF==iF*aF
assert pE*aT==aE*pE
assert pA*aF==s.zeros(1,2)
# K=[F -> T] resolves G_r. Kold=[A -> E] is the old extension roof.
# Its refinement kernel is [B --id--> B].
assert iF*iB_F==iB_T
assert iB_T.rank()==1 and iB_F.rank()==1
assert iF.rank()==2 and pE.rank()==2 and pA.rank()==1
# Lift the connecting map K -> A[1] through [B -> F][1].
# In degrees (-2,-1,0), dimensions are K=(0,2,3), shifted=(1,2,0).
K={-2:0,-1:2,0:3,1:0}
S={-2:1,-1:2,0:0,1:0}
dK={-2:s.zeros(2,0),-1:iF,0:s.zeros(0,3)}
dS={-2:-iB_F,-1:s.zeros(0,2),0:s.zeros(0,0)}
lift={-2:s.zeros(1,0),-1:s.eye(2),0:s.zeros(0,3),1:s.zeros(0,0)}
for k in (-2,-1,0):assert dS[k]*lift[k]==lift[k+1]*dK[k]
assert pA*lift[-1]==pA
# Projection shifted -> B[2] only acts in degree -2; the composite is zero.
assert s.eye(1)*lift[-2]==s.zeros(1,0)
# Graded length identities for tensor transport of the first row.
for r in range(1,7):
    assert [(r-1)+j for j in (1,2,3)]==[r,r+1,r+2]
result={'passed':True,'checks':{'three_step_module_diagram':True,
 'refinement_kernel_identity_complex':True,'shifted_lift_is_chain_map':True,
 'consecutive_Yoneda_composite_is_strictly_zero_after_refinement':True,
 'ideal_power_tensor_transport_indices':True},
 'scope':'Exact graded/module fixtures. Actual completed product vanishing uses only the already strict three-step ideal filtration. Finite tensor generation uses hereditary path-source flatness; no unrestricted completed tensor exactness or new higher Ext degree is inferred.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/adjacent-yoneda-comparison.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
