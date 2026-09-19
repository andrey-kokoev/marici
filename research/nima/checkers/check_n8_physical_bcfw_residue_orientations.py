#!/usr/bin/env python3
"""Orient the eleven physical BCFW bridge-coordinate residues."""
from pathlib import Path
import json,collections
R=Path(__file__).resolve().parents[3];prep=json.loads((R/'research/nima/results/n8-physical-bcfw-residue-representatives.json').read_text());anc=json.loads((R/'research/nima/results/n8-bcfw-bridge-orientation-anchors.json').read_text());anchors={(x['history'],x['cyclic_start']):x for x in anc['anchors']};rows=[]
for q in prep['representatives']:
 fs=[]
 for f in q['source_facets']:
  c=f['exposing_bridge_chart'];a=anchors[(f['history_index'],c['cyclic_start'])];delete=(-1)**(c['coordinate']-1);fs.append({**f,'bridge_to_seed_sign':a['bridge_to_seed_sign'],'residue_deletion_sign':delete,'seed_oriented_residue_sign':a['bridge_to_seed_sign']*delete})
 rows.append({**q,'source_facets':fs,'sign_distribution':dict(collections.Counter(str(x['seed_oriented_residue_sign']) for x in fs))})
checks={'eleven_oriented_facets':sum(len(x['source_facets']) for x in rows)==11,'all_anchored':all((f['history_index'],f['exposing_bridge_chart']['cyclic_start']) in anchors for q in rows for f in q['source_facets']),'all_unit_signs':all(abs(f['seed_oriented_residue_sign'])==1 for q in rows for f in q['source_facets'])};out={'schema':'marici.nima.n8-physical-bcfw-residue-orientations.v1','representatives':rows,'checks':checks,'passed':all(checks.values())};p=R/'research/nima/results/n8-physical-bcfw-residue-orientations.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'signs':[(x['physical_bracket'],[(f['history_index'],f['seed_oriented_residue_sign']) for f in x['source_facets']]) for x in rows],'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
