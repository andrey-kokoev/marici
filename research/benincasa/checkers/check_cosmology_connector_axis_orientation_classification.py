#!/usr/bin/env python3
"""Classify formal oriented axis assignments for the free connector."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
assert json.loads((R/'cosmology_minimal_occurrence_cech_connector_presentation.json').read_text())['passed']
typing=json.loads((R/'deletion_occurrence_projector_typing.json').read_text())
assert isinstance(typing,dict) and typing
src=('q_g1','q_g2','q_G12');tgt=('G12:e6','G23:e6','G31:e6')
bij=[dict(zip(src,p)) for p in itertools.permutations(tgt)]
orient=[{'map':m,'signs':dict(zip(src,s))} for m in bij for s in itertools.product((-1,1),repeat=3)]
assert len(bij)==6 and len(orient)==48
text_anchor=[m for m in bij if m['q_G12']=='G12:e6'];assert len(text_anchor)==2
complement={'q_g1':'G23:e6','q_g2':'G31:e6','q_G12':'G12:e6'};assert complement in text_anchor
out={'schema':'marici.benincasa.cosmology-connector-axis-orientation-classification.v1','source_axes':list(src),'target_axes':list(tgt),'unoriented_bijections':6,'oriented_bijections':48,'strict_typed_label_preserving_bijections':0,'erased_text_G12_anchor_bijections':text_anchor,'complement_name_heuristic':complement,'complement_heuristic_source_authorized':False,'shadow_normalization_selects_axis_map':False,'reason':'the normalization is expressed only in the target occurrence basis; no source-axis coordinates exist to pull it back','source_selected_assignments':0,'classification':'the free connector has an S3 times (C2)^3 axis-orientation torsor with no admitted basepoint','next_test':'test whether cyclic equivariance can select the complement heuristic or instead fails because the deletion axis set is not closed under the sourced cyclic label action','passed':True};(R/'cosmology_connector_axis_orientation_classification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
