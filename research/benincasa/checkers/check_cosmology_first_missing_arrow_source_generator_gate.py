#!/usr/bin/env python3
"""DPC audit of the first compositional missing arrow."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
def load(n):
 d=json.loads((R/n).read_text());assert d['passed'];return d
rees=load('cosmology_rees_generator_extraction_interface_gate.json');cones=load('cosmology_existing_relative_face_cone_primitive_map_audit.json');cm=load('cosmology_cayley_menger_exceptional_incoming_generator_audit.json');status=load('cosmology_primitive_tau_current_source_envelope_status.json')
assert not rees['interface_checks']['labelled_kernel_or_cokernel_vectors_serialized'];assert not cm['primitive_incoming_generator_found'];assert 'incoming generator' in cones['decision'];assert status['missing_arrows'][0]=='labelled Rees exceptional generator and connecting image'
routes=[
 {'route':'Rees invariant-factor census','source_generator':False,'residual':'ranks retained but transformation vectors discarded'},
 {'route':'relative face cones','source_generator':False,'residual':'conditional unit column and closed cocycle, but no incoming total-chain generator'},
 {'route':'Cayley-Menger/blowup/wall candidates','source_generator':False,'residual':'face leg, missing specialization, or unselected absolute lift'},
]
out={'schema':'marici.benincasa.cosmology-first-missing-arrow-source-generator-gate.v1','problem':'choose the first compositional target for reopening the primitive-lift chain','bold_conjecture':'a source-labelled generator with verified boundary and connecting image is prerequisite to every surviving primitive route','rivals':['begin with downstream pairing and projection','treat the conditional relative cocycle as its own source','infer generators from invariant-factor multiplicity'],'risky_consequences':'a composable bypass from an existing source object into the coefficient complex would refute generator-first ordering','strongest_falsification_attempt':routes,'exact_residual':'all three candidate route families stop before a labelled incoming generator; no bypass reaches the coefficient object','conjecture_disposition':'provisionally retained in the audited envelope','scope':'prerequisite and first dependency, not proof that downstream maps cannot be developed in parallel and not global uniqueness of a Rees construction','highest_leverage_missing_capability':'serialize row/column transformations and labelled kernel or cokernel vectors, then verify boundary and connecting image','next_conjecture':'the existing Rees computation can be upgraded to emit enough transformation data to construct the labelled exceptional generator','next_falsifier':'inspect the engine inputs and outputs; exhibit lost provenance that cannot be reconstructed or serialize a verified generator','passed':True};(R/'cosmology_first_missing_arrow_source_generator_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
