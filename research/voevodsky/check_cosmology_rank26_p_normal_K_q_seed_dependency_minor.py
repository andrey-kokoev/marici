"""Materialize bounded source dependency closures for canonical q-seed identities."""
from __future__ import annotations
import json,sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
import check_cosmology_rank26_p_normal_K_q_boundary_correction_source_words as words
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_seed_dependency_minor.json'
def add(d,k,v):dag.add_value(d,k,v)
def main():
 assert rees.AMBIENT==14 and base.PRIME==32003
 sig=json.loads((RES/'cosmology_rank26_p_normal_K_q_canonical_signature_a14.json').read_text());protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);nI=4*len(base.monomials_at_most(14));nK=64*len(base.monomials_at_most(10));SK=special[nI:nI+nK];qrows=special[nI+nK:];qd=words.qdesc();qkey={d:i for i,d in enumerate(qd)};Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for exp in base.monomials_at_most(10):Kdesc.append((kp,levels,exp))
 levels=(1,1,2,1,1);results={}
 for kp in (0,1):
  selected=[]
  for term in sig['signatures'][f'k{kp}']['terms']:selected.append(qkey[(term['mark'],term['q_pole'],tuple(term['levels']),tuple(term['exponent']))])
  pivots={};nodes={};creation=[]
  for i,row in enumerate(T):dag.add_pivot(row,pivots,nodes,creation,('T',i))
  for i,row in enumerate(SK):dag.add_pivot(row,pivots,nodes,creation,('S_K',i))
  for qi in selected:dag.add_pivot(qrows[qi],pivots,nodes,creation,('Q',qi))
  target=dx[nI+Kdesc.index((kp,levels,(0,0)))];res,tr=dag.trace(target,pivots);assert not res;pending={}
  for p,a in tr:add(pending,p,a)
  source={};active_nodes=0;edges=0;maxdepth=0
  for p in reversed(creation):
   a=pending.pop(p,0)
   if not a:continue
   node=nodes[p];active_nodes+=1;maxdepth=max(maxdepth,node['depth']);add(source,tuple(node['origin']),a*node['raw_coefficient'])
   for q,b in node['dependencies']:add(pending,q,a*b);edges+=1
  assert not pending;recon={};cols=set(target)
  for (kind,index),a in source.items():
   row=T[index] if kind=='T' else SK[index] if kind=='S_K' else qrows[index];cols.update(row)
   for c,v in row.items():add(recon,c,a*v)
  assert recon==target
  results[f'k{kp}']={'selected_q_rows':len(selected),'normalized_trace_length':len(tr),'active_pivot_nodes':active_nodes,'dependency_edges_traversed':edges,'maximum_depth':maxdepth,'source_rows_total':len(source),'T_source_rows':sum(k[0]=='T' for k in source),'S_K_source_rows':sum(k[0]=='S_K' for k in source),'Q_source_rows':sum(k[0]=='Q' for k in source),'retained_columns':len(cols),'source_generators':[{'kind':k[0],'row_index':k[1]} for k in sorted(source)],'retained_column_indices':sorted(cols),'target_row_index':nI+Kdesc.index((kp,levels,(0,0))),'reconstruction_verified':True}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-seed-dependency-minor.v1','status':'canonical_seed_dependency_minors_materialized','field':base.PRIME,'ambient_relation_degree':14,'results':results,'decision':'The active source closures provide bounded candidate minors for exact rational elimination.','limitations':['minor selected by one modular pivot order','integer/rational matrix not yet rebuilt','single prime closure census'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
