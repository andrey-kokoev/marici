#!/usr/bin/env python3
"""Repository audit for a ringed unmarked-gallery correspondence."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2];files=list((R/'research/voevodsky').glob('check_*.rs'));hits=[];positive=[]
for p in files:
 s=p.read_text()
 if 'unmarked gallery' in s or 'unmarked_gallery' in s:hits.append(p.name)
 # Positive status must be explicit; mentions inside next-experiment requests do not count.
 if 'ringed_unmarked_gallery_correspondence":"PASS' in s.replace(' ',''):positive.append(p.name)
texts={n:(R/'research/voevodsky'/n).read_text() for n in hits}
checks={'relevant_found':len(hits)>0,'no_positive_correspondence':not positive,'explicit_missing':any('no spatial Gal projections' in s or 'ringed_q_projection' in s and 'FAIL' in s for s in texts.values()),'carrier_only':any('carrier staircase' in s or 'finite algebraic carrier' in s for s in texts.values())}
assert all(checks.values()),(hits,positive,checks)
out={'schema':'marici.voevodsky.CR1-ringed-unmarked-gallery-correspondence.v1','action':'CR1PK1a2a1a1a1_construct_ringed_unmarked_gallery_correspondence','outcome':'--','searched_checkers':len(files),'relevant_checkers':hits,'available':'finite unmarked gallery BM carrier and monotone staircase projections','missing':'a ringed geometric span with spatial Gal projections and relative-dualizing counit','positive_constructions_found':positive,'branch_disposition':'blocked; evaluate independent target-side unlocalized Koszul-Cech comparison','next':'CR1PK1a2a1a1a2_construct_target_unlocalized_Koszul_Cech_comparison','metric_delta':{'formal_coherence_survivors_percent':0.0,'geometrically_certified_complete_paths_percent':0.0,'new_typed_interfaces':0,'newly_blocked_descendant_branches':1},'checks':checks,'passed':True};p=R/'research/voevodsky/results/CR1_ringed_unmarked_gallery_correspondence.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'outcome':'--','relevant':len(hits),'positive':len(positive),'survivors':32,'next':out['next']}))
