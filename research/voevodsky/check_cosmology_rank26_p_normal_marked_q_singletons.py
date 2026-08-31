"""Audit singleton-column form of active marked-q p-normal derivative rows."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_marked_q_singletons.json'
def profile(rows):
 active=[r for r in rows[4704:] if r]; assert len(active)==10080 and all(len(r)==1 for r in active)
 columns=[next(iter(r)) for r in active]; coefficients=[next(iter(r.values())) for r in active]
 return {'rows':25200,'active_rows':len(active),'singleton_rows':len(active),'distinct_singleton_columns':len(set(columns)),'column_multiplicity_min':min(columns.count(c) for c in set(columns)),'column_multiplicity_max':max(columns.count(c) for c in set(columns)),'coefficient_values':sorted(set(coefficients)),'column_set':set(columns)}
def main():
 assert rees.AMBIENT==14
 prior=json.loads((RES/'cosmology_rank26_p_normal_marked_q_support.json').read_text()); rowwise=json.loads((RES/'cosmology_rank26_p_normal_degree14_rowwise_two_prime.json').read_text()); assert prior['passed'] and rowwise['passed']
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); dirs={k:tuple(v) for k,v in {'nx':protocol['integral_unit_normals']['nx'],'ny':protocol['integral_unit_normals']['ny'],'p_tangent':protocol['integral_unit_normals']['p_tangent_difference']}.items()}
 _,columns=rees.column_packet(); profiles={}
 for name,direction in dirs.items():
  rows,_=adapter.derivative_rows(columns,point,direction)
  if name=='p_tangent':
   active=[r for r in rows[4704:] if r]; assert len(active)==20160 and all(len(r)==1 for r in active)
   cols={next(iter(r)) for r in active}; profiles[name]={'rows':25200,'active_rows':len(active),'singleton_rows':len(active),'distinct_singleton_columns':len(cols),'column_set':cols}
  else: profiles[name]=profile(rows)
 nx=profiles['nx']['column_set']; ny=profiles['ny']['column_set']; tt=profiles['p_tangent']['column_set']
 intersection=len(nx&ny); union=len(nx|ny)
 assert (len(nx),len(ny),intersection,union,len(tt))==(7560,7560,5670,9450,9450)
 assert nx|ny==tt
 for x in profiles.values(): x.pop('column_set')
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-marked-q-singletons.v1','status':'active_marked_q_derivatives_are_primitive_singleton_columns','field':rees.base.PRIME,'ambient_relation_degree':14,'profiles':profiles,'column_set_relations':{'nx_distinct_columns':7560,'ny_distinct_columns':7560,'nx_ny_intersection':intersection,'nx_ny_union':union,'tangent_columns_equal_union_of_nx_ny':True},'two_prime_absorption_import':{'every_nx_singleton_reduces_to_zero_mod_S_plus_T':True,'every_ny_singleton_reduces_to_zero_mod_S_plus_T':True,'evidence':'degree14 rowwise two-prime certificate'},'decision':'For marked-q relations the p-normal derivative is not a complicated combination: each active row is a unit singleton basis column. The fixed S+T span therefore contains every such active labelled column individually over both tested primes.','limitations':['singleton shape checked over F_32003; integral unit derivative formulas make support characteristic-independent away from sign','does not retain S+T expansion coefficients','does not explain IBP or K families'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
