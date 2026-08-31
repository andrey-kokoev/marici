#!/usr/bin/env python3
"""Type obstruction for the occurrence-to-ordered-Cech connector."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
t=json.loads((R/'deletion_occurrence_projector_typing.json').read_text())
del_labels=[x['label'] for x in t['deletion_axes']];occ_labels=[x['label'] for x in t['occurrence_axes']]
assert set(del_labels).isdisjoint(occ_labels)
assert t['checks']['every_deletion_changes_the_module_mask']
assert t['checks']['occurrence_support_is_an_endomorphism']
assert t['checks']['no_deletion_edge_is_an_occurrence_endomorphism']
out={'schema':'marici.benincasa.cosmology-occurrence-to-cech-connector-obstruction.v1','source_category':{'objects':8,'arrows':12,'axes':del_labels,'variance':'each arrow changes the denominator-module mask'},'occurrence_category':{'axes':occ_labels,'variance':'projector is an endomorphism on one occurrence-chart module'},'candidate_matrix':t['candidate_occurrence_projector'],'typed_failures':['axis label sets are disjoint','source and target objects are not identified','deletion arrows change module while occurrence support is an endomorphism','no components on all eight source objects','no twelve naturality squares'],'zero_map_comment':'the zero connector exists abstractly but cannot send the antisymmetric word to its nonzero occurrence shadow','disposition':'no nonzero source-derived connector is defined by the current candidate','minimal_enlargement':['source-derived object map from deletion masks to occurrence-chart modules','axis map preserving labels and orientation','component maps on all eight objects','commutativity on all twelve deletion edges'],'next_source_candidate':'complete rank-twelve triangular transport extending the A2 e6 occurrence morphism','passed':True};(R/'cosmology_occurrence_to_cech_connector_obstruction.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
