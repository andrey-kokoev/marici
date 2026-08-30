"""Interval triangle budget for |F'| on the quarter-radius disk."""
import json
from decimal import Decimal, localcontext
from pathlib import Path

ROOT=Path(__file__).parents[1]
payload=json.loads((ROOT/'results'/'central-xi-log-even-series-interval.json').read_text())
with localcontext() as context:
    context.prec=90;D=Decimal
    a=[tuple(map(D,x)) for x in payload['ell_prime_coefficient_intervals_through_degree_five']]
    g=[]
    for n in range(5):
        lo=D(n+1)*(D(4)*a[n][0]-a[n+1][1]);hi=D(n+1)*(D(4)*a[n][1]-a[n+1][0]);g.append((lo,hi))
    radius=D('0.25');variation=sum((max(abs(g[n][0]),abs(g[n][1]))*radius**n for n in range(1,5)),D(0))
    polynomial_lower=g[0][0]-variation;target=D(1)/16;tail_allowance=polynomial_lower-target
result={'disk_radius':str(radius),'F_prime_coefficients_degrees_0_through_4':[[str(x) for x in box] for box in g],
        'known_polynomial_radial_variation_upper_bound':str(variation),
        'known_polynomial_modulus_lower_bound':str(polynomial_lower),'target_modulus_lower_bound':'0.0625',
        'allowable_omitted_tail_supremum':str(tail_allowance),'positive_tail_allowance':tail_allowance>0,
        'disk_gate_reduces_to_tail_bound':True,'omitted_tail_bound_proved':False,'rh_proved':False}
if __name__=='__main__':
    output=ROOT/'results'/'central-F-prime-disk-polynomial-budget.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
