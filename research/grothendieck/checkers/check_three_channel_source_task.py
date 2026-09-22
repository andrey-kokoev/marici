"""Fast exact-rational regression tests against the certified task fixtures."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,copy

p=Path(__file__).with_name('three_channel_source_task.py')
s=importlib.util.spec_from_file_location('source_task',p);t=importlib.util.module_from_spec(s);s.loader.exec_module(t)
engine=t.SourceTask()
fixtures=json.loads((t.RESULTS/'three-channel-source-task-fixtures.json').read_text(encoding='utf-8'))
for mode,cases in fixtures.items():
    good=engine.certify(cases['feasible'])
    bad=engine.certify(cases['infeasible'])
    unknown=engine.certify(cases['witness_withheld'])
    assert good['status']=='CERTIFIED_FEASIBLE' and good['nonvacuous_positive_task_certificate']
    assert bad['status']=='CERTIFIED_INFEASIBLE'
    assert unknown['status']=='UNRESOLVED' and not unknown['nonvacuous_positive_task_certificate']
    parts={n:Q(v) for n,v in bad['necessary_cost_by_channel'].items()}
    assert parts['positive']+parts['crossed']<t.DEFAULT_BUDGET
    assert parts['vacuum']<t.DEFAULT_BUDGET<sum(parts.values())
    # A failed proposed witness is not an infeasibility proof.
    failed=copy.deepcopy(cases['feasible']);failed['witness']['positive']='2'
    assert engine.certify(failed)['status']=='UNRESOLVED'
    # Relaxing the prior preserves this witness but can destroy universal positivity.
    relaxed=copy.deepcopy(cases['feasible']);relaxed['budget']='1000000000'
    relaxed_result=engine.certify(relaxed)
    assert relaxed_result['status']=='CERTIFIED_FEASIBLE'
    assert not relaxed_result['nonvacuous_positive_task_certificate']
    # The joint tail weights reproduce the separately reported extreme bounds.
    tail=good['tail_l1_upper_bounds'];joint=good['joint_tail_region'];B=Q(joint['bound'])
    assert Q(joint['vacuum_weight'])*Q(tail['vacuum_rational'])==B
    assert Q(joint['residual_weight'])*Q(tail['residual_per_w_squared_rational'])==B
    for bounds in good['aggregate_readout_enclosures'].values():
        assert Q(bounds['lower_decimal'])<=Q(bounds['lower_rational'])
        assert Q(bounds['upper_rational'])<=Q(bounds['upper_decimal'])
for field,value in [('budget','-1'),('budget',0.1),('moment_order',1)]:
    invalid=copy.deepcopy(fixtures['private']['feasible']);invalid[field]=value
    try:engine.certify(invalid)
    except ValueError:pass
    else:raise AssertionError('Invalid or ignored prior accepted')
print('PASS: both modes, all three statuses, failed witnesses, prior sensitivity, coupled tails, outward rounding and input rejection')
