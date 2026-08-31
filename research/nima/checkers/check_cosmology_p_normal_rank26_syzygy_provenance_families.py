"""Classify replayable syzygy dependencies by source relation family."""
import json
from collections import Counter
from pathlib import Path
R=Path(__file__).resolve().parents[1]/'results';OUT=R/'cosmology_p_normal_rank26_syzygy_provenance_families.json'
Q_NAMES=('g1','g2','g3','g23','g31')
def load(p):return json.loads((R/p).read_text())
def family(i):
 if i<180:return 'IBP'
 if i<1140:return 'K_multiplication'
 return 'q_'+Q_NAMES[(i-1140)//1728]+'_multiplication'
def main():
 tables={}
 for p in (32003,32009):
  d=load(f'cosmology_p_normal_rank26_syzygy_provenance_full_a8_p{p}.json');rows=[]
  for c in d['candidates']:
   counts=Counter(family(int(i)) for i in c['source_coefficients']);rows.append({'candidate':c['candidate'],'family_counts':dict(sorted(counts.items())),'uses_all_five_marked_q_families':all(counts['q_'+q+'_multiplication'] for q in Q_NAMES),'uses_no_q_multiplication_family':not any(k.startswith('q_') for k in counts)})
  tables[str(p)]=rows
 assert tables['32003']==tables['32009']
 packet={'schema':'marici.cosmology-p-normal-rank26-syzygy-provenance-families.v1','status':'seven_provenance_candidates_classified_full_five_mark_interface_not_three_wall_cone','source_id_ranges':{'IBP':[0,179],'K_multiplication':[180,1139],'q_family_block_size':1728,'q_family_order':list(Q_NAMES)},'candidates':tables['32003'],'cross_prime_family_support_identical':True,'bulk_only_candidates':[x['candidate'] for x in tables['32003'] if x['uses_no_q_multiplication_family']],'all_five_q_family_candidates':[x['candidate'] for x in tables['32003'] if x['uses_all_five_marked_q_families']],'target_interface':'ordered principal three-wall cone (g1,g2,g3) with exceptional sigma123','comparison_to_target_constructed':False,'interpretation':'the replayable source dependencies are now localized by generator family, but they live in the complete five-mark Laurent presentation; candidates 0,1 use only IBP/K families and candidates 2-6 use all five marked q families, so no candidate is already a sourced principal-three-wall cone cell','tau_p_map_constructed':False,'physical_period_constructed':False,'next_gate':'construct and verify a source map from the complete five-mark provenance packet to the ordered principal-three-wall relative cone, including treatment of g23 and g31 contributions','passed':True}
 OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet,indent=2))
if __name__=='__main__':main()
