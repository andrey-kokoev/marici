"""Compare bounded rank-26 syzygy provenance receipts across two primes."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]/'results';OUT=R/'cosmology_p_normal_rank26_syzygy_provenance_summary.json'
def load(p):return json.loads((R/p).read_text())
def main():
 a=load('cosmology_p_normal_rank26_syzygy_provenance_a8_p32003.json');b=load('cosmology_p_normal_rank26_syzygy_provenance_a8_p32009.json')
 assert a['passed'] and b['passed'] and a['selected_length_one_image_count']==b['selected_length_one_image_count']==7
 labels_a=[x['pivot_label'] for x in a['candidates']];labels_b=[x['pivot_label'] for x in b['candidates']];counts_a=[x['source_coefficient_count'] for x in a['candidates']];counts_b=[x['source_coefficient_count'] for x in b['candidates']]
 assert labels_a==labels_b and counts_a==counts_b and all(x['special_replay_zero'] for x in a['candidates']+b['candidates'])
 packet={'schema':'marici.cosmology-p-normal-rank26-syzygy-provenance-summary.v1','status':'seven_source_replayable_syzygy_image_candidates_materialized_two_primes','primes':[32003,32009],'ambient':8,'candidate_count':7,'pivot_labels':labels_a,'source_coefficient_counts':counts_a,'same_labelled_pivots_across_primes':True,'same_source_support_counts_across_primes':True,'all_special_dependency_replays_zero':True,'full_sidecars':[a['full_sidecar'],b['full_sidecar']],'full_sidecar_sha256':[a['full_sidecar_sha256'],b['full_sidecar_sha256']],'normal_images_previously_proved_p_tangent':'research/nima/results/cosmology_p_normal_rank26_syzygy_bockstein_summary.json','tau_p_map_constructed':False,'physical_period_constructed':False,'interpretation':'the seven finite-cutoff syzygy images now have bounded source-row provenance and stable labelled pivot identities; this enables a source-family audit of why their entire span is p-tangent, but does not revive a normal quotient','next_gate':'classify the seven source dependencies by relation family and derive the normal-tangent equality from those generator identities','passed':True}
 OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet,indent=2))
if __name__=='__main__':main()
