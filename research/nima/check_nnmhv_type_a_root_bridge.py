#!/usr/bin/env python3
"""Type-A root/quiver/persistence bridge of the selected NNMHV kernel."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'));from nnmhv_coherence_paths import compile_nnmhv_histories
rows=[]
for N in range(6,16):
 m=N-5;selected=[h for h in compile_nnmhv_histories(N) if h.branch=='left-nested' and h.outer_pair[0]==2 and h.inner_pair[0]==3];roots=[]
 for h in selected:
  b1=h.outer_pair[1];b2=h.inner_pair[1];i=b2-4;j=b1-4;roots.append({'interval':[i,j],'root_coefficients':[1 if i<=a<=j else 0 for a in range(1,m+1)],'matrix_unit':[i,j+1],'simple':i==j,'has_boundary_update':bool(h.boundary_updates)})
 expected={(i,j) for i in range(1,m+1) for j in range(i,m+1)};actual={tuple(r['interval']) for r in roots};concat=all((i,k) in actual for i,j in actual for p,k in actual if p==j+1)
 rows.append({'N':N,'type':f'A_{m}','rank':m,'histories':len(selected),'positive_roots':m*(m+1)//2,'roots':roots,'all_positive_roots_once':actual==expected and len(actual)==len(roots),'interval_concatenation_closes':concat,'boundary_updates_are_exactly_simple_roots':all(r['simple']==r['has_boundary_update'] for r in roots)})
checks={'selected_histories_equal_all_positive_roots':all(x['all_positive_roots_once'] for x in rows),'root_addition_by_adjacent_interval_concatenation':all(x['interval_concatenation_closes'] for x in rows),'boundary_updates_equal_simple_roots':all(x['boundary_updates_are_exactly_simple_roots'] for x in rows),'tested_A1_through_A10':len(rows)==10}
out={'schema':'marici.nima.nnmhv-type-a-root-bridge.v1','dictionary':{'history_endpoints':'(b1,b2)','positive_root_interval':'[i,j]=[b2-4,b1-4]','root':'alpha_i+...+alpha_j','matrix_realization':'E_(i,j+1) in strictly upper triangular sl_(m+1)','simple_root':'b1=b2','quiver':'indecomposable interval representation of linearly oriented A_m'},'rows':rows,'checks':checks,'passed':all(checks.values()),'meaning':'The selected component is canonically indexed by the positive roots/interval modules of type A. Boundary replacement localizes exactly on simple roots; composite histories are concatenated roots.','bridges':['Lie theory of sl_(m+1)','A_m quiver representations','persistence interval modules and barcodes','cluster-algebra root combinatorics','boundary updates as simple generators']};p=ROOT/'research/nima/results/nnmhv-type-a-root-bridge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'dictionary':out['dictionary'],'checks':checks,'meaning':out['meaning'],'bridges':out['bridges'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
