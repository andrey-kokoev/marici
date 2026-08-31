"""Census full T+S_K+Q dependency closures for every top-three-degree K target."""
from __future__ import annotations
import json,sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
VRES=ROOT/'research'/'voevodsky'/'results';A=rees.AMBIENT;OUT=ROOT/'research'/'benincasa'/'results'/f'cosmology_physical_half_twist_boundary_full_source_closure_census_a{A}.json';charts.GAMMA=-pow(2,-1,base.PRIME)%base.PRIME
def main():
 assert A in (12,14,16) and base.PRIME==32003
 protocol=json.loads((VRES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));SK=special[nI:nI+nK];Q=special[nI+nK:];piv={};nodes={};creation=[]
 for kind,rows in [('T',T),('S_K',SK),('Q',Q)]:
  for i,r in enumerate(rows):dag.add_pivot(r,piv,nodes,creation,(kind,i))
 Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for lev in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for e in base.monomials_at_most(A-4):Kdesc.append((kp,lev,e))
 levels=(1,1,2,1,1);records=[]
 for kp in (0,1):
  for e in [e for e in base.monomials_at_most(A-4) if sum(e)>=A-6]:
   target=dx[nI+Kdesc.index((kp,levels,e))];rem,tr=dag.trace(target,piv);assert not rem;pending={}
   for p,a in tr:dag.add_value(pending,p,a)
   source={};active=edges=depth=0
   for p in reversed(creation):
    a=pending.pop(p,0)
    if not a:continue
    node=nodes[p];active+=1;depth=max(depth,node['depth']);dag.add_value(source,tuple(node['origin']),a*node['raw_coefficient'])
    for q,b in node['dependencies']:dag.add_value(pending,q,a*b);edges+=1
   assert not pending;cols=set(target)
   for kind,i in source:cols.update({'T':T,'S_K':SK,'Q':Q}[kind][i])
   records.append({'k_pole':kp,'exponent':list(e),'source_rows':len(source),'T_rows':sum(k[0]=='T' for k in source),'S_K_rows':sum(k[0]=='S_K' for k in source),'Q_rows':sum(k[0]=='Q' for k in source),'retained_columns':len(cols),'maximum_depth':depth,'edges':edges,'source_generators':[{'kind':k[0],'row_index':k[1]} for k in sorted(source)],'retained_column_indices':sorted(cols)})
 summary={}
 for kp in (0,1):
  rs=[r for r in records if r['k_pole']==kp];m=max(r['source_rows'] for r in rs);summary[f'k{kp}']={'targets':len(rs),'source_rows_min':min(r['source_rows'] for r in rs),'source_rows_max':m,'columns_min':min(r['retained_columns'] for r in rs),'columns_max':max(r['retained_columns'] for r in rs),'q_rows_min':min(r['Q_rows'] for r in rs),'q_rows_max':max(r['Q_rows'] for r in rs),'depth_max':max(r['maximum_depth'] for r in rs),'records':rs,'maximal_records':[r for r in rs if r['source_rows']==m]}
 out={'schema':'marici.benincasa.cosmology-physical-half-twist-boundary-full-source-closure-census.v1','status':'physical_half_twist_all_boundary_full_source_closures_censused','physical_gamma':'-1/2','field':base.PRIME,'ambient_relation_degree':A,'summary':summary,'decision':'Every top-three-degree target has a bounded full-source closure suitable for exact rational solving.','limitations':['p=32003 pivot-selected closures','not exact rational verification'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
