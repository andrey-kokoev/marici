#!/usr/bin/env python3
"""Minimal faithful decorated projective-transport bundle at seven points."""
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'));from nnmhv_coherence_paths import compile_nnmhv_histories
tr=json.loads((ROOT/'research/nima/results/nnmhv-projective-transport-correspondences.json').read_text());cm=json.loads((ROOT/'research/nima/results/seven-point-history-parity-cell-matching.json').read_text());cells={m['history_index']:m for m in cm['matches']};hs=compile_nnmhv_histories(7)
def projective(mat):
 q=[Fraction(x) for row in mat for x in row];p=next(x for x in q if x);return tuple(str(x/p) for x in q)
rows=[]
for i,(h,t) in enumerate(zip(hs,tr['histories'])):
 base=(t['xi_transport']['rank'],projective(t['xi_transport']['matrix']));rows.append({'history_index':i,'base_rank':base[0],'base_projective_matrix':list(base[1]),'fiber_inner_pair':list(h.inner_pair),'fiber_outer_pair':list(h.outer_pair),'branch':h.branch,'simplex':cells[i]['simplex'],'canonical_form_ratio':cells[i]['full_canonical_form_ratio']})
def unique(fields):return len({tuple(str(r[f]) for f in fields) for r in rows})==len(rows)
checks={'transport_base_not_faithful':not unique(('base_rank','base_projective_matrix')),'inner_pair_decorates_base_faithfully':unique(('base_rank','base_projective_matrix','fiber_inner_pair')),'outer_pair_alone_does_not_resolve_collision':not unique(('base_rank','base_projective_matrix','fiber_outer_pair')),'all_decorated_points_have_distinct_cells':len({tuple(r['simplex']) for r in rows})==6,'all_canonical_weights_normalized':all(r['canonical_form_ratio']=='1' for r in rows)}
out={'schema':'marici.nima.seven-point-decorated-transport-bundle.v1','base':'P(Mat_2), with Segre rank-one boundary','minimal_tested_fiber':'inner R-invariant endpoint pair (a2,b2)','sections':rows,'checks':checks,'passed':all(checks.values()),'reconstruction':'Omega_(7,2,4) = sum over decorated points ([T_h],(a2,b2)) of Omega_h','channel_action':{'insertion':'changes the base image ruling by adjoining the new null edge','reflow':'moves the kernel ruling and the endpoint-pair fiber at fixed inserted image'}};p=ROOT/'research/nima/results/seven-point-decorated-transport-bundle.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
