"""Test literal descriptor-coefficient transport of exact rational boundary words."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_boundary_exact_literal_transport.json'
def word(r,shift=0):
 out={}
 for x in r['exact_word']:
  f,k,l,ax,m,e=x['descriptor'];d=(x['kind'],f,k,tuple(l),ax,m,(e[0],e[1]+shift));a=Fraction(x['numerator'],x['denominator']);out[d]=out.get(d,Fraction())+a
 return {k:v for k,v in out.items() if v}
def main():
 packets={A:json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{A}.json').read_text()) for A in (12,14,16)};indexes={A:{(r['k_pole'],*r['exponent']):r for r in p['records']} for A,p in packets.items()};summaries={};failures=[]
 for lo,hi in ((12,14),(14,16),(12,16)):
  s=hi-lo;matched=0;total=0;diff_terms=[]
  for r in packets[lo]['records']:
   kp=r['k_pole'];i,j=r['exponent'];t=indexes[hi][(kp,i,j+s)];a=word(r,s);b=word(t);total+=1
   if a==b:matched+=1
   else:
    n=sum(a.get(k,Fraction())!=b.get(k,Fraction()) for k in set(a)|set(b));diff_terms.append(n);failures.append({'inclusion':f'A{lo}_to_A{hi}','k_pole':kp,'source_exponent':[i,j],'coefficient_difference_terms':n})
  summaries[f'A{lo}_to_A{hi}']={'targets':total,'literal_matches':matched,'failures':total-matched,'difference_terms_min':min(diff_terms) if diff_terms else 0,'difference_terms_max':max(diff_terms) if diff_terms else 0}
 passed=not failures;out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-exact-literal-transport.v1','status':'all_exact_boundary_words_transport_literally' if passed else 'exact_boundary_words_do_not_transport_literally','summaries':summaries,'failure_sample':failures[:12],'decision':'All independently selected exact words are coefficient-identical under typed transport.' if passed else 'Exact target identities exist, but independently selected exact source words are not literal ambient transports; coherence must be tested through their exact syzygy differences.','limitations':['finite ambient degrees 12,14,16','p=32003-selected exact square closures','literal representative comparison only'],'passed':passed};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
