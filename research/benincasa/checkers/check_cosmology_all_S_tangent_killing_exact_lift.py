#!/usr/bin/env python3
"""Reconstruct an exact rational tangent-killing witness for the all-S column."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky'),str(ROOT/'research'/'benincasa'/'checkers')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_all_S_primitive_column_relation_lift as lift
import check_cosmology_physical_half_twist_seed_exact_rational_minor as exact
import check_cosmology_rank26_p_normal_K_q_exact_base_representative_solves as solver
OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_all_S_tangent_killing_exact_lift.json'
def main():
 protocol=json.loads((ROOT/'research'/'voevodsky'/'results'/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);direction=tuple(protocol['integral_unit_normals']['p_tangent_difference']);origp,origa=base.PRIME,rees.AMBIENT;rees.AMBIENT=6;base.PRIME=32003;_,columns=rees.column_packet();target_index=columns[(0,1,1,1,1,1,(0,0))];seed=lift.census(direction,point,columns,{target_index:1});origins=[]
 for o in seed['sources']:
  key=(o['kind'],o['row_index'])
  if key not in origins:origins.append(key)
 packets={}
 for p in exact.PS:
  base.PRIME=p;special=list(rees.raw_relations(point,columns));derived,_=adapter.derivative_rows(columns,point,direction);packets[p]={'special':special,'derived':derived}
 erows=[exact.exact_row([packets[p][kind][i] for p in exact.PS]) for kind,i in origins];target={target_index:exact.Fraction(1)};cols=sorted(set(target).union(*(r.keys() for r in erows)));coef,rank=solver.solve_rect(erows,target,cols);recon={}
 for a,row in zip(coef,erows):
  for c,v in row.items():solver.addq(recon,c,a*v)
 assert recon==target;base.PRIME,rees.AMBIENT=origp,origa
 sources=[{'kind':k,'row_index':i,'numerator':a.numerator,'denominator':a.denominator} for (k,i),a in zip(origins,coef) if a]
 out={'schema':'marici.benincasa.cosmology-all-S-tangent-killing-exact-lift.v1','field':'Q','ambient_relation_degree':6,'source_selection_prime':32003,'reconstruction_primes':list(exact.PS),'target_column':target_index,'selected_rows':len(origins),'nonzero_exact_sources':len(sources),'equations':len(cols),'rank':rank,'max_denominator':max(s['denominator'] for s in sources),'exact_reconstruction_verified':True,'sources':sources,'decision':'The primitive all-S derivative column is exactly in the special plus p-tangent derived-relation span over Q at ambient degree 6.','limitations':['finite ambient degree','source selection is presentation dependent','does not construct the ordered vertex map'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='sources'},indent=2))
if __name__=='__main__':main()
