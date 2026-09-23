"""Rigorous two-sheet trace enclosure at the rational minimum-eight target."""
import json
from pathlib import Path
from fractions import Fraction as Q
import check_nine_point_algebraic_target_pushforward as first
F=first;OUT=Path(__file__).resolve().parents[1]/'results'
# The other quadratic root is the conjugate of the certified positive root.
root=F.other;iv=F.iv
coefs=[F.affine(expr,root) for expr in F.solution]
C=[[iv(F.C[i][j])+sum(coefs[2*i+k]*F.K[k][j] for k in range(2)) for j in range(8)] for i in range(2)]
x,y=C[0][0],C[1][0];v,w=C[0][2],C[1][2]
delta=x*w-y*v;assert not delta.contains_zero()
D=[[(w*C[0][j]-v*C[1][j])/delta for j in range(8)],
   [(-y*C[0][j]+x*C[1][j])/delta for j in range(8)]]
weights=[D[0][1],D[1][3],-D[0][4],-D[0][5],-D[0][6],-D[0][7]]
assert all(not weight.contains_zero() for weight in weights)
t=D[1][4]/weights[2];u=D[1][6]/weights[4]
assert not u.contains_zero() and not (t-u).contains_zero()
# The exact four paired-minor identities modulo the graph quadratic
# guarantee this rational chart also parametrizes the NONPOSITIVE root.
for j in (5,7):
 prototype=weights[3]*t if j==5 else weights[5]*u
 assert (D[1][j]-prototype).contains_zero()
chart=[[iv(1),weights[0],iv(0),iv(0),-weights[2],-weights[3],-weights[4],-weights[5]],
       [iv(0),iv(0),iv(1),weights[1],weights[2]*t,weights[3]*t,weights[4]*u,weights[5]*u]]
Y=F.projected(chart);A=[[Y[0][0],Y[0][1]],[Y[1][0],Y[1][1]]]
detA=A[0][0]*A[1][1]-A[0][1]*A[1][0];assert not detA.contains_zero()
R=[[A[1][1]/detA,-A[0][1]/detA],[-A[1][0]/detA,A[0][0]/detA]]
B=F.leftmul(R,[row[2:] for row in Y]);columns=[]
for k in range(8):
 deriv=[[iv(0) for _ in range(8)] for _ in range(2)]
 if k==0:deriv[0][1]=iv(1)
 elif k==1:deriv[1][3]=iv(1)
 elif k in (2,3,4,5):
  j=k+2;deriv[0][j]=iv(-1);deriv[1][j]=t if k<=3 else u
 elif k==6:deriv[1][4]=weights[2];deriv[1][5]=weights[3]
 else:deriv[1][6]=weights[4];deriv[1][7]=weights[5]
 dY=F.projected(deriv)
 dB=F.leftmul(R,[[dY[i][j+2]-sum(dY[i][h]*B[h][j] for h in range(2)) for j in range(4)] for i in range(2)])
 columns.append([dB[i][j] for i in range(2) for j in range(4)])
jac=F.determinant([[columns[k][i] for k in range(8)] for i in range(8)]);assert not jac.contains_zero()
product=iv(1)
for weight in weights:product=product*weight
source=-iv(1)/(product*u*(t-u));second=source/jac
trace=F.pushed+second
assert not second.contains_zero() and not trace.contains_zero()
# Both sheets have the same rational observed target (the source fibre is
# C0+T*K). The trace is the sum with Jacobian orientation, not the positive
# branch alone; coefficient remains represented by an exact algebraic trace.
result={'schema':'marici.nima.nine-point-fixed-target-two-sheet-trace.v1','passed':True,
 'original_target':'research/nima/results/nine-point-support-stress.json:first_no_seven_support_target',
 'root_polynomial':str(F.P.as_expr()),'positive_root_interval':[str(F.left),str(F.right)],
 'conjugate_root_interval':[str(root.lo),str(root.hi)],
 'positive_sheet_coefficient_enclosure':F.outward(F.pushed),
 'nonpositive_sheet_coefficient_enclosure':F.outward(second),
 'full_algebraic_trace_coefficient_enclosure':F.outward(trace),
 'nonpositive_sheet_jacobian_enclosure':F.outward(jac),
 'nonpositive_sheet_source_coefficient_enclosure':F.outward(source),
 'trace_differs_from_positive_local_sheet':not second.contains_zero(),
 'scope':'Exact outward-rational interval for the BOTH-sheet canonical source-form pushforward at ONE fixed rational nine-point target. Does not produce the global rational target form, full sourced psi superfunction comparison, or nine-point history assignment.'}
(OUT/'nine-point-fixed-target-two-sheet-trace.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'positive':result['positive_sheet_coefficient_enclosure'],
 'conjugate':result['nonpositive_sheet_coefficient_enclosure'],
 'trace':result['full_algebraic_trace_coefficient_enclosure']},indent=2))
