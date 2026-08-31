#!/usr/bin/env python3
"""Extract an exact elimination DAG for one canonical diagonal-death witness."""
import argparse,hashlib,importlib,itertools,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009));ap.add_argument('--candidate',type=int,default=0);a=ap.parse_args();P=a.prime;os.environ.update(MARICI_FIELD_PRIME=str(P),MARICI_AMBIENT='12',MARICI_POINT='2,3,-5');sys.path.insert(0,str(ROOT/'research'/'benincasa'));r=importlib.import_module('check_rank26_total_energy_triple_relation_module');r.charts.GAMMA=-pow(2,-1,P)%P;r.AMBIENT=12;r.charts.K_DEPTH=4;_,tc=r.column_packet();relations=list(r.raw_relations((3,6,-3),tc));M=lambda d:(d+1)*(d+2)//2;nI=4*2*M(12);nK=4*32*M(8)
 def family(i):return 'IBP' if i<nI else ('K' if i<nI+nK else 'q')
 metadata=[]
 for kp in range(4):
  for axis in range(2):
   for e in r.base.monomials_at_most(12):metadata.append(('IBP',kp,axis,(1,1,1,1,1),e))
 for kp in range(4):
  for lev in itertools.product(range(1,3),repeat=5):
   for e in r.base.monomials_at_most(8):metadata.append(('K',kp,None,lev,e))
 for qi in range(5):
  for kp in range(5):
   for lev in itertools.product(range(1,3),repeat=5):
    if lev[qi]==2:continue
    for e in r.base.monomials_at_most(11):metadata.append(('q',kp,qi,lev,e))
 assert len(metadata)==len(relations)
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
 r.AMBIENT=10;r.charts.K_DEPTH=3;_,sc=r.column_packet();labels={c:l for l,c in sc.items()};sources=json.loads((ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_kd3_a10_p{P}.json').read_text())['candidates'];profiles=[]
 for src in sources:
  target={tc[labels[int(c)]]:v for c,v in src['generator_coordinates'].items()};row=dict(target);target_deps=[]
  while row and max(row) in piv:
   pr,nid=piv[max(row)];k=row[max(row)];sub(row,pr,k);target_deps.append([nid,k])
  assert not row;closure=set();stack=[x[0] for x in target_deps]
  while stack:
   n=stack.pop()
   if n in closure:continue
   closure.add(n);stack.extend(x[0] for x in nodes[n]['deps'])
  skeleton={'target_node_ids':[x[0] for x in target_deps],'nodes':{str(n):{'relation_index':nodes[n]['relation_index'],'family':nodes[n]['family'],'dep_node_ids':[z[0] for z in nodes[n]['deps']]} for n in sorted(closure)}}
  pe=src['pivot_label'][-1];norm=[]
  for n in closure:
   fam,kp,tag,lev,e=metadata[nodes[n]['relation_index']];norm.append((fam,kp,tag,lev,(e[0]-pe[0],e[1]-pe[1])))
  support_hash=hashlib.sha256(json.dumps(sorted(norm,key=repr),separators=(',',':')).encode()).hexdigest()
  profiles.append({'candidate':src['candidate'],'pivot_label':src['pivot_label'],'closure_node_count':len(closure),'closure_family_counts':{f:sum(nodes[n]['family']==f for n in closure) for f in ('IBP','K','q')},'target_reduction_step_count':len(target_deps),'skeleton_sha256':hashlib.sha256(json.dumps(skeleton,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'shift_normalized_relation_support_sha256':support_hash})
 out={'schema':'marici.benincasa.cosmology-half-twist-diagonal-witness-profiles.v1','prime':P,'source':'(10,3)','target':'(12,4)','candidate_count':len(profiles),'profiles':profiles,'all_exact_zero':True,'passed':True};path=ROOT/'research'/'benincasa'/'results'/f'cosmology_half_twist_diagonal_witness_profiles_p{P}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'prime':P,'profiles':profiles,'passed':True},indent=2))

if __name__=='__main__':main()
