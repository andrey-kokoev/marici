#!/usr/bin/env python3
"""Resolve apparent n=8 spurious target branches as half-exposed internal Bruhat facets."""
from pathlib import Path
import json,collections
ROOT=Path(__file__).resolve().parents[3];bru=json.loads((ROOT/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());cov=json.loads((ROOT/'research/nima/results/n8-coordinate-to-bruhat-boundary-coverage.json').read_text());push=json.loads((ROOT/'research/nima/results/n8-external-boundary-pushforward-rank.json').read_text());target={(r['history_index'],r['alpha']):r for r in push['rank7_details']};inc=collections.defaultdict(list)
for c in bru['cells']:
 for f in c['bruhat_facets']:inc[tuple(f)].append(c['history_index'])
vis=collections.defaultdict(list)
for r in cov['visible_facet_incidences']:vis[tuple(r['boundary_permutation'])].append(r)
shared=[]
for f,hs in sorted(inc.items()):
 if len(hs)!=2:continue
 vr=vis.get(f,[]);row={'boundary_permutation':list(f),'histories':hs,'visible_incidence_count':len(vr),'visible_branches':[]}
 for z in vr:
  t=target.get((z['history_index'],z['alpha']));entry={'history_index':z['history_index'],'seed':z['seed'],'alpha':z['alpha']}
  if t is not None:entry.update({'target_brackets':t['target_boundary_brackets'],'standard':bool(t['standard_boundary_brackets']),'nonstandard':bool(t['nonstandard_boundary_brackets']),'unlabelled':not t['target_boundary_brackets']})
  row['visible_branches'].append(entry)
 shared.append(row)
one=[r for r in shared if r['visible_incidence_count']==1];both=[r for r in shared if r['visible_incidence_count']==2];none=[r for r in shared if r['visible_incidence_count']==0];onebranches=[r['visible_branches'][0] for r in one];checks={'forty_shared_bruhat_facets':len(shared)==40,'twentythree_visible_on_both_sides':len(both)==23,'sixteen_visible_on_one_side':len(one)==16,'one_hidden_on_both_sides':len(none)==1,'one_sided_are_fifteen_nonstandard_plus_one_unlabelled':sum(x.get('nonstandard',False) for x in onebranches)==15 and sum(x.get('unlabelled',False) for x in onebranches)==1 and not any(x.get('standard',False) for x in onebranches),'unlabelled_one_is_history13_quartic':[(x['history_index'],x['seed'],x['alpha']) for x in onebranches if x.get('unlabelled')]==[(13,'G',4)]}
out={'schema':'marici.nima.n8-hidden-internal-facet-resolution.v1','shared_facets':shared,'one_sided_internal_facets':one,'fully_hidden_internal_facets':none,'checks':checks,'passed':all(checks.values()),'conclusion':'Every apparent nonphysical rank-seven branch in the coordinate-visible census is the exposed side of a shared internal Bruhat facet. Fifteen carry nonstandard bracket labels and the remaining one is the verified history-13 quartic. Their missing partner incidences were omitted by the single-chart alpha-zero census.'};p=ROOT/'research/nima/results/n8-hidden-internal-facet-resolution.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'fully_hidden_internal_facets':none,'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
