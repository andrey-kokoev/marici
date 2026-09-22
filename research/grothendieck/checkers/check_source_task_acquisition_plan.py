"""Exact-rational replay of the calibration floor and acquisition decision."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,copy

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('plan',HERE/'plan_source_task_acquisition.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
plan=p.AcquisitionPlan();t=p.t;report=plan.report
bounds=lambda d:(Q(d['lower_rational']),Q(d['upper_rational']))
threshold=plan.threshold;r=plan.radius;delta=r/10
low_c=bounds(report['gain_at_lower_C']);high_c=bounds(report['gain_at_upper_C'])
assert low_c[1]<threshold<high_c[0]
c=bounds(report['C_bin_interval']);critical=bounds(report['critical_C_interval'])
assert c[0]<critical[0]<critical[1]<c[1]
saved=copy.deepcopy(plan.data)
frozen=json.loads((p.OUT/'calibration-refinement-frozen-inputs.json').read_text(encoding='utf-8'))
for mode,data in plan.data.items():
    lo,hi=plan.engine.calibrations(mode)['positive']
    assert lo+2*r<threshold<hi-2*r
    result=plan.engine.certify(data)
    assert result==report['remaining_cases'][mode]
    assert result['status']=='UNRESOLVED' and result['conditional_aggregate_bounds_positive']
    assert Q(result['automatic_witness_search']['moment_cost'])>t.DEFAULT_BUDGET
    for name,expected in [('lower_threshold','CERTIFIED_FEASIBLE'),('upper_threshold','CERTIFIED_INFEASIBLE')]:
        assert plan.engine.certify(frozen['cases'][mode][name])['status']==expected
    cases=[(lo-r-delta,'CALIBRATION_INCOMPATIBLE'),(lo-r,'SOURCE_PRIOR_INCOMPATIBLE'),
           (threshold-r-delta,'SOURCE_PRIOR_INCOMPATIBLE'),(threshold-r,'UNRESOLVED'),
           (threshold,'UNRESOLVED'),(threshold+r-delta,'UNRESOLVED'),
           (threshold+r,'TASK_CERTIFIED_CONDITIONAL_ON_VALID_REFERENCE'),
           (hi+r,'TASK_CERTIFIED_CONDITIONAL_ON_VALID_REFERENCE'),(hi+r+delta,'CALIBRATION_INCOMPATIBLE')]
    for center,expected in cases:
        answer=plan.classify_reference(mode,center)
        assert answer['hypothetical'] and answer['outcome']==expected
        if expected=='TASK_CERTIFIED_CONDITIONAL_ON_VALID_REFERENCE':
            certificate=answer['source_certificate']
            assert certificate['automatic_witness_search']['accepted']
            assert certificate['nonvacuous_positive_task_certificate']
            assert Q(certificate['automatic_witness_search']['moment_cost'])<=t.DEFAULT_BUDGET
            supplied=copy.deepcopy(data);supplied['auto_witness']=False
            supplied['witness']={'positive':'499/400','crossed':'0','vacuum':'1/100'}
            checked=p._ConditionedGain(plan.engine,mode,bounds(answer['conditioned_gain_interval'])).certify(supplied)
            assert checked['witness_check']['accepted']
            assert Q(checked['witness_check']['moment_cost'])==t.DEFAULT_BUDGET
    # Zero-radius equality is feasible; positive-radius equality need not resolve.
    assert plan.classify_reference(mode,threshold,0)['outcome']=='TASK_CERTIFIED_CONDITIONAL_ON_VALID_REFERENCE'
    assert plan.classify_reference(mode,threshold)['outcome']=='UNRESOLVED'
    # Worst-case noise endpoint checks complement the algebraic all-error proof.
    for gain,expected in [(threshold-2*r-delta,'SOURCE_PRIOR_INCOMPATIBLE'),
                          (threshold+2*r,'TASK_CERTIFIED_CONDITIONAL_ON_VALID_REFERENCE')]:
        for noise in (-r,Q(0),r):assert plan.classify_reference(mode,gain+noise)['outcome']==expected
    assert plan.classify_reference(mode,threshold-r)['outcome']=='UNRESOLVED'

    # A repeat on the UNKNOWN source only intersects the existing raw interval.
    oldlo,oldhi=t.interval(data['raw']['positive']);cap=Q(499,400)
    assert oldlo>cap*lo and oldlo<cap*hi
    repeat_cases=[(oldlo-r-delta,'READINGS_INCOMPATIBLE'),(oldhi+r+delta,'READINGS_INCOMPATIBLE'),
                  (oldlo,'UNRESOLVED'),(cap*hi+r,'UNRESOLVED'),
                  (cap*hi+r+delta,'SOURCE_PRIOR_INCOMPATIBLE')]
    for center,expected in repeat_cases:assert plan.classify_repeat(mode,center)['outcome']==expected
    # Regression scan, not the proof of the continuous outcome partition.
    for j in range(41):
        center=lo-r+(hi-lo+2*r)*Q(j,40)
        answer=plan.classify_reference(mode,center)
        expected=('SOURCE_PRIOR_INCOMPATIBLE' if center+r<threshold else
                  'TASK_CERTIFIED_CONDITIONAL_ON_VALID_REFERENCE' if center-r>=threshold else 'UNRESOLVED')
        assert answer['outcome']==expected
    for action in (plan.classify_repeat,plan.classify_reference):
        for invalid in (-1,True,0.1):
            try:action(mode,threshold,invalid)
            except ValueError:pass
            else:raise AssertionError('Invalid radius accepted')
assert plan.data==saved
print('PASS: calibration-method floor, preserved data/prior, task-positive reference branches, strict endpoints, worst-case noise bounds, unknown-source repeat obstruction and input rejection')
