"""Three-prime bounded rational reconstruction for canonical q-lift coefficients."""
from __future__ import annotations
import json,math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_canonical_three_prime_reconstruction.json';PS=(32003,32009,32027);B=4_000_000
def key(t):return (t['mark'],t['q_pole'],tuple(t['levels']),tuple(t['exponent']))
def crt(vals):
 M=math.prod(PS);x=0
 for a,p in zip(vals,PS):m=M//p;x=(x+a*m*pow(m,-1,p))%M
 return x,M
def reconstruct(vals):
 R,M=crt(vals);c=set()
 for d in range(1,B+1):
  r=R*d%M;n=r if r<=M//2 else r-M
  if abs(n)<=B:c.add(Fraction(n,d))
 return sorted(c)
def packet(p):
 path=RES/f'cosmology_rank26_p_normal_K_q_canonical_signature_p{p}_a14.json'
 if p==32003 and not path.exists():path=RES/'cosmology_rank26_p_normal_K_q_canonical_signature_a14.json'
 return json.loads(path.read_text())
def main():
 packets={p:packet(p) for p in PS};results={}
 for kp in ('k0','k1'):
  maps={p:{key(t):t['coefficient'] for t in packets[p]['signatures'][kp]['terms']} for p in PS};assert len({frozenset(m) for m in maps.values()})==1;terms=[]
  for k in sorted(maps[PS[0]]):
   vals=[maps[p][k] for p in PS];c=reconstruct(vals);entry={'descriptor':{'mark':k[0],'q_pole':k[1],'levels':list(k[2]),'exponent':list(k[3])},'candidate_count':len(c),'residues':dict(zip(map(str,PS),vals))}
   if len(c)==1:
    f=c[0];assert all(f.numerator*pow(f.denominator,-1,p)%p==a for p,a in zip(PS,vals));entry|={'numerator':f.numerator,'denominator':f.denominator}
   terms.append(entry)
  solved=[t for t in terms if t['candidate_count']==1];results[kp]={'term_count':len(terms),'uniquely_reconstructed':len(solved),'unreconstructed':len(terms)-len(solved),'max_abs_numerator':max((abs(t['numerator']) for t in solved),default=0),'max_denominator':max((t['denominator'] for t in solved),default=0),'terms':terms}
 all_done=all(v['unreconstructed']==0 for v in results.values())
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-canonical-three-prime-reconstruction.v1','status':'all_canonical_coefficients_uniquely_reconstructed' if all_done else 'three_prime_reconstruction_incomplete','primes':list(PS),'bounds':{'max_abs_numerator':B,'max_denominator':B},'results':results,'all_reconstructed':all_done,'decision':'All coefficients reconstruct.' if all_done else 'Some coefficients have no rational lift inside the maximal symmetric uniqueness bound; characteristic-zero promotion remains withheld.','limitations':['three finite primes','bounded uniqueness','reconstructed coefficients still require direct characteristic-zero identity verification'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'results':{k:{x:y for x,y in v.items() if x!='terms'} for k,v in results.items()}},indent=2))
if __name__=='__main__':main()
