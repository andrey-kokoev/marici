"""Back-substitute lower-edge boundary correction cells to original T and S_K rows."""
from __future__ import annotations
import hashlib,json,sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
RES=ROOT/'research'/'voevodsky'/'results';A=rees.AMBIENT;OUT=RES/f'cosmology_rank26_p_normal_K_q_boundary_correction_words_A{A-2}_to_A{A}.json'
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
def expand(row,pivots,nodes,creation):
 residue,tr=dag.trace(row,pivots);assert not residue;pending={}
 for p,a in tr:dag.add_value(pending,p,a)
 source={}
 for p in reversed(creation):
  a=pending.pop(p,0)
  if not a:continue
  node=nodes[p];dag.add_value(source,tuple(node['origin']),a*node['raw_coefficient'])
  for q,b in node['dependencies']:dag.add_value(pending,q,a*b)
 assert not pending;return source,len(tr)
def main():
 assert A in (14,16) and base.PRIME==32003
 sp=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_signatures_a{A-2}.json').read_text());tp=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_signatures_a{A}.json').read_text());tl={(r['k_pole'],*r['exponent']):r for r in tp['records']}
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));tangent,_=adapter.derivative_rows(columns,point,td);nI=4*count(A);nK=64*count(A-4);SK=special[nI:nI+nK];qrows=special[nI+nK:];qd=qdesc();qkey={d:i for i,d in enumerate(qd)}
 pivots={};nodes={};creation=[]
 for i,row in enumerate(tangent):dag.add_pivot(row,pivots,nodes,creation,('T',i))
 for i,row in enumerate(SK):dag.add_pivot(row,pivots,nodes,creation,('S_K',i))
 results={}
 for kp in (0,1):
  s=next(r for r in sp['records'] if r['k_pole']==kp and r['exponent']==[0,A-8]);t=tl[(kp,0,A-6)];row={}
  for term in s['terms']:
   qi=qkey[(term['mark'],term['q_pole'],tuple(term['levels']),(term['exponent'][0],term['exponent'][1]+2))]
   for c,v in qrows[qi].items():add(row,c,term['coefficient']*v)
  for term in t['terms']:
   qi=qkey[(term['mark'],term['q_pole'],tuple(term['levels']),tuple(term['exponent']))]
   for c,v in qrows[qi].items():add(row,c,-term['coefficient']*v)
  coeff,trace=expand(row,pivots,nodes,creation);reconstructed={}
  for (kind,index),a in coeff.items():
   source=tangent[index] if kind=='T' else SK[index]
   for c,v in source.items():add(reconstructed,c,a*v)
  assert reconstructed==row;digest=hashlib.sha256()
  for key,a in sorted(coeff.items()):digest.update(f'{key[0]}:{key[1]}:{a};'.encode())
  results[f'k{kp}']={'source_coordinate':[0,A-8],'target_coordinate':[0,A-6],'normalized_trace_length':trace,'source_rows':len(coeff),'T_rows':sum(k[0]=='T' for k in coeff),'S_K_rows':sum(k[0]=='S_K' for k in coeff),'coefficient_sha256':digest.hexdigest(),'coefficients':[{'kind':k[0],'row_index':k[1],'coefficient':a} for k,a in sorted(coeff.items())],'reconstruction_verified':True}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-correction-source-words.v1','status':'lower_edge_correction_words_reconstructed','from_ambient':A-2,'to_ambient':A,'results':results,'decision':'Representative lower-edge correction cells back-substitute completely to original T and S_K rows.','limitations':['two representatives per inclusion','row-index-dependent digest','single prime','uniform coefficient transport not yet tested'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
