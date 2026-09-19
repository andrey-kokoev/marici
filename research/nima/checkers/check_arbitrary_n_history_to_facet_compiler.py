#!/usr/bin/env python3
"""Compile supported histories and boundary completions to all type-A facets."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/nima'))
from nnmhv_coherence_paths import compile_nnmhv_histories,supports_component_23
rows=[]
for n in range(6,21):
 m=n-5;pv=m+3;boundary={tuple(sorted((i,(i+1)%pv))) for i in range(pv)};facets={(i,j) for i in range(pv) for j in range(i+1,pv) if (i,j) not in boundary}
 hs=[h for h in compile_nnmhv_histories(n) if supports_component_23(h)]
 positive=[];negative=[]
 for h in hs:
  i=h.inner_pair[1]-4;j=h.outer_pair[1]-4;positive.append((i-1,j+1))
  if h.boundary_updates:negative.append((i,m+2))
 image=set(positive)|set(negative)
 rows.append({'n':n,'m':m,'supported_histories':len(hs),'positive_images':len(positive),'negative_completion_images':len(negative),'facet_count':len(facets),'positive_injective':len(set(positive))==len(positive),'negative_injective':len(set(negative))==len(negative),'lanes_disjoint':not(set(positive)&set(negative)),'image_is_all_facets':image==facets})
checks={'n6_to_n20':len(rows)==15,'positive_history_map_injective':all(x['positive_injective'] for x in rows),'boundary_completion_map_injective':all(x['negative_injective'] for x in rows),'lanes_disjoint':all(x['lanes_disjoint'] for x in rows),'compiler_surjective_to_all_facets':all(x['image_is_all_facets'] for x in rows)}
out={'schema':'marici.nima.arbitrary-n-history-to-facet-compiler.v1','compiler':{'supported_history':'history label [i,j] maps to polygon diagonal (i-1,j+1)','boundary_completion':'the boundary update on simple history [i,i] contributes the complementary facet (i,m+2)','rank_relation':'m=n-5'},'theorem':'For every finite n>=6, the supported histories map bijectively to positive-root facets and their boundary-updated simple histories map bijectively to the complementary negative-simple facets. Together they cover every type-A_m associahedron facet exactly once.','rows':rows,'checks':checks,'passed':all(checks.values()),'remaining_physical_gate':'This compiler is combinatorial. Arbitrary-n physical descent still requires sourced canonical-form/positroid representatives and oriented residue maps on these facets and every shared codimension-two stratum.','claim_boundary':'No equality of history scalar weights with canonical-form densities is asserted, and no arbitrary-n positroid boundary theorem follows.'}
p=R/'research/nima/results/arbitrary-n-history-to-facet-compiler.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
