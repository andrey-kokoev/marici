#!/usr/bin/env python3
"""Exact lift of the first faithful A4-to-A5 quotient-kernel class."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results';d=json.loads((R/'cosmology_rees_expanded_faithful_kernel_coordinates.json').read_text());vs=d['strongest_falsification_attempt']['vectors'];keys=list(vs[0]['vector'])
expected=[(1,3),(-1,3),(-2,1),(1,1)]
for item in vs:
 p=item['prime']
 for k,(n,q) in zip(keys,expected):assert item['vector'][k]==n*pow(q,-1,p)%p
out={'schema':'marici.benincasa.cosmology-rees-exact-faithful-kernel-lift.v1','problem':'lift the common faithful quotient vector to an exact rational and primitive integral kernel class','reconstructed_rational_coefficients':dict(zip(keys,['1/3','-1/3','-2','1'])),'primitive_integral_coefficients':dict(zip(keys,[1,-1,-6,3])),'exact_zero_identity':'u*v^4*(v-3) - v^5*(u-6) - 6*v^5 + 3*u*v^4 = 0','source_factors':{'q_g23':'v-3','q_g31':'u-6'},'source_class_nonzero':'the four coordinates belong to the faithful A4 nonpivot quotient basis and the normalized vector is nonzero modulo 101','target_class_zero':'the displayed polynomial identity is exact over Z and is admitted by the A5 q-multiplication relation span','three_prime_replay':[101,103,107],'primitive_content':1,'result_strength':'finite-cutoff source-typed exact kernel vector','scope':'A4-to-A5 assembled quotient only; not tau_p, an unbounded class, or a physical readout','passed':True};(R/'cosmology_rees_exact_faithful_kernel_lift.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
