"""Redundant-row quotient: proof retraction strictifies linearly, but surplus remains."""
from pathlib import Path
import json
from fractions import Fraction as Q
# A=[-1,1], A'=[-1,1,1], bounds b=[0,1], b'=[0,1,2].
M=((1,0),(0,1),(0,1));N=((1,0,0),(0,1,0))
def matvec(A,x):return tuple(sum(Q(a)*Q(b) for a,b in zip(row,x)) for row in A)
def mul(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
I2=((1,0),(0,1));I3=((1,0,0),(0,1,0),(0,0,1))
assert mul(N,M)==I2 and mul(M,N)!=I3
normal=(-1,1);expanded=(-1,1,1);b=(0,1);bp=(0,1,2)
assert matvec(M,normal)==expanded and matvec(N,expanded)==normal
surplus=tuple(x-y for x,y in zip(bp,matvec(M,b)));assert surplus==(0,0,1)
# The row-module kernel of N is span(e3). That quotient forces MN=I,
# but surplus e3 maps to zero: proof surplus is erased, not preserved.
e3=(0,0,1);assert matvec(N,e3)==(0,0) and matvec(N,surplus)==(0,0)
# The relation among NORMALS is span(e3-e2), but N does not kill that
# direction and hence cannot be the drop-row map on this quotient.
normal_syzygy=(0,-1,1)
assert sum(a*b for a,b in zip(expanded,normal_syzygy))==0
assert matvec(N,normal_syzygy)==(0,-1)
# Even if one projects along e3-e2, the bound surplus e3 survives; no
# simultaneous strictification of row-normal identity and bound identity.
# A vector belongs to span(e3-e2) iff first=0 and second=-third.
assert surplus[1]!=-surplus[2]
# Two equal feasible intervals with different surplus on the third row:
# projection of the quotient row data alone does not retain exact proof.
report={'passed':True,'row_retraction_NM_identity':True,'reverse_MN_nonidentity':True,'drop_kernel':'span(e3), kills strictly positive surplus (0,0,1)','normal_syzygy':'span(e3-e2), not killed by drop N and does not contain surplus','positive_surplus_lost_under_strictification':True,'scope':'One explicit rational redundant-row Farkas diagram, not impossibility for all enriched complexes or analytic realization.'}
out=Path(__file__).resolve().parents[1]/'results/farkas-syzygy-surplus.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
