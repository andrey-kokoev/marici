#!/usr/bin/env python3
"""Complete invariant n=8 external-facet pushforward census."""
from pathlib import Path
import json,collections
R=Path(__file__).resolve().parents[3];bru=json.loads((R/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());cov=json.loads((R/'research/nima/results/n8-coordinate-to-bruhat-boundary-coverage.json').read_text());old=json.loads((R/'research/nima/results/n8-external-boundary-pushforward-rank.json').read_text());new=json.loads((R/'research/nima/results/n8-missing-bruhat-facet-pushforwards.json').read_text());inc=collections.Counter()
for c in bru['cells']:
 for f in c['bruhat_facets']:inc[tuple(f)]+=1
vkey={(r['history_index'],r['alpha']):tuple(r['boundary_permutation']) for r in cov['visible_facet_incidences']};visible=[]
for r in old['rank7_details']:
 f=vkey[(r['history_index'],r['alpha'])]
 if inc[f]==1:visible.append({'origin':'coordinate-visible','history_index':r['history_index'],'alpha':r['alpha'],'boundary_permutation':list(f),'target_rank':7,'target_brackets':r['target_boundary_brackets']})
# Coordinate-visible true external facets are all rank seven; rank-six alpha limits were not Bruhat facets.
missing=[{'origin':'atlas-required',**r} for r in new['details']];rows=visible+missing;rank7=[r for r in rows if r['target_rank']==7];labels=collections.Counter(tuple(x) for r in rank7 for x in r['target_brackets']);physical=[]
for i in range(1,9):
 for j in range(i+1,9):
  q=tuple(sorted({i,i%8+1,j,j%8+1}))
  if len(q)==4:physical.append(q)
physical=sorted(set(physical));checks={'eighty_six_external_facets':len(rows)==86,'forty_five_visible_true_external':len(visible)==45,'forty_one_atlas_required_external':len(missing)==41,'eighty_rank_seven':len(rank7)==80,'six_contracted':sum(r['target_rank']<7 for r in rows)==6,'exactly_twenty_physical_labels':set(labels)==set(physical) and len(labels)==20,'cyclic_orbit_multiplicities_6_3_2':collections.Counter(labels.values())=={6:8,3:8,2:4},'no_nonphysical_rank_seven_labels':all(len(r['target_brackets'])==1 and tuple(r['target_brackets'][0]) in physical for r in rank7)};out={'schema':'marici.nima.n8-complete-external-pushforward.v1','rank_distribution':dict(collections.Counter(str(r['target_rank']) for r in rows)),'physical_bracket_multiplicities':{' '.join(map(str,k)):v for k,v in sorted(labels.items())},'contracted_facets':[r for r in rows if r['target_rank']<7],'facets':rows,'checks':checks,'passed':all(checks.values()),'conclusion':'After invariant removal of half-exposed shared facets, every noncontracted external source facet maps to a physical bracket. The 20 physical brackets have cyclic-orbit source multiplicities 6 (eight labels), 3 (eight labels), and 2 (four labels); six further external facets contract.'};p=R/'research/nima/results/n8-complete-external-pushforward.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('facets','contracted_facets')},indent=2));raise SystemExit(0 if out['passed'] else 1)
