#!/usr/bin/env python3
"""Test whether the existing locally-closed bang span supplies PS1M6's missing arrow."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
pair=json.loads((R/'relative-pair-gysin-gate-certificate.json').read_text())
typeg=json.loads((R/'overlap-coefficient-type-gate-certificate.json').read_text())
norm=json.loads((R/'overlap-normal-specialization-gate-certificate.json').read_text())
det=json.loads((R/'two-cut-cousin-determinant-gate-certificate.json').read_text())
phys=json.loads((R/'three-cut-relative-chain-pairing-certificate.json').read_text())
assert pair['canonical_six_functor_bang_span'] and not pair['proper_gysin_correspondence']
assert not typeg['canonical_full_sector_transition']
assert not norm['degree_zero_map_from_nearby_cycles_to_costalk']
assert not norm['canonical_retraction_variance'] and norm['ordinary_euler_class']==0
assert not det['source_realizes_primitive']
assert phys['chain_boundary_cut_incidence']==[0,0,0]
out={'schema':'marici.benincasa.PS1M7-bang-correspondence-extension.v1','prospective_action':'PS1M7_use_existing_bang_span_as_overlap_arrow','resolution':'-+','available_correspondence':{'carrier':'locally closed common open in both sector opens','six_functor_span':True,'supported_object':'K_overlap=p12^!L12=p23^!L23','canonical_variance':['K_overlap -> L12','K_overlap -> L23']},'failed_requirements':{'full_sector_to_supported_retraction':False,'degree_zero_nearby_to_costalk_map':False,'normal_euler_class':0,'joint_koszul_class_realized_by_source':False,'literal_positive_chain_cut_incidence':[0,0,0]},'conclusion':'The existing bang correspondence has the wrong variance for the desired comparison: it inserts one common supported object into both sectors but does not retract either full sector to it. Purity shifts the costalk by [-2](-1), the principal normal Euler class vanishes, and the source does not realize 1/(q_G12 q_G23). Hence this correspondence cannot provide the missing overlap column map.','reopening_interface':['a source-authorized secondary/excess supported class of the purity degree','a genuine joint-pole coefficient','or a relative chain whose boundary meets the marked cuts with the required orientations'],'passed':True}
(R/'results/PS1M7_bang_correspondence_extension.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
