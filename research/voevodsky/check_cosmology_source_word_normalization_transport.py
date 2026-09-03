"""Audit normalization and transport interfaces of all exact seed words."""
from __future__ import annotations
import json,math
from pathlib import Path
import cosmology_exact_source_certificate as certificate
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results'
OUT=RES/'cosmology_source_word_normalization_transport.json'
FAMILIES=[('IBP','cosmology_IBP_exact_source_certificates_a12.json',{'T'}),('K','cosmology_nonmarked_K_exact_seeds_a12.json',{'T','S_K'}),('q','cosmology_q_exact_source_certificates_a12.json',{'T','Q'})]
def main():
 ids=set();reports={};total=0;empty=0;transport_records=0
 for family,name,allowed in FAMILIES:
  records=json.loads((RES/name).read_text())['records'];fam_empty=0
  for record in records:
   c=record['source_certificate'];assert c['schema']=='marici.voevodsky.exact-source-certificate.v1'
   assert c['canonical_target_id']=='target:'+certificate.digest(c['descriptor']);assert c['canonical_target_id'] not in ids;ids.add(c['canonical_target_id'])
   assert c['source_basis_digest']==certificate.digest(c['source_basis']);assert len(c['row_digests'])==len(c['source_basis'])
   assert all(origin[0] in allowed and isinstance(origin[1],int) and origin[1]>=0 for origin in c['source_basis'])
   word=c['sparse_word'];indices=[t['basis_index'] for t in word];assert indices==sorted(set(indices));assert all(0<=i<len(c['source_basis']) for i in indices)
   assert all(t['numerator']!=0 and t['denominator']>0 and math.gcd(abs(t['numerator']),t['denominator'])==1 for t in word)
   if not word:fam_empty+=1
   if 'transport' in c:transport_records+=1
  reports[family]={'records':len(records),'empty_words':fam_empty,'allowed_basis_families':sorted(allowed),'normalized':True};total+=len(records);empty+=fam_empty
 assert total==1224 and len(ids)==1224 and transport_records==0
 aggregate=json.loads((RES/'cosmology_full_rank26_characteristic_zero_absorption.json').read_text())
 assert 'square transport' in aggregate['exact_sources']['IBP'] and 'transport components' in aggregate['exact_sources']['K'] and 'naturality' not in aggregate['exact_sources']['q']
 out={'schema':'marici.voevodsky.cosmology-source-word-normalization-transport.v1','status':'all_words_normalized_transport_certificate_interface_absent','reports':reports,'total_certificates':total,'globally_unique_target_ids':len(ids),'empty_exact_words':empty,'normalization_passed':True,'transport_records':transport_records,'transport_audit':'failed_typed_interface_gate','reason':'The aggregate states transport conclusions in prose, but no seed certificate names the x^2/y^2 action on target IDs and ordered source-basis IDs, transported coefficient word, or commutation residual. Equality of parity descriptors and prose naturality cannot verify coefficient-word stability.','retained_claim':'All 1,224 A12 algebraic seed contractions are exact, normalized, and replayable.','withheld_claim':'Their serialized coefficient words are stable under arbitrary-even constructor transport.','next_gate':'serialize-source-word-transport-action','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
