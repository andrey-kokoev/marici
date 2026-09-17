#!/usr/bin/env python3
"""Fail-closed first trial of the completed Weil form as a positive pro-Gram shape."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
V=ROOT/'research/voevodsky/results'
def load(n): return json.loads((V/n).read_text())
source=load('compact_weil_source_identity_contract.json')
rung=load('rung4_positive_observation_coherence.json')
uniform=load('uniform_weil_proof_gate_audit.json')
criteria={
 'finite_forms_source_typed':source['matrix_assembly_internally_defined'],
 'external_source_identity_verified':not source['external_source_verification_required'],
 'every_finite_packet_psd':uniform['steps']['8_form_core_passage']['all_L_premise'],
 'refinement_cells_defined':all(x['restriction_coherent'] for x in rung['successor_cells']),
 'faithful_completion_verified':uniform['steps']['8_form_core_passage']['source_identity_audited'],
 'uniform_asymptotic_closure':uniform['steps']['6_asymptotic_threshold_N0']['closed'],
}
# A positive pro-Gram shape requires all six; coherence alone is deliberately insufficient.
admitted=all(criteria.values())
out={'schema':'marici.nima.positive-geometry-shape-trial.v1','candidate':{'objects':'finite source-typed observer packets','shape':'compatible cone-valued Gram forms','faces':'zero-extension/refinement restrictions','completion':'faithful projective graph completion'},'admission_criteria':criteria,'positive_geometry_admitted':admitted,'first_open_gates':[k for k,v in criteria.items() if not v],'hostile_controls':rung['signed_coherence_hostile'],'rh_claimed':False,'passed':True}
p=ROOT/'research/nima/results/positive-geometry-shape-trial.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
