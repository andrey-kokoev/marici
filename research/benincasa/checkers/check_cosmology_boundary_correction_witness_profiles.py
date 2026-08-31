#!/usr/bin/env python3
"""Extract one exact T/S_K witness DAG for a boundary correction cell."""
import hashlib,json,os,sys
from itertools import product
from pathlib import Path
os.environ['MARICI_FIELD_PRIME']='32003';os.environ['MARICI_AMBIENT']='14'
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
V=ROOT/'research'/'voevodsky'/'results';R=ROOT/'research'/'benincasa'/'results';A=rees.AMBIENT
def count(n):return len(base.monomials_at_most(n))
def add(d,k,v):
 v=(d.get(k,0)+v)%base.PRIME
 if v:d[k]=v
 else:d.pop(k,None)
def qdesc():
 out=[]
 for qi,name in enumerate(rees.NAMES):
  for kp in range(charts.K_DEPTH+1):
   for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
    if levels[qi]==charts.Q_DEPTH:continue
    for exp in base.monomials_at_most(A-1):out.append((name,kp,levels,exp))
 return out
def main():
 source=json.loads((V/'cosmology_rank26_p_normal_K_q_boundary_signatures_a12.json').read_text());target=json.loads((V/'cosmology_rank26_p_normal_K_q_boundary_signatures_a14.json').read_text());protocol=json.loads((V/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));tangent,_=adapter.derivative_rows(columns,point,td);nI=4*count(A);nK=64*count(A-4);qrows=special[nI+nK:];descriptors=qdesc();qkey={d:i for i,d in enumerate(descriptors)};basis=tangent+special[nI:nI+nK];families=['T']*len(tangent)+['K']*nK
 def sub(d,s,k):
  for c,v in s.items():add(d,c,-k*v)
 piv={};nodes=[]
 for ri,src in enumerate(basis):
  row=dict(src);deps=[]
  while row and max(row) in piv:
   pr,nid=piv[max(row)];k=row[max(row)];sub(row,pr,k);deps.append([nid,k])
  if row:
   p=max(row);iv=pow(row[p],-1,base.PRIME);row={c:v*iv%base.PRIME for c,v in row.items()};nid=len(nodes);nodes.append({'relation_index':ri,'family':families[ri],'scale':iv,'deps':deps});piv[p]=(row,nid)
 target_lookup={(x['k_pole'],*x['exponent']):x for x in target['records']};profiles=[]
 for idx,s in enumerate(source['records']):
  kp=s['k_pole'];i,j=s['exponent'];t=target_lookup[(kp,i,j+2)];row={}
  for term in s['terms']:
   qi=qkey[(term['mark'],term['q_pole'],tuple(term['levels']),(term['exponent'][0],term['exponent'][1]+2))]
   for c,v in qrows[qi].items():add(row,c,term['coefficient']*v)
  for term in t['terms']:
   qi=qkey[(term['mark'],term['q_pole'],tuple(term['levels']),tuple(term['exponent']))]
   for c,v in qrows[qi].items():add(row,c,-term['coefficient']*v)
  raw_support=len(row);target_deps=[]
  while row and max(row) in piv:
   pr,nid=piv[max(row)];k=row[max(row)];sub(row,pr,k);target_deps.append([nid,k])
  assert not row;closure=set();stack=[x[0] for x in target_deps]
  while stack:
   n=stack.pop()
   if n in closure:continue
   closure.add(n);stack.extend(x[0] for x in nodes[n]['deps'])
  skel={'target_node_ids':[x[0] for x in target_deps],'nodes':{str(n):{'relation_index':nodes[n]['relation_index'],'family':nodes[n]['family'],'deps':[z[0] for z in nodes[n]['deps']]} for n in sorted(closure)}}
  profiles.append({'record':idx,'k_pole':kp,'source_exponent':[i,j],'target_exponent':[i,j+2],'raw_support':raw_support,'closure_nodes':len(closure),'T_nodes':sum(nodes[n]['family']=='T' for n in closure),'K_nodes':sum(nodes[n]['family']=='K' for n in closure),'target_steps':len(target_deps),'skeleton_sha256':hashlib.sha256(json.dumps(skel,sort_keys=True,separators=(',',':')).encode()).hexdigest()})
 out={'schema':'marici.benincasa.cosmology-boundary-correction-witness-profiles.v1','field':base.PRIME,'from_ambient':12,'to_ambient':14,'record_count':len(profiles),'profiles':profiles,'all_exact':True,'passed':True};(R/'cosmology_boundary_correction_witness_profiles.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'record_count':len(profiles),'distinct_profiles':sorted(set((x['closure_nodes'],x['T_nodes'],x['K_nodes'],x['target_steps']) for x in profiles)),'passed':True},indent=2))

if __name__=='__main__':main()
