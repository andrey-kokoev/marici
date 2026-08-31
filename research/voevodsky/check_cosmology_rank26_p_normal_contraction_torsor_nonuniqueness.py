"""Materialize nonunique affine families of exact contractions from overlap syzygies."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_contraction_torsor_nonuniqueness.json'
def word(r,axis):
 out={}
 for x in r['exact_word']:
  f,k,l,ax,m,e=x['descriptor'];q=list(e);q[axis]+=2;d=(x['kind'],f,k,tuple(l),ax,m,tuple(q));a=Fraction(x['numerator'],x['denominator']);out[d]=out.get(d,Fraction())+a
 return {k:v for k,v in out.items() if v}
def add(a,b,scale=Fraction(1)):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,Fraction())+scale*v
 return {k:v for k,v in out.items() if v}
def main():
 syz=json.loads((RES/'cosmology_rank26_p_normal_two_monomial_overlap_syzygies.json').read_text());assert syz['passed'];summaries={};total=0
 for lo,hi in ((12,14),(14,16),(16,18)):
  low=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{lo}.json').read_text());li={(r['k_pole'],*r['exponent']):r for r in low['records']};high=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{hi}.json').read_text());cells=[]
  for h in high['records']:
   kp=h['k_pole'];i,j=h['exponent']
   if i<2 or j<2:continue
   wx=word(li[(kp,i-2,j)],0);wy=word(li[(kp,i,j-2)],1);c=add(wx,wy,-1);assert c
   variants=[add(wx,c,Fraction(n)) for n in (0,1,2)];assert len({tuple(sorted(v.items(),key=repr)) for v in variants})==3;cells.append(len(c))
  total+=len(cells);summaries[f'A{lo}_to_A{hi}']={'overlap_targets':len(cells),'nonzero_syzygy_actions':len(cells),'three_distinct_affine_contractions_each':len(cells),'syzygy_terms_min':min(cells),'syzygy_terms_max':max(cells)}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-contraction-torsor-nonuniqueness.v1','status':'exact_contraction_torsor_is_nontrivial','overlap_targets':total,'summaries':summaries,'decision':'Every overlap target admits a nonzero exact syzygy action and therefore at least three explicitly distinct rational contraction words with the same target. Exact source data without an additional normalization does not select a unique contraction.','limitations':['nonuniqueness does not prove that no externally supplied natural normalization can exist','finite degrees A12 through A18','uses previously verified exact-zero overlap syzygies'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
