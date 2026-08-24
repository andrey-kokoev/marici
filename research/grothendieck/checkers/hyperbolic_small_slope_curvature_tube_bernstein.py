"""Exact Bernstein certificate for DG<0 on the capped faithful tail tube."""

from math import comb
import sympy as sp


p,c,r,e = sp.symbols("p c r e")
y = r/p
d = (1+c+2*y+e)/8
t = 1-p**2*d
q = c*p
slope_sum,product=p+q,p*q
nt=4*t**3+2*t*product-2*t*(2+product)*r**2-slope_sum*r*(1-r**2)
nr=-t*slope_sum+2*(1-2*t**2-t**2*product)*r+3*t*slope_sum*r**2
ntt=12*t**2+2*product-2*(2+product)*r**2
ntr=-4*t*(2+product)*r-slope_sum*(1-3*r**2)
nrr=2*(1-2*t**2-t**2*product)+6*t*slope_sum*r
vt,vr=1-t**2,p*(1-r**2)
dg=sp.expand(-2*t*vt*nt-2*p*r*vr*nr+vt**2*ntt+2*vt*vr*ntr+vr**2*nrr)

u,s,h=sp.symbols("u s h",nonnegative=True)
mapped=sp.cancel((-dg/p**2).subs({
    p:u/10,
    r:2*(u/10)+(sp.Rational(3,10)-2*(u/10))*s,
    e:-sp.Rational(2,5)*h,
}))
numerator,denominator=sp.fraction(mapped)
cube=sp.Poly(sp.expand(numerator),u,s,c,h)
variables=(u,s,c,h)
degrees=tuple(cube.degree(variable) for variable in variables)
power={monomial:coefficient for monomial,coefficient in cube.terms()}


def bernstein(index):
    total=sp.Rational(0)
    for monomial,coefficient in power.items():
        if all(monomial[axis]<=index[axis] for axis in range(4)):
            weight=sp.Rational(1)
            for axis in range(4):
                weight*=sp.Rational(comb(index[axis],monomial[axis]),
                                    comb(degrees[axis],monomial[axis]))
            total+=coefficient*weight
    return sp.factor(total)


coefficients={
    (i,j,k,m):bernstein((i,j,k,m))
    for i in range(degrees[0]+1)
    for j in range(degrees[1]+1)
    for k in range(degrees[2]+1)
    for m in range(degrees[3]+1)
}
negative={index:value for index,value in coefficients.items() if value<0}
zero={index:value for index,value in coefficients.items() if value==0}
positive={index:value for index,value in coefficients.items() if value>0}

print(f"mapped_denominator_factor={sp.factor(denominator)}")
print(f"cube_degrees={degrees}")
print(f"bernstein_coefficient_count={len(coefficients)}")
print(f"bernstein_negative_count={len(negative)}")
print(f"bernstein_zero_count={len(zero)}")
print(f"bernstein_zero_indices={tuple(zero)}")
print(f"bernstein_minimum_positive={min(positive.values()) if positive else None}")
corner_witnesses={
    (j,k,m):coefficients[(degrees[0],j,k,m)]
    for j in (0,degrees[1])
    for k in (0,degrees[2])
    for m in (0,degrees[3])
}
strict_corners=all(value>0 for value in corner_witnesses.values())
print(f"u_positive_face_corner_witnesses={corner_witnesses}")
print(f"u_positive_face_all_corners_strict={strict_corners}")
print(f"capped_tail_curvature_certified={not negative and strict_corners}")
