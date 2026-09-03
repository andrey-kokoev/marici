"""Exact uniform nonvanishing bound for Chart-1 logarithms on |y|<=1/4."""
from fractions import Fraction as F
from pathlib import Path
import json
qmax=F(7,16);R=F(1,4)
p_lower=F(2*3141592653589793238,10**18)
# A=p/q >= p_lower/qmax.  K(A)=6A/(A-3)^2 decreases for A>3.
Amin=p_lower/qmax
Kmax=6*Amin/(Amin-3)**2
# Both m(y) and m(4y) occur. For |y|<=R, z=q|4y|<=7/16.
# sum_{n>=1} z^n/(2n)! <= (z/2)/(1-z/12), since successive ratios <=z/12.
z=4*qmax*R
coshm1_bound=(z/2)/(1-z/12)
bound=Kmax*coshm1_bound
assert Amin>3 and z==F(7,16) and bound<1
result={"scope":"uniform for Chart-1 real q and the stated rational 2*pi bracket",
 "disk_radius":str(R),"A_min":str(Amin),
 "cosh_minus_one_bound":str(coshm1_bound),"log_argument_perturbation_bound":str(bound),
 "bound_float":float(bound),"strictly_below_one":bound<1}
out=json.dumps(result,indent=2)+"\n"
Path("research/grothendieck/results/theta-nq-complex-disk.json").write_text(out)
print(out,end="")
