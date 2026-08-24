"""Exact q-variation of G along the source Bregman graph at fixed X,p."""

import sympy as sp
import math
import random

from hyperbolic_boundary_critical_curvature_sweep import directional_curvature, state
from hyperbolic_boundary_unimodality_sweep import boundary_derivative

p, q, t, r = sp.symbols("p q T R")
s, product = p+q, p*q
nt = 4*t**3+2*t*product-2*t*(2+product)*r**2-s*r*(1-r**2)
nr = -t*s+2*(1-2*t**2-t**2*product)*r+3*t*s*r**2
g = sp.expand((1-t**2)*nt+p*(1-r**2)*nr)

# X=artanh(T) is fixed.  R=tanh(pX-Delta(p,q)), and
# Delta_q=-(p-q)/(2(1-q^2)).
rq = (1-r**2)*(p-q)/(2*(1-q**2))
source_q = sp.factor(sp.diff(g,q)+rq*sp.diff(g,r))
numerator = sp.factor(source_q*2*(1-q**2))

print("source_q_numerator_factor=", numerator)
print("degrees_p_q_T_R=", sp.Poly(numerator,p,q,t,r).degree_list())

# Reduce modulo G, viewed as an affine polynomial in q.
g0 = sp.expand(g.subs(q,0))
gq = sp.expand(sp.diff(g,q))
assert sp.expand(g-g0-q*gq) == 0
critical_numerator = sp.factor(
    sp.together(numerator.subs(q,-g0/gq))*gq**3
)
critical_numerator = sp.factor(critical_numerator)
print("critical_reduction_times_gq3=", critical_numerator)

source_q_function = sp.lambdify((p,q,t,r), source_q, "math")
rows = []
for pv in (0.1,0.2,0.3,0.5,0.7,0.9,0.99,0.999,0.9999):
    minimum, maximum = (math.inf,None), (-math.inf,None)
    curvature_normalized_minimum=(math.inf,None)
    source_normalized_minimum=(math.inf,None)
    for index in range(101):
        cv = index/100
        qv = cv*pv
        lo,hi = 0.0,1.0
        while boundary_derivative(pv,qv,hi)>0:
            hi*=2
        for _ in range(70):
            mid=(lo+hi)/2
            if boundary_derivative(pv,qv,mid)>0: lo=mid
            else: hi=mid
        holding=(lo+hi)/2
        tv,rv=state(pv,qv,holding)
        value=source_q_function(pv,qv,tv,rv)
        curvature=directional_curvature(tv,rv,pv,qv)
        curvature_normalized=-curvature/(1-pv)
        source_normalized=-value/(1-pv)
        if curvature_normalized<curvature_normalized_minimum[0]:
            curvature_normalized_minimum=(curvature_normalized,(cv,holding))
        if source_normalized<source_normalized_minimum[0]:
            source_normalized_minimum=(source_normalized,(cv,holding))
        if value<minimum[0]: minimum=(value,(cv,holding,tv,rv))
        if value>maximum[0]: maximum=(value,(cv,holding,tv,rv))
    rows.append((pv,minimum,maximum,curvature_normalized_minimum,source_normalized_minimum))
print("physical_critical_source_q_ranges=")
for row in rows:
    print(row)

rng=random.Random(20260823)
positive=0
largest=(-math.inf,None)
for _ in range(1_000_000):
    pv=rng.random()
    qv=pv*rng.random()
    a,b=math.atanh(pv),math.atanh(qv)
    defect=(pv*(a-b)-math.log(math.cosh(a))+math.log(math.cosh(b)))/2
    x=defect/pv+10**(-5+6*rng.random())
    tv,rv=math.tanh(x),math.tanh(pv*x-defect)
    value=source_q_function(pv,qv,tv,rv)
    if value>largest[0]: largest=(value,(pv,qv,x,tv,rv,defect))
    if value>1e-12: positive+=1
print("physical_carrier_source_q_sweep=",{
    "trials":1_000_000,"positive":positive,"largest":largest
})
