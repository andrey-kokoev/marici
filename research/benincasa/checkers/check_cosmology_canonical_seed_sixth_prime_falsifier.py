#!/usr/bin/env python3
"""Out-of-sample test of five-prime rational candidates at prime 32057."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research'/'benincasa'/'results';p=32057
rat=json.loads((R/'cosmology_canonical_seed_five_prime_reconstruction.json').read_text());obs=json.loads((R/'cosmology_canonical_q_seed_signature_a14_p32057.json').read_text())
def key_term(t):return (t['mark'],t['q_pole'],tuple(t['levels']),tuple(t['exponent']))
def key_desc(d):return (d[0],d[1],tuple(d[2]),tuple(d[3]))
results={};total=0;matches=0
for pole in ('k0','k1'):
 O={key_term(t):t['coefficient'] for t in obs['signatures'][pole]['terms']};rows=[]
 for x in rat['results'][pole]['terms']:
  k=key_desc(x['descriptor']);n,d=x['rational'];pred=n*pow(d,-1,p)%p;ok=pred==O[k];rows.append({'descriptor':x['descriptor'],'rational':[n,d],'predicted':pred,'observed':O[k],'match':ok});total+=1;matches+=ok
 results[pole]={'matches':sum(x['match'] for x in rows),'terms':rows}
out={'schema':'marici.benincasa.cosmology-canonical-seed-sixth-prime-falsifier.v1','training_primes':[32003,32009,32027,32029,32051],'out_of_sample_prime':p,'matches':matches,'term_count':total,'all_match':matches==total,'characteristic_zero_relation_replayed':False,'interpretation':'the complete five-prime rational coefficient vector predicts every independently extracted sixth-prime pivot coefficient; this is out-of-sample modular evidence, not an exact rational relation proof','passed':matches==total};(R/'cosmology_canonical_seed_sixth_prime_falsifier.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('out_of_sample_prime','matches','term_count','all_match','passed')},indent=2))
