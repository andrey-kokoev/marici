#!/usr/bin/env python3
"""Compute principal-lattice saturation and audit its source semantics."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
for n in ['cosmology_minimal_primitive_source_enlargement.json','cosmology_universal_minimal_integral_source_extension.json']:
 assert json.loads((R/n).read_text())['passed']
def in_L(v): return v[0]%2==0
window=[(a,b) for a in range(-8,9) for b in range(-8,9)]
sat=[v for v in window if any(in_L((n*v[0],n*v[1])) for n in range(1,5))]
assert sat==window
odd=[v for v in window if not in_L(v)];assert all(((v[0]-1)%2==0) for v in odd)
out={'schema':'marici.benincasa.cosmology-principal-lattice-saturation-source-gate.v1','ambient_lattice':'Z^2','source_image_lattice':'2Z direct-sum Z','index':2,'saturation':'Z^2','quotient':'Z/2','unique_missing_coset':'(1,0)+(2Z direct-sum Z)','target_in_missing_coset':True,'coordinate_result':{'primitive_target_available_in_saturation':True,'normal_form':[1,0]},'semantic_result':{'source_generator_constructed':False,'ordered_boundary_constructed':False,'g23_g31_labels_constructed':False,'comparison_map_constructed':False},'reason':'saturation is computed inside the target coordinate lattice and has no inverse image operation on the source complex','noncanonical_representatives':'all (1,b) and sign-related representatives differ by the old lattice; target coordinates can normalize them but do not label a source preimage','conclusion':'canonical saturation recovers the formal over-lattice but not a source-authorized primitive class','next_test':'saturate the joint column-boundary graph and test whether the required pair ((1,0),(0,-2,2)) lies in it','passed':True};(R/'cosmology_principal_lattice_saturation_source_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
