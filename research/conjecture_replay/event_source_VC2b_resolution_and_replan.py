#!/usr/bin/env python3
"""Admit VC2b=-- and its granularity repair through the immutable event log."""
import json,sys
from dataclasses import asdict
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path[:0]=[str(R/'research/conjecture_net')]
from event_log import EventLog,ResolutionEvent,StateDelta,TopologyEvent,digest
from interpretation_planner import *
plan=json.loads((R/'research/conjecture_replay/results/VC2_granular_replan.json').read_text());audit=R/'research/benincasa/results/VC2b_overlap_differential_typing_audit.json'
g0=digest({'plan':plan['schema'],'actions':[x['name'] for x in plan['remaining_actions']]});s0=digest({'interfaces':plan['current_interfaces']});s1=digest({'parent':s0,'add':['VC2b_interface_invalid'],'outcome':'--'})
resolution=ResolutionEvent('VC2b_construct_stage2_overlap_differential',digest(plan['outcome_contracts']['VC2b_construct_stage2_overlap_differential']),g0,s0,'--',('++','+-','-+'),(f'{audit.relative_to(R).as_posix()}#{digest(json.loads(audit.read_text()))}',),0.1,(('status','typing-audit'),),StateDelta(add_interfaces=('VC2b_interface_invalid',),add_facts=('VC2b=--',)),(('VC2b=--','entails','VC2b_interface_invalid'),),('VC2_stage2_differential',),s1,'2026-09-11T00:00:00Z')
g1=digest({'parent':g0,'split':{'VC2b':['VC2b0','VC2b1','VC2b2']}})
topology=TopologyEvent(g0,'split',('VC2b0_reconstruct_char0_H1','VC2b1_construct_overlap_domain','VC2b2_compare_overlap_to_H1'),('VC2b_construct_stage2_overlap_differential',),(('VC2b_construct_stage2_overlap_differential',('VC2b0_reconstruct_char0_H1','VC2b1_construct_overlap_domain','VC2b2_compare_overlap_to_H1')),),('VC2b0 & VC2b1 -> VC2b2',),g1,'typing audit exposed two missing prerequisite interfaces',(resolution.event_id,),'2026-09-11T00:00:01Z')
log=EventLog(g0,s0).append(resolution).append(topology)
def A(n,c,req,add):
 bs={}
 for o in OUTCOMES:
  x=next(iter(add if o=='++' else {f'{n}:{o}'}));bs[o]=Branch(.25,Effect(add=frozenset({x})),(Implication(Proposition('branch',(n,o)),'entails',Proposition(x),'checker'),))
 return Action(n,c,frozenset(req),bs)
actions=[A('VC2b0_reconstruct_char0_H1',8,['VC2_stage1_quotient'],{'char0_H1_presentation'}),A('VC2b1_construct_overlap_domain',4,['local_IBP_core'],{'overlap_domain'}),A('VC2b2_compare_overlap_to_H1',6,['char0_H1_presentation','overlap_domain'],{'VC2_stage2_differential'}),A('VC2c_verify_exchange_and_path_coherence',3,['VC2_stage2_differential'],{'VC2_coherent_complex'}),A('VC2d_physical_boundary_descent',3,['VC2_coherent_complex'],{'filtered_IBP_lowering'})]
state=State(frozenset(),frozenset({'VC2_stage1_quotient','local_IBP_core','VC2b_interface_invalid'}));decoder=Decoder('VC2d_physical_boundary_descent',None,frozenset({'filtered_IBP_lowering'}),'filtered_IBP_lowering');v=Planner(actions,[decoder],target='filtered_IBP_lowering',require_implications=True).solve_expected(state)
graph_metrics={g0:{'frontier_width':1.,'minimum_declared_depth':1.,'interface_deficit':2.},g1:{'frontier_width':2.,'minimum_declared_depth':5.,'interface_deficit':4.}}
def metric(p):return {**graph_metrics[p.graph_digest],'sunk_cost':p.sunk_cost,'event_count':float(len(p.event_ids))}
out={'schema':'marici.conjecture-replay.VC2b-event-sourced-transition.v1','initial':{'graph_digest':g0,'state_id':s0},'events':[{'event_id':resolution.event_id,**asdict(resolution)},{'event_id':topology.event_id,**asdict(topology)}],'projection':asdict(log.project()),'metric_snapshots':{'before':log.metric_snapshot(metric,0),'after_resolution':log.metric_snapshot(metric,1),'after_topology':log.metric_snapshot(metric,2)},'metric_delta_total':log.metric_delta(metric,0,2),'replanned_policy':{'first_action':v.first_action,'success':v.success,'expected_cost':v.expected_cost},'passed':v.first_action in {'VC2b0_reconstruct_char0_H1','VC2b1_construct_overlap_domain'}}
assert out['passed'];(R/'research/conjecture_replay/results/VC2b_event_sourced_transition.json').write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'events':2,'metrics':out['metric_delta_total'],'next':v.first_action,'cost':v.expected_cost}))
