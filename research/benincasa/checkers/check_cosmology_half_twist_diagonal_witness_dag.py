#!/usr/bin/env python3
"""Extract an exact elimination DAG for one canonical diagonal-death witness."""
import argparse,hashlib,importlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009));ap.add_argument('--candidate',type=int,default=0);a=ap.parse_args();P=a.prime;os.environ.update(MARICI_FIELD_PRIME=str(P),MARICI_AMBIENT='12',MARICI_POINT='2,3,-5');sys.path.insert(0,str(ROOT/'research'/'benincasa'));r=importlib.import_module('check_rank26_total_energy_triple_relation_module');r.charts.GAMMA=-pow(2,-1,P)%P;r.AMBIENT=12;r.charts.K_DEPTH=4;_,tc=r.column_packet();relations=list(r.raw_relations((3,6,-3),tc));M=lambda d:(d+1)*(d+2)//2;nI=4*2*M(12);nK=4*32*M(8)
 def family(i):return 'IBP' if i<nI else ('K' if i<nI+nK else 'q')
 def sub(d,s,k):
  for c,v in s.items():
   z=(d.get(c,0)-k*v)%P
   if z:d[c]=z
   else:d.pop(c,None)
 piv={};nodes=[]
 for ri,source in enumerate(relations):
  row=dict(source);deps=[]
  while row and max(row) in piv:
   pr,nid=piv[max(row)];k=row[max(row)];sub(row,pr,k);deps.append([nid,k])
  if row:
   p=max(row);iv=pow(row[p],-1,P);row={c:v*iv%P for c,v in row.items()};nid=len(nodes);nodes.append({'relation_index':ri,'family':family(ri),'scale':iv,'deps':deps});piv[p]=(row,nid)
 r.AMBIENT=10;r.charts.K_DEPTH=3;_,sc=r.column_packet();labels={c:l for l,c in sc.items()};src=json.loads((ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_kd3_a10_p{P}.json').read_text())['candidates'][a.candidate];target={tc[labels[int(c)]]:v for c,v in src['generator_coordinates'].items()};row=dict(target);target_deps=[]
 while row and max(row) in piv:
  pr,nid=piv[max(row)];k=row[max(row)];sub(row,pr,k);target_deps.append([nid,k])
 assert not row
 closure=set();stack=[x[0] for x in target_deps]
 while stack:
  n=stack.pop()
  if n in closure:continue
  closure.add(n);stack.extend(x[0] for x in nodes[n]['deps'])
 compact={str(n):nodes[n] for n in sorted(closure)};families={f:sum(nodes[n]['family']==f for n in closure) for f in ('IBP','K','q')};payload={'target_deps':target_deps,'nodes':compact};digest=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 out={'schema':'marici.benincasa.cosmology-half-twist-diagonal-witness-dag.v1','prime':P,'candidate':a.candidate,'source':'(10,3)','target':'(12,4)','target_pivot_label':src['pivot_label'],'relation_count':len(relations),'basis_node_count':len(nodes),'closure_node_count':len(closure),'closure_family_counts':families,'target_reduction_step_count':len(target_deps),'dag_sha256':digest,'replay_contract':'regenerate ordered target raw_relations; each node is scale*(relation_index - sum(dep_coefficient*dep_node)); target=sum(target_dep_coefficient*dep_node)','payload':payload,'exact_zero_replay':True,'passed':True};path=ROOT/'research'/'benincasa'/'results'/f'cosmology_half_twist_diagonal_witness_dag_c{a.candidate}_p{P}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('prime','candidate','closure_node_count','closure_family_counts','target_reduction_step_count','dag_sha256','passed')},indent=2))
if __name__=='__main__':main()
