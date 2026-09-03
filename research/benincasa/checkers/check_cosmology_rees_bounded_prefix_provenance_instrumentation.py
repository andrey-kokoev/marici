#!/usr/bin/env python3
"""DPC provenance-growth instrumentation on an actual bounded Rees prefix."""
import importlib,itertools,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
prior=json.loads((R/'cosmology_rees_provenance_memory_scaling_bound.json').read_text());assert prior['passed']
p=101;ambient=4;os.environ.update(MARICI_FIELD_PRIME=str(p),MARICI_AMBIENT=str(ambient),MARICI_POINT='2,3,-5');sys.path.insert(0,str(B))
rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');low,cols=rees.column_packet();rows=list(itertools.islice(rees.raw_relations((3,6,-3),cols),512));limit=len(rows)
def clean(a):return {k:v%p for k,v in a.items() if v%p}
def add_scaled(a,b,c):
 z=dict(a)
 for k,v in b.items():z[k]=(z.get(k,0)+c*v)%p
 return clean(z)
def scale(a,c):return clean({k:c*v for k,v in a.items()})
pivots={};operations=0;metrics=[];marks={64,128,256,512}
for rid,original in enumerate(rows):
 row=clean(original);combo={rid:1}
 while row:
  pivot=max(row)
  if pivot not in pivots:break
  prow,pcombo=pivots[pivot];c=row[pivot];row=add_scaled(row,prow,-c);combo=add_scaled(combo,pcombo,-c);operations+=1
 if row:
  pivot=max(row);inv=pow(row[pivot],p-2,p);pivots[pivot]=(scale(row,inv),scale(combo,inv))
 n=rid+1
 if n in marks or n==limit:
  ps=[len(c) for r,c in pivots.values()];rs=[len(r) for r,c in pivots.values()]
  metrics.append({'prefix_rows':n,'rank':len(pivots),'reduction_operations':operations,'mean_pivot_nnz':sum(rs)/len(rs),'max_pivot_nnz':max(rs),'mean_provenance_nnz':sum(ps)/len(ps),'max_provenance_nnz':max(ps),'provenance_entries':sum(ps)})
assert metrics and all(metrics[i]['prefix_rows']<metrics[i+1]['prefix_rows'] for i in range(len(metrics)-1))
last=metrics[-1]
out={'schema':'marici.benincasa.cosmology-rees-bounded-prefix-provenance-instrumentation.v1','problem':'measure provenance growth on an actual bounded Rees relation prefix','bold_conjecture':'count-only bounded-prefix metrics suffice to establish direct full-presentation feasibility','rivals':['direct all-pivot vectors','checkpointed replay','target-only extraction'],'risky_consequences':'provenance support and operation growth must remain controlled across prefixes, but bounded data must not be extrapolated silently to 9,780 rows','strongest_falsification_attempt':{'prime':p,'ambient':ambient,'column_count':len(cols),'available_relation_rows':'not exhausted; prefix-only iterator','instrumented_prefix_limit':limit,'metrics':metrics},'exact_residual':'bounded metrics are measured, but no theorem extrapolates their density to the full ambient-eight presentation','conjecture_disposition':'falsified as a full-feasibility claim; retained as instrumentation proof','instrumentation_works':True,'full_scale_feasibility_established':False,'last_prefix_provenance_to_dense_ratio':last['provenance_entries']/(last['rank']*last['prefix_rows']),'full_run_launched':False,'next_conjecture':'checkpointed replay can bound retained provenance independently of full coefficient-vector density','next_falsifier':'construct a checkpoint DAG certificate and verify replay while retaining only bounded local combinations','passed':True};(R/'cosmology_rees_bounded_prefix_provenance_instrumentation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
