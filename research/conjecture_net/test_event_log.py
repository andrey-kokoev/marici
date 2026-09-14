from dataclasses import FrozenInstanceError
from event_log import CorrectionEvent,EventLog,ResolutionEvent,StateDelta,TopologyEvent,digest

def fixture():
 g0=digest({'actions':['A']});g1=digest({'actions':['A1','A2']});s0=digest({'state':0});s1=digest({'state':1})
 top=TopologyEvent(g0,'split',('A1','A2'),('A',),(('A',('A1','A2')),),('A1->A2',),g1,'granularity correction',('evidence:1',),'2026-01-01T00:00:00Z')
 res=ResolutionEvent('A1',digest({'contract':'A1'}),g1,s0,'-+',('++','+-','--'),('checker:sha256',),5.0,(('elapsed_seconds','300'),('status','timeout')),StateDelta(add_interfaces=('A1_obstructed',),add_facts=('A1=-+',)),(('A1=-+','entails','A1_obstructed'),),('A1_success',),s1,'2026-01-01T00:05:00Z')
 return EventLog(g0,s0).append(top).append(res),top,res

def test_replay_and_metrics():
 log,top,res=fixture();p=log.project()
 assert p.graph_digest==top.new_graph_digest and p.state_id==res.state_after_id
 assert p.interfaces==frozenset({'A1_obstructed'}) and p.sunk_cost==5
 metric=lambda x:{'sunk_cost':x.sunk_cost,'event_count':float(len(x.event_ids))}
 assert log.metric_delta(metric,1,2)=={'sunk_cost':5.0,'event_count':1.0}

def test_immutable_and_deterministic():
 log,_,res=fixture();assert res.event_id==res.event_id
 try:res.execution_cost=2
 except FrozenInstanceError:pass
 else:raise AssertionError('event mutated')

def test_resume_preserves_cumulative_projection_and_bounds():
 log,_,_=fixture();base=log.project();resumed=EventLog.resume(base)
 assert resumed.project()==base
 for bad in (-1,1):
  try:resumed.project(bad)
  except IndexError:pass
  else:raise AssertionError('out-of-range event count accepted')

def test_correction_replaces_outcome():
 log,_,res=fixture();p=log.project();later=digest('later')
 correction=CorrectionEvent('A1',res.event_id,p.graph_digest,p.state_id,'-+','+-',('audit',),StateDelta(remove_facts=('A1=-+',),add_facts=('A1=+-',)),later,'t')
 q=log.append(correction).project();assert ('A1','+-') in q.resolved_actions and ('A1','-+') not in q.resolved_actions and 'A1=+-' in q.facts

def test_rejects_broken_chains():
 log,_,res=fixture()
 bad=ResolutionEvent(**{**res.__dict__,'state_before_id':'wrong','state_after_id':'later'})
 try:log.append(bad)
 except ValueError as e:assert 'state-chain' in str(e)
 else:raise AssertionError('broken chain accepted')

if __name__=='__main__':
 test_replay_and_metrics();test_immutable_and_deterministic();test_resume_preserves_cumulative_projection_and_bounds();test_correction_replaces_outcome();test_rejects_broken_chains();print('PASS 5/5')
