"""Exact Cauchy majorants for degree>=14 tails of scaled Chart-1 H and J."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
q0,q1=F(3,10),F(7,16);p0=F(2*3141592653589793238,10**18);p1=F(2*3141592653589793239,10**18)
R0=F(1,8);r=F(1,64);rho=r/R0;Amin=p0/q1;Amax=p1/q0
Kmax=6*Amin/(Amin-3)**2
Kqmax=6*(Amax+3)/(Amin-3)**3*(Amax/q0)
def hm(scale):
 t=scale*R0;H=(t/2)/(1-t/12);B=Kmax*H
 M=Amax*H+B/(1-B)
 Mq=(Amax/q0)*H+Kqmax*H/(1-B)
 assert B<1
 return M,Mq,B
def exp_up(x,N=100):
 terms=[x**n/F(factorial(n)) for n in range(N+2)]
 return sum(terms[:N+1],F(0))+terms[N+1]/(1-x/F(N+2))
m,mq,b=hm(1);m4,mq4,b4=hm(4);eta=m4+4*m;etaq=mq4+4*mq
E2=exp_up(2*m);E4=exp_up(4*m);Ee=exp_up(eta);U=1+E2;C=1+Ee
MR=U**2+E4*C
# R=u^2-e^-4m*c; bound both q derivatives directly.
uq=2*E2*mq;cq=Ee*etaq
MRq=2*U*uq+E4*(4*mq*C+cq)
# H/z^3: n>=14 corresponds k=n-3>=11, coefficient multiplier k+1.
kH=11;SH=rho**kH*((kH+1)-kH*rho)/(1-rho)**2
Htail=MR/R0**3*SH
# J/z^2: k=n-2>=12, multiplier q*r_n' +(k+2)r_n.
kJ=12
SJ0=rho**kJ/(1-rho);SJn=rho**kJ*((kJ+2)-(kJ+1)*rho)/(1-rho)**2
Jtail=(q1*MRq*SJ0+MR*SJn)/R0**2
result={"scope":"uniform Chart-1 exact Cauchy majorants on complex |z|<=1/8",
 "b_z_float":float(b),"b_4z_float":float(b4),"R_magnitude_float":float(MR),"Rq_magnitude_float":float(MRq),
 "H_scaled_tail_float":float(Htail),"J_scaled_tail_float":float(Jtail),
 "H_tail_below_margin":Htail<F(14),"J_tail_below_margin":Jtail<F(7,10)}
assert result["H_tail_below_margin"] and result["J_tail_below_margin"]
out=json.dumps(result,indent=2)+"\n";Path("research/grothendieck/results/theta-chart1-scaled-tail.json").write_text(out);print(out,end="")
