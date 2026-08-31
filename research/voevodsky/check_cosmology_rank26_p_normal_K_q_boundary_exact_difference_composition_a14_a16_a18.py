"""Compare direct A14-to-A18 exact boundary cells with transported adjacent composites."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_boundary_exact_difference_composition_a14_a16_a18.json'
def word(r,shift=0):
 out={}
 for x in r['exact_word']:
  f,k,l,ax,m,e=x['descriptor'];d=(x['kind'],f,k,tuple(l),ax,m,(e[0],e[1]+shift));a=Fraction(x['numerator'],x['denominator']);out[d]=out.get(d,Fraction())+a
 return {k:v for k,v in out.items() if v}
def add(a,b,scale=Fraction(1)):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,Fraction())+scale*v
 return {k:v for k,v in out.items() if v}
def shiftword(a,n):return {(kind,f,k,l,ax,m,(e[0],e[1]+n)):v for (kind,f,k,l,ax,m,e),v in a.items()}
def main():
 packets={A:json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{A}.json').read_text()) for A in (14,16,18)};idx={A:{(r['k_pole'],*r['exponent']):r for r in p['records']} for A,p in packets.items()};records=[]
 for r14 in packets[14]['records']:
  kp=r14['k_pole'];i,j=r14['exponent'];r16=idx[16][(kp,i,j+2)];r18=idx[18][(kp,i,j+4)];d14_16=add(word(r14,2),word(r16),-1);d16_18=add(word(r16,2),word(r18),-1);direct=add(word(r14,4),word(r18),-1);composite=add(shiftword(d14_16,2),d16_18);residual=add(direct,composite,-1);records.append({'k_pole':kp,'source_exponent':[i,j],'direct_terms':len(direct),'composite_terms':len(composite),'coefficient_dictionaries_identical':not residual,'residual_terms':len(residual)})
 matches=sum(r['coefficient_dictionaries_identical'] for r in records);assert matches==len(records)
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-exact-difference-composition.v1','status':'all_exact_boundary_difference_cells_compose_strictly','ambient_triple':[14,16,18],'cells_tested':len(records),'strict_coefficient_matches':matches,'direct_terms_min':min(r['direct_terms'] for r in records),'direct_terms_max':max(r['direct_terms'] for r in records),'composite_terms_min':min(r['composite_terms'] for r in records),'composite_terms_max':max(r['composite_terms'] for r in records),'residual_terms':sum(r['residual_terms'] for r in records),'decision':'For every A14 boundary coordinate, the direct A14-to-A18 exact source-syzygy cell equals the transported A14-to-A16 cell plus the A16-to-A18 cell coefficientwise.','limitations':['finite ambient degrees 14,16,18','does not establish an unbounded recurrence'],'records':records,'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
