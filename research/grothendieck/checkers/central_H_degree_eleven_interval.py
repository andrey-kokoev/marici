"""Directed centered H coefficients through degree eleven."""
import json
from decimal import Decimal
from fractions import Fraction
from math import factorial
from pathlib import Path

import central_interval_jet_first_cell_probe as P

I=P.I; D=Decimal; P.O=81; P.DEPTH=300
q=[I.box(0),I.box(1)]+[I.box(0)]*(P.O-1)
s=P.add(P.c(Fraction(1,2)),q)
eta,eta_s=P.eta_pair(s)
for n in range(P.O+1):
    eta_tail=D(4)*D(10)**n/(D(300)+D('0.4'))*D(2)**(-300)
    eta_s_tail=D(4)*D(n+1)*D(10)**(n+1)/(D(300)+D('0.4'))*D(2)**(-300)
    eta[n]=I.add(eta[n],(eta_tail.copy_negate(),eta_tail))
    eta_s[n]=I.add(eta_s[n],(eta_s_tail.copy_negate(),eta_s_tail))

r=P.expj(P.mul(P.sub(P.c(1),s),P.cb(I.log2)))
zlog=P.sub(P.div(eta_s,eta),P.div(P.mul(r,P.cb(I.log2)),P.sub(P.c(1),r)))
endpoint=P.add(P.inv(s),P.inv(P.sub(s,P.c(1))))
gamma=P.digamma(P.scale(s,Fraction(1,2)))
b18=I.qbox(Fraction(43867,798)); base=I.div(b18,I.scale(I.powi(I.box(1000),18),18))[1]
for n in range(P.O+1):
    error=I.up.divide(I.up.multiply(base,D(2)**18),D(1000)**n)
    gamma[n]=I.add(gamma[n],(error.copy_negate(),error))

xi_log=P.add(endpoint,P.cb(I.neg(I.scale(I.logpi,Fraction(1,2)))),P.scale(gamma,Fraction(1,2)),zlog)
even=[xi_log[n] for n in range(0,P.O+1,2)]
ell_prime=[I.scale(xi_log[2*n+1],Fraction(1,2)) for n in range(40)]

P.O=39
t=[I.box(0),I.box(1)]+[I.box(0)]*38
f_deep=P.mul(P.sub(P.scale(t,4),P.c(1)),ell_prime)
f=f_deep[:30]
P.O=29
g=[I.scale(f[n+1],n+1) for n in range(29)]+[I.box(0)]
h=P.powj(g,Fraction(-1,2))

assert all(a<=0<=b for a,b in even)
result={
    'centered_q_order':81,
    'F_coefficients_through_degree_twenty_three':[[str(a),str(b)] for a,b in f[:24]],
    'F_coefficients_through_degree_twenty_nine':[[str(a),str(b)] for a,b in f],
    'F_coefficients_through_degree_thirty_nine':[[str(a),str(b)] for a,b in f_deep],
    'H_coefficients_through_degree_eleven':[[str(a),str(b)] for a,b in h[:12]],
    'all_reflection_forced_even_coefficients_contain_zero':True,
    'analytic_eta_and_gamma_tail_bounds_included':True,
    'directed_decimal_rounding':True,
    'interval_certified':True,
    'zero_locations_used':False,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-H-degree-eleven-interval.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f"H_coefficient_count={len(h[:12])}")
    print(f"H_degree_eleven_interval={h[11]}")
    print('interval_certified=True')
    print('rh_proved=False')
