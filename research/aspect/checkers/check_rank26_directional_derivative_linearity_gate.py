#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/aspect/results';runs=[]
for a in (8,16):
 for p in (32003,32009):runs.append(json.loads((R/f'rank26_directional_derivative_linearity_half_a{a}_p{p}.json').read_text()))
assert all(x['passed'] for x in runs) and {(x['ambient'],x['prime'],x['rows_checked']) for x in runs}=={(8,32003,9780),(8,32009,9780),(16,32003,39076),(16,32009,39076)}
out={'schema':'marici.aspect.rank26-directional-derivative-linearity-gate.v1','gamma_mode':'half','primes':[32003,32009],'ambient_degrees':[8,16],'identity':'b_tangent=b_nx-b_ny on the common special-syzygy domain','rowwise_verified':True,'surjectivity_of_difference_derived':False,'remaining_exact_gate':'construct a source involution or homotopy forcing image(b_nx-b_ny)=image(b_nx)=image(b_ny), rather than inferring this from equal finite ranks','unbounded_stabilization_proved':False,'passed':True};(R/'rank26_directional_derivative_linearity_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','runs':4}))
