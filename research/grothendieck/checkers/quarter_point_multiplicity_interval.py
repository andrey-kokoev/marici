"""Christoffel-weight interval for the fifth top-node multiplicity estimate."""
import json
from decimal import Decimal,Context,ROUND_FLOOR,ROUND_CEILING
from pathlib import Path
root=Path(__file__).parents[1]/'results'
j=json.loads((root/'quarter-point-jacobi-diagonal.json').read_text());r=json.loads((root/'quarter-point-fifth-ritz-interval.json').read_text())
down=Context(prec=70,rounding=ROUND_FLOOR);up=Context(prec=70,rounding=ROUND_CEILING)
def box(x):return Decimal(x[0]),Decimal(x[1])
def add(x,y):return down.add(x[0],y[0]),up.add(x[1],y[1])
def mul(x,y):
    lo=[down.multiply(a,b) for a in x for b in y];hi=[up.multiply(a,b) for a in x for b in y]
    return min(lo),max(hi)
def square(x):
    if x[0]<=0<=x[1]:return Decimal(0),max(up.multiply(x[0],x[0]),up.multiply(x[1],x[1]))
    return mul(x,x)
def divp(x,y):return mul(x,(down.divide(Decimal(1),y[1]),up.divide(Decimal(1),y[0])))
u=box(r['largest_u_ritz_interval']);norms=list(map(box,j['polynomial_norm_intervals']))
polys=[[box(x) for x in p] for p in j['monic_polynomial_coefficient_intervals']]
def evaluate(p,x):
    value=(Decimal(0),Decimal(0))
    for coefficient in reversed(p):value=add(mul(value,x),coefficient)
    return value
christoffel=(Decimal(0),Decimal(0))
for p,h in zip(polys,norms):christoffel=add(christoffel,divp(square(evaluate(p,u)),h))
weight=(down.divide(Decimal(1),christoffel[1]),up.divide(Decimal(1),christoffel[0]))
multiplicity=divp(weight,u)
assert multiplicity[0]>1
def strings(x):return [str(x[0]),str(x[1])]
result={'top_quadrature_weight_interval':strings(weight),'blind_multiplicity_interval':strings(multiplicity),'interval_certified':True,'zero_locations_used':False,'simplicity_proved':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'quarter-point-multiplicity-interval.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
