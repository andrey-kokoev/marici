#!/usr/bin/env python3
"""Classify which target-special relation families kill the (10,3) image at (12,4)."""
import argparse,importlib,itertools,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009));a=ap.parse_args();P=a.prime;os.environ.update(MARICI_FIELD_PRIME=str(P),MARICI_AMBIENT='12',MARICI_POINT='2,3,-5');sys.path.insert(0,str(ROOT/'research'/'benincasa'));r=importlib.import_module('check_rank26_total_energy_triple_relation_module');r.charts.GAMMA=-pow(2,-1,P)%P;r.AMBIENT=12;r.charts.K_DEPTH=4;_,tc=r.column_packet();allrows=list(r.raw_relations((3,6,-3),tc));M=lambda d:(d+1)*(d+2)//2;nI=4*2*M(12);nK=4*32*M(8);blocks={'IBP':allrows[:nI],'K':allrows[nI:nI+nK],'q':allrows[nI+nK:]};assert sum(map(len,blocks.values()))==len(allrows)
 r.AMBIENT=10;r.charts.K_DEPTH=3;_,sc=r.column_packet();labels={c:l for l,c in sc.items()};src=json.loads((ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_kd3_a10_p{P}.json').read_text());targets=[{tc[labels[int(c)]]:v for c,v in x['generator_coordinates'].items()} for x in src['candidates']]
 def sub(d,s,k):
  for c,v in s.items():
   z=(d.get(c,0)-k*v)%P
   if z:d[c]=z
   else:d.pop(c,None)
 def test(fams):
  piv={}
  for row in itertools.chain.from_iterable(blocks[x] for x in fams):
   row=dict(row)
   while row and max(row) in piv:sub(row,piv[max(row)],row[max(row)])
   if row:
    p=max(row);iv=pow(row[p],-1,P);piv[p]={c:v*iv%P for c,v in row.items()}
  exact=[]
  for row in targets:
   row=dict(row)
   while row and max(row) in piv:sub(row,piv[max(row)],row[max(row)])
   exact.append(not row)
  return {'families':list(fams),'exact_count':sum(exact),'exact_candidates':[i for i,x in enumerate(exact) if x]}
 tests=[test(x) for x in [('IBP','K'),('IBP','q'),('K','q'),('IBP','K','q')]];assert tests[-1]['exact_count']==9
 out={'schema':'marici.benincasa.cosmology-half-twist-diagonal-family-necessity.v1','prime':P,'source':'(10,3)','target':'(12,4)','family_row_counts':{k:len(v) for k,v in blocks.items()},'tests':tests,'passed':True};path=ROOT/'research'/'benincasa'/'results'/f'cosmology_half_twist_diagonal_family_necessity_p{P}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
