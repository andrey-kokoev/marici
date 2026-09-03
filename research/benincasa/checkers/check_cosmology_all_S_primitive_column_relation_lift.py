#!/usr/bin/env python3
"""Test the primitive all-S normal column against special and derived relation spans."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky'),str(ROOT/'research'/'benincasa'/'checkers')]
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_all_S_primitive_column_relation_lift.json'
def census(direction,point,columns,target):
 special=list(rees.raw_relations(point,columns));derived,_=adapter.derivative_rows(columns,point,direction);piv={};nodes={};creation=[]
 for i,row in enumerate(special):dag.add_pivot(row,piv,nodes,creation,('special',i))
 try:
  special_rem,_=dag.trace(target,piv);special_in=not bool(special_rem)
 except AssertionError:special_in=False
 for i,row in enumerate(derived):dag.add_pivot(row,piv,nodes,creation,('derived',i))
 rem,trace=dag.trace(target,piv);origins=[]
 if not rem:
  pending={}
  for p,a in trace:dag.add_value(pending,p,a)
  for p in reversed(creation):
   a=pending.pop(p,0)
   if not a:continue
   node=nodes[p];origins.append({'kind':node['origin'][0],'row_index':node['origin'][1],'coefficient':a})
   for q,b in node['dependencies']:dag.add_value(pending,q,a*b)
  assert not pending
 return {'target_in_special_span':special_in,'target_in_span':not bool(rem),'residual_support':len(rem),'source_count':len(origins),'derived_source_count':sum(o['kind']=='derived' for o in origins),'sources':origins}
def main():
 protocol=json.loads((ROOT/'research'/'voevodsky'/'results'/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);_,columns=rees.column_packet();label=(0,1,1,1,1,1,(0,0));target={columns[label]:1};dirs={'nx':tuple(protocol['integral_unit_normals']['nx']),'ny':tuple(protocol['integral_unit_normals']['ny']),'p_tangent':tuple(protocol['integral_unit_normals']['p_tangent_difference'])};tests={k:census(v,point,columns,target) for k,v in dirs.items()};out={'schema':'marici.benincasa.cosmology-all-S-primitive-column-relation-lift.v1','field':rees.base.PRIME,'ambient_relation_degree':rees.AMBIENT,'point':list(point),'target_label':[0,1,1,1,1,1,[0,0]],'tests':tests,'primitive_column_has_normal_relation_lift':tests['nx']['target_in_span'] and tests['ny']['target_in_span'],'primitive_column_killed_by_p_tangent_quotient':tests['p_tangent']['target_in_span'],'normal_choice_agrees_at_span_membership':tests['nx']['target_in_span']==tests['ny']['target_in_span'],'limitations':['finite field','finite ambient degree','span membership does not construct the ordered vertex map or total differential'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'tests':{k:{a:b for a,b in v.items() if a!='sources'} for k,v in tests.items()}},indent=2))
if __name__=='__main__':main()
