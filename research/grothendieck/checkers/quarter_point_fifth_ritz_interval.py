"""Sturm-inertia interval enclosure of the fifth extremal Ritz node."""
import json
from decimal import Decimal,Context,ROUND_FLOOR,ROUND_CEILING
from pathlib import Path
root=Path(__file__).parents[1]/'results'
a=json.loads((root/'quarter-point-jacobi-diagonal.json').read_text())['jacobi_diagonal_a0_through_a4']
b=json.loads((root/'quarter-point-jacobi-coefficients.json').read_text())['jacobi_off_diagonal_squares_b1_through_b4']
a=[(Decimal(x[0]),Decimal(x[1])) for x in a];b=[(Decimal(x[0]),Decimal(x[1])) for x in b]
down=Context(prec=70,rounding=ROUND_FLOOR);up=Context(prec=70,rounding=ROUND_CEILING)
def sub(x,y):return down.subtract(x[0],y[1]),up.subtract(x[1],y[0])
def reciprocal(x):
    assert x[1]<0 or x[0]>0
    lo=down.divide(Decimal(1),x[1]);hi=up.divide(Decimal(1),x[0])
    return min(lo,hi),max(lo,hi)
def mul(x,y):
    lo=[down.multiply(u,v) for u in x for v in y];hi=[up.multiply(u,v) for u in x for v in y]
    return min(lo),max(hi)
def inertia_below(x):
    point=(x,x);pivots=[sub(a[0],point)]
    for i in range(1,5):
        if pivots[-1][0]<=0<=pivots[-1][1]:return None
        pivots.append(sub(sub(a[i],point),mul(b[i-1],reciprocal(pivots[-1]))))
    if any(p[0]<=0<=p[1] for p in pivots):return None
    return sum(p[1]<0 for p in pivots)

known_low=Decimal('0.0049');known_high=Decimal('0.0051')
assert inertia_below(known_low)==4 and inertia_below(known_high)==5
lo,hi=known_low,known_high
for _ in range(240):
    mid=(lo+hi)/2
    if inertia_below(mid)==4:lo=mid
    else:hi=mid
lower=lo
lo,hi=known_low,known_high
for _ in range(240):
    mid=(lo+hi)/2
    if inertia_below(mid)==5:hi=mid
    else:lo=mid
upper=hi
assert lower<upper
# gamma decreases: lower gamma comes from upper u and conversely.
def gamma(u,rounding):
    c=down if rounding==ROUND_FLOOR else up
    rad=c.subtract(c.divide(Decimal(1),u),Decimal('0.25'))
    value=c.sqrt(rad)
    return c.next_minus(value) if rounding==ROUND_FLOOR else c.next_plus(value)
gamma_box=(gamma(upper,ROUND_FLOOR),gamma(lower,ROUND_CEILING))
result={'largest_u_ritz_interval':[str(lower),str(upper)],
        'transformed_ordinate_interval':[str(gamma_box[0]),str(gamma_box[1])],
        'lower_endpoint_inertia':inertia_below(lower),'upper_endpoint_inertia':inertia_below(upper),
        'interval_eigenvalue_certified':True,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'quarter-point-fifth-ritz-interval.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
