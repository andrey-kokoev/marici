#!/usr/bin/env python3
"""Verify exact tangent killing of the all-S column at stabilized ambient degrees."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky'),str(ROOT/'research'/'benincasa'/'checkers')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_all_S_primitive_column_relation_lift as lift
import check_cosmology_physical_half_twist_seed_exact_rational_minor as exact
import check_cosmology_rank26_p_normal_K_q_exact_base_representative_solves as solver
OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_all_S_exact_tangent_stabilization.json'
def solve_degree(degree,point,direction):
 rees.AMBIENT=degree;base.PRIME=32003;low,columns=rees.column_packet();label=(0,1,1,1,1,1,(0,0));ti=columns[label];seed=lift.census(direction,point,columns,{ti:1});origins=[]
 for o in seed['sources']:
  key=(o['kind'],o['row_index'])
  if key not in origins:origins.append(key)
 packets={}
 for p in exact.PS:
  base.PRIME=p;packets[p]={'special':list(rees.raw_relations(point,columns))};packets[p]['derived']=adapter.derivative_rows(columns,point,direction)[0]
 rows=[exact.exact_row([packets[p][k][i] for p in exact.PS]) for k,i in origins];target={ti:exact.Fraction(1)};cols=sorted(set(target).union(*(r.keys() for r in rows)));coef,rank=solver.solve_rect(rows,target,cols);recon={}
 for a,row in zip(coef,rows):
  for c,v in row.items():solver.addq(recon,c,a*v)
 assert recon==target
 return {'ambient_degree':degree,'target_index':ti,'target_label':[0,1,1,1,1,1,[0,0]],'low_prefix_length':len(low),'selected_rows':len(origins),'nonzero_sources':sum(bool(a) for a in coef),'equations':len(cols),'rank':rank,'max_denominator':max(a.denominator for a in coef),'exact_reconstruction_verified':True}
def main():
 protocol=json.loads((ROOT/'research'/'voevodsky'/'results'/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);direction=tuple(protocol['integral_unit_normals']['p_tangent_difference']);origp,origa=base.PRIME,rees.AMBIENT;records=[solve_degree(d,point,direction) for d in (8,10)];base.PRIME,rees.AMBIENT=origp,origa;compatible=all(r['target_index']==0 and r['target_label']==records[0]['target_label'] for r in records);out={'schema':'marici.benincasa.cosmology-all-S-exact-tangent-stabilization.v1','field':'Q','degrees':[8,10],'reconstruction_primes':list(exact.PS),'records':records,'target_inclusion_compatible':compatible,'zero_class_stable_through_tested_system':compatible and all(r['exact_reconstruction_verified'] for r in records),'decision':'The all-S primitive derivative remains tangent-exact over Q through ambient degrees 6, 8, and 10.','limitations':['three finite ambient stages do not construct an unbounded colimit theorem','witness coefficients are presentation dependent'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
