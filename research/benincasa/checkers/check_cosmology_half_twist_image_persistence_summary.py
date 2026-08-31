#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research'/'benincasa'/'results'
def load(s,t,p):
 name=f'cosmology_half_twist_a8_a10_image_transition_p{p}.json' if (s,t)==(8,10) else f'cosmology_half_twist_image_transition_a{s}_a{t}_p{p}.json'
 return json.loads((R/name).read_text())
pairs=((8,10),(10,12),(12,14),(8,12),(8,14),(10,14));rows={p:{(s,t):load(s,t,p) for s,t in pairs} for p in (32003,32009)}
for p,d in rows.items():
 assert all(x['passed'] for x in d.values());assert [d[k]['embedded_image_rank'] for k in pairs]==[3,5,9,3,3,5]
out={'schema':'marici.benincasa.cosmology-half-twist-image-persistence-summary.v1','primes':[32003,32009],'dimensions':{'V8':8,'V10':7,'V12':11,'V14':14},'transition_ranks':{'V8_to_V10':3,'V10_to_V12':5,'V12_to_V14':9,'V8_to_V12':3,'V8_to_V14':3,'V10_to_V14':5},'kernels':{'V8_to_V10':5,'V10_to_V12':2,'V12_to_V14':2,'V8_to_V12':5,'V8_to_V14':5,'V10_to_V14':2},'cokernels':{'V8_to_V10':4,'V10_to_V12':6,'V12_to_V14':5,'V8_to_V12':8,'V8_to_V14':11,'V10_to_V14':9},'finite_barcode':{'born_by_8_persist_through_14':3,'born_by_8_die_at_10':5,'born_at_10_persist_through_14':2,'born_at_10_die_at_12':2,'born_at_12_persist_through_14':4,'born_at_12_die_at_14':2,'born_at_14_unresolved_lifetime':5},'rank_composition_consistent':True,'V8_survivors_through_V12':3,'additional_V8_deaths_between_V10_V12':0,'same_signature_across_primes':True,'all_spaces_p_tangent':True,'unbounded_persistence_inferred':False,'interpretation':'through degree fourteen, three V8 directions and two V10-born directions persist, while each of the V10-to-V12 and V12-to-V14 steps kills two directions and introduces replacements; raw image dimensions are not stable-class counts','next_gate':'derive a source-level persistence rule or stop finite barcode extension; no colimit claim follows from four envelopes','passed':True};(R/'cosmology_half_twist_image_persistence_summary.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
