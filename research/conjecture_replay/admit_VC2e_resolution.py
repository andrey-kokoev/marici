#!/usr/bin/env python3
import json,sys
from dataclasses import asdict
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from event_log import *
prior=json.loads((R/'research/conjecture_replay/results/VC2_admitted_continuation_events.json').read_text());e=R/'research/benincasa/results/G12_polynomial_weighted_overlap_span.json';result=json.loads(e.read_text());p=prior['projection'];g=p['graph_digest'];s0=p['state_id'];s1=digest({'parent':s0,'VC2e':'++','add':'VC2_weighted_overlap_membership'})
ev=ResolutionEvent('VC2e_polynomial_weighted_overlap_span',digest({'minimum_degree_search':list(range(16))}),g,s0,'++',('+-','-+','--'),(f'{e.relative_to(R).as_posix()}#{digest(result)}',),sum(x['elapsed_seconds'] for x in result['results'])/60,(('elapsed_seconds',str(sum(x['elapsed_seconds'] for x in result['results']))),('minimum_degree',str(result['minimum_weight_degree']))),StateDelta(add_interfaces=('VC2_weighted_overlap_membership',),add_facts=('VC2e=++',)),(('VC2e=++','entails','VC2_weighted_overlap_membership'),),(),s1,'2026-09-11T00:00:06Z');log=EventLog(g,s0).append(ev)
out={'schema':'marici.conjecture-replay.VC2e-admitted-resolution.v1','continuation_of':prior['events'][-1]['event_id'],'event':{'event_id':ev.event_id,**asdict(ev)},'projection':asdict(log.project()),'metric_delta':{'sunk_cost':ev.execution_cost,'interface_count':1,'frontier_width':0},'next_recommendation':'VC2f_exact_weighted_overlap_reconstruction','passed':True};(R/'research/conjecture_replay/results/VC2e_admitted_resolution.json').write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'outcome':'++','cost':ev.execution_cost,'next':out['next_recommendation']}))
