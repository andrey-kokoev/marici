#!/usr/bin/env python3
"""Canonical dagger and Hilbert-Schmidt structure on NNMHV creation shells."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'));from nnmhv_coherence_paths import compile_nnmhv_histories
def key(h):return (h.outer_pair,h.inner_pair,h.branch)
def coord(h):return (h.inner_pair[0],h.inner_pair[1]-2) if h.branch=='left-nested' else (h.inner_pair[0],h.outer_pair[1]-1)
rows=[]
for N in range(7,13):
 old={key(h) for h in compile_nnmhv_histories(N-1)};shell=[h for h in compile_nnmhv_histories(N) if key(h) not in old];by={(h.outer_pair[0],)+coord(h):h for h in shell};pairs=[]
 for h in shell:
  a,p,q=(h.outer_pair[0],)+coord(h);partner=by.get((a,q,p));pairs.append({'a1':a,'p':p,'q':q,'branch':h.branch,'dagger_branch':partner.branch if partner else None,'fixed':p==q})
 rows.append({'N':N,'dimension':len(shell),'fixed_points':sum(x['fixed'] for x in pairs),'expected_fixed_points':sum(range(1,N-4)),'pairs':pairs})
checks={'dagger_closed':all(x['dagger_branch'] is not None for r in rows for x in r['pairs']),'dagger_involutive':all(all((x['a1'],x['p'],x['q']) in {(y['a1'],y['p'],y['q']) for y in r['pairs']} and (x['a1'],x['q'],x['p']) in {(y['a1'],y['p'],y['q']) for y in r['pairs']} for x in r['pairs']) for r in rows),'off_diagonal_exchanges_branches':all(x['fixed'] or x['branch']!=x['dagger_branch'] for r in rows for x in r['pairs']),'diagonal_is_left_nested':all(not x['fixed'] or x['branch']=='left-nested' for r in rows for x in r['pairs']),'fixed_point_count_matches_blocks':all(r['fixed_points']==r['expected_fixed_points'] for r in rows)}
out={'schema':'marici.nima.nnmhv-shell-dagger-structure.v1','dagger':'E_(p,q)^dagger = E_(q,p)','algebra':'W_N = direct_sum_r End(U_r)','pairing':'<A,B>_HS = sum_r Tr(A_r^dagger B_r)','rows':rows,'checks':checks,'passed':all(checks.values()),'selected_component_observation':'The (2,3) support theorem selects left-nested upper-triangular histories only, so that component is not dagger-closed and is not itself a Hermitian state. Dagger closure belongs to the full shell before component projection.'};p=ROOT/'research/nima/results/nnmhv-shell-dagger-structure.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'dagger':out['dagger'],'pairing':out['pairing'],'checks':checks,'passed':out['passed'],'selected_component_observation':out['selected_component_observation']},indent=2));raise SystemExit(0 if out['passed'] else 1)
