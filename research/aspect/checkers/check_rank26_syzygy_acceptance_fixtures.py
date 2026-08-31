#!/usr/bin/env python3
"""Accept and type the seven two-prime rank-26 syzygy provenance fixtures."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results';A=ROOT/'research/aspect/results'
def load(name):return json.loads((N/name).read_text())
def main():
 summary=load('cosmology_p_normal_rank26_syzygy_provenance_summary.json');families=load('cosmology_p_normal_rank26_syzygy_provenance_families.json');p3=load('cosmology_p_normal_rank26_syzygy_provenance_a8_p32003.json');p9=load('cosmology_p_normal_rank26_syzygy_provenance_a8_p32009.json')
 sidecar_hashes=[]
 for relative,expected in zip(summary['full_sidecars'],summary['full_sidecar_sha256'],strict=True):
  actual=hashlib.sha256((ROOT/relative).read_bytes()).hexdigest();assert actual==expected;sidecar_hashes.append(actual)
 labels3=[c['pivot_label'] for c in p3['candidates']];labels9=[c['pivot_label'] for c in p9['candidates']];counts3=[c['source_coefficient_count'] for c in p3['candidates']];counts9=[c['source_coefficient_count'] for c in p9['candidates']]
 checks={'seven_candidates':summary['candidate_count']==len(labels3)==len(labels9)==7,'same_pivot_labels':labels3==labels9==summary['pivot_labels'],'same_support_counts':counts3==counts9==summary['source_coefficient_counts'],'special_replay_zero':all(c['special_replay_zero'] for c in p3['candidates']+p9['candidates']),'sidecar_digests_match':len(sidecar_hashes)==2,'family_partition_complete':families['bulk_only_candidates']==[0,1] and families['all_five_q_family_candidates']==[2,3,4,5,6]}
 assert all(checks.values());out={'schema':'marici.aspect.rank26-syzygy-acceptance-fixtures.v1','checks':checks,'accepted_candidate_count':7,'source_coefficient_counts':counts3,'pivot_labels':labels3,'principal_three_wall_cone_candidates':[],'interface_obstruction':'candidates 0,1 have no marked-wall q support; candidates 2-6 include g23 and g31 and cannot be projected to (g1,g2,g3) without a sourced comparison','normal_quotient_survivor':False,'tau_p_map_constructed':False,'next_gate':'construct five-mark to principal-three-wall relative-cone comparison or derive p-tangent absorption from replayed family identities','passed':True};A.mkdir(exist_ok=True);(A/'rank26_syzygy_acceptance_fixtures.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','candidates':7,'principal_cone':0}))
if __name__=='__main__':main()
