"""Measure and emit the CSE graph for flat predictor-face derivatives."""

import sympy as sp
import math
import time
from decimal import Decimal

import theta_inner_interval_certificate as interval
from hyperbolic_compact_middle_centered_certificate import sqrt_i


u,c,e=sp.symbols("u c e")
u0=sp.Rational("0.3566749439387324");u1=sp.Rational("0.9162907318741551")
x=(u-u0)/(u1-u0)
powers=((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(4,0),(4,1),(5,0))
coefficient_strings=(
    "1.164635150766844","0.3517780852211224","0.19755133767897876",
    "0.05033228385167804","0.01978898922398497","0.0193960952110962",
    "0.18498950268144243","-0.01334593293346967","-0.30309010031946954",
    "-0.19722469717057795","-0.07603945507205546","-0.33910216233395035",
    "-0.3560549871042063","0.3937702930671297","0.2217643158516427",
    "0.2772342364691563","0.22307100450986603","-0.28127191534612644",
    "-0.16252394253717495","0.0037800581039069037","0.040614553959312585",
)
predictor=sum(sp.Rational(value)*x**i*c**j for value,(i,j) in zip(coefficient_strings,powers))
m=predictor+e
p=sp.exp(-u);q=c*p;holding=m+2*u
et=sp.exp(holding)*sp.sqrt((1+p)*(1-q)/((1-p)*(1+q)))
t=(et-1)/(et+1)
er=sp.sqrt((1-q**2)/(1-p**2))*sp.exp(p*holding)
r=(er-1)/(er+1)
s=p+q;product=p*q
nt=4*t**3+2*t*product-2*t*(2+product)*r**2-s*r*(1-r**2)
nr=-t*s+2*(1-2*t**2-t**2*product)*r+3*t*s*r**2
g=(1-t**2)*nt+p*(1-r**2)*nr

face=[g,sp.diff(g,u),sp.diff(g,c),sp.diff(g,u,2),sp.diff(g,u,c),sp.diff(g,c,2),
      sp.diff(g,e),sp.diff(g,u,e),sp.diff(g,c,e),sp.diff(g,e,2)]
replacements,reduced=sp.cse(face,order="canonical",optimizations="basic")
print(f"face_outputs={len(face)}")
print(f"face_cse_temporaries={len(replacements)}")
print(f"face_total_operations_before={sum(sp.count_ops(item) for item in face)}")
print(f"face_total_operations_after={sum(sp.count_ops(value) for _,value in replacements)+sum(sp.count_ops(item) for item in reduced)}")
print(f"face_largest_temporary_operations={max(sp.count_ops(value) for _,value in replacements)}")


class F:
    """Scalar-friendly outward interval used by generated lambdify code."""
    def __init__(self,value):self.v=value if isinstance(value,interval.I) else self.coerce(value).v
    @staticmethod
    def coerce(value):
        if isinstance(value,F):return value
        if isinstance(value,interval.I):return F(value)
        if isinstance(value,float):
            lo=Decimal.from_float(math.nextafter(value,-math.inf));hi=Decimal.from_float(math.nextafter(value,math.inf));return F(interval.I(lo,hi))
        return F(interval.I.point(value))
    def __add__(self,other):return F(self.v+F.coerce(other).v)
    __radd__=__add__
    def __neg__(self):return F(-self.v)
    def __sub__(self,other):return self+(-F.coerce(other))
    def __rsub__(self,other):return F.coerce(other)+(-self)
    def __mul__(self,other):return F(self.v*F.coerce(other).v)
    __rmul__=__mul__
    def __truediv__(self,other):return F(self.v/F.coerce(other).v)
    def __rtruediv__(self,other):return F.coerce(other)/self
    def __pow__(self,n):
        if n>=0:return F(self.v.power(n))
        return F(self.v.power(-n).reciprocal())
    def exp(self):return F(self.v.exp())
    def sqrt(self):return F(sqrt_i(self.v))


started=time.perf_counter()
flat=sp.lambdify((u,c,e),face,modules=[{"exp":lambda value:value.exp(),"sqrt":lambda value:value.sqrt()}],cse=True,docstring_limit=0)
print(f"face_lambdify_seconds={time.perf_counter()-started:.6f}")
arguments=(F(interval.I(Decimal("2.2"),Decimal("2.21"))),F(interval.I(Decimal("0.4"),Decimal("0.41"))),F(interval.I.point("-0.02")))
started=time.perf_counter()
for _ in range(100):sample=flat(*arguments)
print(f"face_100_interval_evaluations_seconds={time.perf_counter()-started:.6f}")
print("face_sample_G=",sample[0].v)

# Curvature tube graph: value, three first derivatives, six Hessian entries.
vt=1-t**2;vr=p*(1-r**2)
ntt=12*t**2+2*product-2*(2+product)*r**2
ntr=-4*t*(2+product)*r-s*(1-3*r**2)
nrr=2*(1-2*t**2-t**2*product)+6*t*s*r
dg=-2*t*vt*nt-2*p*r*vr*nr+vt**2*ntt+2*vt*vr*ntr+vr**2*nrr
curvature=-dg
tube=[curvature,sp.diff(curvature,u),sp.diff(curvature,c),sp.diff(curvature,e),
      sp.diff(curvature,u,2),sp.diff(curvature,u,c),sp.diff(curvature,u,e),
      sp.diff(curvature,c,2),sp.diff(curvature,c,e),sp.diff(curvature,e,2)]
started=time.perf_counter();tube_replacements,tube_reduced=sp.cse(tube,order="canonical",optimizations="basic")
print(f"tube_outputs={len(tube)}")
print(f"tube_cse_temporaries={len(tube_replacements)}")
print(f"tube_total_operations_before={sum(sp.count_ops(item) for item in tube)}")
print(f"tube_total_operations_after={sum(sp.count_ops(value) for _,value in tube_replacements)+sum(sp.count_ops(item) for item in tube_reduced)}")
print(f"tube_cse_seconds={time.perf_counter()-started:.6f}")
started=time.perf_counter();flat_tube=sp.lambdify((u,c,e),tube,modules=[{"exp":lambda value:value.exp(),"sqrt":lambda value:value.sqrt()}],cse=True,docstring_limit=0)
print(f"tube_lambdify_seconds={time.perf_counter()-started:.6f}")
started=time.perf_counter()
for _ in range(20):tube_sample=flat_tube(*arguments)
print(f"tube_20_interval_evaluations_seconds={time.perf_counter()-started:.6f}")
print("tube_sample_curvature=",tube_sample[0].v)
