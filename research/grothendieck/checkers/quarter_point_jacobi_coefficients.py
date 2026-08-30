"""Certified first Jacobi off-diagonal squares from Hausdorff determinants."""
import json
from decimal import Decimal,Context,ROUND_FLOOR,ROUND_CEILING
from pathlib import Path
root=Path(__file__).parents[1]/'results'
def load(name):return json.loads((root/name).read_text(encoding='utf-8'))
first=load('quarter-point-end-to-end-interval.json');second=load('quarter-point-order-two-interval.json');third=load('quarter-point-order-three-interval.json')
fourth=load('quarter-point-order-four-interval.json')
down=Context(prec=70,rounding=ROUND_FLOOR);up=Context(prec=70,rounding=ROUND_CEILING)
def box(x):return Decimal(x[0]),Decimal(x[1])
def mul(x,y):
    lo=[down.multiply(a,b) for a in x for b in y];hi=[up.multiply(a,b) for a in x for b in y]
    return min(lo),max(hi)
def sub(x,y):return down.subtract(x[0],y[1]),up.subtract(x[1],y[0])
def square(x):return mul(x,x)
def divp(x,y):return mul(x,(down.divide(Decimal(1),y[1]),up.divide(Decimal(1),y[0])))
A=list(map(box,first['moment_intervals']))
D0=A[0];D1=sub(mul(A[0],A[2]),square(A[1]));D2=box(second['order_two_determinant_intervals'][0]);D3=box(third['order_three_determinant_intervals'][0]);D4=box(fourth['order_four_determinant_intervals'][0])
b1=divp(D1,square(D0));b2=divp(mul(D2,D0),square(D1));b3=divp(mul(D3,D1),square(D2));b4=divp(mul(D4,D2),square(D3))
assert all(x[0]>0 for x in (b1,b2,b3,b4))
def strings(x):return [str(x[0]),str(x[1])]
result={'ordinary_hankel_determinants':[strings(x) for x in (D0,D1,D2,D3,D4)],'jacobi_off_diagonal_squares_b1_through_b4':[strings(x) for x in (b1,b2,b3,b4)],'coefficients_interval_certified':True,'interpretation_conditional_on_full_hierarchy':True,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'quarter-point-jacobi-coefficients.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
