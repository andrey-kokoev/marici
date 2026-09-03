#!/usr/bin/env python3
"""DPC gate for source-envelope deltas after the fixed-envelope obstruction."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
def load(n):
 d=json.loads((R/n).read_text());assert d['passed'];return d
boundary=load('cosmology_final_source_envelope_strength_boundary.json');status=load('cosmology_primitive_tau_current_source_envelope_status.json')
missing=status['missing_arrows']
# Risky consequences for representative deltas. Proximity is intentionally rejected.
cases=[
 {'name':'matching abstract sign character','adjacent':True,'constructs_missing_arrow':False,'interfaces_typed':False,'reopens':False},
 {'name':'another even coefficient vector','adjacent':True,'constructs_missing_arrow':False,'interfaces_typed':True,'reopens':False},
 {'name':'labelled Rees generator with verified connecting image','adjacent':True,'constructs_missing_arrow':True,'interfaces_typed':True,'reopens':True},
 {'name':'complete primitive G-to-R chain','adjacent':True,'constructs_missing_arrow':True,'interfaces_typed':True,'reopens':True},
]
assert all(c['reopens']==(c['constructs_missing_arrow'] and c['interfaces_typed']) for c in cases)
out={'schema':'marici.benincasa.cosmology-source-envelope-delta-reopening-gate.v1','problem':'distinguish a substantive source-envelope enlargement from an adjacent artifact','bold_conjecture':'any new adjacent artifact reopens the primitive-lift programme','rivals':['proximity gate','typed missing-arrow gate','complete-chain-only gate'],'risky_consequences':'the proximity gate admits matching characters and coefficient patterns even when no typed arrow composes','strongest_falsification_attempt':cases,'exact_residual':'two adjacent cases construct no missing arrow and therefore leave every obstruction unchanged','conjecture_disposition':'falsified','surviving_scope':'a delta reopens one branch iff it constructs a previously missing typed arrow with matching interfaces; only a complete primitive chain supersedes the fixed-envelope obstruction','missing_arrow_targets':missing,'branch_reopening_is_objective_supersession':False,'complete_chain_required_for_supersession':True,'relevance_by_proximity_rejected':True,'next_conjecture':'the source-labelled generator and connecting image is the first compositional missing arrow and therefore the highest-leverage reopening target','next_falsifier':'construct another missing arrow that composes without the source generator, or show the generator cannot feed the coefficient object','passed':True};(R/'cosmology_source_envelope_delta_reopening_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
