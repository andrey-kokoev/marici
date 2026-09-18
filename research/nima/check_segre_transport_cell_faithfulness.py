#!/usr/bin/env python3
"""Test whether projective transport alone faithfully labels canonical cells."""
import json
from pathlib import Path
from fractions import Fraction
ROOT=Path(__file__).resolve().parents[2];tr=json.loads((ROOT/'research/nima/results/nnmhv-projective-transport-correspondences.json').read_text());cm=json.loads((ROOT/'research/nima/results/seven-point-history-parity-cell-matching.json').read_text());simplex={m['history_index']:tuple(m['simplex']) for m in cm['matches']}
def canonical(mat):
 vals=[Fraction(x) for row in mat for x in row];pivot=next(x for x in vals if x);return tuple(x/pivot for x in vals)
groups={}
for h in tr['histories']:
 r=h['xi_transport'];groups.setdefault((r['rank'],canonical(r['matrix'])),[]).append(h['history_index'])
collisions=[]
for (rank,key),ids in groups.items():
 if len(ids)>1:collisions.append({'rank':rank,'history_indices':ids,'simplices':[list(simplex[i]) for i in ids],'distinct_cells':len({simplex[i] for i in ids})})
nonfaithful=[c for c in collisions if c['distinct_cells']>1];checks={'projective_transport_collisions_exist':bool(collisions),'one_transport_labels_distinct_certified_cells':bool(nonfaithful),'rank_one_collision_present':any(c['rank']==1 for c in nonfaithful),'all_six_cells_still_canonically_distinct':len(set(simplex.values()))==6}
out={'schema':'marici.nima.segre-transport-cell-faithfulness.v1','collisions':collisions,'checks':checks,'passed':all(checks.values()),'conclusion':'Projective transport is a non-faithful shadow of the history cellulation. Canonical residues cannot be functions of the Segre point alone; they require a decorated history/weight fiber over P(Mat_2).','minimal_lift':'([T_h], h, Omega_h), with insertion and reflow acting on the transport base and canonical weight fiber together.'};p=ROOT/'research/nima/results/segre-transport-cell-faithfulness.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
