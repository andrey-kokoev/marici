#!/usr/bin/env python3
"""DPC elimination-DAG prototype for checkpointed provenance replay."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prior=json.loads((R/'cosmology_rees_bounded_prefix_provenance_instrumentation.json').read_text());assert prior['passed']
p=101
def clean(a):return {k:v%p for k,v in a.items() if v%p}
def add_scaled(a,b,c):
 z=dict(a)
 for k,v in b.items():z[k]=(z.get(k,0)+c*v)%p
 return clean(z)
def scale(a,c):return clean({k:c*v for k,v in a.items()})
# Triangular rows force provenance growth; final rows add exact dependencies.
rows=[]
for i in range(8):rows.append({j:1 for j in range(i,8)})
rows += [add_scaled(rows[2],rows[5],3),add_scaled(rows[1],rows[7],7)]
pivots={};nodes=[];checkpoints=[]
for rid,original in enumerate(rows):
 row=clean(original);edges=[]
 while row:
  pivot=max(row)
  if pivot not in pivots:break
  prow,nid=pivots[pivot];c=row[pivot];row=add_scaled(row,prow,-c);edges.append({'pivot_node':nid,'coefficient':c})
 inv=1
 if row:
  pivot=max(row);inv=pow(row[pivot],p-2,p);row=scale(row,inv)
 node={'row_id':rid,'edges':edges,'normalization':inv,'is_null':not bool(row)};nid=len(nodes);nodes.append(node)
 if row:pivots[max(row)]=(row,nid)
 if (rid+1)%4==0:
  state=[(k,sorted(v[0].items()),v[1]) for k,v in sorted(pivots.items())];checkpoints.append({'rows_consumed':rid+1,'pivot_count':len(pivots),'digest':hashlib.sha256(json.dumps(state).encode()).hexdigest()})
def replay(nid,combo=False,override=None,memo=None):
 memo={} if memo is None else memo
 key=(nid,combo,id(override));
 if key in memo:return memo[key]
 n=nodes[nid] if override is None or nid!=override[0] else override[1]
 z={n['row_id']:1} if combo else rows[n['row_id']]
 for edge in n['edges']:
  z=add_scaled(z,replay(edge['pivot_node'],combo,override,memo),-edge['coefficient'])
 z=scale(z,n['normalization']);memo[key]=z;return z
valid=[]
for col,(row,nid) in sorted(pivots.items()):valid.append(replay(nid)==row)
for nid,n in enumerate(nodes):
 if n['is_null']:valid.append(replay(nid)=={})
assert all(valid)
# Corrupt one recorded reduction edge.
target=next(i for i,n in enumerate(nodes) if n['edges']);bad=dict(nodes[target]);bad['edges']=[dict(e) for e in bad['edges']];bad['edges'][0]['coefficient']=(bad['edges'][0]['coefficient']+1)%p
corrupt_residual=add_scaled(replay(target),replay(target,override=(target,bad)),-1);assert corrupt_residual
expanded_entries=sum(len(replay(nid,True)) for row,nid in pivots.values());edge_count=sum(len(n['edges']) for n in nodes)
out={'schema':'marici.benincasa.cosmology-rees-checkpointed-provenance-replay.v1','problem':'avoid simultaneous expansion of every source-combination vector while retaining replayable provenance','bold_conjecture':'an acyclic elimination log plus pivot checkpoints replays certificates and exposes corruption with compact retained dependencies','rivals':['expanded provenance vectors','rank-only checkpoints','operation log without replay digests'],'risky_consequences':'all pivots and null rows must replay, checkpoint digests must be stable, and changing one edge coefficient must give a nonzero residual','strongest_falsification_attempt':{'prime':p,'input_rows':len(rows),'pivot_count':len(pivots),'null_count':sum(n['is_null'] for n in nodes),'dag_nodes':len(nodes),'reduction_edges':edge_count,'expanded_pivot_provenance_entries':expanded_entries,'checkpoints':checkpoints,'valid_replays':all(valid),'corrupt_residual_nnz':len(corrupt_residual)},'exact_residual':'valid replay residuals vanish and the corrupted edge leaves a nonzero residual','conjecture_disposition':'retained for the bounded DAG prototype','simultaneous_expanded_provenance_required':False,'storage_boundary':'DAG storage scales with recorded reduction operations; this prototype does not bound full-operation growth','integral_generator_constructed':False,'next_conjecture':'stable DAG certificates can be matched across primes to reconstruct one integral labelled candidate','next_falsifier':'compare normalized supports and rational reconstruction across at least two good primes, with a deliberately incompatible prime certificate','passed':True};(R/'cosmology_rees_checkpointed_provenance_replay.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
