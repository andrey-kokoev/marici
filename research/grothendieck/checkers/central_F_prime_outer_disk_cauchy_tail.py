"""Cauchy budget reducing the quarter-disk tail to a unit-disk source bound."""
import json
from decimal import Decimal, localcontext
from pathlib import Path

with localcontext() as context:
    context.prec=80;D=Decimal
    outer_radius=D(1);inner_radius=D('0.25');degree=5;outer_bound=D(20)
    tail=outer_bound*(inner_radius/outer_radius)**degree/(1-inner_radius/outer_radius)
    allowance=D('0.0298826193544477705247295467774323832704235736221185784464828327745602429810737451513459562')
    residual=allowance-tail
result={'outer_disk_radius':str(outer_radius),'proposed_outer_disk_F_prime_bound':str(outer_bound),
        'inner_disk_radius':str(inner_radius),'omitted_tail_starts_at_degree':degree,
        'cauchy_geometric_tail_bound':str(tail),'available_tail_allowance':str(allowance),
        'residual_tail_margin':str(residual),'outer_disk_gate_suffices':residual>0,
        'outer_disk_analyticity_and_bound_proved':False,'rh_proved':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-F-prime-outer-disk-cauchy-tail.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
