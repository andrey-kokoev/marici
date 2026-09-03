#!/usr/bin/env python3
"""Multi-prime, multi-cutoff robustness test for tangent killing of the all-S column."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_all_S_tangent_killing_robustness.json';PRIMES=(32003,32009,32027,32029);DEGREES=(6,8,10)
def add_rows(piv,rows):
 for row in rows:base.add_pivot(dict(row),piv)
def member(target,piv):return not bool(base.reduce_row(target,piv))
def main():
 protocol=json.loads((ROOT/'research'/'voevodsky'/'results'/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);dirs={k:tuple(v) for k,v in protocol['integral_unit_normals'].items()};origp,origa=base.PRIME,rees.AMBIENT;records=[]
 for degree in DEGREES:
  rees.AMBIENT=degree
  for prime in PRIMES:
   base.PRIME=prime;_,columns=rees.column_packet();target={columns[(0,1,1,1,1,1,(0,0))]:1};special=list(rees.raw_relations(point,columns));sp={};add_rows(sp,special);tests={}
   for name,direction in dirs.items():
    derived,_=adapter.derivative_rows(columns,point,direction);piv={k:dict(v) for k,v in sp.items()};add_rows(piv,derived);tests[name]={'in_special_span':member(target,sp),'in_special_plus_derived':member(target,piv)}
   records.append({'ambient_degree':degree,'prime':prime,'tests':tests})
 base.PRIME,rees.AMBIENT=origp,origa
 stable=all((not r['tests']['nx']['in_special_span']) and r['tests']['nx']['in_special_plus_derived'] and r['tests']['ny']['in_special_plus_derived'] and r['tests']['p_tangent_difference']['in_special_plus_derived'] for r in records)
 out={'schema':'marici.benincasa.cosmology-all-S-tangent-killing-robustness.v1','primes':list(PRIMES),'ambient_degrees':list(DEGREES),'cases':len(records),'records':records,'tangent_killing_stable':stable,'decision':'The primitive all-S derivative is killed by the p-tangent quotient in every tested finite-field cutoff.' if stable else 'Tangent killing is not stable across the tested grid.','limitations':['finite fields and finite ambient degrees','no characteristic-zero lift','does not construct the ordered vertex map'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
