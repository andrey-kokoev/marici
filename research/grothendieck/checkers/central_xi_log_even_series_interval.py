"""Directed interval coefficients for the centered reflection-even Xi series."""
import json
from decimal import Decimal
from fractions import Fraction
from math import factorial
from pathlib import Path

import central_interval_jet_first_cell_probe as P

I=P.I;D=Decimal;P.O=13;P.DEPTH=300
q=[I.box(0),I.box(1)]+[I.box(0)]*(P.O-1);s=P.add(P.c(Fraction(1,2)),q)
eta,eta_s=P.eta_pair(s)

# Inject Cauchy Euler-tail bounds into Taylor coefficients.
for n in range(P.O+1):
    eta_tail=D(4)*D(factorial(n))*D(10)**n/(D(300)+D('0.4'))*D(2)**(-300)/D(factorial(n))
    eta_s_tail=D(4)*D(factorial(n+1))*D(10)**(n+1)/(D(300)+D('0.4'))*D(2)**(-300)/D(factorial(n))
    eta[n]=I.add(eta[n],(eta_tail.copy_negate(),eta_tail))
    eta_s[n]=I.add(eta_s[n],(eta_s_tail.copy_negate(),eta_s_tail))

r=P.expj(P.mul(P.sub(P.c(1),s),P.cb(I.log2)))
zlog=P.sub(P.div(eta_s,eta),P.div(P.mul(r,P.cb(I.log2)),P.sub(P.c(1),r)))
endpoint=P.add(P.inv(s),P.inv(P.sub(s,P.c(1))))
gamma=P.digamma(P.scale(s,Fraction(1,2)))
b18=I.qbox(Fraction(43867,798));base=I.div(b18,I.scale(I.powi(I.box(1000),18),18))[1]
for n in range(P.O+1):
    error=I.up.divide(I.up.multiply(base,D(2)**18),D(1000)**n)
    gamma[n]=I.add(gamma[n],(error.copy_negate(),error))

xi_log=P.add(endpoint,P.cb(I.neg(I.scale(I.logpi,Fraction(1,2)))),P.scale(gamma,Fraction(1,2)),zlog)
even_intervals=[xi_log[n] for n in range(0,P.O+1,2)]
ell_prime=[I.scale(xi_log[2*n+1],Fraction(1,2)) for n in range(6)]

# Convert the certified ell' coefficients into H coefficients at t=0.
P.O=5
t=[I.box(0),I.box(1)]+[I.box(0)]*4
f=P.mul(P.sub(P.scale(t,4),P.c(1)),ell_prime)
g=[I.scale(f[n+1],n+1) for n in range(5)]+[I.box(0)]
h=P.powj(g,Fraction(-1,2));h2=I.scale(h[2],2);h3=I.scale(h[3],6)

assert h2[1]<0 and h3[0]>0
result={"centered_q_order":13,"eta_euler_depth":300,"digamma_recurrence_target":1000,
        "even_Xi_log_derivative_coefficient_intervals":[[str(a),str(b)] for a,b in even_intervals],
        "all_even_intervals_contain_zero":all(a<=0<=b for a,b in even_intervals),
        "ell_prime_coefficient_intervals_through_degree_five":[[str(a),str(b)] for a,b in ell_prime],
        "H_double_prime_at_zero_interval":[str(x) for x in h2],
        "H_triple_prime_at_zero_interval":[str(x) for x in h3],
        "strict_boundary_concavity":h2[1]<0,"strict_positive_H_triple_prime":h3[0]>0,
        "analytic_tail_bounds_included":True,"directed_decimal_rounding":True,
        "interval_certified":True,"zero_locations_used":False,"rh_proved":False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-xi-log-even-series-interval.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
