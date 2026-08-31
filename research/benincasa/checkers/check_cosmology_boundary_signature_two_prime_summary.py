#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research'/'benincasa'/'results';V=ROOT/'research'/'voevodsky'/'results';summary={}
def support(r):return [(x['mark'],x['q_pole'],tuple(x['levels']),tuple(x['exponent'])) for x in r['terms']]
for A,n in ((12,48),(14,60),(16,72)):
 a=json.loads((V/f'cosmology_rank26_p_normal_K_q_boundary_signatures_a{A}.json').read_text());b=json.loads((V/f'cosmology_rank26_p_normal_K_q_boundary_signatures_p32009_a{A}.json').read_text());assert len(a['records'])==len(b['records'])==n
 la={(x['k_pole'],tuple(x['exponent'])):x for x in a['records']};lb={(x['k_pole'],tuple(x['exponent'])):x for x in b['records']};assert la.keys()==lb.keys();assert all(support(la[k])==support(lb[k]) for k in la);summary[str(A)]={'records':n,'typed_q_support_identical_across_primes':True,'coefficient_hashes_identical_across_primes':all(la[k]['signature_sha256']==lb[k]['signature_sha256'] for k in la)}
out={'schema':'marici.benincasa.cosmology-boundary-signature-two-prime-summary.v1','primes':[32003,32009],'ambient_degrees':[12,14,16],'summary':summary,'all_typed_supports_identical':True,'correction_composition_at_32009_tested':False,'passed':True};(B/'cosmology_boundary_signature_two_prime_summary.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
