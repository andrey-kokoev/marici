#!/usr/bin/env python3
"""Fit the observed range-compatible losses to the jump-tail 1/(k(k+1)) law."""
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';vals=[]
for name in ('range_compatible_continuum_correction_L06495.json','range_compatible_continuum_correction_L06495_to3000.json','range_compatible_continuum_correction_L06495_to4000.json'):
 d=json.loads((root/name).read_text());vals.append(d['minimum_loss'])
blocks=[vals[0],vals[1]-vals[0],vals[2]-vals[1]];scaled=[blocks[k-1]*k*(k+1) for k in (1,2,3)];C=max(scaled);tail=C/4;current=json.loads((root/'range_compatible_continuum_correction_L06495_to4000.json').read_text())['corrected_min'];out={'schema':'marici.voevodsky.continuum-residual-telescoping-tail-L06495.v1','block_losses':blocks,'scaled_C_estimates':scaled,'conservative_empirical_C':C,'mode4000_infinite_tail_model_bound':tail,'lower_after_model_tail':current-tail,'model':'block k (modes 1000k..1000(k+1)-1) <= C/(k(k+1))','status':'floating asymptotic model; analytic Legendre jump bound required','passed_empirically':current-tail>0,'passed':False,'rh_proved':False};p=root/'continuum_residual_telescoping_tail_L06495.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_empirically']
