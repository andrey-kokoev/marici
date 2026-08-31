#!/usr/bin/env python3
"""Map physical K_DEPTH=2 candidates into the isolated K_DEPTH=3 special quotient."""
import argparse,importlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009));a=ap.parse_args();P=a.prime;os.environ['MARICI_FIELD_PRIME']=str(P);os.environ['MARICI_AMBIENT']='8';os.environ['MARICI_POINT']='2,3,-5';sys.path.insert(0,str(ROOT/'research'/'benincasa'));rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');rees.charts.GAMMA=-pow(2,-1,P)%P;rees.charts.K_DEPTH=2;_,oldcols=rees.column_packet();oldlabels={c:l for l,c in oldcols.items()};old=json.loads((ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_p{P}.json').read_text());rees.charts.K_DEPTH=3;_,cols=rees.column_packet();target=json.loads((ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_kd3_a8_p{P}.json').read_text());rows=list(rees.raw_relations((3,6,-3),cols))
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
 piv={}
 for r in rows:insert(r,piv)
 records=[];span=dict(piv)
 for x in old['candidates']:
  mapped={cols[oldlabels[int(c)]]:v for c,v in x['generator_coordinates'].items()};res=reduce(mapped,piv);independent=insert(mapped,span);records.append({'candidate':x['candidate'],'old_K_pole':x['pivot_label'][0],'residual_support':len(res),'survives_K_DEPTH3_special_quotient':bool(res),'independent_in_embedded_old_image':independent})
 embedded_rank=len(span)-len(piv);complement=[]
 for x in target['candidates']:
  if insert({int(c):v for c,v in x['generator_coordinates'].items()},span):complement.append(x['candidate'])
 out={'schema':'marici.benincasa.cosmology-half-twist-k-depth2-to3-map.v1','prime':P,'ambient':8,'source_K_DEPTH':2,'target_K_DEPTH':3,'source_candidate_count':8,'target_candidate_count':13,'records':records,'old_survivor_count':sum(r['survives_K_DEPTH3_special_quotient'] for r in records),'embedded_old_image_rank':embedded_rank,'target_complement_indices':complement,'target_complement_rank':len(complement),'full_target_image_rank':len(span)-len(piv),'old_K2_survivor_count':sum(r['survives_K_DEPTH3_special_quotient'] for r in records if r['old_K_pole']==2),'old_K1_survivor_count':sum(r['survives_K_DEPTH3_special_quotient'] for r in records if r['old_K_pole']==1),'geometric_persistence_constructed':False,'passed':True};path=ROOT/'research'/'benincasa'/'results'/f'cosmology_half_twist_k_depth2_to3_map_p{P}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
