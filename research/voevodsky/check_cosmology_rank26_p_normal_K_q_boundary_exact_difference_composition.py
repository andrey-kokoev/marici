"""Compare direct exact boundary difference cells with transported adjacent composites."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_boundary_exact_difference_composition.json'
def word(r,shift=0):
 out={}
 for x in r['exact_word']:
  f,k,l,ax,m,e=x['descriptor'];d=(x['kind'],f,k,tuple(l),ax,m,(e[0],e[1]+shift));a=Fraction(x['numerator'],x['denominator']);out[d]=out.get(d,Fraction())+a
 return {k:v for k,v in out.items() if v}
def add(a,b,scale=Fraction(1)):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,Fraction())+scale*v
 return {k:v for k,v in out.items() if v}
def shiftword(a,n):
 return {(kind,f,k,l,ax,m,(e[0],e[1]+n)):v for (kind,f,k,l,ax,m,e),v in a.items()}
def main():
 packets={A:json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{A}.json').read_text()) for A in (12,14,16)};idx={A:{(r['k_pole'],*r['exponent']):r for r in p['records']} for A,p in packets.items()};records=[]
 for r12 in packets[12]['records']:
  kp=r12['k_pole'];i,j=r12['exponent'];r14=idx[14][(kp,i,j+2)];r16=idx[16][(kp,i,j+4)]
  d12_14=add(word(r12,2),word(r14),Fraction(-1));d14_16=add(word(r14,2),word(r16),Fraction(-1));direct=add(word(r12,4),word(r16),Fraction(-1));composite=add(shiftword(d12_14,2),d14_16);difference=add(direct,composite,Fraction(-1));records.append({'k_pole':kp,'source_exponent':[i,j],'direct_terms':len(direct),'composite_terms':len(composite),'coefficient_dictionaries_identical':not difference,'residual_terms':len(difference)})
 matches=sum(r['coefficient_dictionaries_identical'] for r in records);assert matches==len(records)
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-exact-difference-composition.v1','status':'all_exact_boundary_difference_cells_compose_strictly','cells_tested':len(records),'strict_coefficient_matches':matches,'direct_terms_min':min(r['direct_terms'] for r in records),'direct_terms_max':max(r['direct_terms'] for r in records),'composite_terms_min':min(r['composite_terms'] for r in records),'composite_terms_max':max(r['composite_terms'] for r in records),'residual_terms':sum(r['residual_terms'] for r in records),'decision':'For every A12 boundary coordinate, the direct A12-to-A16 exact source-syzygy cell equals the transported A12-to-A14 cell plus the A14-to-A16 cell coefficientwise.','limitations':['finite ambient degrees 12,14,16','coherence of selected exact representatives modulo their exact difference cells','does not establish an unbounded ambient recurrence'],'records':records,'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
