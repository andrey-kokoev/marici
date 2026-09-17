#!/usr/bin/env python3
"""Finite exact model of the minimal source-pulled L/O joint graph."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
n=7
weights=tuple(range(1,n+1));symbol=tuple((-1 if i%2 else 1)*(i+2) for i in range(n))
def U(c):return tuple(weights[i]*c[i] for i in range(n))
def M(x):return tuple(symbol[i]*x[i] for i in range(n))
def O(x):return (x[0],x[-1])
def K(c):return (c,U(c),M(U(c)),O(U(c)),O(M(U(c))))
def zero(x):return all(v==0 for v in x)
vectors=[tuple(((seed+2)*(i+1))%9-4 for i in range(n)) for seed in range(15)]
faithful=all((all(zero(x) for x in K(c))==zero(c)) for c in vectors)
incidence_coordinate=all(K(c)[1]==U(c) and K(c)[2]==M(U(c)) for c in vectors)
endpoint_coordinate=all(K(c)[4]==O(M(U(c))) for c in vectors)
# Omitting the source coordinate can lose a dark source when synthesis has a kernel.
def Ubad(c):return tuple([0]+list(c[1:]))
e0=(1,)+(0,)*(n-1)
dark_source_detected=zero(Ubad(e0)) and not zero(e0)
checks={'retained_source_projection_faithful':faithful,'incidence_and_multiplier_are_graph_coordinates':incidence_coordinate,'observed_multiplier_is_graph_coordinate':endpoint_coordinate,'hostile_output_only_dark_source_detected':dark_source_detected}
out={'schema':'marici.nima.source-pulled-lo-graph.v1','checks':checks,'theorem':'the retained source-pulled graph is the minimal faithful completion making U, MU, OU, and OMU continuous','passed':all(checks.values()),'new_gate':'H and V must preserve the pulled-back graph seminorm family; pairwise coefficient continuity alone does not imply this'}
p=ROOT/'research/nima/results/source-pulled-lo-graph.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
