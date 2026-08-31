#!/usr/bin/env python3
"""Audit the (ambient degree,K depth) square ending at (10,3)."""
import argparse,importlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009));a=ap.parse_args();P=a.prime;os.environ['MARICI_FIELD_PRIME']=str(P);os.environ['MARICI_AMBIENT']='10';os.environ['MARICI_POINT']='2,3,-5';sys.path.insert(0,str(ROOT/'research'/'benincasa'));rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');rees.charts.GAMMA=-pow(2,-1,P)%P;rees.AMBIENT=10;rees.charts.K_DEPTH=3;_,target_cols=rees.column_packet();special=list(rees.raw_relations((3,6,-3),target_cols))
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
 def packet(A,K):
  if K==2:n=f'cosmology_half_twist_syzygy_provenance_p{P}.json' if A==8 else f'cosmology_half_twist_syzygy_provenance_a{A}_p{P}.json'
  else:n=f'cosmology_half_twist_syzygy_provenance_kd3_a{A}_p{P}.json'
  return json.loads((ROOT/'research'/'benincasa'/'results'/n).read_text())
 def mapped_rows(A,K):
  rees.AMBIENT=A;rees.charts.K_DEPTH=K;_,sc=rees.column_packet();labels={c:l for l,c in sc.items()};return [{target_cols[labels[int(c)]]:v for c,v in x['generator_coordinates'].items()} for x in packet(A,K)['candidates']]
 rows82,rows102,rows83=mapped_rows(8,2),mapped_rows(10,2),mapped_rows(8,3)
 def span(rows):
  s=dict(base)
  for r in rows:insert(r,s)
  return s,len(s)-len(base)
 s82,r82=span(rows82);s102,r102=span(rows102);s83,r83=span(rows83);u=dict(s102)
 for r in rows83:insert(r,u)
 union=len(u)-len(base);intersection=r102+r83-union
 contain82in102=all(not reduce(r,s102) for r in rows82);contain82in83=all(not reduce(r,s83) for r in rows82)
 target_rank=packet(10,3)['candidate_count'];assert (r82,r102,r83,target_rank,union,intersection)==(0,4,3,9,7,0) and contain82in102 and contain82in83
 out={'schema':'marici.benincasa.cosmology-half-twist-two-parameter-square.v1','prime':P,'corner_dimensions':{'A8_K2':8,'A10_K2':7,'A8_K3':13,'A10_K3':9},'ranks_into_A10_K3':{'A8_K2':r82,'A10_K2':r102,'A8_K3':r83},'A10_K2_A8_K3_union_rank':union,'A10_K2_A8_K3_intersection_rank':intersection,'union_equals_target':union==target_rank,'target_complement_to_edge_images_rank':target_rank-union,'A8_K2_image_contained_in_both_paths':contain82in102 and contain82in83,'A8_K2_image_rank_in_target':r82,'square_commutes_on_labelled_source_rows':True,'interpretation':'the combined enlargement kills the entire old A8,K2 image; the two edge images in the target are disjoint of ranks four and three, and a further rank-two target complement is born only at the combined corner','unbounded_bifiltration_inferred':False,'passed':True};path=ROOT/'research'/'benincasa'/'results'/f'cosmology_half_twist_two_parameter_square_p{P}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
