#!/usr/bin/env python3
"""Factor each newly-created NNMHV history shell into square matrix blocks."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'));from nnmhv_coherence_paths import compile_nnmhv_histories
def key(h):return (h.outer_pair,h.inner_pair,h.branch)
rows=[]
for N in range(7,13):
 old={key(h) for h in compile_nnmhv_histories(N-1)};shell=[h for h in compile_nnmhv_histories(N) if key(h) not in old];blocks=[]
 for a1 in range(2,N-3):
  hs=[h for h in shell if h.outer_pair[0]==a1];labels=tuple(range(a1+1,N-2));coords=[]
  for h in hs:
   if h.branch=='left-nested':p,q=h.inner_pair[0],h.inner_pair[1]-2
   else:p,q=h.inner_pair[0],h.outer_pair[1]-1
   coords.append((p,q,h.branch))
  blocks.append({'a1':a1,'r':len(labels),'basis_labels':list(labels),'dimension':len(hs),'coordinates':[{'p':p,'q':q,'branch':b} for p,q,b in coords],'fills_full_matrix':{(p,q) for p,q,b in coords}==set(__import__('itertools').product(labels,repeat=2)),'left_is_weak_upper':all(p<=q for p,q,b in coords if b=='left-nested'),'right_is_strict_lower':all(p>q for p,q,b in coords if b=='right-nested')})
 rows.append({'N':N,'shell_dimension':len(shell),'blocks':blocks})
checks={'tested_N7_through_N12':len(rows)==6,'every_block_is_full_matrix':all(b['fills_full_matrix'] and b['dimension']==b['r']**2 for r in rows for b in r['blocks']),'nesting_is_matrix_orientation':all(b['left_is_weak_upper'] and b['right_is_strict_lower'] for r in rows for b in r['blocks']),'shells_are_sum_of_matrix_blocks':all(r['shell_dimension']==sum(b['r']**2 for b in r['blocks']) for r in rows)}
out={'schema':'marici.nima.nnmhv-shell-matrix-blocks.v1','decomposition':'W_N = direct_sum_(a1=2)^(N-4) End(U_(N-3-a1))','coordinate_rule':{'left_nested':'(p,q)=(a2,b2-2), p<=q','right_nested':'(p,q)=(a2,b1-1), p>q'},'rows':rows,'checks':checks,'passed':all(checks.values()),'interpretation':'Each creation shell is a direct sum of full matrix algebras. Branch polarity is exactly triangular matrix orientation.'};p=ROOT/'research/nima/results/nnmhv-shell-matrix-blocks.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'decomposition':out['decomposition'],'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
