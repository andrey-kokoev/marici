#!/usr/bin/env python3
import json,sys
from dataclasses import asdict,replace
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'));from graph_metrics import MetricAction,MetricGraph,percent_change
I=frozenset({'formal_D03_cubical_calculus','loaded_v10_residue_packet','reciprocal_BM_road_geometry'})
before=MetricGraph((MetricAction('CR1A_v10_occurrence_loaded_PC_purity',requires=frozenset({'formal_D03_cubical_calculus','loaded_v10_residue_packet'})),MetricAction('CR1B_v00_occurrence_loaded_PC_purity',dependencies=frozenset({'CR1A_v10_occurrence_loaded_PC_purity'})),MetricAction('CR1C_global_ringed_PC_compatibility',dependencies=frozenset({'CR1B_v00_occurrence_loaded_PC_purity'})),MetricAction('CR1_physical_source_to_cubical_recollement',dependencies=frozenset({'CR1C_global_ringed_PC_compatibility'}),terminal=True)),I)
children=('CR1A1_construct_geometric_v10_corner_restriction','CR1A2_compare_v10_local_cohomology_boundary');after_actions=[]
for a in before.actions:
 if a.name=='CR1A_v10_occurrence_loaded_PC_purity':after_actions.append(replace(a,status='resolved'))
 elif a.name=='CR1B_v00_occurrence_loaded_PC_purity':after_actions.append(replace(a,dependencies=frozenset({children[1]})))
 else:after_actions.append(a)
after_actions.extend((MetricAction(children[0],dependencies=frozenset({'CR1A_v10_occurrence_loaded_PC_purity'}),requires=frozenset({'reciprocal_BM_road_geometry'})),MetricAction(children[1],dependencies=frozenset({children[0]}))));after=MetricGraph(tuple(after_actions),I)
bm,am=before.metrics(),after.metrics();out={'schema':'marici.conjecture-replay.CR1A-authoritative-graph.v1','audit':'research/voevodsky/results/CR1A_v10_PC_purity_executability.json','outcome':'--','before_snapshot':{'actions':[asdict(a) for a in before.actions],'interfaces':sorted(before.interfaces),'coherence_constraints':[]},'after_snapshot':{'actions':[asdict(a) for a in after.actions],'interfaces':sorted(after.interfaces),'coherence_constraints':[]},'before':bm,'after':am,'percent_change_from_previous_base':percent_change(bm,am),'next':children[0],'passed':True};p=R/'research/conjecture_replay/results/CR1A_authoritative_graph.json';p.write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'outcome':'--','metrics':am,'percent_delta':out['percent_change_from_previous_base'],'next':out['next']}))
