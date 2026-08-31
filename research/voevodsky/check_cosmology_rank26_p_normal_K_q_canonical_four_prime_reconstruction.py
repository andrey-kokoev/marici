"""Standard rational reconstruction of canonical q-lift coefficients from four primes."""
from __future__ import annotations
import json,math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_canonical_four_prime_reconstruction.json';PS=(32003,32009,32027,32029)
def key(t):return (t['mark'],t['q_pole'],tuple(t['levels']),tuple(t['exponent']))
def packet(p):
 path=RES/f'cosmology_rank26_p_normal_K_q_canonical_signature_p{p}_a14.json'
 if p==32003 and not path.exists():path=RES/'cosmology_rank26_p_normal_K_q_canonical_signature_a14.json'
 return json.loads(path.read_text())
def crt(vals):
 M=math.prod(PS);x=0
 for a,p in zip(vals,PS):m=M//p;x=(x+a*m*pow(m,-1,p))%M
 return x,M
def reconstruct(vals):
 x,m=crt(vals);bound=math.isqrt(m//2);r0,r1=m,x;t0,t1=0,1
 while r1>bound:
  q=r0//r1;r0,r1=r1,r0-q*r1;t0,t1=t1,t0-q*t1
 n,d=r1,t1
 if d<0:n,d=-n,-d
 if d and abs(n)<=bound and d<=bound and math.gcd(n,d)==1 and (x*d-n)%m==0:return Fraction(n,d),bound,m
 return None,bound,m
def main():
 packets={p:packet(p) for p in PS};results={}
 for kp in ('k0','k1'):
  maps={p:{key(t):t['coefficient'] for t in packets[p]['signatures'][kp]['terms']} for p in PS};assert len({frozenset(m) for m in maps.values()})==1;terms=[]
  for k in sorted(maps[PS[0]]):
   vals=[maps[p][k] for p in PS];f,bound,modulus=reconstruct(vals);entry={'descriptor':{'mark':k[0],'q_pole':k[1],'levels':list(k[2]),'exponent':list(k[3])},'residues':dict(zip(map(str,PS),vals)),'reconstructed':f is not None}
   if f is not None:
    assert all(f.numerator*pow(f.denominator,-1,p)%p==a for p,a in zip(PS,vals));entry|={'numerator':f.numerator,'denominator':f.denominator}
   terms.append(entry)
  solved=[t for t in terms if t['reconstructed']];results[kp]={'term_count':len(terms),'reconstructed':len(solved),'unreconstructed':len(terms)-len(solved),'max_abs_numerator':max((abs(t['numerator']) for t in solved),default=0),'max_denominator':max((t['denominator'] for t in solved),default=0),'terms':terms}
 all_done=all(v['unreconstructed']==0 for v in results.values())
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-canonical-four-prime-reconstruction.v1','status':'all_canonical_coefficients_rationally_reconstructed' if all_done else 'four_prime_reconstruction_incomplete','primes':list(PS),'modulus_product':math.prod(PS),'symmetric_uniqueness_bound':math.isqrt(math.prod(PS)//2),'results':results,'all_reconstructed':all_done,'decision':'All coefficients reconstruct.' if all_done else 'At least one coefficient has no standard rational reconstruction inside the four-prime uniqueness bound; direct characteristic-zero verification is required.','limitations':['four finite primes','rational reconstruction is not direct characteristic-zero row verification','pivot-selected representative'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'results':{k:{x:y for x,y in v.items() if x!='terms'} for k,v in results.items()}},indent=2))
if __name__=='__main__':main()
