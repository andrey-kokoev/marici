from event_log import EventLog,RefinementEvent,digest

def test_refinement_replay_and_percent_metrics():
 g0=digest('g0');g1=digest('g1');s=digest('s');e=RefinementEvent(g0,'P',('cheap_type','expensive_glue'),digest('contracts'),(('cheap_type','expensive_glue'),),digest('aggregate'),g1,'next rung',(),'t');log=EventLog(g0,s).append(e);assert log.project().graph_digest==g1
 metric=lambda p:{'events':float(len(p.event_ids)),'cost':p.sunk_cost}
 assert log.metric_percent_delta(metric,0,1)=={'events':None,'cost':None}

def test_bad_refinement_rejected():
 g=digest('g');s=digest('s');e=RefinementEvent(g,'P',(),digest('c'),(),digest('a'),digest('g1'),'bad',(),'t')
 try:EventLog(g,s).append(e);assert False
 except ValueError:pass

if __name__=='__main__':test_refinement_replay_and_percent_metrics();test_bad_refinement_rejected();print('PASS 2/2')
