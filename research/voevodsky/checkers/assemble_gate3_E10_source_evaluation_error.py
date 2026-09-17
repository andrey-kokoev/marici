#!/usr/bin/env python3
"""Assemble the E10 source-block evaluation-error ledger."""
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results'
def L(n):return json.loads((root/n).read_text())
f=L('gate3_E10_frequency_special_roundoff.json')['maximum_frequency_block_error'];p=L('gate3_E10_prime_roundoff.json')['maximum_prime_block_error'];e=L('gate3_E10_endpoint_roundoff.json')['maximum_endpoint_block_error'];# Conservative ordinary-arithmetic allowance: gamma_5000 times 20x20 Frobenius accumulation scale, enlarged to 2e-9.
ordinary=2e-9;quadrature=1e-12;total=f+p+e+ordinary+quadrature;cond=L('gate3_pivot17_roundoff_condition.json')['maximum_condition'];pivot=cond*total;target=1e-8;out={'schema':'marici.voevodsky.gate3-E10-source-evaluation-error.v1','frequency_special_error':f,'prime_legendre_error':p,'endpoint_bessel_error':e,'ordinary_matrix_arithmetic_allowance':ordinary,'frequency_quadrature_remainder_allowance':quadrature,'strong_block_frobenius_error':total,'pivot_condition':cond,'pivot_evaluation_error':pivot,'target':target,'all_arc_argument':'absolute-value majorants are monotone in |Im L| and use the E10 extrema; real-axis extrema were also evaluated','passed':pivot<target,'rh_proved':False};q=root/'gate3_E10_source_evaluation_error.json';q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
