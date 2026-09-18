#!/usr/bin/env python3
"""Orientation cancellation on shared selected n=8 positroid boundaries."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
src=json.loads((ROOT/'research/benincasa/results/n8_selected_chart_boundaries.json').read_text());groups=src['boundary_matching']['shared_boundaries'];rows=[]
for g in groups:
 roots={tuple(x['root']) for x in g};orients=[x['orientation'] for x in g]
 rows.append({'roots':[list(x) for x in sorted(roots)],'branches':[{'history_index':x['history_index'],'seed':x['seed'],'alpha':x['alpha'],'residue_orientation':x['orientation']} for x in g],'multiplicity':len(g),'orientation_sum':sum(orients),'opposite_pair':len(g)==2 and sorted(orients)==[-1,1]})
checks={'seven_shared_strata':len(rows)==7,'every_shared_stratum_has_two_branches':all(r['multiplicity']==2 for r in rows),'every_shared_pair_oppositely_oriented':all(r['opposite_pair'] and r['orientation_sum']==0 for r in rows)}
out={'schema':'marici.nima.n8-shared-boundary-orientation-cancellation.v1','rows':rows,'checks':checks,'passed':all(checks.values()),'theorem':'For all seven codimension-one positroid cells shared by the six selected sourced charts, the two alpha-zero residue incidences have opposite signs. If both residues are normalized to the unique canonical form of that common positroid cell, they cancel coefficientwise.','normalization_gate':'Cell-key equality and opposite incidence prove the oriented combinatorial condition. An explicit transition-map calculation is still required if the two chart residues are not assumed to use the canonical unit-residue normalization of the source dlog forms.','unmatched_boundaries':'The remaining 34 distinct boundary keys are unmatched only within the six selected histories; they may meet the other fourteen n=8 histories or the exterior amplitude boundary.','negative_simple_gate':'Boundary-correction form differences still require transported and untransported representatives on a common chart.'};p=ROOT/'research/nima/results/n8-shared-boundary-orientation-cancellation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
