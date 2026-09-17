#!/usr/bin/env python3
"""Finite exact witness for the L/O joint graph and endpoint intertwiner."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
n=9
symbol=tuple((k+2)*(-1 if k%2 else 1) for k in range(n))
def M(x):return tuple(symbol[i]*x[i] for i in range(n))
def O(x):return (x[0],x[-1])
def D(y):return (symbol[0]*y[0],symbol[-1]*y[1])
def norm2(x):return sum(v*v for v in x)
def graph_norm2(x):return norm2(x)+norm2(M(x))+norm2(O(x))+norm2(O(M(x)))
vectors=[tuple(((seed+1)*(i+2))%7-3 for i in range(n)) for seed in range(13)]
intertwining=all(O(M(x))==D(O(x)) for x in vectors)
faithful=all(graph_norm2(x)>=norm2(x) and (graph_norm2(x)==0)==all(v==0 for v in x) for x in vectors)
# Hostile readout not supported on multiplier eigencoordinates breaks naturality.
def badO(x):return (x[0]+x[1],x[-1])
hostile_detected=any(badO(M(x))!=D(badO(x)) for x in vectors)
checks={'endpoint_multiplier_intertwining':intertwining,'joint_graph_norm_faithful':faithful,'hostile_nonintertwining_readout_detected':hostile_detected}
out={'schema':'marici.nima.convolution-observation-joint-graph.v1','dimension':n,'checks':checks,'theorem':'closed multiplier and retained closed observation admit a faithful common joint graph; O M_a = D_a^partial O persists on completion','passed':all(checks.values()),'boundary':'finite witness for the general closed-graph proof; arithmetic incidence into this domain remains separate'}
p=ROOT/'research/nima/results/convolution-observation-joint-graph.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
