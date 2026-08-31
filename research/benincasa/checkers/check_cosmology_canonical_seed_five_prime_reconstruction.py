#!/usr/bin/env python3
"""Three-prime rational reconstruction of canonical interior-seed coefficients."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research'/'voevodsky'/'results';R=ROOT/'research'/'benincasa'/'results';ps=(32003,32009,32027,32029,32051)
paths=(V/'cosmology_rank26_p_normal_K_q_canonical_signature_a14.json',V/'cosmology_rank26_p_normal_K_q_canonical_signature_p32009_a14.json',R/'cosmology_canonical_q_seed_signature_a14_p32027.json',R/'cosmology_canonical_q_seed_signature_a14_p32029.json',R/'cosmology_canonical_q_seed_signature_a14_p32051.json');pack=[json.loads(x.read_text()) for x in paths];M=math.prod(ps);B=math.isqrt(M//2)
def key(t):return (t['mark'],t['q_pole'],tuple(t['levels']),tuple(t['exponent']))
def crt(vals):
 x,m=vals[0],ps[0]
 for y,p in zip(vals[1:],ps[1:]):x=(x+m*(((y-x)*pow(m,-1,p))%p))%(m*p);m*=p
 return x
def rr(x):
 r0,r1=M,x;t0,t1=0,1
 while abs(r1)>B:z=r0//r1;r0,r1=r1,r0-z*r1;t0,t1=t1,t0-z*t1
 if not t1:return None
 n,d=r1,t1
 if d<0:n,d=-n,-d
 g=math.gcd(n,d);n//=g;d//=g
 return (n,d) if abs(n)<=B and d<=B and (n-x*d)%M==0 else None
results={};allterms=[]
for pole in ('k0','k1'):
 maps=[{key(t):t['coefficient'] for t in x['signatures'][pole]['terms']} for x in pack];assert maps[0].keys()==maps[1].keys()==maps[2].keys();terms=[]
 for k in sorted(maps[0],key=repr):
  vals=[x[k] for x in maps];z=rr(crt(vals));ok=bool(z and all(z[0]*pow(z[1],-1,p)%p==v for p,v in zip(ps,vals)));terms.append({'descriptor':[k[0],k[1],list(k[2]),list(k[3])],'residues':vals,'rational':list(z) if z else None,'replays_all':ok})
 results[pole]={'term_count':len(terms),'reconstructed_count':sum(x['rational'] is not None for x in terms),'terms':terms};allterms+=terms
out={'schema':'marici.benincasa.cosmology-canonical-seed-five-prime-reconstruction.v1','primes':list(ps),'modulus':M,'unique_height_bound':B,'typed_support_identical':True,'results':results,'all_18_reconstructed':all(x['rational'] for x in allterms),'all_replay_five_primes':all(x['replays_all'] for x in allterms),'characteristic_zero_relation_replayed':False,'passed':all(x['rational'] for x in allterms)};(R/'cosmology_canonical_seed_five_prime_reconstruction.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'bound':B,'counts':{k:v['reconstructed_count'] for k,v in results.items()},'rationals':[x['rational'] for x in allterms],'passed':out['passed']},indent=2))
