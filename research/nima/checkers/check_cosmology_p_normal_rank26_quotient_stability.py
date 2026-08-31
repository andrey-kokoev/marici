"""Aggregate p-normal raw relation quotient ranks through ambient degree 14."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research'/'nima'/'results';V=ROOT/'research'/'voevodsky'/'results';OUT=N/'cosmology_p_normal_rank26_quotient_stability.json'
def load(p):return json.loads(p.read_text())
def main():
 v=load(V/'cosmology_rank26_p_normal_two_prime_quotient.json');runs=[]
 for prime,s in v['rank_signatures'].items():runs.append((8,int(prime),s))
 for a in (10,12,14):
  for p in (32003,32009):
   q=load(N/f'cosmology_rank26_p_normal_quotient_rank_a{a}_p{p}.json');e=q['extension_ranks'];runs.append((a,p,{'special_exact_image':q['ranks']['special_exact_image'],'special_plus_p_tangent_derivatives':q['ranks']['special_plus_p_tangent_derivatives'],**e}))
 for a,p,s in runs:
  assert s['nx_over_special_plus_p_tangent']==s['ny_over_special_plus_p_tangent']==s['nx_and_ny_over_special_plus_p_tangent']==0
 table=[{'ambient':a,'prime':p,**s} for a,p,s in runs]
 packet={'schema':'marici.cosmology-p-normal-rank26-quotient-stability.v1','status':'raw_normal_derivative_quotient_zero_degrees8_through14_two_primes','point':[3,6,-3],'ambient_degrees':[8,10,12,14],'primes':[32003,32009],'runs':table,'p_tangent_extension_by_degree':{'8':97,'10':101,'12':107,'14':113},'all_unit_normal_extensions_after_tangent':0,'interpretation':'through degree 14, the special exact image plus the p-tangent derived span absorbs all raw nx and ny relation derivatives; the raw-row adapter produces no horn line','relation_to_rees_census':'the rank-13 supported-module census remains real, but its seven length-one summands have not been explicitly extracted; the raw derivative-span test does not furnish their tau comparison','unbounded_stabilization_proved':False,'explicit_length_one_generators_extracted':False,'tau_p_map_constructed':False,'physical_period_constructed':False,'next_gate':'either extract the seven length-one Rees generators explicitly and evaluate their connecting images, or prove from moving-relation/Euler coherence that raw normal absorption persists unboundedly','passed':True}
 OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet,indent=2))
if __name__=='__main__':main()
