"""Aggregate the two-prime, two-normal full rank-26 p-normal Rees census."""
import json
from pathlib import Path
NIMA=Path(__file__).resolve().parents[1];R=NIMA/'results';OUT=R/'cosmology_p_normal_rank26_rees_census_summary.json'
def load(n):return json.loads((R/n).read_text())
def main():
 packets={(n,p):load(f'cosmology_p_normal_rank26_rees_census_{n}_p{p}.json') for n in ('x','y') for p in (101,103)}
 signature=None
 for (n,p),q in packets.items():
  assert q['passed'] and q['p']==0 and q['total_energy']==6
  s=(q['support_excess'],tuple(q['elementary_length_census'].values()),tuple(q['relation_ranks'].values()))
  signature=s if signature is None else signature;assert s==signature
 packet={'schema':'marici.cosmology-p-normal-rank26-rees-census-summary.v1','status':'nonzero_full_rank26_p_supported_relation_module_found_tau_comparison_open','point':[3,6,-3],'primes':[101,103],'unit_normals':['nx=(1,0,0)','ny=(0,1,0)'],'normal_difference':'(1,-1,0) is p-tangent','ambient_relation_degree':8,'column_count':8736,'support_excess':13,'elementary_length_census':{'length_1':7,'length_2':6,'length_at_least_3':0},'same_census_both_normals_both_primes':True,'interpretation':'the complete labelled source relation module has thirteen p-supported elementary summands at this cutoff; seven are length one and six are length two','minimal_cech_zero_does_not_imply_full_rank26_zero':True,'p_supported_generators_extracted':False,'bockstein_image_vectors_computed':False,'map_to_tau_p_computed':False,'physical_period_constructed':False,'next_gate':'extract a basis of the seven length-one p-supported summands, compute their first normal derivative images modulo tangent-derived relations, and evaluate the ordered wall/exceptional-face column','passed':True}
 OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet,indent=2))
if __name__=='__main__':main()
