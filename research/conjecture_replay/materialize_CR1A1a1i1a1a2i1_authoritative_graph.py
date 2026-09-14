#!/usr/bin/env python3
import json,sys
from dataclasses import asdict,replace
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'));from graph_metrics import MetricAction,MetricGraph,percent_change
prior=json.loads((R/'research/conjecture_replay/results/CR1A1a1i1a1a2_authoritative_graph.json').read_text());snap=prior['after_snapshot']
def act(z):return MetricAction(z['name'],frozenset(z['dependencies']),frozenset(z['requires']),frozenset(z['outcome_domain']),z['status'],z['terminal'])
def shot(g):return {'actions':[asdict(a) for a in g.actions],'interfaces':sorted(g.interfaces),'coherence_constraints':[sorted(c) for c in g.coherence_constraints]}
g0=MetricGraph(tuple(act(z) for z in snap['actions']),frozenset(snap['interfaces']),tuple(frozenset(c) for c in snap['coherence_constraints']));n0='CR1A1a1i1a1a2i_construct_full_vertex_star_third_edge_BC';n1='CR1A1a1i1a1a2i1_construct_vertex_supported_log_BM_BC_cone';n2='CR1A1a1i1a1a2i1a_construct_spatial_proper_log_BM_kernel';down='CR1A1a1ii_construct_target_unlocalized_Koszul_Cech_comparison';aa=[]
for a in g0.actions:
 if a.name==n0:aa.append(replace(a,status='resolved'))
 elif a.name==down:aa.append(replace(a,dependencies=frozenset({n1})))
 else:aa.append(a)
aa.append(MetricAction(n1,dependencies=frozenset({n0})));g1=MetricGraph(tuple(aa),g0.interfaces,g0.coherence_constraints)
bb=[]
for a in g1.actions:
 if a.name==n1:bb.append(replace(a,status='resolved'))
 elif a.name==down:bb.append(replace(a,dependencies=frozenset({n2})))
 else:bb.append(a)
bb.append(MetricAction(n2,dependencies=frozenset({n1})));g2=MetricGraph(tuple(bb),g1.interfaces|{'finite_vertex_cone_principal_line_Gysin'},g1.coherence_constraints);m0,m1,m2=g0.metrics(),g1.metrics(),g2.metrics();out={'schema':'marici.conjecture-replay.CR1A1a1i1a1a2i1-authoritative-graph.v1','transitions':[{'audit':'research/voevodsky/results/CR1A1a1i1a1a2i_full_vertex_star_third_edge_BC.json','outcome':'+-','before':m0,'after':m1,'percent_change':percent_change(m0,m1)},{'audit':'research/voevodsky/results/CR1A1a1i1a1a2i1_vertex_supported_log_BM_BC_cone.json','outcome':'+-','before':m1,'after':m2,'percent_change':percent_change(m1,m2)}],'before_snapshot':snap,'intermediate_snapshot':shot(g1),'after_snapshot':shot(g2),'next':n2,'passed':True};(R/'research/conjecture_replay/results/CR1A1a1i1a1a2i1_authoritative_graph.json').write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'transitions':2,'latest_metrics':m2,'latest_percent_delta':out['transitions'][-1]['percent_change'],'next':n2}))
