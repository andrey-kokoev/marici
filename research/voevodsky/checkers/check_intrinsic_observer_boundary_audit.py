"""Independent finite-module audit of the intrinsic boundary formulas.

Exact nilpotent-action fixtures test module identities, not reconstruction
from numerical observer states. The companion proof derives the identities
for the actual source quotient and its already checked graded-line lift.
"""
from pathlib import Path
import json
import sympy as s

def jordan(n):
    J=s.zeros(n)
    for i in range(n-1):J[i+1,i]=1
    return J
J=s.diag(jordan(3),jordan(2))
J2=s.diag(s.zeros(1),jordan(2))
p=s.Matrix([[1,0,0,0,0],[0,0,0,1,0],[0,0,0,0,1]])
assert p*J==J2*p and p.rank()==3
assert J**3==s.zeros(5) and J2**2==s.zeros(3)
E=s.eye(5)
K=E[:,1:3]
M=s.Matrix.hstack(*J.columnspace())
L=s.Matrix.hstack(*(J**2).columnspace())
assert K.rank()==2 and M.rank()==3 and L.rank()==1
assert M.row_join(K).rank()==M.rank() # K subset M, so N=K here
N=K
assert (J*N).rank()==L.rank()==(J*N).row_join(L).rank()
assert p*L==s.zeros(3,1)
Q=s.Matrix.hstack(*(J2.columnspace()))
assert Q.rank()==1
# Equivariant old-line lift. Defined on Q (last base coordinate) only.
j=s.zeros(5,3);j[4,2]=1
assert p*j*Q==Q
assert J*j*Q==j*J2*Q
rhoM=(s.eye(5)-j*p)*M
assert rhoM.rank()==2 and rhoM.row_join(N).rank()==2
assert (s.eye(5)-j*p)*L==L
# Any map N -> a t-annihilated scalar must kill JN=L.
JN=N.gauss_jordan_solve(J*N)[0]
assert JN==jordan(2)
# The scalar lambda on L, normalized to 1, cannot extend equivariantly.
# r=(a,b) on N would need r JN=0 and b=1.
a,b=s.symbols('a b')
r=s.Matrix([[a,b]])
assert s.solve(list(r*JN)+[b-1],(a,b))==[]
# Independent copies model separately retained top readouts: the boundary
# map is injective for each coefficient covector, since IN=L in all copies.
for copies in (1,2,3):
    JNmulti=s.diag(*([jordan(2)]*copies))
    assert JNmulti.rank()==copies and (JNmulti**2)==s.zeros(2*copies)
# Actual top coefficient audit: all cubic scalar frames have the same row;
# the separately retained private coordinates and vacuum add independent rows.
S0,Sx=s.symbols('S0 Sx',nonzero=True)
res=s.Matrix([[S0,Sx,0]])
p0=s.Matrix([[1,0,0]]);px=s.Matrix([[0,1,0]]);vac=s.Matrix([[0,0,1]])
assert res.rank()==1
assert res.col_join(vac).rank()==2
assert res.col_join(p0).col_join(px).rank()==2
assert res.col_join(p0).col_join(px).col_join(vac).rank()==3
# Source calibration is not recoverable from the fixed module alone:
# scaling compatible surjective evaluations leaves all action/rank data fixed.
scale=s.Rational(2)
assert (scale*M).columnspace()==M.columnspace() or (scale*M).row_join(M).rank()==M.rank()
result={'passed':True,'checks':{
 'L_is_second_ideal_action_image':True,'N_is_kernel_intersect_first_action_image':True,
 'old_line_projection_has_image_N':True,'I_times_N_equals_L':True,
 'nonzero_top_readout_cannot_extend_to_N':True,
 'boundary_readout_ranks_1_2_3':True,
 'source_calibration_separate_from_module_data':True},
 'scope':'Exact finite module/rank fixtures. Actual intrinsic-image identities follow from surjective evaluation of I/I^4 and the proved source-compatible line lift. Numerical states alone do not supply the source action, ideal, labels, or source-evaluation calibration.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/intrinsic-observer-boundary-audit.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
