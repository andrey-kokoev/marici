#!/usr/bin/env python3
"""Compute a labelled physical syzygy-image transition between adjacent envelopes."""
import argparse,importlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009));ap.add_argument('--source',type=int,choices=(8,10,12),default=10);ap.add_argument('--target',type=int,choices=(12,14),default=12);a=ap.parse_args();P=a.prime;os.environ['MARICI_FIELD_PRIME']=str(P);os.environ['MARICI_AMBIENT']=str(a.source);os.environ['MARICI_POINT']='2,3,-5';sys.path.insert(0,str(ROOT/'research'/'benincasa'));rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');rees.charts.GAMMA=-pow(2,-1,P)%P
 _,cold=rees.column_packet();lold={c:l for l,c in cold.items()};pold_path=(ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_p{P}.json') if a.source==8 else (ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_a{a.source}_p{P}.json');pold=json.loads(pold_path.read_text());rees.AMBIENT=a.target;_,cols=rees.column_packet();pnew=json.loads((ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_a{a.target}_p{P}.json').read_text());special=list(rees.raw_relations((3,6,-3),cols))
 def sub(dst,src,k):
  for c,v in src.items():
   z=(dst.get(c,0)-k*v)%P
   if z:dst[c]=z
   else:dst.pop(c,None)
 def reduce(row,piv):
  row=dict(row)
  while row and max(row) in piv:sub(row,piv[max(row)],row[max(row)])
  return row
 def insert(row,piv):
  row=reduce(row,piv)
  if not row:return False
  p=max(row);iv=pow(row[p],-1,P);piv[p]={c:v*iv%P for c,v in row.items()};return True
 base={}
 for r in special:insert(r,base)
 span=dict(base);status=[]
 for x in pold['candidates']:
  row={cols[lold[int(c)]]:v for c,v in x['generator_coordinates'].items()};alive=insert(row,span);status.append({'source_candidate':x['candidate'],'nonzero_mod_target_special_and_prior_embedded':alive})
 embedded_rank=len(span)-len(base);complement=[]
 for x in pnew['candidates']:
  if insert({int(c):v for c,v in x['generator_coordinates'].items()},span):complement.append(x['candidate'])
 target_rank=len(span)-len(base);assert target_rank==pnew['candidate_count'] and embedded_rank+len(complement)==target_rank
 out={'schema':'marici.benincasa.cosmology-half-twist-image-transition.v1','prime':P,'source_ambient':a.source,'target_ambient':a.target,'source_image_rank':pold['candidate_count'],'target_image_rank':pnew['candidate_count'],'embedded_status':status,'embedded_image_rank':embedded_rank,'target_complement_indices':complement,'target_complement_rank':len(complement),'combined_rank':target_rank,'full_target_image_recovered':True,'ordinal_scope':'indices are digest-bound and greedy-order local','tau_p_map_constructed':False,'physical_period_constructed':False,'passed':True};path=ROOT/'research'/'benincasa'/'results'/f'cosmology_half_twist_image_transition_a{a.source}_a{a.target}_p{P}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
