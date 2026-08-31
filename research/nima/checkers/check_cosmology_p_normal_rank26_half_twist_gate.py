"""Audit the physical half-twist p-normal Rees and resolved syzygy results."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]/'results';OUT=R/'cosmology_p_normal_rank26_half_twist_gate.json'
def load(n):return json.loads((R/n).read_text())
def main():
 census=[load(f'cosmology_p_normal_rank26_rees_census_half_{n}_p{p}.json') for n in ('x','y') for p in (32003,32009)];degrees=(8,10,12,14,16);syz=[load(f'cosmology_p_normal_rank26_syzygy_bockstein_half_a{a}_p{p}.json') for a in degrees for p in (32003,32009)]
 for q in census:assert q['passed'] and q['gamma_mode']=='half' and q['support_excess']==14 and q['elementary_length_census']=={'length_1':8,'length_2':6,'length_at_least_3':0}
 expected={8:8,10:7,12:11,14:14,16:18}
 for q in syz:
  rank=expected[q['ambient']];assert q['passed'] and q['gamma_mode']=='half' and all(q['directions'][d]['bockstein_image_rank']==rank for d in ('nx','ny','tangent')) and q['combined_image_ranks']['all']==rank and q['normal_images_equal'] and q['tangent_image_contained_in_normal_image']
 packet={'schema':'marici.cosmology-p-normal-rank26-half-twist-gate.v1','status':'physical_half_twist_images_through_degree16_equal_p_tangent','point':[3,6,-3],'primes':[32003,32009],'ambient_degrees':list(degrees),'physical_gamma':'-1/2','support_excess':14,'elementary_length_census':{'length_1':8,'length_2':6,'length_at_least_3':0},'resolved_syzygy_image_ranks':expected,'p_normal_image_mod_tangent_ranks':{str(a):0 for a in degrees},'generic_gamma5_prior_results_are_not_physical_half_twist':True,'generic_gamma5_comparison':{'support_excess':13,'length_1':7,'resolved_image_rank':7},'physical_extra_length_one_direction':1,'physical_extra_direction_survives_mod_p_tangent':False,'all_tested_half_twist_images_equal_p_tangent':True,'tau_p_map_constructed':False,'physical_period_constructed':False,'interpretation':'the physical coefficient changes the finite Rees census, so generic-gamma results cannot certify the physical target; after correct half-twist recomputation every resolved image through degree sixteen is exactly p-tangent','next_gate':'further finite cutoffs cannot prove the unbounded statement; a source-level factorization identity or new comparison morphism is required','passed':True}
 OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet,indent=2))
if __name__=='__main__':main()
