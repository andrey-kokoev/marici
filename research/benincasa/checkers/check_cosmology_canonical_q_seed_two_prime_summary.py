#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research'/'benincasa'/'results';V=ROOT/'research'/'voevodsky'/'results'
def load(p,A):return json.loads(((B/f'cosmology_canonical_q_seed_signature_a{A}_p{p}.json') if p==32009 else (V/f'cosmology_rank26_p_normal_K_q_canonical_signature_a{A}.json')).read_text())
def desc(x):return [(t['mark'],t['q_pole'],tuple(t['levels']),tuple(t['exponent'])) for t in x['terms']]
pack={(p,A):load(p,A) for p in (32003,32009) for A in (12,14,16)};checks={}
for k,n in (('k0',7),('k1',11)):
 byp={}
 for p in (32003,32009):
  sig=[pack[p,A]['signatures'][k] for A in (12,14,16)];assert all(x['q_rows']==n for x in sig);assert all(x['terms']==sig[0]['terms'] for x in sig);byp[str(p)]={'row_count':n,'ambient_stable_digest':sig[0]['descriptor_coefficient_sha256']}
 assert desc(pack[32003,12]['signatures'][k])==desc(pack[32009,12]['signatures'][k]);checks[k]={'by_prime':byp,'descriptor_support_identical_across_primes':True,'coefficients_identical_across_primes':False}
out={'schema':'marici.benincasa.cosmology-canonical-q-seed-two-prime-summary.v1','primes':[32003,32009],'ambient_degrees':[12,14,16],'checks':checks,'ambient_compatibility_at_each_prime':True,'descriptor_support_two_prime_stable':True,'characteristic_zero_coefficients_reconstructed':False,'source_natural_uniqueness_verified':False,'boundary_operator_constructed':False,'interpretation':'both primes independently give ambient-constant 7-row and 11-row seeds on identical typed descriptor support; coefficient residues are prime-specific and have not been reconstructed over Q','passed':True};(B/'cosmology_canonical_q_seed_two_prime_summary.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
