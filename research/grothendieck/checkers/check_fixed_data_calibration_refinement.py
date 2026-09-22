"""Fast rational replay of the fixed-data calibration refinement certificates."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,copy

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('source_task',HERE/'three_channel_source_task.py')
t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
OUT=t.RESULTS
baseline=t.SourceTask();refined=t.SourceTask(OUT/'three-channel-source-task-calibration-refined.json')
report=json.loads((OUT/'fixed-data-calibration-refinement.json').read_text(encoding='utf-8'))
frozen_path=OUT/'calibration-refinement-frozen-inputs.json'
frozen=json.loads(frozen_path.read_text(encoding='utf-8'))
assert hashlib.sha256(frozen_path.read_bytes()).hexdigest()==report['frozen_inputs_sha256']
for name,digest in report['protected_file_hashes'].items():
    assert hashlib.sha256((OUT/name).read_bytes()).hexdigest()==digest
expected={'lower_threshold':'CERTIFIED_FEASIBLE','upper_threshold':'CERTIFIED_INFEASIBLE','middle_threshold':'UNRESOLVED'}
for mode,cases in frozen['cases'].items():
    for name,data in cases.items():
        before=baseline.certify(data);after=refined.certify(data)
        assert before['status']=='UNRESOLVED' and not before['nonvacuous_positive_task_certificate']
        assert after['status']==expected[name]
        assert Q(after['necessary_moment_cost_lower_bound'])>=Q(before['necessary_moment_cost_lower_bound'])
        # Recheck the saved certificate, not just its classification label.
        assert before==report['before'][mode][name]
        assert after==report['after'][mode][name]
        if name=='lower_threshold':
            witness=after['automatic_witness_search'];assert witness['accepted']
            assert after['nonvacuous_positive_task_certificate']
            supplied=copy.deepcopy(data);supplied.pop('auto_witness')
            supplied['witness']=witness['coefficients_at_A2']
            assert refined.certify(supplied)['witness_check']['accepted']
        elif name=='upper_threshold':
            assert before['conditional_aggregate_bounds_positive']
            costs={n:Q(v) for n,v in after['necessary_cost_by_channel'].items()}
            assert costs['positive']<t.DEFAULT_BUDGET<sum(costs.values())
    for channel,interval in refined.calibrations(mode).items():
        assert t.contains(baseline.calibrations(mode)[channel],interval)

# Sign, zero-crossing, empty robust intersection, and invalid gain cases.
assert t.robust_inner((Q(4),Q(8)),(Q(2),Q(3)))==(Q(2),Q(8,3))
assert t.robust_inner((Q(-8),Q(-4)),(Q(2),Q(3)))==(Q(-8,3),Q(-2))
assert t.robust_inner((Q(-1),Q(1)),(Q(2),Q(3)))==(Q(-1,3),Q(1,3))
assert t.robust_inner((Q(1),Q(1)),(Q(2),Q(3))) is None
assert t.closest_to_zero((Q(-8,3),Q(-2)))==Q(-2)
for gain in [(Q(0),Q(1)),(Q(2),Q(1))]:
    try:t.robust_inner((Q(1),Q(2)),gain)
    except ValueError:pass
    else:raise AssertionError('Invalid gain accepted')

prior=json.loads((OUT/'three-channel-source-task-fixtures.json').read_text(encoding='utf-8'))
for mode,cases in prior.items():
    for name in ('feasible','infeasible'):
        old=baseline.certify(cases[name]);new=refined.certify(cases[name])
        assert old['status']==new['status']
        if name=='feasible':
            assert new['witness_check']['accepted'] and new['nonvacuous_positive_task_certificate']
            for target,bounds in new['aggregate_readout_enclosures'].items():
                previous=old['aggregate_readout_enclosures'][target]
                assert Q(previous['lower_rational'])<=Q(bounds['lower_rational'])<=Q(bounds['upper_rational'])<=Q(previous['upper_rational'])
    automatic=copy.deepcopy(cases['witness_withheld']);automatic['auto_witness']=True
    assert baseline.certify(automatic)['automatic_witness_search']['accepted']
    rejected=copy.deepcopy(automatic);rejected['witness']={'positive':'2','crossed':'0','vacuum':'1/100'}
    recovered=baseline.certify(rejected)
    assert not recovered['witness_check']['accepted'] and recovered['automatic_witness_search']['accepted']
    point=copy.deepcopy(automatic);point['raw']['positive']['radius']='0'
    result=baseline.certify(point)
    assert result['status']=='UNRESOLVED' and result['automatic_witness_search']['inner_boxes']['positive'] is None
    invalid=copy.deepcopy(automatic);invalid['auto_witness']='true'
    try:baseline.certify(invalid)
    except ValueError:pass
    else:raise AssertionError('Nonboolean search flag accepted')

# A purported refinement cannot widen an old calibration interval.
saved=copy.deepcopy(refined.refinements)
refined.refinements['private']['positive']['upper']=['1','1']
try:refined.calibrations('private')
except ValueError:pass
else:raise AssertionError('Widened calibration accepted')
refined.refinements=saved
spec=importlib.util.spec_from_file_location('adaptive',HERE/'certify_source_task_adaptively.py')
adaptive=importlib.util.module_from_spec(spec);spec.loader.exec_module(adaptive)
for mode,cases in frozen['cases'].items():
    for name,data in cases.items():
        saved=copy.deepcopy(data);answer=adaptive.certify(data)
        assert data==saved and len(answer['attempts'])==2 and answer['status']==expected[name]
    # A robust witness resolves the old witness-withheld case without refinement.
    answer=adaptive.certify(prior[mode]['witness_withheld'],OUT/'does-not-exist.json')
    assert answer['status']=='CERTIFIED_FEASIBLE' and len(answer['attempts'])==1
    pending=adaptive.certify(cases['middle_threshold'],OUT/'does-not-exist.json')
    assert pending['status']=='UNRESOLVED' and 'refinement_pending' in pending
print('PASS: fixed data, unchanged deployment/prior, three outcomes, preserved certificates, robust witnesses, exact nesting, adaptive early exit and rejection tests')
