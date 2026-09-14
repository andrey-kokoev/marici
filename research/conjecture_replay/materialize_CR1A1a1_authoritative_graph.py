#!/usr/bin/env python3
import json,sys
from dataclasses import asdict,replace
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'));from graph_metrics import MetricAction,MetricGraph,percent_change
prior=json.loads((R/'research/conjecture_replay/results/CR1A1a_authoritative_graph.json').read_text());snap=prior['after_snapshot']
def act(z):return MetricAction(z['name'],frozenset(z['dependencies']),frozenset(z['requires']),frozenset(z['outcome_domain']),z['status'],z['terminal'])
bg=MetricGraph(tuple(act(z) for z in snap['actions']),frozenset(snap['interfaces']),tuple(frozenset(c) for c in snap['coherence_constraints']));old='CR1A1a1_materialize_tau0_unlocalized_relative_Thom_costalk';down='CR1A1a2_construct_ringed_staircase_AW_counit';ch=('CR1A1a1i_construct_ringed_unmarked_gallery_correspondence','CR1A1a1ii_construct_target_unlocalized_Koszul_Cech_comparison');aa=[]
for a in bg.actions:
 if a.name==old:aa.append(replace(a,status='resolved'))
 elif a.name==down:aa.append(replace(a,dependencies=frozenset({ch[1]})))
 else:aa.append(a)
aa.extend((MetricAction(ch[0],dependencies=frozenset({old})),MetricAction(ch[1],dependencies=frozenset({ch[0]}))));ag=MetricGraph(tuple(aa),bg.interfaces,bg.coherence_constraints+(frozenset(ch),));before,after=bg.metrics(),ag.metrics();out={'schema':'marici.conjecture-replay.CR1A1a1-authoritative-graph.v1','audit':'research/voevodsky/results/CR1A1a1_tau0_unlocalized_relative_Thom_costalk.json','outcome':'+-','before_snapshot':snap,'after_snapshot':{'actions':[asdict(a) for a in ag.actions],'interfaces':sorted(ag.interfaces),'coherence_constraints':[sorted(c) for c in ag.coherence_constraints]},'before':before,'after':after,'percent_change_from_previous_base':percent_change(before,after),'next':ch[0],'passed':True};(R/'research/conjecture_replay/results/CR1A1a1_authoritative_graph.json').write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'outcome':'+-','percent_delta':out['percent_change_from_previous_base'],'next':ch[0]}))
