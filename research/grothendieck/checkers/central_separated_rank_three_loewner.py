"""Directed separated rank-three Loewner minor on the central interval."""
import json
from decimal import Decimal
from pathlib import Path

import reduced_source_central_interval_chords as I

D=Decimal; ROOT=Path(__file__).parents[1]
payload=json.loads((ROOT/'results'/'central-H-degree-eleven-interval.json').read_text())
f=[(D(a),D(b)) for a,b in payload['F_coefficients_through_degree_twenty_three']]
points=[D(0),D('.005'),D('.01')]
M=D('6.038308'); r=D('.01')
tail=I.up.divide(I.up.multiply(M,r**23),I.down.subtract(D(1),r))
error=(tail.copy_negate(),tail)

def evaluate(coefficients,x):
    value=coefficients[-1]
    point=I.box(x)
    for coefficient in reversed(coefficients[:-1]): value=I.add(coefficient,I.mul(point,value))
    return value
def kernel(x,y):
    if x==y:
        derivative=[I.scale(f[n],n) for n in range(1,len(f))]
        return I.add(evaluate(derivative,x),error)
    return I.add(I.div(I.sub(evaluate(f,y),evaluate(f,x)),I.box(y-x)),error)
def determinant3(a):
    return I.add(I.mul(a[0][0],I.sub(I.mul(a[1][1],a[2][2]),I.mul(a[1][2],a[2][1]))),
                 I.neg(I.mul(a[0][1],I.sub(I.mul(a[1][0],a[2][2]),I.mul(a[1][2],a[2][0])))),
                 I.mul(a[0][2],I.sub(I.mul(a[1][0],a[2][1]),I.mul(a[1][1],a[2][0]))))

matrix=[[kernel(x,y) for y in points] for x in points]
det=determinant3(matrix)
strict=det[0]>0
result={
    'points':[str(x) for x in points],
    'Loewner_matrix':[[[str(a),str(b)] for a,b in row] for row in matrix],
    'degree_at_least_twenty_three_kernel_tail_bound':str(tail),
    'determinant_interval':[str(x) for x in det],
    'strictly_positive_separated_rank_three_minor':strict,
    'directed_decimal_rounding':True,
    'interval_certified':strict,
    'zero_locations_used':False,
    'rh_proved':False,
}
if __name__=='__main__':
    output=ROOT/'results'/'central-separated-rank-three-loewner.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
