#!/usr/bin/env python3
"""Census sourced relative-chain candidates for the (1,-1) soft-divisor torsor."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3];B=R/'research/benincasa'
move=json.loads((B/'results/moving_wall_leray_base_boundary.json').read_text())
stokes=json.loads((B/'soft-endpoint-stokes-cospan.json').read_text())
variance=json.loads((B/'soft-endpoint-relative-variance.json').read_text())
occ=json.loads((B/'soft-endpoint-physical-occurrence-covector.json').read_text())
soft=json.loads((B/'results/soft_logarithmic_ext_line.json').read_text())
candidates=[
 {'name':'fixed-endpoint moving-wall Leray normalization','module':'base-soft residue module','vector':[int(x) for x in move['residue_vectors_ordered_s3_s2']['entry_304_leray_normalization']],'typed':True},
 {'name':'soft-endpoint Stokes bulk boundary','module':'marked-relative endpoint-port cone','vector':stokes['boundary_map']['column'],'typed':True},
 {'name':'physical positive occurrence selector','module':'deck occurrence module at each port','vector':occ['physical_chain_covector'],'typed':True},
]
target=[1,-1]
for c in candidates:c['matches_vector']=c['vector']==target;c['lands_in_target_module']=c['module']=='base-soft residue module'
checks={
 'target_is_integral_torsor_generator':soft['integral_residue_generator'][:2]==target,
 'moving_wall_wrong_vector':candidates[0]['vector']==[0,-1],
 'stokes_has_target_vector':candidates[1]['matches_vector'],
 'stokes_wrong_module':not candidates[1]['lands_in_target_module'],
 'occurrence_selector_not_boundary_character':candidates[2]['vector']==[1,0],
 'ports_have_different_relative_types':variance['endpoint_types']['xi=-1']['source_normal_order']!=variance['endpoint_types']['xi=+1']['source_normal_order'],
 'no_endpoint_to_endpoint_map':stokes['architecture'].endswith('there is no source boundary map from one endpoint port to the other'),
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.v-alg-relative-chain-census.v1','target':{'module':'ordered base-soft divisor residue lattice','basis':['v=0','v=2'],'vector':target},'candidates':candidates,'result':'No existing source-authorized candidate both has boundary (1,-1) and lands in the base-soft residue module. The Stokes bulk has the right integer vector only in a different marked-relative endpoint-port cone.','type_obstruction':'Equal coordinate vectors in nonidentified lattices do not define a specialization map. The two Stokes ports additionally differ by one marked logarithmic residue degree.','unique_next_constructor':{'name':'endpoint-port-to-base-soft Gysin comparison','domain':'cone(unmarked CM port at xi=+1 direct-sum marked residue-CM port at xi=-1)','codomain':'Div^0({v=0,v=2})','requirements':['respect cone degree shift','commute with residue','send Stokes boundary to (1,-1)','preserve positive-occurrence covectors','derive from source specialization rather than rank matching']},'checks':checks,'passed':True}
d=R/'research/voevodsky/results/valg_relative_chain_candidate_census.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'candidates':len(candidates),'admissible_matches':sum(c['matches_vector'] and c['lands_in_target_module'] for c in candidates),'next':out['unique_next_constructor']['name']}))
