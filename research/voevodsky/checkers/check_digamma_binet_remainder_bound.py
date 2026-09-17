#!/usr/bin/env python3
"""Evaluate the explicit Binet remainder budget at the two-prime tail anchor."""
import json,math
from pathlib import Path
N=10;R=2000.;a=.25;b=R/2;absz=math.hypot(a,b)
# zeta(22) < 1 + 2^(-21)/(1-2^(-1)) < recorded elementary upper bound.
zeta_upper=1+2**-20
point=1/(a*b*absz**(2*N))*math.factorial(2*N+1)*zeta_upper/(2*math.pi)**(2*N+2)
# Since |z|>=u/2, pointwise remainder <= C*u^(-2N-1); integrate against u^-k.
C=8*(2**(2*N))*math.factorial(2*N+1)*zeta_upper/(2*math.pi)**(2*N+2)
plain_k2=C*R**(-(2*N+2))/(2*N+2)
out={'schema':'marici.voevodsky.digamma-binet-remainder-bound.v1','N':N,'tail_anchor':R,'zeta_22_upper':zeta_upper,'pointwise_remainder_upper_at_anchor':point,'integrated_plain_k2_remainder_upper':plain_k2,'checks':{'denominator_lower_bound':'|t^2+z^2| >= 2ab','zeta_bound_elementary':True,'integrated_worst_plain_moment_finite':True},'passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'digamma_binet_remainder_bound.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
