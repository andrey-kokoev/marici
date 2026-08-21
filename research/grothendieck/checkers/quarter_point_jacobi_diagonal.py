"""Interval Lanczos extraction of the first Jacobi diagonal coefficients."""
import json
from decimal import Decimal,Context,ROUND_FLOOR,ROUND_CEILING
from pathlib import Path

root=Path(__file__).parents[1]/'results'
mom=json.loads((root/'quarter-point-order-four-interval.json').read_text())
off=json.loads((root/'quarter-point-jacobi-coefficients.json').read_text())
down=Context(prec=70,rounding=ROUND_FLOOR);up=Context(prec=70,rounding=ROUND_CEILING)
def box(x):return Decimal(x[0]),Decimal(x[1])
def add(x,y):return down.add(x[0],y[0]),up.add(x[1],y[1])
def neg(x):return x[1].copy_negate(),x[0].copy_negate()
def mul(x,y):
    lo=[down.multiply(a,b) for a in x for b in y];hi=[up.multiply(a,b) for a in x for b in y]
    return min(lo),max(hi)
def divp(x,y):return mul(x,(down.divide(Decimal(1),y[1]),up.divide(Decimal(1),y[0])))
zero=(Decimal(0),Decimal(0));one=(Decimal(1),Decimal(1))
A=list(map(box,mom['moments_A0_through_A9']));b=list(map(box,off['jacobi_off_diagonal_squares_b1_through_b4']))
def inner(p,q,shift=0):
    total=zero
    for i,x in enumerate(p):
        for j,y in enumerate(q):total=add(total,mul(mul(x,y),A[i+j+shift]))
    return total
def xpoly(p):return [zero]+p
def combine(*terms):
    size=max(len(p) for _,p in terms);out=[zero for _ in range(size)]
    for scalar,p in terms:
        for i,x in enumerate(p):out[i]=add(out[i],mul(scalar,x))
    return out

p=[one];previous=[];alphas=[];norms=[];polynomials=[]
for n in range(5):
    norm=inner(p,p);alpha=divp(inner(p,p,1),norm)
    norms.append(norm);alphas.append(alpha);polynomials.append(p)
    if n<4:
        terms=[(one,xpoly(p)),(neg(alpha),p)]
        if n>0:terms.append((neg(b[n-1]),previous))
        previous,p=p,combine(*terms)

def strings(x):return [str(x[0]),str(x[1])]
support_tests=[x[0]>0 and x[1]<4 for x in alphas]
norm_ratios=[divp(norms[n],norms[n-1]) for n in range(1,5)]
ratio_consistency=[max(norm_ratios[i][0],b[i][0])<=min(norm_ratios[i][1],b[i][1]) for i in range(4)]
result={'jacobi_diagonal_a0_through_a4':[strings(x) for x in alphas],
        'polynomial_norm_intervals':[strings(x) for x in norms],
        'monic_polynomial_coefficient_intervals':[[strings(x) for x in p] for p in polynomials],
        'each_diagonal_inside_support_0_4':support_tests,
        'norm_ratio_off_diagonal_consistency':ratio_consistency,
        'all_diagonals_resolved':all(x[0]<x[1] for x in alphas),
        'interval_method':'uncorrelated outward interval Lanczos',
        'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'quarter-point-jacobi-diagonal.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
