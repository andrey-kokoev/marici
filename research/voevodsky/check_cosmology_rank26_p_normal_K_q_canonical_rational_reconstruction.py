"""Bounded rational reconstruction of canonical q-lift coefficients from two primes."""
from __future__ import annotations
import json,math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_canonical_rational_reconstruction.json';P1=32003;P2=32009;DB=22000;NB=22000
def key(t):return (t['mark'],t['q_pole'],tuple(t['levels']),tuple(t['exponent']))
def reconstruct(a,b):
 candidates=set()
 for d in range(1,DB+1):
  r=a*d%P1
  for n in (r-P1,r,r+P1):
   if abs(n)<=NB and n%P2==b*d%P2:candidates.add(Fraction(n,d))
 return sorted(candidates)
def main():
 x=json.loads((RES/'cosmology_rank26_p_normal_K_q_canonical_signature_a14.json').read_text());y=json.loads((RES/'cosmology_rank26_p_normal_K_q_canonical_signature_p32009_a14.json').read_text());results={}
 for kp in ('k0','k1'):
  a={key(t):t['coefficient'] for t in x['signatures'][kp]['terms']};b={key(t):t['coefficient'] for t in y['signatures'][kp]['terms']};assert set(a)==set(b);terms=[]
  for k in sorted(a):
   c=reconstruct(a[k],b[k]);entry={'descriptor':{'mark':k[0],'q_pole':k[1],'levels':list(k[2]),'exponent':list(k[3])},'candidate_count':len(c),'p32003':a[k],'p32009':b[k]}
   if len(c)==1:
    f=c[0];assert f.numerator*pow(f.denominator,-1,P1)%P1==a[k] and f.numerator*pow(f.denominator,-1,P2)%P2==b[k];entry|={'numerator':f.numerator,'denominator':f.denominator}
   terms.append(entry)
  solved=[t for t in terms if t['candidate_count']==1];results[kp]={'terms':terms,'term_count':len(terms),'uniquely_reconstructed':len(solved),'unreconstructed':len(terms)-len(solved),'max_abs_numerator':max((abs(t['numerator']) for t in solved),default=0),'max_denominator':max((t['denominator'] for t in solved),default=0)}
 all_done=all(v['unreconstructed']==0 for v in results.values())
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-canonical-rational-reconstruction.v1','status':'unique_bounded_rational_lifts_reconstructed' if all_done else 'bounded_rational_reconstruction_incomplete','bounds':{'max_denominator':DB,'max_abs_numerator':NB},'primes':[P1,P2],'results':results,'all_reconstructed':all_done,'decision':'Every coefficient reconstructs.' if all_done else 'The declared uniqueness bound does not reconstruct every canonical coefficient; characteristic-zero promotion is withheld.','limitations':['uniqueness only within declared bounds','two-prime reconstruction','rational coefficients do not by themselves prove a characteristic-zero source identity'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'results':{k:{x:y for x,y in v.items() if x!='terms'} for k,v in results.items()}},indent=2))
if __name__=='__main__':main()
