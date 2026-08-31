"""Back-substitute lower-edge boundary correction cells to original T and S_K rows."""
from __future__ import annotations
import hashlib,json,sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
RES=ROOT/'research'/'voevodsky'/'results';A=rees.AMBIENT;OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_boundary_direct_correction_words_A12_to_A16.json'
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
 assert A==16 and base.PRIME==32003
 sp=json.loads((RES/'cosmology_rank26_p_normal_K_q_boundary_signatures_a12.json').read_text());tp=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_signatures_a{A}.json').read_text());tl={(r['k_pole'],*r['exponent']):r for r in tp['records']}
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));tangent,_=adapter.derivative_rows(columns,point,td);nI=4*count(A);nK=64*count(A-4);SK=special[nI:nI+nK];qrows=special[nI+nK:];qd=qdesc();qkey={d:i for i,d in enumerate(qd)}
 pivots={};nodes={};creation=[]
 for i,row in enumerate(tangent):dag.add_pivot(row,pivots,nodes,creation,('T',i))
 for i,row in enumerate(SK):dag.add_pivot(row,pivots,nodes,creation,('S_K',i))
 records=[]
 for s in sp['records']:
  kp=s['k_pole'];i,j=s['exponent'];t=tl[(kp,i,j+4)];row={}
  for term in s['terms']:
   qi=qkey[(term['mark'],term['q_pole'],tuple(term['levels']),(term['exponent'][0],term['exponent'][1]+4))]
   for c,v in qrows[qi].items():add(row,c,term['coefficient']*v)
  for term in t['terms']:
   qi=qkey[(term['mark'],term['q_pole'],tuple(term['levels']),tuple(term['exponent']))]
   for c,v in qrows[qi].items():add(row,c,-term['coefficient']*v)
  coeff,trace=expand(row,pivots,nodes,creation);reconstructed={}
  for (kind,index),a in coeff.items():
   srcrow=tangent[index] if kind=='T' else SK[index]
   for c,v in srcrow.items():add(reconstructed,c,a*v)
  assert reconstructed==row;records.append({'k_pole':kp,'source_coordinate':[i,j],'target_coordinate':[i,j+4],'trace':trace,'source_rows':len(coeff),'T_rows':sum(k[0]=='T' for k in coeff),'S_K_rows':sum(k[0]=='S_K' for k in coeff),'coefficients':[{'kind':k[0],'row_index':k[1],'coefficient':a} for k,a in sorted(coeff.items())]})

 out={'schema':'marici.benincasa.cosmology-boundary-direct-correction-all.v1','field':base.PRIME,'from_ambient':12,'to_ambient':16,'record_count':len(records),'records':records,'all_reconstructed':True,'passed':True};OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_boundary_direct_correction_all.json';OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'record_count':len(records),'profiles':sorted(set((x['k_pole'],x['source_rows'],x['T_rows'],x['S_K_rows'],x['trace']) for x in records)),'passed':True},indent=2))

if __name__=='__main__':main()
