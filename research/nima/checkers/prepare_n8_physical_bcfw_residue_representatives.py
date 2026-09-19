#!/usr/bin/env python3
"""Select genuine BCFW bridge charts for the 11 physical orbit representatives."""
from pathlib import Path
import json,collections
R=Path(__file__).resolve().parents[3];full=json.loads((R/'research/nima/results/n8-complete-external-pushforward.json').read_text());atlas=json.loads((R/'research/nima/results/n8-complete-cyclic-bcfw-bridge-atlas.json').read_text());charts=collections.defaultdict(list)
for x in atlas['charts']:charts[x['history_index']].append(x)
reps={(1,2,3,4):'four-consecutive',(1,2,4,5):'one-edge-gap',(1,2,5,6):'opposite-edge-pair'};rows=[]
for label,name in reps.items():
 fs=[]
 for r in full['facets']:
  if r['target_rank']!=7 or tuple(r['target_brackets'][0])!=label:continue
  f=tuple(r['boundary_permutation']);choices=[]
  for c in charts[r['history_index']]:
   for e in c['exposed_facets']:
    if tuple(e['boundary_permutation'])==f:choices.append({'cyclic_start':c['cyclic_start'],'coordinate':e['coordinate']})
  assert choices;fs.append({'history_index':r['history_index'],'boundary_permutation':list(f),'origin':r['origin'],'exposing_bridge_chart':choices[0],'all_exposing_bridge_charts':choices})
 rows.append({'physical_bracket':list(label),'cyclic_orbit_type':name,'source_facet_count':len(fs),'source_facets':fs})
checks={'three_orbits':len(rows)==3,'counts_6_3_2':[x['source_facet_count'] for x in rows]==[6,3,2],'eleven_facets':sum(x['source_facet_count'] for x in rows)==11,'all_have_bridge_charts':all(f['all_exposing_bridge_charts'] for x in rows for f in x['source_facets'])};out={'schema':'marici.nima.n8-physical-bcfw-residue-representatives.v1','representatives':rows,'checks':checks,'passed':all(checks.values())};p=R/'research/nima/results/n8-physical-bcfw-residue-representatives.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'representatives':rows,'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
