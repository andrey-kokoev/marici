#!/usr/bin/env python3
"""Test whether the seven dual candidates carry enough data for cyclic classification."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];A=ROOT/'research/aspect/results'
ds=[json.loads((A/f'rank26_candidate_dual_selector_p{p}.json').read_text()) for p in (32003,32009)]
assert all(len(d['candidates'])==7 for d in ds)
allowed={'candidate','residual_coordinate_count','annihilated','annihilation_provenance_count','annihilation_replay_zero'}
assert all(set(c)==allowed for d in ds for c in d['candidates'])
supports=[[c['annihilation_provenance_count'] for c in d['candidates']] for d in ds];assert supports[0]==supports[1]
out={'schema':'marici.benincasa.cosmology-rees-seven-candidate-cyclic-content-gate.v1','candidate_count':7,'stable_cross_prime_provenance_support_counts':supports[0],'serialized_fields':sorted(allowed),'missing_fields':['source_id coefficients','labelled generator coordinates','cyclic permutation image','normal-image coordinates','p-tangent coordinates'],'cyclic_orbits_classifiable':False,'reason':'candidate ordinals and equal support cardinalities do not define a cyclic action or semantic cross-prime identity','missing_eighth_symmetry_constrained':False,'nonpromotion':'deterministic ordinal agreement is envelope-local and is not a labelled source generator','next_route':'process the Aspect production-selector response; only the contracted labelled output can support orbit classification','passed':True};(ROOT/'research/benincasa/results/cosmology_rees_seven_candidate_cyclic_content_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
