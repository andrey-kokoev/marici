"""Exact metric-minimalization gate for the admitted finite C34 projection fixture."""
import json,sys
from pathlib import Path
try:
 import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s

I=s.eye(4);Z=s.zeros(4)
P0=s.diag(1,1,0,0)
QT=s.zeros(4)
for a,b in ((0,2),(1,3)):
 QT[a,a]=s.Rational(9,25);QT[a,b]=QT[b,a]=s.Rational(12,25);QT[b,b]=s.Rational(16,25)
Q0=P0; dQ=QT-Q0
F_T=QT.col_join(I-QT);F_0=Q0.col_join(I-Q0)
J2=s.diag(I,-I);Psi=(F_T.col_join(F_0))/s.sqrt(2);J4=s.diag(J2,-J2)
Theta=((Psi*P0).col_join(Psi))/s.sqrt(2);z=s.zeros(16);K8=z.row_join(J4).col_join(J4.row_join(z))
Eplus=(s.eye(32)+K8)/2;Eminus=(s.eye(32)-K8)/2
XT=Eplus*Theta;X0=Eminus*Theta
P=s.simplify(XT.T*XT);Q=s.simplify(X0.T*X0);D=s.simplify(P-Q);total=s.simplify(P+Q)
# Here each invariant two-dimensional block has eigenvalues 2/25 and -18/25.
absD=s.simplify(-s.Rational(4,5)*D+s.Rational(18,125)*s.eye(4))
K=s.simplify((total-absD)/2)
# Sylvester criterion in the natural order is exact for this positive definite fixture.
leading=[s.factor(K[:n,:n].det()) for n in range(1,5)]
comm=s.simplify(P*Q-Q*P)
checks={'projection_pair_exact':QT*QT==QT and Q0*Q0==Q0,'signed_difference_exact':D==Theta.T*K8*Theta,'absolute_value_square':absD*absD==D*D,'absolute_value_positive':all(v>=0 for v in absD.eigenvals()),'forced_remainder_identity':P-(D+absD)/2==K and Q-(-D+absD)/2==K,'forced_remainder_positive_definite':all(v>0 for v in leading),'polarized_grams_noncommuting':comm!=s.zeros(4),'minimalized_sum_equals_absolute_difference':s.simplify(P+Q-2*K)==absD}
out={'schema':'marici.voevodsky.relative-c34-metric-minimalization-gate.v1','source_dimension':4,'signed_eigenvalues':{str(k):int(v) for k,v in D.eigenvals().items()},'forced_remainder_leading_principal_minors':[str(x) for x in leading],'forced_remainder_rank':K.rank(),'checks':checks,'all_exact':all(checks.values()),'meaning':'The admitted noncommuting finite C34 fixture passes the metric common-remainder gate exactly; its balanced positive remainder can be removed to recover |D|.','claim_boundary':'One finite projection fixture. This does not establish positivity, successor compatibility, or Mosco convergence for the semilocal regulator family.'}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'relative-c34-metric-minimalization-gate.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
