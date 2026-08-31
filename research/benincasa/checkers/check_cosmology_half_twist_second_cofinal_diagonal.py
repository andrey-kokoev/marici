#!/usr/bin/env python3
"""Map the physical image from (A,KD)=(10,3) to (12,4)."""
import argparse,importlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009));a=ap.parse_args();P=a.prime;os.environ['MARICI_FIELD_PRIME']=str(P);os.environ['MARICI_AMBIENT']='12';os.environ['MARICI_POINT']='2,3,-5';sys.path.insert(0,str(ROOT/'research'/'benincasa'));rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');rees.charts.GAMMA=-pow(2,-1,P)%P;rees.AMBIENT=12;rees.charts.K_DEPTH=4;_,tc=rees.column_packet();rows=list(rees.raw_relations((3,6,-3),tc))
 def sub(d,s,k):
  for c,v in s.items():
   z=(d.get(c,0)-k*v)%P
   if z:d[c]=z
   else:d.pop(c,None)
 def red(r,piv):
  r=dict(r)
  while r and max(r) in piv:sub(r,piv[max(r)],r[max(r)])
  return r
 def ins(r,piv):
  r=red(r,piv)
  if not r:return False
  p=max(r);iv=pow(r[p],-1,P);piv[p]={c:v*iv%P for c,v in r.items()};return True
 piv={}
 for r in rows:ins(r,piv)
 source=json.loads((ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_kd3_a10_p{P}.json').read_text());target=json.loads((ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_kd4_a12_p{P}.json').read_text());rees.AMBIENT=10;rees.charts.K_DEPTH=3;_,sc=rees.column_packet();labels={c:l for l,c in sc.items()};span=dict(piv);records=[]
 for x in source['candidates']:
  r={tc[labels[int(c)]]:v for c,v in x['generator_coordinates'].items()};q=red(r,piv);records.append({'candidate':x['candidate'],'pivot_K_pole':x['pivot_label'][0],'target_special_residual_support':len(q),'survives':bool(q),'independent':ins(r,span)})
 rank=len(span)-len(piv);assert rank==0 and not any(x['survives'] for x in records)
 out={'schema':'marici.benincasa.cosmology-half-twist-second-cofinal-diagonal.v1','prime':P,'source_corner':{'ambient':10,'K_DEPTH':3,'image_rank':source['candidate_count']},'target_corner':{'ambient':12,'K_DEPTH':4,'image_rank':target['candidate_count']},'direct_image_rank':rank,'kernel_rank':source['candidate_count']-rank,'all_source_directions_special_exact_at_target':True,'records':records,'two_step_pattern_matches_first_diagonal':True,'unbounded_diagonal_vanishing_inferred':False,'interpretation':'the second cofinal diagonal enlargement kills the complete prior physical image, reproducing the first diagonal death at the next ambient and K-depth pair','next_gate':'extract a uniform labelled homotopy for (A,KD)->(A+2,KD+1); finite repetition alone is not induction','passed':True};path=ROOT/'research'/'benincasa'/'results'/f'cosmology_half_twist_second_cofinal_diagonal_p{P}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'prime':P,'source_rank':source['candidate_count'],'target_rank':target['candidate_count'],'direct_rank':rank,'passed':True},indent=2))
if __name__=='__main__':main()
