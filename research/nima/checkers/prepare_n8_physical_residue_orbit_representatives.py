#!/usr/bin/env python3
"""Prepare the three cyclic-orbit representative physical residue sums."""
from pathlib import Path
import json,collections
R=Path(__file__).resolve().parents[3];full=json.loads((R/'research/nima/results/n8-complete-external-pushforward.json').read_text());atlas=json.loads((R/'research/nima/results/n8-rank2-cyclic-positive-atlas.json').read_text());ac={x['history_index']:x for x in atlas['cells']};reps={(1,2,3,4):'four-consecutive',(1,2,4,5):'one-edge-gap',(1,2,5,6):'opposite-edge-pair'};rows=[]
for label,name in reps.items():
 fs=[]
 for r in full['facets']:
  if r['target_rank']!=7 or tuple(r['target_brackets'][0])!=label:continue
  f=tuple(r['boundary_permutation']);choices=[]
  for c in ac[r['history_index']]['charts']:
   for e in c['exposed_facets']:
    if tuple(e['boundary_permutation'])==f:choices.append({'cyclic_start':c['cyclic_start'],'coordinate':e['coordinate'],'kind':e['kind']})
  assert choices,(r['history_index'],f);fs.append({'history_index':r['history_index'],'boundary_permutation':list(f),'origin':r['origin'],'exposing_chart':choices[0],'all_exposing_charts':choices})
 rows.append({'physical_bracket':list(label),'cyclic_orbit_type':name,'source_facet_count':len(fs),'source_facets':fs})
alllabels=collections.Counter(tuple(r['target_brackets'][0]) for r in full['facets'] if r['target_rank']==7);orbit_counts=collections.Counter()
for q,m in alllabels.items():
 cyclic=any(set(q)=={i,i%8+1,j,j%8+1} for i in range(1,9) for j in range(i+1,9));assert cyclic
 # classify by multiplicity, which distinguishes the three cyclic edge-separation orbits here.
 orbit_counts[m]+=1
checks={'three_orbit_representatives':len(rows)==3,'representative_preimage_counts_6_3_2':[r['source_facet_count'] for r in rows]==[6,3,2],'eleven_representative_pushforwards':sum(r['source_facet_count'] for r in rows)==11,'all_facets_have_positive_exposing_charts':all(r['all_exposing_charts'] for x in rows for r in x['source_facets']),'orbit_multiplicity_distribution':orbit_counts=={6:8,3:8,2:4}};out={'schema':'marici.nima.n8-physical-residue-orbit-representatives.v1','representatives':rows,'all_twenty_label_multiplicities':{' '.join(map(str,k)):v for k,v in sorted(alllabels.items())},'checks':checks,'passed':all(checks.values()),'next_step':'For each of the eleven listed charts, anchor its seven-form orientation and compute the generically finite Jacobian into a common normalized target chart on the stated bracket.'};p=R/'research/nima/results/n8-physical-residue-orbit-representatives.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'representatives':rows,'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
