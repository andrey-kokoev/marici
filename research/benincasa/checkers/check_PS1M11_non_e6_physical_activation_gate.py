#!/usr/bin/env python3
"""Test whether existing source data can physically activate nearby e3/e5 directions."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
st=json.loads((R/'relative-stokes-pairing-gate.json').read_text())
red=json.loads((R/'marked-relative-reduction-engine-certificate.json').read_text())
mov=json.loads((R/'results/PS1C1a1i_materialize_moving_Theta101.json').read_text())
phys=json.loads((R/'three-cut-relative-chain-pairing-certificate.json').read_text())
assert 'e3' in red['gauge_dependent_coordinates'] and 'e5' in red['gauge_dependent_coordinates']
assert set(['e3','e5']).issubset(st['naive_contraction_falsifier']['exceptional_support'])
assert not st['naive_contraction_falsifier']['contraction_descends_to_relative_class']
assert mov['resolution']=='-+'
assert phys['six_occurrence_relative_boundary_pairing']==[0]*6
out={'schema':'marici.benincasa.PS1M11-non-e6-physical-activation-gate.v1','prospective_action':'PS1M11_activate_nearby_e3_or_e5_with_existing_relative_chain','resolution':'-+','tests':{'e3_gauge_dependent':True,'e5_gauge_dependent':True,'naive_contraction_descends':False,'literal_positive_chain_pairing':[0,0,0,0,0,0],'moving_wall_source_canonical_lift':False},'reason':'The only ambient directions distinguishing the cut-nearby rank-three image from the common e6 line are e3 and e5, but both vary under exact relative gauges. Direct coordinate contraction is therefore not a physical scalar. Leray-tube activation would require the moving-wall Gauss-Manin coefficient, and the frozen source fixes only its central restriction, leaving arbitrary E*F corrections that change the physical residues.','conclusion':'No current source-authorized relative chain activates a non-e6 nearby component. The compatible nearby packet remains unactivated and cannot establish a second physical realization.','reopening_interface':'supply a source-canonical moving-wall coefficient/connection and an oriented Leray tube whose e3 or e5 residue pairing is gauge invariant and nonzero','passed':True}
(R/'results/PS1M11_non_e6_physical_activation_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
