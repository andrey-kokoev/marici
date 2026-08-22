"""Upgrade every certified central chord average to pointwise H''<0."""
import json
from decimal import Decimal
from pathlib import Path

import reduced_source_central_interval_chords as C

D=C.D; ROOT=Path(__file__).parents[1]
h_payload=json.loads((ROOT/'results'/'central-H-degree-eleven-interval.json').read_text())
h=[(D(a),D(b)) for a,b in h_payload['H_coefficients_through_degree_eleven']]

def absolute_upper(x): return max(abs(x[0]),abs(x[1]))
def h3_polynomial(cell):
    coefficients=[C.scale(h[n],n*(n-1)*(n-2)) for n in range(3,12)]
    value=coefficients[-1]
    for coefficient in reversed(coefficients[:-1]): value=C.add(coefficient,C.mul(cell,value))
    return value
def tail_upper(x):
    # H is bounded by 7/2 on |t|<=1/4. Differentiate the geometric
    # coefficient majorant sum_{n>=12} q^n three times.
    R=D('.25'); q=C.up.divide(x,R); one_minus=C.down.subtract(D(1),q)
    terms=[C.up.divide(C.up.multiply(D(1320),q**9),one_minus),
           C.up.divide(C.up.multiply(D(396),q**10),one_minus**2),
           C.up.divide(C.up.multiply(D(72),q**11),one_minus**3),
           C.up.divide(C.up.multiply(D(6),q**12),one_minus**4)]
    return C.up.multiply(C.up.divide(D('3.5'),R**3),sum(terms,D(0)))

rows=[]
for average,a,midpoint,b in C.curvature_rows:
    polynomial=h3_polynomial((a,b)); tail=tail_upper(b)
    h3_bound=C.up.add(absolute_upper(polynomial),tail)
    margin=average[1].copy_negate()
    residual=C.down.subtract(margin,C.up.multiply(b-a,h3_bound))
    rows.append((residual,a,b,margin,h3_bound,polynomial,tail))

worst=min(rows,key=lambda row:row[0])
assert all(row[0]>0 for row in rows)
boundary_payload=json.loads((ROOT/'results'/'central-xi-log-even-series-interval.json').read_text())
boundary_h2=tuple(D(x) for x in boundary_payload['H_double_prime_at_zero_interval'])
boundary_width=D('1e-8')
boundary_polynomial=h3_polynomial((D(0),boundary_width))
boundary_tail=tail_upper(boundary_width)
boundary_h3_bound=C.up.add(absolute_upper(boundary_polynomial),boundary_tail)
boundary_residual=C.down.subtract(boundary_h2[1].copy_negate(),
                                  C.up.multiply(boundary_width,boundary_h3_bound))
assert boundary_residual>0
result={
    'chord_count':len(rows),
    'all_chords_upgraded_to_pointwise_concavity':True,
    'domain':['0','1e-2'],
    'boundary_sliver_concavity_certified':True,
    'boundary_sliver_residual_margin':str(boundary_residual),
    'worst_residual_margin':str(worst[0]),
    'worst_chord':[str(worst[1]),str(worst[2])],
    'worst_average_curvature_margin':str(worst[3]),
    'worst_H_triple_prime_bound':str(worst[4]),
    'worst_H_triple_prime_polynomial_interval':[str(x) for x in worst[5]],
    'worst_Cauchy_tail_bound':str(worst[6]),
    'H_disk_bound':'3.5',
    'H_disk_radius':'0.25',
    'directed_decimal_rounding':True,
    'interval_certified':True,
    'zero_locations_used':False,
    'rh_proved':False,
}
if __name__=='__main__':
    output=ROOT/'results'/'central-all-chords-continuum-upgrade.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
