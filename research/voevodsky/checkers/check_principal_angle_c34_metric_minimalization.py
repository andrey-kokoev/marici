"""Symbolic principal-angle theorem for the C34 metric minimalization gate."""
import json,sys
from pathlib import Path
try:
 import sympy as sp
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as sp

s,c=sp.symbols('s c', real=True, nonnegative=True)
D=sp.Matrix([[-s**2,c*s/2],[c*s/2,0]])
T=sp.diag(1,sp.Rational(1,2))
absD=-s*D+s*c**2*sp.eye(2)/2
K=sp.simplify((T-absD)/2)
# Reduce with c^2=1-s^2.
red=lambda x:sp.factor(x.subs(c**2,1-s**2))
k11=red(K[0,0]);k22=red(K[1,1]);det=red(K.det())
expected_det=(1-s)*(s**3-s+2)/16
# Spectral values of D on a principal-angle block.
lam_plus=s*(1-s)/2;lam_minus=-s*(1+s)/2
checks={'absolute_value_polynomial_identity':sp.simplify((absD*absD-D*D).subs(c**2,1-s**2))==sp.zeros(2),'k11_formula':sp.simplify(k11-(2-s-s**3)/4)==0,'k22_formula':sp.simplify(k22-(1-s+s**3)/4)==0,'determinant_factorization':sp.simplify(det-expected_det)==0,'signed_eigenvalue_sum':sp.simplify(lam_plus+lam_minus-D.trace())==0,'signed_eigenvalue_product':sp.simplify((lam_plus*lam_minus-D.det()).subs(c**2,1-s**2))==0,'endpoint_s0_positive':K.subs({s:0,c:1})==sp.diag(sp.Rational(1,2),sp.Rational(1,4)),'endpoint_s1_semidefinite':K.subs({s:1,c:0})==sp.diag(0,sp.Rational(1,4))}
# On [0,1], k11,k22 are nonnegative. The cubic has its minimum at 1/sqrt(3),
# where it equals 2-2/(3sqrt(3))>0; hence det >= 0.
out={'schema':'marici.voevodsky.principal-angle-c34-metric-minimalization.v1','principal_angle_parameters':'c>=0, s>=0, c^2+s^2=1','signed_eigenvalues':['s(1-s)/2','-s(1+s)/2'],'forced_remainder_entries':{'k11':'(2-s-s^3)/4','k12':'c*s^2/4','k22':'(1-s+s^3)/4'},'forced_remainder_determinant':'(1-s)(s^3-s+2)/16','positivity_domain':'0<=s<=1','strictness':'positive definite for 0<=s<1; positive semidefinite at s=1','checks':checks,'all_exact':all(checks.values()),'consequence':'Every Halmos principal-angle block of the admitted C34 projection-pair dilation passes the common-remainder metric gate; orthogonal direct sums preserve the result.','claim_boundary':'Applies to the canonical projection-pair eight-leg placement model. Identification with every external semilocal physical Gram remains a separate transport theorem.'}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'principal-angle-c34-metric-minimalization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
