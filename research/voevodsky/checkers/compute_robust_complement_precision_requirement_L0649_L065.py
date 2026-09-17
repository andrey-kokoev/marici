#!/usr/bin/env python3
"""Precision requirement obtained by scaling the explicit binary roundoff model."""
import json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results';d=json.loads((root/'robust_complement_certificate_L0649_L065.json').read_text());base=d['base_floor'];E53=d['modeled_errors']['binary64_robust_output_operator_error'];B=1.8316876996878346;fixed=d['modeled_errors']['source_assembly_4x_refinement']+d['modeled_errors']['moving_branch_interpolation_tail'];rows=[]
for bits in (53,56,60,64,80,113,160):
 scale=2.0**(53-bits);e=E53*scale;gram=2*B*e+e*e;lower=base-fixed-gram;rows.append({'mantissa_bits':bits,'output_operator_error':e,'gram_error':gram,'lower':lower,'ten_percent_reserve':lower>0.1*base})
minimum=next(x['mantissa_bits'] for x in rows if x['ten_percent_reserve']);out={'schema':'marici.voevodsky.robust-complement-precision-requirement-L0649-L065.v1','model':'all arithmetic and 4096-ulp special-function reserves scale with unit roundoff; analytic/source errors held fixed','base_floor':base,'rows':rows,'minimum_tested_bits_for_10_percent_reserve':minimum,'recommended_bits':113,'passed_design':rows[-2]['lower']>0,'passed':False,'reason_not_certificate':'precision sizing only; directed high-precision assembly has not been executed','rh_proved':False};p=root/'robust_complement_precision_requirement_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_design']
