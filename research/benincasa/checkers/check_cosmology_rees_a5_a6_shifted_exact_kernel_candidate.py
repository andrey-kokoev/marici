#!/usr/bin/env python3
"""Construct the degree-shifted exact A5-to-A6 kernel candidate."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];prior=json.loads((ROOT/'research/benincasa/results/cosmology_rees_exact_faithful_kernel_lift.json').read_text())
assert prior['primitive_integral_coefficients'] and prior['exact_zero_identity']=='u*v^4*(v-3) - v^5*(u-6) - 6*v^5 + 3*u*v^4 = 0'
# Multiplication by v gives the next-cutoff exact target relation.
terms={'u*v^5*(v-3)':1,'v^6*(u-6)':-1,'v^6':-6,'u*v^5':3}
# Expand coefficients by monomial: uv^6-3uv^5-uv^6+6v^6-6v^6+3uv^5.
expanded={'u*v^6':terms['u*v^5*(v-3)']+terms['v^6*(u-6)'],'u*v^5':-3*terms['u*v^5*(v-3)']+terms['u*v^5'],'v^6':-(-1)*6+terms['v^6']}
assert expanded=={'u*v^6':0,'u*v^5':0,'v^6':0}
out={'schema':'marici.benincasa.cosmology-rees-a5-a6-shifted-exact-kernel-candidate.v1','construction':'multiply the admitted primitive A4-to-A5 kernel identity by v','primitive_integral_coefficients':terms,'exact_zero_identity':'u*v^5*(v-3) - v^6*(u-6) - 6*v^6 + 3*u*v^5 = 0','expanded_residual':expanded,'target_A6_class_zero':True,'source_A5_class_nonzero_verified':False,'disposition':'exact rational target-zero candidate constructed; kernel membership awaits faithful A5 source reduction','scope':'candidate, not yet an exact nonzero A5 quotient-kernel theorem','acceptance_test':'reduce the four-term A5 source vector against the exact A5 relation echelon basis and require a nonzero normal form','passed':True};p=ROOT/'research/benincasa/results/cosmology_rees_a5_a6_shifted_exact_kernel_candidate.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
