#!/usr/bin/env python3
"""Test lexicographic affine-inversion incidence signs against visible n=8 transitions."""
from pathlib import Path
import json,collections
ROOT=Path(__file__).resolve().parents[3];bru=json.loads((ROOT/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());cov=json.loads((ROOT/'research/nima/results/n8-coordinate-to-bruhat-boundary-coverage.json').read_text());tr=json.loads((ROOT/'research/nima/results/n8-all-shared-boundary-transitions.json').read_text());n=8
def F(f,j):q,r=divmod(j-1,n);return f[r]+q*n
def inv(f):return tuple((i,j) for i in range(1,n+1) for j in range(i+1,i+n+1) if F(f,i)>F(f,j))
top={c['history_index']:tuple(c['affine_permutation']) for c in bru['cells']};inc=collections.defaultdict(list)
for c in bru['cells']:
 for g in c['bruhat_facets']:
  g=tuple(g);A=set(inv(top[c['history_index']]));B=set(inv(g));added=sorted(B-A);removed=sorted(A-B);inc[g].append({'history':c['history_index'],'added':added,'removed':removed,'symmetric_difference':len(A^B)})
# Candidate sign: parity of the inserted inversion in lexicographically sorted facet inversion set, when nested.
for g,rs in inc.items():
 G=list(inv(g))
 for r in rs:r['candidate_sign']=((-1)**G.index(tuple(r['added'][0]))) if len(r['added'])==1 and not r['removed'] else None
visible_pairs=[]
for r in tr['pairs']:
 if r.get('positive_orthant_classification')!='positive_to_positive':continue
 L,R=r['left'],r['right'];vl=next(x for x in cov['visible_facet_incidences'] if x['history_index']==L['history'] and x['alpha']==L['alpha']);g=tuple(vl['boundary_permutation']);recs=inc[g];sl=next(x['candidate_sign'] for x in recs if x['history']==L['history']);sr=next(x['candidate_sign'] for x in recs if x['history']==R['history']);expected=-(-1)**(L['alpha']-1)*(-1)**(R['alpha']-1)*int(r['log_jacobian']);visible_pairs.append({'histories':[L['history'],R['history']],'candidate_sign_ratio':None if sl is None or sr is None else sr*sl,'transition_required_ratio':expected,'matches':sl is not None and sr is not None and sr*sl==expected})
shared=[x for x in inc.values() if len(x)==2];checks={'forty_shared_facets':len(shared)==40,'all_covers_nested_single_inversion':all(r['candidate_sign'] is not None for rs in inc.values() for r in rs),'twentythree_visible_pairs':len(visible_pairs)==23,'candidate_matches_all_visible_transition_orientations':all(x['matches'] for x in visible_pairs)};out={'schema':'marici.nima.n8-bruhat-orientation-candidate.v1','visible_pair_tests':visible_pairs,'shared_incidences':shared,'checks':checks,'passed':all(checks.values()),'claim_boundary':'Lexicographic inversion insertion is only admitted as an orientation rule if it reproduces every independently computed visible transition sign.'};p=ROOT/'research/nima/results/n8-bruhat-orientation-candidate.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed'],'failures':[x for x in visible_pairs if not x['matches']]},indent=2));raise SystemExit(0 if out['passed'] else 1)
