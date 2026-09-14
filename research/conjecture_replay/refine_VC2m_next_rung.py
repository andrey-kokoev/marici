#!/usr/bin/env python3
import json,sys
from dataclasses import asdict
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from event_log import EventLog,RefinementEvent,digest
from refinement import *
prior=json.loads((R/'research/conjecture_replay/results/VC2l_admitted_percent_metrics.json').read_text());p=prior['projection']
gates=(
 Gate('VC2m1_axis_exceptional_incidence',frozenset(),(InterfaceType('axis_exceptional_incidence','signed-minor axis strata','resolved E=0 exceptional divisor'),),1,3,2,2,True),
 Gate('VC2m2_exceptional_point_identification',frozenset({'axis_exceptional_incidence'}),(InterfaceType('axis_exceptional_labels','axis boundary lattice','pminus,p0,pplus lattice'),),1,2,2,1,True),
 Gate('VC2m3_local_multiplicity',frozenset({'axis_exceptional_labels'}),(InterfaceType('axis_exceptional_multiplicity','labelled axis germs','integral exceptional 0-chains'),),2,1,2,1),
 Gate('VC2m4_orientation',frozenset({'axis_exceptional_multiplicity'}),(InterfaceType('axis_exceptional_orientation','oriented axis germs','oriented exceptional endpoints'),),1,1,2,1,True),
 Gate('VC2m5_exchange_equivariance',frozenset({'axis_exceptional_orientation'}),(InterfaceType('axis_exceptional_exchange_map','exchange module on axes','exchange module on exceptional endpoints'),),1,1,1,1,True),
 Gate('VC2m6_integral_image_and_gluing',frozenset({'axis_exceptional_exchange_map'}),(InterfaceType('global_BD_endpoint_collar_current','local BD collars','integral relative current'),),8,1,2,1),)
deps=tuple((gates[i].name,gates[i+1].name) for i in range(len(gates)-1));plan=RefinementPlan('VC2m_signed_minor_axis_to_exceptional_endpoint_specialization',gates,deps);plan.validate();first=plan.next_gate(frozenset());assert first and first.name==gates[0].name
contract={'parent':plan.parent_action,'gates':[{'name':g.name,'requires':sorted(g.requires),'produces':[asdict(x) for x in g.produces],'estimated_cost':g.estimated_cost,'branch_elimination':g.branch_elimination,'interface_tightening':g.interface_tightening,'falsification_power':g.falsification_power,'hard_type_gate':g.hard_type_gate,'score':g.score()} for g in gates],'dependencies':deps,'aggregation':asdict(plan.aggregation)}
g1=digest({'parent':p['graph_digest'],'refinement':contract});ev=RefinementEvent(p['graph_digest'],plan.parent_action,tuple(g.name for g in gates),digest(contract['gates']),deps,digest(contract['aggregation']),g1,'defer expensive gluing until typed incidence, labels, multiplicity, orientation, and exchange pass',(prior['events'][-1]['event_id'],),'2026-09-11T00:00:26Z');log=EventLog(p['graph_digest'],p['state_id']).append(ev)
before={'executable_frontier':1.,'declared_action_count':1.,'minimum_first_test_cost':8.,'information_per_cost':0.25};after={'executable_frontier':1.,'declared_action_count':6.,'minimum_first_test_cost':first.estimated_cost,'information_per_cost':first.score()};pct={k:100*(after[k]-before[k])/before[k] for k in before}
out={'schema':'marici.conjecture-replay.VC2m-next-rung-refinement.v1','refinement_event':{'event_id':ev.event_id,**asdict(ev)},'projection':asdict(log.project()),'contract':contract,'recommendation':first.name,'metric_projection':{'base':'immediately previous coarse VC2m action','percent_change_from_previous_base':pct,'absolute_values_omitted_by_policy':True,'estimate_warning':'cost and information terms are prospectively declared engineering scores, not calibrated observations'},'passed':True};(R/'research/conjecture_replay/results/VC2m_next_rung_refinement.json').write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'first':first.name,'percent_delta':pct,'event':ev.event_id}))
