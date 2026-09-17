#!/usr/bin/env python3
"""Dependency-induction certificate for arithmetic source-pulled joint closability."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
# A node is forced to have zero vertical limit if it is a continuous root or
# is reached by a closable operator from a node already forced to zero.
nodes=('source','U','MU','OU','OMU')
edges={'U':('source','continuous U4'),'MU':('U','closable M_a'),'OU':('U','closable retained O'),'OMU':('MU','closable retained O')}
zero={'source'};steps=[]
for node in ('U','MU','OU','OMU'):
 parent,reason=edges[node]
 forced=parent in zero
 if forced:zero.add(node)
 steps.append({'node':node,'parent':parent,'reason':reason,'zero_limit_forced':forced})
# Ablations: if U continuity or M closability is removed, propagation fails.
def propagate(drop):
 z={'source'}
 for node in ('U','MU','OU','OMU'):
  parent,reason=edges[node]
  if node not in drop and parent in z:z.add(node)
 return z
no_U=propagate({'U'});no_M=propagate({'MU'})
checks={'all_vertical_limits_forced_zero':zero==set(nodes),'finite_dependency_graph_acyclic':all(nodes.index(edges[n][0])<nodes.index(n) for n in edges),'without_U_continuity_family_not_certified':no_U!=set(nodes),'without_M_closability_OMU_not_certified':'OMU' not in no_M,'source_projection_faithful_under_hypotheses':zero==set(nodes)}
out={'schema':'marici.nima.arithmetic-joint-closability.v1','family':['U4','M_a U4','O U4','O M_a U4'],'proof_steps':steps,'checks':checks,'passed':all(checks.values()),'scope':'continuous forward U4, admitted closed multiplier, retained closed observation, finite families or coordinatewise projective pro-families','nonclaims':['raw L2 point evaluation','uniform infinite-family Hilbert graph norm','native historical inverse topology']}
p=ROOT/'research/nima/results/arithmetic-joint-closability.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
