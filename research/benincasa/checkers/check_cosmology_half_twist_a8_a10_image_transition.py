#!/usr/bin/env python3
"""Construct the finite image-space transition from embedded a8 generators to the a10 basis."""
import argparse,importlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009));a=ap.parse_args();P=a.prime;os.environ['MARICI_FIELD_PRIME']=str(P);os.environ['MARICI_AMBIENT']='8';os.environ['MARICI_POINT']='2,3,-5';sys.path.insert(0,str(ROOT/'research'/'benincasa'));rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');rees.charts.GAMMA=-pow(2,-1,P)%P
 _,c8=rees.column_packet();l8={c:l for l,c in c8.items()};p8=json.loads((ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_p{P}.json').read_text());rees.AMBIENT=10;_,cols=rees.column_packet();p10=json.loads((ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_a10_p{P}.json').read_text());special=list(rees.raw_relations((3,6,-3),cols))
 def add(dst,src,k):
  for c,v in src.items():
   z=(dst.get(c,0)-k*v)%P
   if z:dst[c]=z
   else:dst.pop(c,None)
 def reduce(row,piv):
  row=dict(row)
  while row and max(row) in piv:add(row,piv[max(row)],row[max(row)])
  return row
 def insert(row,piv):
  row=reduce(row,piv)
  if not row:return False
  p=max(row);iv=pow(row[p],-1,P);piv[p]={c:v*iv%P for c,v in row.items()};return True
 base={}
 for r in special:insert(r,base)
 span=dict(base);embedded=[]
 for x in p8['candidates']:
  row={cols[l8[int(c)]]:v for c,v in x['generator_coordinates'].items()};alive=insert(row,span);embedded.append({'a8_candidate':x['candidate'],'nonzero_mod_a10_special':alive})
 assert sum(x['nonzero_mod_a10_special'] for x in embedded)==3
 complement=[]
 for x in p10['candidates']:
  row={int(c):v for c,v in x['generator_coordinates'].items()}
  if insert(row,span):complement.append(x['candidate'])
 assert len(span)-len(base)==7 and len(complement)==4
 out={'schema':'marici.benincasa.cosmology-half-twist-a8-a10-image-transition.v1','prime':P,'embedded_a8_status':embedded,'embedded_survivor_indices':[x['a8_candidate'] for x in embedded if x['nonzero_mod_a10_special']],'a10_candidate_count':7,'greedy_a10_complement_indices':complement,'embedded_image_rank':3,'complement_rank':4,'combined_rank':7,'full_a10_image_recovered':True,'ordinal_scope':'candidate indices are local to their source/input digest and greedy order','tau_p_map_constructed':False,'physical_period_constructed':False,'passed':True};path=ROOT/'research'/'benincasa'/'results'/f'cosmology_half_twist_a8_a10_image_transition_p{P}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
