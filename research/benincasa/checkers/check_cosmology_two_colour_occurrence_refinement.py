#!/usr/bin/env python3
"""Construct a provenance-faithful two-colour occurrence refinement."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
assert json.loads((R/'cosmology_six_axis_fiber_congruence_source_descent.json').read_text())['passed']
src=('q_g3','q_G12','q_g1','q_G23','q_g2','q_G31')
col=('G12:S','G12:P','G23:S','G23:P','G31:S','G31:P')
axis_map=dict(zip(src,col));assert len(set(axis_map.values()))==6
# Relabelling is bijective on all masks.
images={tuple(col[i] for i,b in enumerate(v) if b) for v in itertools.product((0,1),repeat=6)};assert len(images)==64
shadow=(0,-1,1)
lifts=[]
for vals in itertools.product(range(-2,3),repeat=6):
 if tuple(vals[2*i]+vals[2*i+1] for i in range(3))==shadow and sum(map(abs,vals))==2:lifts.append(vals)
assert len(lifts)==4
kernel=[[1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1]]
out={'schema':'marici.benincasa.cosmology-two-colour-occurrence-refinement.v1','colour_meaning':{'S':'singleton complement','P':'same pair'},'source_to_coloured_axis_map':axis_map,'axis_map_bijective':True,'mask_map_faithful':True,'domain_masks':64,'distinct_coloured_images':len(images),'forgetful_map':'sum S and P coordinates for each occurrence pair','forgetful_kernel_rank':3,'forgetful_kernel_basis':kernel,'uncoloured_shadow':list(shadow),'minimal_l1_coloured_lifts':[list(x) for x in lifts],'minimal_lift_count':len(lifts),'coloured_lift_selected_by_source':False,'formal_result':'the coloured six-axis target preserves all deletion provenance and removes the absorption congruence','source_realized':False,'remaining_data':'actual coloured occurrence modules and a source-derived splitting of the physical shadow','next_test':'impose cyclic equivariance on coloured shadow splittings and classify the surviving integral choices','passed':True};(R/'cosmology_two_colour_occurrence_refinement.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
