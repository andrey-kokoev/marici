"""Exact Bernstein test trapping G=0 inside -0.3<e<0 on the radial cap."""

from math import comb
import sympy as sp


p,c,r,e=sp.symbols("p c r e")
y=r/p
d=(1+c+2*y+e)/8
t=1-p**2*d
q=c*p
slope_sum,product=p+q,p*q
nt=4*t**3+2*t*product-2*t*(2+product)*r**2-slope_sum*r*(1-r**2)
nr=-t*slope_sum+2*(1-2*t**2-t**2*product)*r+3*t*slope_sum*r**2
g=sp.expand((1-t**2)*nt+p*(1-r**2)*nr)

u,s,h=sp.symbols("u s h",nonnegative=True)
mapping={p:u/10,r:2*(u/10)+(sp.Rational(3,10)-2*(u/10))*s}


def cube_polynomial(expression,variables):
    mapped=sp.cancel(expression.subs(mapping))
    numerator,denominator=sp.fraction(mapped)
    return sp.Poly(sp.expand(numerator),*variables),sp.factor(denominator)


def bernstein_audit(poly,variables):
    degrees=tuple(poly.degree(variable) for variable in variables)
    power={monomial:coefficient for monomial,coefficient in poly.terms()}
    def coefficient(index):
        total=sp.Rational(0)
        for monomial,value in power.items():
            if all(monomial[axis]<=index[axis] for axis in range(len(variables))):
                weight=sp.Rational(1)
                for axis in range(len(variables)):
                    weight*=sp.Rational(comb(index[axis],monomial[axis]),
                                        comb(degrees[axis],monomial[axis]))
                total+=value*weight
        return sp.factor(total)
    indices=[()]
    for degree in degrees:
        indices=[prefix+(i,) for prefix in indices for i in range(degree+1)]
    values={index:coefficient(index) for index in indices}
    return {
        "degrees":degrees,
        "count":len(values),
        "negative":sum(1 for value in values.values() if value<0),
        "zero":sum(1 for value in values.values() if value==0),
        "positive":sum(1 for value in values.values() if value>0),
        "minimum":min(values.values()),
    }


targets={
    "G_e0_positive":g.subs(e,0)/p**2,
    "minus_G_e_minus_0.3_positive":-g.subs(e,-sp.Rational(3,10))/p**2,
    "G_e_derivative_positive":sp.diff(g,e).subs(e,-sp.Rational(3,10)*h)/p**2,
}
for name,expression in targets.items():
    variables=(u,s,c,h) if h in expression.free_symbols else (u,s,c)
    poly,denominator=cube_polynomial(expression,variables)
    audit=bernstein_audit(poly,variables)
    print(f"{name}_denominator={denominator}")
    print(f"{name}_audit={audit}")
    print(f"{name}_nonnegative_certified={audit['negative']==0}")

# Exact adaptive subdivision for the only unresolved face, -G(e=-0.3).
face_expression=sp.cancel(targets["minus_G_e_minus_0.3_positive"].subs(mapping))
face_num,face_den=sp.fraction(face_expression)
assert face_den==1
queue=[(((sp.Rational(0),sp.Rational(1)),)*3,0)]
accepted=[]
unresolved=[]
max_depth=9
while queue:
    box,depth=queue.pop()
    substitution={
        variable:lo+(hi-lo)*variable
        for variable,(lo,hi) in zip((u,s,c),box)
    }
    local=sp.Poly(sp.expand(face_num.subs(substitution)),u,s,c)
    audit=bernstein_audit(local,(u,s,c))
    if audit["negative"]==0:
        accepted.append((box,audit["minimum"]))
        continue
    if depth>=max_depth:
        unresolved.append((box,audit))
        continue
    axis=max(range(3),key=lambda index:box[index][1]-box[index][0])
    lo,hi=box[axis];mid=(lo+hi)/2
    left=list(box);right=list(box)
    left[axis]=(lo,mid);right[axis]=(mid,hi)
    queue.extend(((tuple(left),depth+1),(tuple(right),depth+1)))

print(f"lower_face_adaptive_accepted={len(accepted)}")
print(f"lower_face_adaptive_unresolved={len(unresolved)}")
print(f"lower_face_adaptive_minimum={min(value for _,value in accepted) if accepted else None}")
print(f"lower_face_strictly_positive_certified={not unresolved and all(value>0 for _,value in accepted)}")
