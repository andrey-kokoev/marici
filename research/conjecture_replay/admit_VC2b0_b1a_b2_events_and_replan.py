#!/usr/bin/env python3
"""Admit completed VC2 continuation evidence and replan from immutable events."""
import json,sys
from dataclasses import asdict
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from event_log import *
from interpretation_planner import *
prior=json.loads((R/'research/conjecture_replay/results/VC2b1_event_sourced_resolution.json').read_text());g0=prior['projection']['graph_digest'];s0=prior['projection']['state_id'];log=EventLog(g0,s0)
def evidence(path):
 p=R/path;return f'{path}#{digest(json.loads(p.read_text()))}'
def res(action,outcome,before,adds,facts,evidence_path,cost,telemetry,invalid=()):
 after=digest({'parent':before,'action':action,'outcome':outcome,'adds':list(adds),'facts':list(facts)})
 ev=ResolutionEvent(action,digest({'frozen_action':action}),log.project().graph_digest,before,outcome,tuple(o for o in ('++','+-','-+','--') if o!=outcome),(evidence(evidence_path),),cost,tuple(telemetry),StateDelta(add_interfaces=tuple(adds),add_facts=tuple(facts)),((f'{action}={outcome}','entails',next(iter(adds))),),tuple(invalid),after,'2026-09-11T00:00:03Z')
 return ev,after
# VC2b0 was completed after b1; admit it.
e0,s1=res('VC2b0_reconstruct_char0_H1','++',s0,('char0_H1_presentation',),('VC2b0=++',),'research/benincasa/results/G12_char0_H1_presentation.json',0.,(('runtime','not measured'),));log=log.append(e0)
# Topology inserted b1a after b2's typing failure.
g1=digest({'parent':g0,'insert':'VC2b1a_construct_coefficient_overlap_representatives'})
t1=TopologyEvent(g0,'insert',('VC2b1a_construct_coefficient_overlap_representatives',),(),(),('VC2b1a -> VC2b2',),g1,'VC2b2 typing audit required coefficient-valued representatives',(evidence('research/benincasa/results/VC2b2_overlap_to_H1_comparison_audit.json'),),'2026-09-11T00:00:04Z');log=log.append(t1)
e1,s2=res('VC2b1a_construct_coefficient_overlap_representatives','++',s1,('coefficient_overlap_representatives',),('VC2b1a=++',),'research/benincasa/results/G12_coefficient_overlap_representatives.json',0.1,(('status','exact 44-entry construction'),));log=log.append(e1)
e2,s3=res('VC2b2_compare_overlap_to_H1','-+',s2,('VC2b2_overlap_span_obstructed',),('VC2b2=-+',),'research/benincasa/results/G12_overlap_span_in_H1.json',9.547/60,(('elapsed_seconds','9.547'),('implementation','two-prime sparse')),('VC2_stage2_differential',));log=log.append(e2)
# Repair topology: polynomial-weighted overlaps are a new priced action.
g2=digest({'parent':g1,'replace':'VC2b2_with_VC2e_weighted_overlap'})
t2=TopologyEvent(g1,'replace',('VC2e_polynomial_weighted_overlap_span',),('VC2b2_compare_overlap_to_H1',),(),('VC2e ++ -> VC2_stage2_differential',),g2,'constant logarithmic overlaps have rank six but miss the target',(e2.event_id,),'2026-09-11T00:00:05Z');log=log.append(t2)
def A(n,c,req,add):
 bs={}
 for o in OUTCOMES:
  x=next(iter(add if o=='++' else {f'{n}:{o}'}));bs[o]=Branch(.25,Effect(add=frozenset({x})),(Implication(Proposition('branch',(n,o)),'entails',Proposition(x),'checker'),))
 return Action(n,c,frozenset(req),bs)
actions=[A('VC2e_polynomial_weighted_overlap_span',3,['char0_H1_presentation','coefficient_overlap_representatives'],{'VC2_stage2_differential'}),A('VC2c_verify_exchange_and_path_coherence',3,['VC2_stage2_differential'],{'VC2_coherent_complex'}),A('VC2d_physical_boundary_descent',3,['VC2_coherent_complex'],{'filtered_IBP_lowering'})]
st=State(frozenset(),frozenset({'char0_H1_presentation','coefficient_overlap_representatives','VC2b2_overlap_span_obstructed'}));dec=Decoder('VC2d_physical_boundary_descent',None,frozenset({'filtered_IBP_lowering'}),'goal');v=Planner(actions,[dec],'goal',require_implications=True).solve_expected(st)
def metric(p):return {'sunk_cost':p.sunk_cost,'event_count':float(len(p.event_ids)),'interface_count':float(len(p.interfaces))}
out={'schema':'marici.conjecture-replay.VC2-admitted-continuation-events.v1','continuation_of':prior['event']['event_id'],'events':[{'event_id':x.event_id,**asdict(x)} for x in (e0,t1,e1,e2,t2)],'projection':asdict(log.project()),'metrics':{'before':log.metric_snapshot(metric,0),'after':log.metric_snapshot(metric,5),'delta':log.metric_delta(metric,0,5)},'admitted_resolution':{'action':e2.action_id,'outcome':e2.selected_outcome,'excluded':e2.excluded_outcomes},'policy':{'first_action':v.first_action,'success':v.success,'expected_cost':v.expected_cost},'passed':v.first_action=='VC2e_polynomial_weighted_overlap_span'};assert out['passed'];(R/'research/conjecture_replay/results/VC2_admitted_continuation_events.json').write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'admitted':'VC2b2=-+','events':5,'delta':out['metrics']['delta'],'next':v.first_action}))
