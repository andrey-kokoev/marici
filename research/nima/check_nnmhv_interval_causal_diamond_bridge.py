#!/usr/bin/env python3
"""Discrete 1+1 causal/kinematic-space bridge of selected history intervals."""
import math,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];rows=[]
for m in range(1,11):
 events={(i,j) for i in range(1,m+1) for j in range(i,m+1)};covers=[]
 for i,j in events:
  for target,kind in (((i-1,j),'left-null'),((i,j+1),'right-null')):
   if target in events:covers.append(((i,j),target,kind))
 path_ok=True
 for i,j in events:
  for k,l in events:
   if k<=i and j<=l:
    # Any causal path independently performs i-k left moves and l-j right moves.
    expected=math.comb((i-k)+(l-j),i-k);dp={(i,j):1}
    for size in range((i-k)+(l-j)+1):
     for a in range(i,k-1,-1):
      b=j+size-(i-a)
      if (a,b) not in events or a<k or b>l or (a,b)==(i,j):continue
      dp[(a,b)]=dp.get((a+1,b),0)+dp.get((a,b-1),0)
    path_ok &= dp.get((k,l),0)==expected
 layers={ell:sum(1 for i,j in events if j-i==ell) for ell in range(m)}
 rows.append({'m':m,'events':len(events),'expected_triangular':m*(m+1)//2,'simple_boundary_events':layers[0],'left_null_edges':sum(k=='left-null' for _,_,k in covers),'right_null_edges':sum(k=='right-null' for _,_,k in covers),'layer_multiplicities':layers,'all_causal_path_counts_binomial':path_ok})
checks={'event_count_is_history_count':all(x['events']==x['expected_triangular'] for x in rows),'simple_roots_form_diagonal_boundary':all(x['simple_boundary_events']==x['m'] for x in rows),'two_null_edge_families_balance':all(x['left_null_edges']==x['right_null_edges'] for x in rows),'interval_length_layers_are_linear':all(all(int(v)==x['m']-int(k) for k,v in x['layer_multiplicities'].items()) for x in rows),'causal_propagator_counts_are_binomial':all(x['all_causal_path_counts_binomial'] for x in rows)}
out={'schema':'marici.nima.nnmhv-interval-causal-diamond-bridge.v1','dictionary':{'history':'interval event [i,j]','null_coordinates':'u=i, v=j','left_null_step':'[i,j] -> [i-1,j]','right_null_step':'[i,j] -> [i,j+1]','time':'tau=j-i (interval size)','space':'sigma=i+j (interval center)','simple_root_boundary':'tau=0'},'rows':rows,'checks':checks,'passed':all(checks.values()),'meaning':'The selected history triangle is a finite discrete 1+1-dimensional causal diamond/interval kinematic space. Its two endpoint moves are null directions, and causal transport multiplicities are binomial.','bridges':['causal sets','1+1 null coordinates','kinematic space of intervals','discrete propagators as path sums','simple roots as the zero-size boundary']};p=ROOT/'research/nima/results/nnmhv-interval-causal-diamond-bridge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'dictionary':out['dictionary'],'checks':checks,'meaning':out['meaning'],'bridges':out['bridges'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
