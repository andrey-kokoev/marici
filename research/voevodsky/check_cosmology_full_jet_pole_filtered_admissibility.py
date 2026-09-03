"""Check all exact positive-jet words against the algebraic pole filtration."""
from __future__ import annotations
import json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_source_word_axis_square_transport as tr
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_full_jet_pole_filtered_admissibility.json'
def grade(d):
 if d[0] in ('IBP','K'):return d[1]+sum(d[2])+1
 if d[0]=='q':return d[2]+sum(d[3])+1
 raise AssertionError(d)
def main():
 ibp,K,q=tr.descs(12);alls=ibp+K+q;decode={'T':alls,'S_K':K,'Q':q};target={};source_records=[]
 for family,name in [('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')]:
  for r in json.loads((RES/name).read_text())['records']:
   c=r['source_certificate'];target[c['canonical_target_id']]=(family,tr.target_desc(family,r));terms=[]
   for t in c['sparse_word']:
    kind,index=c['source_basis'][t['basis_index']];terms.append({'kind':kind,'row_index':index})
   source_records.append((1,'nx',family,c['canonical_target_id'],terms))
 # t1 is a same-grade T generator for each seed.
 for tid,(family,d) in target.items():source_records.append((1,'t1',family,tid,[{'kind':'T','row_index':alls.index(d)}]))
 for file,label in [('cosmology_second_direction_local_exact_words.json','t2'),('cosmology_second_direction_exact_certificate_words.json','t2')]:
  for r in json.loads((RES/file).read_text())['records']:source_records.append((1,label,r['family'],r['target_id'],r['word_terms']))
 for r in json.loads((RES/'cosmology_second_jet_exact_certificate_words.json').read_text())['records']:source_records.append((2,r['component'],r['family'],r['target_id'],r['word_terms']))
 higher=json.loads((RES/'cosmology_higher_jet_exact_membership.json').read_text());
 for r in json.loads((RES/'cosmology_higher_jet_exact_certificate_words.json').read_text())['records']:source_records.append((r['order'],str(r['basis_index']),r['family'],r['target_id'],r['word_terms']))
 census=Counter();excess=Counter();examples=[]
 for order,component,family,tid,terms in source_records:
  tg=grade(target[tid][1]);mg=max((grade(decode[t['kind']][t['row_index']]) for t in terms),default=tg);bad=max(0,mg-tg);census[f'{order}:{family}:{"violation" if bad else "admissible"}']+=1
  if bad:
   excess[(order,bad)]+=1
   if len(examples)<40:examples.append({'order':order,'component':component,'family':family,'target_id':tid,'target_grade':tg,'primitive_max_grade':mg,'excess':bad,'word_terms':len(terms)})
 # Raw zero targets need no primitive and are filtered-admissible.
 zeros={int(k):v['zero_raw'] for k,v in higher['order_census'].items()}
 for order,n in zeros.items():census[f'{order}:structural_zero:admissible']+=n
 total=sum(census.values());assert total==101592
 violations=sum(excess.values())
 out={'schema':'marici.voevodsky.cosmology-full-jet-pole-filtered-admissibility.v1','status':('certificate_grade_violations_found' if violations else 'all_positive_jet_words_pole_filtered_exact'),'jet_seed_components':total,'certificate_or_zero_census':dict(sorted(census.items())),'grade_violations':violations,'excess_census':{f'order_{o}_excess_{e}':n for (o,e),n in sorted(excess.items())},'examples':examples,'decision':('Some chosen exact words use generators above target grade. This proves those certificates are not filtered primitives, not that the target is nonzero in the filtered quotient.' if violations else 'Every exact word lies at or below target grade; the full positive jet is zero in the algebraic pole-filtered quotient.'),'claim_boundary':'The pole filtration is not DNC-derived. A certificate violation requires full F_g-image membership testing before claiming a filtered obstruction.','next_gate':('compute-full-filtered-image-membership-for-grade-violations' if violations else 'classify-pole-filtered-full-jet-zero-theorem'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
