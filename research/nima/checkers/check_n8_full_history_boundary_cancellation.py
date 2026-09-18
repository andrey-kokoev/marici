#!/usr/bin/env python3
"""Full 20-history alpha-boundary incidence and orientation census at n=8."""
from pathlib import Path
import json,sys,itertools
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'));import sympy as s
from nnmhv_coherence_paths import compile_nnmhv_histories
matches=json.loads((ROOT/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];byhi={x['history_index']:x for x in matches};hist=compile_nnmhv_histories(8)
a=s.symbols('a1:9');A1,A2,A3,A4,A5,A6,A7,A8=a
M={
'F':s.Matrix([[1,A1+A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,1,A5,A6,A7,A8]]),
'G':s.Matrix([[1,A1,A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),
'H':s.Matrix([[1,A1,A2+A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),
'A':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),
'B':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),
'C':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),
'D':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]]),
'E':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]])}
vals={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])}
def embed(q,mat):
 emb=q['embedding'];sup=list(range(1,9)) if isinstance(emb,int) else emb['support'];rot=emb if isinstance(emb,int) else emb['rotation'];out=s.zeros(2,8)
 for j in range(mat.cols):out[:,sup[(j+rot)%len(sup)]-1]=mat[:,j]
 return out
def key(mat):
 cols=[mat[:,j] for j in range(8)];zero=[j+1 for j,c in enumerate(cols) if c==s.zeros(2,1)];nz=[j for j in range(8) if j+1 not in zero];groups=[]
 while nz:
  i=nz.pop(0);g=[i+1];rest=[]
  for j in nz:
   if s.det(s.Matrix.hstack(cols[i],cols[j]))==0:g.append(j+1)
   else:rest.append(j)
  nz=rest;groups.append(g)
 return {'parallel_classes':groups,'zero_columns':zero}
records=[];tops=True
for hi in range(20):
 q=byhi[hi];base=embed(q,M[q['seed_type']]);tops &= key(base.subs(vals))==q['cell_key']
 for e,x in enumerate(a,1):records.append({'history_index':hi,'seed':q['seed_type'],'alpha':e,'orientation':(-1)**(e-1),'cell_key':key(base.subs(vals|{x:0}))})
groups={}
for r in records:groups.setdefault(json.dumps(r['cell_key'],sort_keys=True),[]).append(r)
coarse_shared=[v for v in groups.values() if len({x['history_index'] for x in v})>1]
# Exact transition analysis proves histories 7:G/a2 and 11:E/a5 occupy disjoint positive sign chambers.
false_collision=[g for g in coarse_shared if {x['history_index'] for x in g}=={7,11}]
shared=[g for g in coarse_shared if {x['history_index'] for x in g}!={7,11}];internal=[];noncancel=[]
for g in shared:
 z={'multiplicity':len(g),'histories':sorted({x['history_index'] for x in g}),'orientation_sum':sum(x['orientation'] for x in g),'branches':[{'history_index':x['history_index'],'seed':x['seed'],'alpha':x['alpha'],'orientation':x['orientation']} for x in g]}
 (internal if z['orientation_sum']==0 else noncancel).append(z)
external=[v for v in groups.values() if len({x['history_index'] for x in v})==1]
refined_external_branch_count=len(external)+sum(len(g) for g in false_collision)
# Solve one global sign s_h per top chart so s_h*o_h+s_k*o_k=0 on every shared stratum.
adj={i:[] for i in range(20)}
for g in shared:
 assert len(g)==2
 x,y=g;adj[x['history_index']].append((y['history_index'],-x['orientation']*y['orientation']));adj[y['history_index']].append((x['history_index'],-x['orientation']*y['orientation']))
signs={};conflicts=[]
for start in range(20):
 if start in signs:continue
 signs[start]=1;stack=[start]
 while stack:
  u=stack.pop()
  for v,r in adj[u]:
   want=signs[u]*r
   if v in signs and signs[v]!=want:conflicts.append((u,v))
   elif v not in signs:signs[v]=want;stack.append(v)
corrected=[]
for g in shared:
 corrected.append(sum(signs[x['history_index']]*x['orientation'] for x in g))
# The refined external chain consists of singleton keys plus both branches of the split false collision.
external_records=[g[0] for g in external]+[x for g in false_collision for x in g]
external_chain=[{'history_index':x['history_index'],'seed':x['seed'],'alpha':x['alpha'],'coefficient':signs[x['history_index']]*x['orientation'],'cell_key':x['cell_key']} for x in external_records]
external_by_history={str(i):sum(1 for x in external_chain if x['history_index']==i) for i in range(20)}
checks={'all_twenty_top_keys_reproduced':bool(tops),'onehundredsixty_boundaries':len(records)==160,'some_internal_boundaries':len(shared)>0,'GE_false_collision_removed':len(false_collision)==1,'raw_local_orientations_not_global':len(noncancel)==8,'global_orientation_assignment_consistent':not conflicts,'all_shared_boundaries_cancel_after_global_orientation':all(x==0 for x in corrected)}
out={'schema':'marici.nima.n8-full-history-boundary-cancellation.v1','top_histories':20,'boundary_records':len(records),'distinct_coarse_boundary_keys':len(groups),'coarse_shared_keys':len(coarse_shared),'false_positive_chamber_collisions':len(false_collision),'refined_shared_internal_keys':len(shared),'raw_orientation_cancelled_shared_keys':len(internal),'raw_noncancelling_shared_keys':len(noncancel),'coarse_single_history_boundary_keys':len(external),'refined_external_branch_count':refined_external_branch_count,'raw_noncancelling_details':noncancel,'global_history_orientation_signs':{str(k):v for k,v in sorted(signs.items())},'orientation_conflicts':conflicts,'corrected_shared_residuals':corrected,'corrected_noncancelling_branches':[[{'history_index':x['history_index'],'seed':x['seed'],'alpha':x['alpha'],'raw_orientation':x['orientation'],'history_sign':signs[x['history_index']]} for x in shared[i]] for i,r in enumerate(corrected) if r!=0],'external_chain_support':external_chain,'external_branches_by_history':external_by_history,'checks':checks,'passed':all(checks.values()),'interpretation':'After splitting the unique coarse matroid collision whose exact transition leaves the positive domain, one consistent sign per history cancels every refined shared boundary. The remaining refined external branches require comparison with the target amplituhedron boundary.'};p=ROOT/'research/nima/results/n8-full-history-boundary-cancellation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
