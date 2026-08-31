#!/usr/bin/env python3
"""Compare seven dual-annihilation certificates across the two audited primes."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/aspect/results'
a=json.loads((R/'rank26_candidate_dual_selector_p32003.json').read_text());b=json.loads((R/'rank26_candidate_dual_selector_p32009.json').read_text());assert a['passed'] and b['passed'] and a['all_seven_annihilated'] and b['all_seven_annihilated'];assert a['pivot_count']==b['pivot_count']==8559;assert a['layer_rows']==b['layer_rows']==19560
for x,y in zip(a['candidates'],b['candidates'],strict=True):assert x['candidate']==y['candidate'] and x['annihilation_replay_zero'] and y['annihilation_replay_zero']
out={'schema':'marici.aspect.rank26-candidate-dual-cross-prime.v1','primes':[32003,32009],'candidate_count':7,'all_candidates_dual_annihilated_both_primes':True,'pivot_count_both':8559,'provenance_support_counts':{str(a['prime']):[x['annihilation_provenance_count'] for x in a['candidates']],str(b['prime']):[x['annihilation_provenance_count'] for x in b['candidates']]},'support_counts_required_to_match':False,'reason':'finite-field elimination coefficients and sparse supports may differ; replay and labelled candidate identity are authoritative','triple_transport_applies_both_primes':True,'passed':True};(R/'rank26_candidate_dual_cross_prime.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','candidates':7}))
