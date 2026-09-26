"""Exact rational-power identities for polarized Rosen vacuum waves.
No floating point, generic Einstein characteristic solver, or averaging.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

# Finite sums c*u^q for u>0, rational exponents q.
def term(q,a=1):return {F(q):F(a)} if a else {}
def add(*ps):
    out={}
    for p in ps:
        for q,a in p.items():out[q]=out.get(q,F(0))+a
    return {q:a for q,a in out.items() if a}
def scale(a,p):return {q:a*b for q,b in p.items() if a*b}
def mul(p,r):
    out={}
    for q,a in p.items():
        for s,b in r.items():out[q+s]=out.get(q+s,F(0))+a*b
    return {q:a for q,a in out.items() if a}
def derivative(p):return {q-1:q*a for q,a in p.items() if q*a}
def value1(p):return sum(p.values(),F(0))
d2=lambda p:derivative(derivative(p))
k=F(3,10)
r_a=term(F(9,10));r_b=term(F(1,10))
checks={}
for label,r in [('high',r_a),('low',r_b),('mixed',scale(F(1,2),add(r_a,r_b)))]:
    p=mul(r,term(k));q=mul(r,term(-k))
    checks[label+'_focusing_equation']=not add(d2(r),scale(k*k,mul(term(-2),r)))
    # Trace(A)=p''/p+q''/q, numerator suffices since p,q>0.
    checks[label+'_vacuum_trace_numerator']=not add(mul(d2(p),q),mul(d2(q),p))
    checks[label+'_same_conformal_shear']=p==mul(q,term(2*k))
    checks[label+'_corner_area_normalization']=value1(r)==1
    # Coordinate transformation cross terms and du^2 terms cancel identically.
    checks[label+'_rosen_brinkmann_coordinate_identity']=not add(
        scale(-1,derivative(mul(p,derivative(p)))),
        mul(derivative(p),derivative(p)),mul(p,d2(p)))

# Two independent modes: the Wronskian is constant -4/5.
w=add(mul(r_a,derivative(r_b)),scale(-1,mul(derivative(r_a),r_b)))
checks['nonzero_constant_wronskian']=w==term(0,F(-4,5))
# Corner expansion fixes their coefficients: r(1)=R, r'(1)=V.
R,V=F(1),F(1,2)
a=(V-F(1,10)*R)/F(4,5);b=R-a
r=add(scale(a,r_a),scale(b,r_b))
checks['corner_data_select_coefficients']=a==b==F(1,2) and value1(r)==R and value1(derivative(r))==V
# Identical shear and area, different corner expansions -> different tides.
def axial_curvature_at_corner(r):
    p=mul(r,term(k));return value1(d2(p))/value1(p)
Ah= axial_curvature_at_corner(r_a);Am=axial_curvature_at_corner(r)
checks['expansion_is_necessary_data']=Ah==F(6,25) and Am==0
# The mixed example crosses zero curvature with nonzero first derivative.
p=mul(r,term(k))
Aprime=(value1(derivative(d2(p)))*value1(p)-value1(d2(p))*value1(derivative(p)))/value1(p)**2
checks['actual_flat_to_generic_stratum_crossing']=Am==0 and Aprime==F(12,125)
# No shear: r affine, p=q=r, giving A=0 wherever r is nonzero.
rflat=add(term(0,F(1,10)),term(1,F(9,10)))
checks['zero_shear_affine_area_is_flat']=not d2(rflat)
# Dropping focusing while keeping beta generates nonvacuum stress.
wrong=term(0)
pw=mul(wrong,term(k));qw=mul(wrong,term(-k))
checks['unconstrained_area_rejected']=bool(add(mul(d2(pw),qw),mul(d2(qw),pw)))
packet=dict(passed=all(checks.values()),checks=checks,
    beta='(3/10) log u',domain='u>0; positive linear combinations r of u^(9/10), u^(1/10)',
    high_profile_A11_at_corner=str(Ah),mixed_profile_A11_at_corner=str(Am),
    mixed_profile_A11_derivative_at_corner=str(Aprime),
    scope='Exact rational-power vacuum and corner identities. General ODE uniqueness is invoked in the written argument; no theorem about all Einstein characteristic data.',
    checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path(__file__).with_name('characteristic-shear-selection.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
