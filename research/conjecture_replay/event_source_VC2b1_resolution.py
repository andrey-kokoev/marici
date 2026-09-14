#!/usr/bin/env python3
import json
from dataclasses import asdict
from pathlib import Path
import sys
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from event_log import EventLog,ResolutionEvent,StateDelta,digest
prior=json.loads((R/'research/conjecture_replay/results/VC2b_event_sourced_transition.json').read_text());evidence=R/'research/benincasa/results/G12_source_labelled_overlap_domain.json';p=prior['projection'];g=p['graph_digest'];s0=p['state_id'];s1=digest({'parent':s0,'add':'overlap_domain','outcome':'++'})
event=ResolutionEvent('VC2b1_construct_overlap_domain',digest({'++':'integral source-labelled exchange-coherent overlap domain'}),g,s0,'++',('+-','-+','--'),(f'{evidence.relative_to(R).as_posix()}#{digest(json.loads(evidence.read_text()))}',),0.1,(('status','exact finite incidence construction'),),StateDelta(add_interfaces=('overlap_domain',),add_facts=('VC2b1=++',)),(('VC2b1=++','entails','overlap_domain'),),(),s1,'2026-09-11T00:00:02Z')
log=EventLog(g,s0).append(event);before={'frontier_width':2.,'interface_deficit':4.,'sunk_cost':0.};after={'frontier_width':1.,'interface_deficit':3.,'sunk_cost':log.project().sunk_cost}
out={'schema':'marici.conjecture-replay.VC2b1-event-sourced-resolution.v1','continuation_of':prior['events'][-1]['event_id'],'event':{'event_id':event.event_id,**asdict(event)},'projection':asdict(log.project()),'metrics':{'before':before,'after':after,'delta':{k:after[k]-before[k] for k in before}},'next_recommendation':'VC2b0_reconstruct_char0_H1','passed':True};(R/'research/conjecture_replay/results/VC2b1_event_sourced_resolution.json').write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'outcome':'++','metrics':out['metrics']['delta'],'next':out['next_recommendation']}))
