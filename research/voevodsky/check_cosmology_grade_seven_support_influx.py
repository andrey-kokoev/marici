"""Classify the sixty new relation-grade-seven descriptors in grade-eight support."""
import json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_cross_grade_support_replacement as r
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_grade_seven_support_influx.json'
def main():
 raw=json.loads((RES/'cosmology_raw_q_collapse_certificates.json').read_text());sp=json.loads((RES/'cosmology_sparse_raw_q_certificates.json').read_text());u7,d7=r.support(raw['groups'][0],sp['groups'][0]);u8,d8=r.support(raw['groups'][1],sp['groups'][1]);shifted=set()
 for k in u7:
  d=list(d7[k]);d[3]=list(d[3]);d[4]=list(d[4]);d[2]+=1;shifted.add(r.key(d))
 new=u8-shifted;ds=[d8[k] for k in new];assert len(ds)==60 and all(d[2]+sum(d[3])+1==7 for d in ds);qo=Counter(d[2] for d in ds);mi=Counter(tuple(d[3]) for d in ds);ep=Counter(tuple(d[4]) for d in ds);out={'schema':'marici.voevodsky.cosmology-grade-seven-support-influx.v1','status':'new_support_family_classified','count':60,'q_order_census':dict(sorted(qo.items())),'multiindex_family_census':{str(k):v for k,v in sorted(mi.items())},'exact_exponent_pair_count':len(ep),'most_common_exponent_pairs':[{'pair':list(k),'count':v} for k,v in ep.most_common(12)],'decision':'The new relation-grade-seven support is decomposed into exact q-order, multiindex, and exponent-pair families.','claim_boundary':'Descriptor census does not establish why these rows enter the sparse certificate basis.','next_gate':'test-influx-family-necessity-across-all-collapse-relations','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
