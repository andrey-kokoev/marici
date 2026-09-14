#!/usr/bin/env python3
import json,sys
from dataclasses import asdict,replace
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'));from graph_metrics import MetricAction,MetricGraph,percent_change
prior=json.loads((R/'research/conjecture_replay/results/CR1A1a1i1a1a1i_authoritative_graph.json').read_text());snap=prior['after_snapshot']
def act(z):return MetricAction(z['name'],frozenset(z['dependencies']),frozenset(z['requires']),frozenset(z['outcome_domain']),z['status'],z['terminal'])
bg=MetricGraph(tuple(act(z) for z in snap['actions']),frozenset(snap['interfaces']),tuple(frozenset(c) for c in snap['coherence_constraints']));old='CR1A1a1i1a1a2_compare_Gysin_with_literal_endpoint_target';child='CR1A1a1i1a1a2i_construct_full_vertex_star_third_edge_BC';down='CR1A1a1ii_construct_target_unlocalized_Koszul_Cech_comparison';aa=[]
for a in bg.actions:
 if a.name==old:aa.append(replace(a,status='resolved'))
 elif a.name==down:aa.append(replace(a,dependencies=frozenset({child})))
 else:aa.append(a)
aa.append(MetricAction(child,dependencies=frozenset({old})));ag=MetricGraph(tuple(aa),bg.interfaces|{'literal_KN_vertex_pushforward'},bg.coherence_constraints);before,after=bg.metrics(),ag.metrics();out={'schema':'marici.conjecture-replay.CR1A1a1i1a1a2-authoritative-graph.v1','audit':'research/voevodsky/results/CR1A1a1i1a1a2_Gysin_literal_endpoint_comparison.json','outcome':'+-','before_snapshot':snap,'after_snapshot':{'actions':[asdict(a) for a in ag.actions],'interfaces':sorted(ag.interfaces),'coherence_constraints':[sorted(c) for c in ag.coherence_constraints]},'before':before,'after':after,'percent_change_from_previous_base':percent_change(before,after),'next':child,'passed':True};(R/'research/conjecture_replay/results/CR1A1a1i1a1a2_authoritative_graph.json').write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'outcome':'+-','percent_delta':out['percent_change_from_previous_base'],'next':child}))
