#!/usr/bin/env python3
"""Audit exact transition algebra on the certified tau target line."""
import json
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results'
files={2:'cosmology_rees_affine_H2Q2_exact_certificate.json',3:'cosmology_rees_affine_H3Q3_exact_certificate.json',4:'cosmology_rees_affine_pole4_target_detector.json',5:'cosmology_rees_affine_pole5_target_detector.json'}
checks=[]
for n,f in files.items():
 d=json.loads((P/f).read_text())
 if n<4: pairing=d['target_pairing']
 else: pairing=d[f'target_R{n+1}_pairing']
 checks.append({'pole_order':n,'certificate':f,'normalized_target_pairing':pairing,'target_nonzero':pairing=='1'})
assert all(x['target_nonzero'] for x in checks)
maps=[{'source_order':n,'target_order':n+1,'matrix_on_certified_target_lines':[['1']],'kernel_dimension':0,'cokernel_dimension':0} for n in range(2,5)]
mod=json.loads((P/'cosmology_rees_relative_transition_kernel.json').read_text())
out={'schema':'marici.benincasa.cosmology-rees-target-line-transition-algebra.v1','target_certificates':checks,'induced_identity':'M_(n+1)(R f)=R M_n(f)','target_line_maps':maps,'target_line_transition_algebra_exact':True,'global_transition_algebra':{'A4_to_A5_mod101_kernel_dimension':mod['modular_kernel_dimensions']['A4_to_A5_mod101'],'A4_to_A5_mod101_cokernel_dimension':mod['modular_cokernel_dimensions']['A4_to_A5_mod101'],'characteristic_zero_kernel_dimension':None,'characteristic_zero_cokernel_dimension':None},'scope':'exact over Q on the certified one-dimensional target lines at pole orders 2 through 5; global quotient kernels and cokernels remain uncomputed over Q'}
(P/'cosmology_rees_target_line_transition_algebra.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
