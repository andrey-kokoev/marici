#!/usr/bin/env python3
"""Attach exact seed-oriented signs to the 11 physical residue representatives."""
from pathlib import Path
import json,collections
R=Path(__file__).resolve().parents[3];prep=json.loads((R/'research/nima/results/n8-physical-residue-orbit-representatives.json').read_text());anc=json.loads((R/'research/nima/results/n8-polygon-chart-orientation-anchors.json').read_text());anchors={(x['history'],x['cyclic_start']):x for x in anc['anchors']};rows=[]
for q in prep['representatives']:
 fs=[]
 for f in q['source_facets']:
  c=f['exposing_chart'];a=anchors[(f['history_index'],c['cyclic_start'])];sign=a['dlog_jacobian_sign']*((-1)**(c['coordinate']-1));fs.append({**f,'top_chart_orientation_sign':a['dlog_jacobian_sign'],'residue_deletion_sign':(-1)**(c['coordinate']-1),'seed_oriented_residue_sign':sign,'orientation_anchor_jacobian':a['dlog_jacobian_at_sample']})
 rows.append({**q,'source_facets':fs,'sign_distribution':dict(collections.Counter(str(x['seed_oriented_residue_sign']) for x in fs))})
checks={'eleven_oriented_representatives':sum(len(x['source_facets']) for x in rows)==11,'all_have_anchor':all((f['history_index'],f['exposing_chart']['cyclic_start']) in anchors for q in rows for f in q['source_facets']),'all_signs_unit':all(abs(f['seed_oriented_residue_sign'])==1 for q in rows for f in q['source_facets']),'preimage_counts_6_3_2':[len(x['source_facets']) for x in rows]==[6,3,2]};out={'schema':'marici.nima.n8-physical-residue-orientations.v1','representatives':rows,'checks':checks,'passed':all(checks.values()),'next_step':'Invert each seven-dimensional facet map Y=CZ in a shared target chart and divide these oriented residue coefficients by its logarithmic Jacobian.'};p=R/'research/nima/results/n8-physical-residue-orientations.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'signs':[(x['physical_bracket'],[(f['history_index'],f['seed_oriented_residue_sign']) for f in x['source_facets']]) for x in rows],'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
