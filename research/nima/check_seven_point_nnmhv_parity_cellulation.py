#!/usr/bin/env python3
"""Candidate seven-point N2MHV cells from the parity-dual NMHV triangulation."""
import json,sys,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'))
from nnmhv_coherence_paths import compile_nnmhv_histories
# Standard NMHV BCFW simplices [1,i,i+1,j,j+1].
simplices=[]
for i in range(2,5):
 for j in range(i+2,7):
  labels=(1,i,i+1,j,j+1)
  if len(set(labels))==5 and max(labels)<=7:simplices.append(labels)
hs=compile_nnmhv_histories(7);cells=[]
for k,(h,simplex) in enumerate(zip(hs,simplices)):
 cells.append({'history_index':k,'history':{'outer_pair':list(h.outer_pair),'inner_pair':list(h.inner_pair),'branch':h.branch},'parity_dual_nmhv_simplex':list(simplex),'omitted_labels':[i for i in range(1,8) if i not in simplex],'n2mhv_target_geometry':'8-dimensional parity-dual cell in A_(7,2,4)','status':'candidate_pending_canonical_form_match'})
checks={'six_histories':len(hs)==6,'six_parity_simplices':len(simplices)==6,'all_simplices_have_five_distinct_labels':all(len(set(x))==5 for x in simplices),'all_cells_have_two_label_complements':all(len(c['omitted_labels'])==2 for c in cells),'all_bcfw_simplices_have_anchor_one':all(x[0]==1 for x in simplices)}
out={'schema':'marici.nima.seven-point-nnmhv-parity-cellulation.v1','nmhv_triangulation_formula':'[1,i,i+1,j,j+1], 2<=i<j-1<=5','cells':cells,'checks':checks,'passed':all(checks.values()),'claim_boundary':'This fixes the six candidate parity-dual cells, not the history-to-cell bijection. Certification requires matching each generalized-R canonical form.'};p=ROOT/'research/nima/results/seven-point-nnmhv-parity-cellulation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
