#!/usr/bin/env python3
"""Hostile tests for the minimal finite G4 target candidate."""
import copy,json
from pathlib import Path
from evidence_policy import write_result
R=Path(__file__).resolve().parents[2]; c=json.loads((R/'research/conjecture_replay/contracts/CR1-minimal-finite-G4-target-candidate.v1.json').read_text())
def accepts(x):
 o=x.get('discrete_order',[]); m=x.get('minimality',{}); t=x.get('module_types',{}); s=x.get('scope',{})
 return (len(o)==13 and len(set(o))==13 and all(f'p{p}_k{k}_{z}' in o for p in (2,3) for k in (1,2) for z in ('forward','reciprocal')) and o[-3:-1]==['link_(p2k1,p3k2)','link_(p3k2,p2k1)'] and bool(s.get('reciprocal_mate_retained')) and 'function-valued' in s.get('finiteness','') and t.get('link_*','').startswith('Lambda^2 E_F function-valued') and m.get('no_dark_summand') is True and m.get('no_undeclared_quotient') is True and m.get('horizontal_equalizer_not_orbit_sum') is True)
assert accepts(c)
def mutate(fn):
 x=copy.deepcopy(c);fn(x);return x
hostiles={
 'dark_summand':mutate(lambda x:(x['discrete_order'].append('dark'),x['minimality'].__setitem__('no_dark_summand',False))),
 'erase_square_grade':mutate(lambda x:x['discrete_order'].remove('p2_k2_forward')),
 'scalarize_linking':mutate(lambda x:x['module_types'].__setitem__('link_*','C')),
 'drop_reciprocal_mate':mutate(lambda x:x['scope'].__setitem__('reciprocal_mate_retained',False)),
 'orbit_sum':mutate(lambda x:x['minimality'].__setitem__('horizontal_equalizer_not_orbit_sum',False)),
 'undeclared_quotient':mutate(lambda x:x['minimality'].__setitem__('no_undeclared_quotient',False)),
 'merge_forward_reciprocal':mutate(lambda x:x['discrete_order'].remove('p3_k1_reciprocal')),
 'duplicate_label_as_fake_dimension':mutate(lambda x:x['discrete_order'].__setitem__(-1,'wall_even'))
}
checks={k:not accepts(v) for k,v in hostiles.items()};assert all(checks.values())
out={'schema':'marici.conjecture-replay.CR1-minimal-G4-target-hostiles.v1','passed':True,'claim_status':'proved','evidence':[{'class':'SYMBOLIC','claim':'Eight deliberate mutations are rejected by the candidate acceptance predicate while the unmodified candidate passes.','checker':'research/conjecture_replay/check_CR1_minimal_G4_target_hostiles.py'}],'outcome':'candidate minimality and typing clauses are discriminating','baseline_accepts':True,'hostile_rejections':checks,'meaning':{'dark_summand':'rejects nonminimal invisible extension','erase_square_grade':'rejects provenance loss','scalarize_linking':'rejects function-valued response collapse','drop_reciprocal_mate':'rejects orientation loss','orbit_sum':'rejects fourfold divisor duplication','undeclared_quotient':'rejects hidden kernel removal','merge_forward_reciprocal':'rejects half-turn collapse','duplicate_label_as_fake_dimension':'rejects coordinate collision'},'scope':'These tests validate the finite candidate specification. They do not prove completion stability, uniqueness outside the declared universal-property category, G4 physics, zero confinement, or RH.','next':'construct_cutoff_bonding_maps_between_candidates_and_test_isometry_label_naturality_and_response_compatibility'}
write_result(R/'research/conjecture_replay/results/CR1_minimal_G4_target_hostiles.json',out);print(json.dumps({'passed':True,'baseline':True,'hostiles_rejected':sum(checks.values())}))
