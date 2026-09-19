#!/usr/bin/env python3
"""Classify the six external facets contracted by C -> CZ."""
from pathlib import Path
import json,collections
R=Path(__file__).resolve().parents[3];full=json.loads((R/'research/nima/results/n8-complete-external-pushforward.json').read_text());rows=[]
for r in full['contracted_facets']:
 rank=r['target_rank'];rows.append({**r,'source_dimension':7,'image_dimension':rank,'generic_fiber_dimension':7-rank,'target_codimension_in_Gr2_6':8-rank,'divisorial_pushforward_contribution':'zero','reason':'The differential has rank below seven, so this seven-form has no generically-finite pushforward to a target divisor.'})
groups=collections.defaultdict(list)
for r in rows:groups[(r['target_rank'],tuple(tuple(x) for x in r['target_brackets']))].append(r['history_index'])
images=[]
for (rank,brackets),histories in groups.items():images.append({'image_dimension':rank,'target_codimension':8-rank,'histories':histories,'vanishing_brackets':[list(x) for x in brackets],'source_preimage_count':len(histories)})
checks={'six_contracted_external_facets':len(rows)==6,'five_rank6_one_rank5':sum(r['target_rank']==6 for r in rows)==5 and sum(r['target_rank']==5 for r in rows)==1,'fiber_dimensions_one_or_two':collections.Counter(r['generic_fiber_dimension'] for r in rows)=={1:5,2:1},'no_contracted_facet_maps_to_divisor':all(r['target_codimension_in_Gr2_6']>=2 for r in rows),'three_distinct_contracted_image_strata':len(images)==3,'four_facets_share_678_stratum':any(sorted(x['histories'])==[11,12,13,18] for x in images)};out={'schema':'marici.nima.n8-contracted-external-facets.v1','facets':rows,'image_strata':images,'checks':checks,'passed':all(checks.values()),'conclusion':'All six source-boundary canonical seven-forms are contracted to target codimension at least two. They produce no divisorial residue in the amplituhedron pushforward. Five have one-dimensional generic fibers over six-dimensional images; one has a two-dimensional generic fiber over a five-dimensional image.'};p=R/'research/nima/results/n8-contracted-external-facets.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'image_strata':images,'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
