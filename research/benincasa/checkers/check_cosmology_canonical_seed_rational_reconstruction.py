#!/usr/bin/env python3
"""Two-prime CRT and unique-height rational reconstruction of canonical seed coefficients."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research'/'voevodsky'/'results';R=ROOT/'research'/'benincasa'/'results';p,q=32003,32009;M=p*q;B=math.isqrt(M//2)
a=json.loads((V/'cosmology_rank26_p_normal_K_q_canonical_signature_a12.json').read_text());b=json.loads((V/'cosmology_rank26_p_normal_K_q_canonical_signature_p32009_a12.json').read_text())
def key(t):return (t['mark'],t['q_pole'],tuple(t['levels']),tuple(t['exponent']))
def crt(x,y):return (x+p*(((y-x)*pow(p,-1,q))%q))%M
def rr(x):
 r0,r1=M,x;t0,t1=0,1
 while abs(r1)>B:
  z=r0//r1;r0,r1=r1,r0-z*r1;t0,t1=t1,t0-z*t1
 if t1==0:return None
 n,d=r1,t1
 if d<0:n,d=-n,-d
 g=math.gcd(n,d);n//=g;d//=g
 if abs(n)>B or d>B or (n-x*d)%M:return None
 return n,d
results={};all_terms=[]
for pole in ('k0','k1'):
 A={key(t):t['coefficient'] for t in a['signatures'][pole]['terms']};C={key(t):t['coefficient'] for t in b['signatures'][pole]['terms']};assert A.keys()==C.keys();terms=[]
 for k in sorted(A,key=repr):
  x=crt(A[k],C[k]);z=rr(x);terms.append({'descriptor':[k[0],k[1],list(k[2]),list(k[3])],'residues':[A[k],C[k]],'crt':x,'rational':list(z) if z else None,'replays_both':bool(z and z[0]*pow(z[1],-1,p)%p==A[k] and z[0]*pow(z[1],-1,q)%q==C[k])})
 results[pole]={'term_count':len(terms),'reconstructed_count':sum(t['rational'] is not None for t in terms),'terms':terms};all_terms+=terms
out={'schema':'marici.benincasa.cosmology-canonical-seed-rational-reconstruction.v1','primes':[p,q],'modulus':M,'preregistered_unique_height_bound':B,'uniqueness_condition':'abs(numerator),denominator <= floor(sqrt(M/2)); denominator positive','results':results,'all_18_reconstructed':len(all_terms)==18 and all(t['rational'] for t in all_terms),'all_replay_both_primes':all(t['replays_both'] for t in all_terms),'unreconstructed_count':sum(t['rational'] is None for t in all_terms),'characteristic_zero_relation_replayed':False,'passed':all(t['rational'] is not None for t in all_terms)};(R/'cosmology_canonical_seed_rational_reconstruction.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'bound':B,'rationals':[t['rational'] for t in all_terms],'passed':out['passed']},indent=2))
