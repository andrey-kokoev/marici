"""Exact numerical budget for the one-circle first-cell continuum gate."""
import json
from decimal import Decimal, localcontext
from pathlib import Path

with localcontext() as context:
    context.prec=80;D=Decimal
    curvature_margin=D("0.0000359281336177778441800113287376268686998584370838600335651203134843376")
    cell_width=D("2e-8");required_h3_bound=curvature_margin/cell_width
    disk_radius=D("0.25");inner_radius=D("3e-8");H_disk_bound=D(4)
    cauchy_h3_bound=D(6)*H_disk_bound/(disk_radius-inner_radius)**3
    residual_margin=curvature_margin-cell_width*cauchy_h3_bound
result={"first_cell":["1e-8","3e-8"],"certified_average_curvature_margin":str(curvature_margin),
        "required_supremum_H_triple_prime_bound":str(required_h3_bound),
        "proposed_disk_radius":str(disk_radius),"proposed_F_prime_modulus_lower_bound":"1/16",
        "implied_H_modulus_upper_bound":str(H_disk_bound),"cauchy_H_triple_prime_bound":str(cauchy_h3_bound),
        "pointwise_concavity_residual_margin":str(residual_margin),
        "cauchy_bound_closes_if_disk_gate_proved":residual_margin>0,
        "disk_nonvanishing_gate_proved":False,"rh_proved":False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-first-cell-cauchy-gate.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
