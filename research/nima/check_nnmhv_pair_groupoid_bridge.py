#!/usr/bin/env python3
"""Verify the pair-groupoid/path-algebra bridge of NNMHV creation shells."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'));from nnmhv_coherence_paths import compile_nnmhv_histories
def key(h):return (h.outer_pair,h.inner_pair,h.branch)
def coord(h):return (h.inner_pair[0],h.inner_pair[1]-2) if h.branch=='left-nested' else (h.inner_pair[0],h.outer_pair[1]-1)
rows=[]
for N in range(7,13):
 old={key(h) for h in compile_nnmhv_histories(N-1)};shell=[h for h in compile_nnmhv_histories(N) if key(h) not in old];blocks=[]
 for a in range(2,N-3):
  H={(coord(h)):h for h in shell if h.outer_pair[0]==a};labels=tuple(range(a+1,N-2));composition=[]
  for p,q,r in itertools.product(labels,repeat=3):
   left=H[(p,q)];right=H[(q,r)];product=H.get((p,r));composition.append(product is not None)
  dagger_ok=all((q,p) in H for p,q in H);units_ok=all((p,p) in H for p in labels)
  blocks.append({'a1':a,'objects':list(labels),'arrows':len(H),'expected_pair_groupoid_arrows':len(labels)**2,'all_composable_products_close':all(composition),'dagger_reverses_every_arrow':dagger_ok,'identity_arrow_at_every_object':units_ok})
 rows.append({'N':N,'blocks':blocks})
checks={'all_blocks_have_r_squared_arrows':all(b['arrows']==b['expected_pair_groupoid_arrows'] for row in rows for b in row['blocks']),'composition_closes':all(b['all_composable_products_close'] for row in rows for b in row['blocks']),'dagger_is_groupoid_inverse':all(b['dagger_reverses_every_arrow'] for row in rows for b in row['blocks']),'all_groupoid_units_present':all(b['identity_arrow_at_every_object'] for row in rows for b in row['blocks'])}
out={'schema':'marici.nima.nnmhv-pair-groupoid-bridge.v1','identification':{'history':'arrow p -> q in Pair(U_r)','matrix_unit':'E_(p,q)','composition':'E_(p,q) E_(q,r) = E_(p,r)','noncomposable':'E_(p,q) E_(s,r) = 0 for q != s','dagger':'E_(p,q)^dagger = E_(q,p)','unit':'sum_p E_(p,p)'},'algebra':'C[Pair(U_r)] is isomorphic to End(C^r); W_N is the direct sum of these finite groupoid convolution algebras.','rows':rows,'checks':checks,'passed':all(checks.values()),'bridges':['finite groupoids and category theory','quiver/path algebras','finite-dimensional C*-algebras','categorical quantum mechanics','density matrices via positive normalized elements','upper/lower triangular incidence algebras from the nesting order'],'claim_boundary':'The algebraic carrier and dagger are source-derived. Identifying canonical-form coefficients with a positive normalized state remains open.'};p=ROOT/'research/nima/results/nnmhv-pair-groupoid-bridge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'algebra':out['algebra'],'checks':checks,'bridges':out['bridges'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
