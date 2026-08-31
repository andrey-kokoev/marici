"""Test quadratic ambient-index dependence of normalized exact boundary source words."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_boundary_exact_quadratic_ambient_recurrence.json'
def word(r,shift=0):
 out={}
 for x in r['exact_word']:
  f,k,l,ax,m,e=x['descriptor'];d=(x['kind'],f,k,tuple(l),ax,m,(e[0],e[1]+shift));a=Fraction(x['numerator'],x['denominator']);out[d]=out.get(d,Fraction())+a
 return {k:v for k,v in out.items() if v}
def combine(terms):
 out={}
 for scale,w in terms:
  for k,v in w.items():out[k]=out.get(k,Fraction())+scale*v
 return {k:v for k,v in out.items() if v}
def main():
 packets={A:json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{A}.json').read_text()) for A in (12,14,16,18)};idx={A:{(r['k_pole'],*r['exponent']):r for r in p['records']} for A,p in packets.items()};records=[]
 for r12 in packets[12]['records']:
  kp=r12['k_pole'];i,j=r12['exponent'];r14=idx[14][(kp,i,j+2)];r16=idx[16][(kp,i,j+4)];r18=idx[18][(kp,i,j+6)]
  third=combine([(1,word(r12,6)),(-3,word(r14,4)),(3,word(r16,2)),(-1,word(r18))]);records.append({'k_pole':kp,'source_exponent':[i,j],'third_difference_zero':not third,'residual_terms':len(third)})
 matches=sum(r['third_difference_zero'] for r in records);res=[r['residual_terms'] for r in records if r['residual_terms']];passed=matches==len(records)
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-exact-quadratic-ambient-recurrence.v1','status':'quadratic_recurrence_holds' if passed else 'quadratic_recurrence_falsified','cells_tested':len(records),'zero_third_differences':matches,'failures':len(records)-matches,'residual_terms_min':min(res) if res else 0,'residual_terms_max':max(res) if res else 0,'decision':'Normalized exact words have vanishing third ambient finite difference.' if passed else 'Normalized exact words are not quadratic in the even ambient index; no order-at-most-two fitted coefficient recurrence survives all four degrees.','limitations':['selected exact representatives','degrees 12,14,16,18 only','higher-order recurrences are underdetermined','coefficient fitting is not a source-derived theorem'],'records':records,'passed':passed};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
