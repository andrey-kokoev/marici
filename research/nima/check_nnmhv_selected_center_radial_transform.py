#!/usr/bin/env python3
"""Canonical selected-component to Wedderburn-center radial transform."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'));from nnmhv_coherence_paths import compile_nnmhv_histories
rows=[]
for N in range(6,16):
 selected=[h for h in compile_nnmhv_histories(N) if h.branch=='left-nested' and h.outer_pair[0]==2 and h.inner_pair[0]==3];images=[]
 for h in selected:
  b1=h.outer_pair[1];b2=h.inner_pair[1];S=b1+1;a=b1-b2+2;r=b2-4;images.append((S,a,r,b1,b2))
 target=[(S,a,S-3-a) for S in range(6,N+1) for a in range(2,S-3)];image_keys=[x[:3] for x in images];rows.append({'N':N,'selected_dimension':len(selected),'center_blocks':len(target),'bijection':set(image_keys)==set(target) and len(image_keys)==len(set(image_keys)),'entries':[{'b1':b1,'b2':b2,'shell':S,'block_a1':a,'matrix_size':r,'normalized_center_vector':f'I_{r}/sqrt({r})'} for S,a,r,b1,b2 in images]})
checks={'tested_N6_through_N15':len(rows)==10,'radial_map_is_bijective':all(x['bijection'] for x in rows),'dimensions_match':all(x['selected_dimension']==x['center_blocks'] for x in rows),'matrix_size_is_b2_minus_four':all(e['matrix_size']==e['b2']-4 for x in rows for e in x['entries']),'shell_is_b1_plus_one':all(e['shell']==e['b1']+1 for x in rows for e in x['entries'])}
out={'schema':'marici.nima.nnmhv-selected-center-radial-transform.v1','map':{'selected_history':'(b1,b2)','central_block':'(S,a,r)=(b1+1,b1-b2+2,b2-4)','isometric_basis':'T_(b1,b2) maps to normalized central idempotent I_r/sqrt(r)'},'rows':rows,'checks':checks,'passed':all(checks.values()),'meaning':'The selected triangular kernel is canonically the radial/superselection coordinate space of the full AF history algebra. b1 records creation shell, while b2 records irreducible matrix size.','bridges':['center-valued conditional expectation','Morita reduction M_r ~ C','radialization of noncommutative history space','superselection-sector coordinates','K0 basis indexed by minimal central projections'],'claim_boundary':'This is a canonical basis-level isometry. Showing that physical canonical weights intertwine the center-valued trace requires inserting the actual T_n(b1,b2) coefficients.'};p=ROOT/'research/nima/results/nnmhv-selected-center-radial-transform.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'map':out['map'],'checks':checks,'meaning':out['meaning'],'bridges':out['bridges'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
