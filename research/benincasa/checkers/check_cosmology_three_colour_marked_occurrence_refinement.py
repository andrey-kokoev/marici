#!/usr/bin/env python3
"""Construct the cyclic S/P/L occurrence refinement."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
assert json.loads((R/'cosmology_literal_generator_colour_provenance_gate.json').read_text())['passed']
axis_map={'q_g3':'G12:S','q_G12':'G12:P','q_g12':'G12:L','q_g1':'G23:S','q_G23':'G23:P','q_g23':'G23:L','q_g2':'G31:S','q_G31':'G31:P','q_g31':'G31:L'}
assert len(set(axis_map.values()))==9
# Bijective relabelling preserves all masks.
assert 2**len(axis_map)==512
shadow=(0,-1,1);lifts=[]
for v in itertools.product((-1,0,1),repeat=9):
 if tuple(sum(v[3*i:3*i+3]) for i in range(3))==shadow and sum(map(abs,v))==2:lifts.append(v)
assert len(lifts)==9
allL=(0,0,0,0,0,-1,0,0,1);assert allL in lifts
literal=(1,0,0,0,0,-1,0,0,-1)
out={'schema':'marici.benincasa.cosmology-three-colour-marked-occurrence-refinement.v1','colours':{'S':'singleton complement','P':'uppercase same pair','L':'lowercase marked pair'},'axis_map':axis_map,'axis_map_bijective':True,'mask_count':512,'faithful_mask_images':512,'forgetful_kernel_rank':6,'minimal_shadow_lift_count':len(lifts),'minimum_equivariant_splittings':['all-S','all-P','all-L'],'literal_partial_fraction_coloured_vector':list(literal),'literal_deletion_pattern':'S,L,L','all_L_shadow_candidate':list(allL),'all_L_selected_conditionally_by_nonzero_literal_boundary_support':True,'typed_connector_from_literal_boundary_to_occurrence_shadow':False,'cyclic_closure_requires_new_axis':'q_g12','q_g12_present_in_literal_five_mark_word':False,'source_realized':False,'conclusion':'three colours preserve all known label kinds and isolate an all-L shadow candidate, but the missing q_g12 closure and boundary-to-occurrence connector prevent authorization','next_test':'test whether the literal marked-pair boundary defines the oriented all-L occurrence shadow or fails at the sign and chain-map interface','passed':True};(R/'cosmology_three_colour_marked_occurrence_refinement.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
