#!/usr/bin/env python3
"""Evaluate current Aspect Rees outputs against the agreed production acceptance contract."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];C=json.loads((ROOT/'research/benincasa/contracts/sparse-provenance-reducer.v1.json').read_text());A=ROOT/'research/aspect/results';dual=json.loads((A/'rank26_candidate_dual_cross_prime.json').read_text());red=json.loads((A/'sparse_provenance_reducer.json').read_text());target=8
checks={'replay_infrastructure_passed':red['passed'],'candidate_count_agrees_with_length_one_census':dual['candidate_count']==target,'production_extraction_completed':red['production_rank26_extraction_completed'],'all_contract_required_fields_emitted':False}
assert C['acceptance'][2]=='candidate count agrees with the Rees length-one census'
assert checks['replay_infrastructure_passed'] and not checks['candidate_count_agrees_with_length_one_census']
out={'schema':'marici.benincasa.cosmology-rees-production-contract-acceptance.v1','target_count':target,'current_dual_candidate_count':dual['candidate_count'],'deficit':target-dual['candidate_count'],'checks':checks,'contract_accepted':False,'exact_blocker':'the current seven-candidate dual selector cannot biject to eight length-one invariant factors, and the production three-layer selector has not run','handoff_event':10797,'independent_next_test':'classify the cyclic symmetry/orbit content of the seven candidates to constrain the missing eighth generator','passed':True};(ROOT/'research/benincasa/results/cosmology_rees_production_contract_acceptance.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
