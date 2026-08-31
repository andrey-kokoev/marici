#!/usr/bin/env python3
"""Map the eight physical a8 syzygy candidates into the a10 special quotient with provenance."""
import argparse,importlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009));a=ap.parse_args();P=a.prime;os.environ['MARICI_FIELD_PRIME']=str(P);os.environ['MARICI_AMBIENT']='8';os.environ['MARICI_POINT']='2,3,-5';sys.path.insert(0,str(ROOT/'research'/'benincasa'));rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');rees.charts.GAMMA=-pow(2,-1,P)%P
 _,oldcols=rees.column_packet();oldlabels={c:l for l,c in oldcols.items()};packet=json.loads((ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_p{P}.json').read_text());rees.AMBIENT=10;_,cols=rees.column_packet();rows=list(rees.raw_relations((3,6,-3),cols))
 def add(dst,src,k):
  for c,v in src.items():
   z=(dst.get(c,0)+k*v)%P
   if z:dst[c]=z
   else:dst.pop(c,None)
 def reduce_pair(row,prov,piv):
  row,prov=dict(row),dict(prov)
  while row and max(row) in piv:
   p=max(row);q,qp=piv[p];k=row[p];add(row,q,-k);add(prov,qp,-k)
  return row,prov
 piv={}
 for i,row in enumerate(rows):
  r,pr=reduce_pair(row,{i:1},piv)
  if not r:continue
  p=max(r);iv=pow(r[p],-1,P);piv[p]=({c:v*iv%P for c,v in r.items()},{c:v*iv%P for c,v in pr.items()})
 results=[];side=[]
 for item in packet['candidates']:
  mapped={cols[oldlabels[int(c)]]:v for c,v in item['generator_coordinates'].items()};res,prov=reduce_pair(mapped,{},piv);replay={}
  if not res:
   for i,k in prov.items():add(replay,rows[i],k)
   check=dict(mapped);add(check,replay,1);assert not check
  results.append({'candidate':item['candidate'],'pivot_label_a8':item['pivot_label'],'mapped_support':len(mapped),'a10_special_residual_support':len(res),'becomes_special_exact_at_a10':not res,'a10_special_witness_count':len(prov) if not res else 0})
  if not res:side.append({'candidate':item['candidate'],'source_coefficients':{str(i):k for i,k in sorted(prov.items())}})
 out={'schema':'marici.benincasa.cosmology-half-twist-a8-to-a10-candidate-map.v1','prime':P,'gamma_mod_prime':rees.charts.GAMMA,'a8_candidate_count':8,'a10_special_rank':len(piv),'a10_row_count':len(rows),'candidates':results,'special_exact_candidate_count':sum(x['becomes_special_exact_at_a10'] for x in results),'sidecar_witnesses':side,'all_exact_witnesses_replay_zero':True,'passed':True};path=ROOT/'research'/'benincasa'/'results'/f'cosmology_half_twist_a8_to_a10_candidate_map_p{P}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
