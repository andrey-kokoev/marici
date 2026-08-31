"""Falsify the target-typed tangent envelope on six non-quantile singleton strata."""
from __future__ import annotations
import json,sys
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
import check_cosmology_rank26_p_normal_source_template_census as census
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_tangent_envelope_falsifier.json'
def expand(column,pivots,nodes,creation):
 residue,tr=dag.trace({column:1},pivots); assert not residue; pending={}
 for p,a in tr:dag.add_value(pending,p,a)
 source={}
 for p in reversed(creation):
  a=pending.pop(p,0)
  if not a:continue
  node=nodes[p]; dag.add_value(source,tuple(node['origin']),a*node['raw_coefficient'])
  for q,b in node['dependencies']:dag.add_value(pending,q,a*b)
 assert not pending; return source,len(tr)
def main():
 assert rees.AMBIENT==14 and base.PRIME==32003
 prior=json.loads((RES/'cosmology_rank26_p_normal_tangent_envelope.json').read_text()); assert prior['passed']
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); nx=tuple(protocol['integral_unit_normals']['nx']); ny=tuple(protocol['integral_unit_normals']['ny']); t=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet(); ordered=[None]*len(columns)
 for label,column in columns.items():ordered[column]=label
 special=list(rees.raw_relations(point,columns)); dx,_=adapter.derivative_rows(columns,point,nx); dy,_=adapter.derivative_rows(columns,point,ny); tangent,_=adapter.derivative_rows(columns,point,t)
 pivots={};nodes={};creation=[]
 for i,row in enumerate(special):dag.add_pivot(row,pivots,nodes,creation,('S',i))
 for i,row in enumerate(tangent):dag.add_pivot(row,pivots,nodes,creation,('T',i))
 excluded={3420,2962,9560,1279,16699}; singleton={next(iter(r)) for r in dx[4704:] if r}|{next(iter(r)) for r in dy[4704:] if r}
 strata=defaultdict(list)
 for c in sorted(singleton-excluded):
  label=ordered[c]; strata[(label[0],label[1])].append(c)
 selected={f'k{k}_g1_{g}':cols[len(cols)//2] for (k,g),cols in sorted(strata.items())}
 assert set(selected)=={f'k{k}_g1_{g}' for k in (0,1,2) for g in (1,2)}
 desc=census.descriptors(); tests={}; failures=[]
 for stratum,column in selected.items():
  source,trace_len=expand(column,pivots,nodes,creation); assert dag.combine_source(source,special,tangent)=={column:1}
  label=ordered[column]; target_k=label[0]; g1=label[1]; T=[desc[i] for (kind,i),a in source.items() if kind=='T' and a]
  poles=sorted({d['k_pole'] for d in T}); qmarks=sorted({d['mark'] for d in T if d['family']=='q'}); families=sorted({d['family'] for d in T})
  pole_ok=bool(poles) and max(poles)<=target_k; mark_ok=set(qmarks)<={'g1'}; activation_ok=bool(qmarks)==(g1==2)
  if not (pole_ok and mark_ok and activation_ok):failures.append(stratum)
  tests[stratum]={'column':column,'label':{'k_pole':target_k,'g1_level':g1,'q_levels':list(label[1:-1]),'monomial':list(label[-1])},'normalized_trace_length':trace_len,'source_rows':len(source),'T_rows':len(T),'T_families':families,'T_poles':poles,'T_q_marks':qmarks,'pole_rule':pole_ok,'mark_rule':mark_ok,'activation_rule':activation_ok}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-tangent-envelope-falsifier.v1','status':'envelope_survives_six_nonquantile_strata' if not failures else 'envelope_falsified','selection':'median column in each (k_pole,g1_level) stratum after excluding five quantile representatives','tests':tests,'failures':failures,'decision':'The target-typed envelope survives six additional source-expanded singleton columns.' if not failures else 'The tangent-envelope branch is falsified and must be abandoned.','strength':'11 total source-expanded samples if no failures; still finite, single-prime evidence','limitations':['one new column per stratum','single prime','presentation-dependent source expansion','not universal proof'],'passed':not failures}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
