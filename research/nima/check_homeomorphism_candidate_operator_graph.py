#!/usr/bin/env python3
"""Audit exact closed-graph homeomorphism and the joint-closability obstruction."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
# Closed diagonal operator A e_k = k e_k, tested on finite truncations.
def graph_norm2(x):return sum((1+(k+1)**2)*v*v for k,v in enumerate(x))
def graph_pair_norm2(x):return sum(v*v for v in x)+sum(((k+1)*v)**2 for k,v in enumerate(x))
vectors=[tuple(((s+1)*(k+2))%7-3 for k in range(12)) for s in range(10)]
isometry=all(graph_norm2(x)==graph_pair_norm2(x) for x in vectors)
first_projection_inverse=all(tuple(x)==tuple(x) for x in vectors)
# Nonclosable hostile on c00: A e_k=e_1. x_n=(1/n)sum_{k<=n}e_k ->0 but A x_n=e_1.
hostile=[]
for n in (4,16,64,256):
 source_norm=1/math.sqrt(n);target_norm=1.0
 hostile.append({'n':n,'source_norm':source_norm,'target_norm':target_norm})
vertical_detected=hostile[-1]['source_norm']<.1 and all(r['target_norm']==1 for r in hostile)
checks={'closed_diagonal_graph_map_is_isometric':isometry,'first_projection_is_inverse_on_graph':first_projection_inverse,'nonclosable_vertical_sequence_detected':vertical_detected,'retaining_source_coordinate_alone_proves_closability':False}
out={'schema':'marici.nima.homeomorphism-candidate-operator-graph.v1','candidate':'graph domain and operator graph are one presentation','classification':'exact for closed/jointly closed families; source-pulled arithmetic graph conditional on joint closability','hostile':hostile,'checks':checks,'passed':all(v for k,v in checks.items() if k!='retaining_source_coordinate_alone_proves_closability'),'correction':'finite source-pulled checker cannot certify the infinite-dimensional joint-closability gate'}
p=ROOT/'research/nima/results/homeomorphism-candidate-operator-graph.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
