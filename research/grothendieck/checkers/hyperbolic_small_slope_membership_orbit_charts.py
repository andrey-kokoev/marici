"""Exact Bernstein tube-membership certificates on the two faithful R caps."""

from math import comb
import sympy as sp


p,c,r,e=sp.symbols("p c r e")
y=r/p;d=(1+c+2*y+e)/8;t=1-p**2*d;q=c*p
slope_sum,product=p+q,p*q
nt=4*t**3+2*t*product-2*t*(2+product)*r**2-slope_sum*r*(1-r**2)
nr=-t*slope_sum+2*(1-2*t**2-t**2*product)*r+3*t*slope_sum*r**2
g=sp.expand((1-t**2)*nt+p*(1-r**2)*nr)
u,s,h=sp.symbols("u s h",nonnegative=True)

charts={
    "low_square_root":{
        p:sp.Rational(9,100)*u**2,
        r:sp.Rational(18,100)*u**2+
          (sp.Rational(3,10)*u-sp.Rational(18,100)*u**2)*s,
    },
    "high_constant":{
        p:sp.Rational(9,100)+sp.Rational(1,100)*u,
        r:2*(sp.Rational(9,100)+sp.Rational(1,100)*u)+
          (sp.Rational(3,10)-2*(sp.Rational(9,100)+sp.Rational(1,100)*u))*s,
    },
}
targets={
    "upper_face":g.subs(e,0)/p**2,
    "lower_face":-g.subs(e,-sp.Rational(2,5))/p**2,
    "e_derivative":sp.diff(g,e).subs(e,-sp.Rational(2,5)*h)/p**2,
}


def audit(expression,mapping,variables):
    mapped=sp.cancel(expression.subs(mapping));num,den=sp.fraction(mapped)
    poly=sp.Poly(sp.expand(num),*variables)
    degrees=tuple(poly.degree(variable) for variable in variables)
    power={monomial:coefficient for monomial,coefficient in poly.terms()}
    indices=[()]
    for degree in degrees:
        indices=[prefix+(i,) for prefix in indices for i in range(degree+1)]
    values=[]
    for index in indices:
        total=sp.Rational(0)
        for monomial,value in power.items():
            if all(monomial[a]<=index[a] for a in range(len(variables))):
                weight=sp.Rational(1)
                for axis in range(len(variables)):
                    weight*=sp.Rational(comb(index[axis],monomial[axis]),
                                        comb(degrees[axis],monomial[axis]))
                total+=value*weight
        values.append(sp.factor(total))
    return {
        "denominator":sp.factor(den),"degrees":degrees,"count":len(values),
        "negative":sum(1 for value in values if value<0),
        "zero":sum(1 for value in values if value==0),
        "minimum":min(values),
    }


all_pass=True
for chart,mapping in charts.items():
    for target,expression in targets.items():
        variables=(u,s,c,h) if h in expression.free_symbols else (u,s,c)
        result=audit(expression,mapping,variables)
        passed=result["negative"]==0
        all_pass=all_pass and passed
        print(f"{chart}_{target}={result}")
        print(f"{chart}_{target}_nonnegative_certified={passed}")
print(f"faithful_orbit_tube_membership_certified={all_pass}")
