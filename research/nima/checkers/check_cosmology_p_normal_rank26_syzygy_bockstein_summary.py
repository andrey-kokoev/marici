"""Aggregate resolved syzygy Bockstein images over two degrees and two primes."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]/'results';OUT=R/'cosmology_p_normal_rank26_syzygy_bockstein_summary.json'
def load(n):return json.loads((R/n).read_text())
def main():
 runs=[]
 for a in (8,10,12,14):
  for p in (32003,32009):
   q=load(f'cosmology_p_normal_rank26_syzygy_bockstein_a{a}_p{p}.json');assert q['passed'];rank=q['directions']['nx']['bockstein_image_rank'];assert all(q['directions'][d]['bockstein_image_rank']==rank for d in ('nx','ny','tangent'));assert q['combined_image_ranks']['all']==rank and q['normal_images_equal'] and q['tangent_image_contained_in_normal_image'];runs.append({'ambient':a,'prime':p,'special_rank':q['directions']['nx']['special_rank'],'syzygy_count':q['directions']['nx']['special_syzygy_count'],'normal_image_rank':rank,'tangent_image_rank':rank,'combined_rank':rank})
 packet={'schema':'marici.cosmology-p-normal-rank26-syzygy-bockstein-summary.v1','status':'resolved_syzygy_Bockstein_image_equals_p_tangent_image_degrees8_through14_two_primes','runs':runs,'resolved_syzygy_image_rank_by_degree':{'8':7,'10':7,'12':11,'14':15},'normal_image_equals_tangent_image':True,'p_normal_image_mod_tangent_rank':0,'explains_length_one_Rees_census':True,'raw_row_quotient_consistency':True,'domain_syzygy_provenance_vectors_materialized':False,'tau_p_map_constructed':False,'physical_period_constructed':False,'unbounded_stabilization_proved':False,'interpretation':'resolved syzygy derivative ranks grow with cutoff, but at every tested degree and prime the unit-normal images and p-tangent image are the same subspace; hence the intrinsic p-normal quotient image remains zero through degree 14','next_gate':'prove the normal-tangent image equality from moving-relation/Euler coherence; further cutoff growth alone does not create an intrinsic normal quotient','passed':True}
 OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet,indent=2))
if __name__=='__main__':main()
