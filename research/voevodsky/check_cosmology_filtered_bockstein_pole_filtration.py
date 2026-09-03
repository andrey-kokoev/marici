"""Test whether exact primitives respect the algebraic pole filtration."""
from __future__ import annotations
import json,os,sys
from collections import Counter
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'voevodsky')]
import check_cosmology_source_word_axis_square_transport as tr
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_filtered_bockstein_pole_filtration.json'
def grade(d):
 if d[0] in ('IBP','K'):return d[1]+sum(d[2])+1
 if d[0]=='q':return d[2]+sum(d[3])+1
 raise AssertionError(d)
def main():
 filt=json.loads((RES/'cosmology_pole_order_filtration_candidate.json').read_text());assert filt['filtration_violations']==0
 ibp,K,q=tr.descs(12);all_desc=ibp+K+q;decode={'T':all_desc,'S_K':K,'Q':q};files=[('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')]
 tested=0;structural_zero=0;violations=[];excess=Counter();grade_pairs=Counter()
 for family,name in files:
  for record in json.loads((RES/name).read_text())['records']:
   tested+=1;target=tr.target_desc(family,record);tg=grade(target);cert=record['source_certificate'];used=sorted({t['basis_index'] for t in cert['sparse_word']})
   if not used:structural_zero+=1
   maxg=max((grade(decode[cert['source_basis'][i][0]][cert['source_basis'][i][1]]) for i in used),default=tg);grade_pairs[(tg,maxg)]+=1
   if maxg>tg:
    excess[maxg-tg]+=1
    if len(violations)<20:violations.append({'family':family,'target_id':cert['canonical_target_id'],'target_grade':tg,'primitive_max_grade':maxg,'excess':maxg-tg})
 assert tested==1224
 out={'schema':'marici.voevodsky.cosmology-filtered-bockstein-pole-filtration.v1','status':'filtered_exactness_tested','certificates_tested':tested,'structural_zero_words':structural_zero,'filtration_violations':sum(excess.values()),'excess_census':{str(k):v for k,v in sorted(excess.items())},'grade_pair_census':{f'{a}->{b}':n for (a,b),n in sorted(grade_pairs.items())},'examples':violations,'decision':('The pole filtration exposes a filtered obstruction in exactly the certificates whose primitives require higher grade.' if violations else 'Every certified primitive lies at or below its target grade, so the pole-filtered algebraic Bockstein remains zero.'),'scope':'Algebraic pole filtration only; no DNC, support, exceptional, or physical interpretation.','next_gate':('classify-pole-filtered-obstruction-families' if violations else 'audit-alternative-normal-interface-for-nonzero-class'),'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
