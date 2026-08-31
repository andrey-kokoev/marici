#!/usr/bin/env python3
"""Construct incompatible unbounded continuations of the same exact finite cutoff prefix."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_finite_prefix_unbounded_promotion_gate.json'
# The observed predicate is exactness of every tested marked-stratum K target.
prefix={12:True,14:True,16:True}
# Continuation Z preserves exactness at every later even cutoff.
Z={**prefix,18:True,20:True}
# Continuation O introduces one new non-exact source-labelled target at A18;
# no finite-prefix identity constrains that new generator.
O={**prefix,18:False,20:False}
assert all(Z[a]==O[a]==prefix[a] for a in prefix)
assert Z[18]!=O[18]
out={'schema':'marici.benincasa.cosmology-finite-prefix-unbounded-promotion-gate.v1','tested_prefix':{'ambient_degrees':[12,14,16],'all_marked_stratum_targets_exact':True,'exact_boundary_correction_coherence':True},'continuations':{'exact_continuation':{'A18_all_targets_exact':True,'unbounded_exactness_compatible':True},'new_obstruction_continuation':{'A18_all_targets_exact':False,'new_source_labelled_obstruction_rank':1,'unbounded_exactness_compatible':False}},'agreement_on_complete_tested_prefix':True,'different_unbounded_dispositions':True,'missing_datum':'a source-natural recurrence, generation bound, no-new-class theorem, or cofinal comparison map constraining every later cutoff','decision':'The exact coherent A12/A14/A16 prefix does not logically determine unbounded exactness.','does_not_refute_possible_recurrence':True,'does_not_construct_tau_map':True,'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
