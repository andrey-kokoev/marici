"""Exact conservative Cauchy tail bound for the partial_y Nq series."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
q0,q1=F(3,10),F(7,16);R=F(1,4);r=F(1,28);rho=r/R
p0=F(2*3141592653589793238,10**18);p1=F(2*3141592653589793239,10**18)
Amin=p0/q1;Amax=p1/q0
K=6*Amin/(Amin-3)**2
# Positive-series majorants for h=cosh(sqrt(q*s*y))-1 and h_q.
def hm(s):
 z=q1*s*R
 H=(z/2)/(1-z/12)
 Hq=s*R*F(1,2)/(1-z/12)**2
 B=K*H
 # |K_q|, using |dK/dA| and deliberately independent endpoint extrema.
 Kq=6*(Amax+3)/(Amin-3)**3*(Amax/q0)
 Bq=Kq*H+K*Hq
 M=Amax*H+B/(1-B)
 Mq=(Amax/q0)*H+Amax*Hq+Bq/(1-B)
 assert B<1
 return M,Mq,B
m,mq,b=hm(1);m4,mq4,b4=hm(4);eta=m4+4*m;etaq=mq4+4*mq
# Exact exponential upper bound: Taylor plus geometric majorant for the tail.
def exp_up(x,N=80):
 terms=[x**n/F(factorial(n)) for n in range(N+2)]
 tail=terms[N+1]/(1-x/F(N+2))
 return sum(terms[:N+1],F(0))+tail
E2=exp_up(2*m);E4=exp_up(4*m);Ee=exp_up(eta)
# Nq=4(1-e^-2m)e^-2m mq + e^-4m(4mq(1-e^-eta)-e^-eta etaq)
MN=4*(1+E2)*E2*mq + E4*(4*mq*(1+Ee)+Ee*etaq)
n0=20
geom=rho**(n0-1)*(n0-(n0-1)*rho)/(1-rho)**2
tail=MN/R*geom
result={"scope":"uniform magnitude majorant; exact rational arithmetic",
 "circle_radius":str(R),"physical_radius":str(r),"finite_partial_y_polynomial_degree":n0-2,
 "coefficient_tail_starts_at_Nq_degree":n0,
 "b_m_bound":str(b),"b_m4_bound":str(b4),"Nq_circle_magnitude_bound_float":float(MN),
 "partial_y_tail_numerator_hex":hex(tail.numerator),
 "partial_y_tail_denominator_hex":hex(tail.denominator),
 "partial_y_tail_bound_float":float(tail),
 "below_recorded_endpoint_truncation_margin":tail<F(387,1000)}
assert tail<F(387,1000)
out=json.dumps(result,indent=2)+"\n";Path("research/grothendieck/results/theta-nq-cauchy-magnitude.json").write_text(out);print(out,end="")
