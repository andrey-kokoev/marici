"""Fresh calibration-floor audit for the frozen unresolved source task.

Keep the deployed filters, observations and prior fixed. Increase only theta
quadrature to diagnose whether its remaining error is the limiting component.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,runpy,json,hashlib,copy
from flint import arb,ctx

HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

t=module('task',HERE/'three_channel_source_task.py')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def endpoints(x):return Q(str(x.lower().fmpq())),Q(str(x.upper().fmpq()))
def qp(x):return [str(x.numerator),str(x.denominator)]
def ball(q):return arb(q.numerator)/q.denominator

parent_path=OUT/'three-channel-source-task-calibration-refined.json'
parent=t.SourceTask(parent_path)
frozen_path=OUT/'calibration-refinement-frozen-inputs.json'
frozen=json.loads(frozen_path.read_text(encoding='utf-8'))
protected=[parent_path,frozen_path,OUT/'three-channel-source-task-calibration.json',
           OUT/'three-channel-cubic-protocol.json',OUT/'time-bin-cubic-observer.json',
           OUT/'time-bin-cubic-observer-certificate.json',OUT/'fixed-data-calibration-refinement.json']
hashes={p.name:digest(p) for p in protected}
data=frozen['cases']['private']['middle_threshold']
cap=Q(499,400);threshold=t.interval(data['raw']['positive'])[0]/cap
for mode in ('private','reuse'):
    case=frozen['cases'][mode]['middle_threshold']
    assert case['budget']==str(t.DEFAULT_BUDGET)
    assert t.interval(case['raw']['vacuum'])==(Q(1,100),Q(1,100))
    assert t.interval(case['raw']['crossed'])==(Q(0),Q(0))
    assert t.interval(case['raw']['positive'])[0]/cap==threshold
    old=parent.certify(case)
    assert old['status']=='UNRESOLVED' and old['conditional_aggregate_bounds_positive']

norm=runpy.run_path(str(HERE/'certify_even_response_norm.py'))
fit=module('fit',HERE/'build_time_bin_cubic_observer.py')
filters,C,h,_=fit.fit_filters([arb(norm['plus_sq'].upper()),arb(norm['minus_sq'].upper())])
assert filters==json.loads((OUT/'time-bin-cubic-observer.json').read_text(encoding='utf-8'))['filters']
legacy=runpy.run_path(str(HERE/'certify_robust_cubic_template_measurement.py'))
window=legacy['window'];g=window.__globals__;ctx.prec=192
assert g['CELLS']==8192 and g['V']==32
g['CELLS']=262144;g['step']=g['V']/g['CELLS']
A=window(2,2,'planning_fixed_A1');B=window(12,5,'planning_fixed_B1');L=legacy['L']
assert A['mu']-L>0 and B['mu']-L>0

def gain(c):
    return 2*A['X']*B['X']*(c+h*(A['mu']-L))*(c+h*(B['mu']-L))

c_interval=endpoints(C)
fresh=endpoints(gain(C))
low_c_gain=endpoints(gain(ball(c_interval[0])))
high_c_gain=endpoints(gain(ball(c_interval[1])))
# Uniform in ALL remaining window/weak/L uncertainties, even if they become exact:
# the retained Cartesian C interval still crosses the decision threshold.
assert low_c_gain[1]<threshold<high_c_gain[0]
assert fresh[0]<threshold<fresh[1]
alpha=h*(A['mu']-L);beta=h*(B['mu']-L)
critical=-(alpha+beta)/2+(((alpha-beta)/2)**2+ball(threshold)/(2*A['X']*B['X'])).sqrt()
critical_interval=endpoints(critical)
assert c_interval[0]<critical_interval[0]<critical_interval[1]<c_interval[1]

cal=copy.deepcopy(parent.cal)
cal['parent_calibration_file']=parent_path.name;cal['parent_calibration_sha256']=digest(parent_path)
for mode in ('private','reuse'):
    before=parent.calibrations(mode)['positive']
    assert before[0]<fresh[0]<fresh[1]<before[1]
    cal['diagonal_refinements'][mode]['positive']={'lower':qp(fresh[0]),'upper':qp(fresh[1])}
cal['refinement_evidence']={'window_cells':262144,'window_arithmetic_bits':192,'scaled_cutoff':32,
                          'unchanged_filter_sha256':hashes['time-bin-cubic-observer.json'],
                          'frozen_inputs_sha256':hashes[frozen_path.name],
                          'purpose':'Diagnose the remaining Cartesian C_bin response-enclosure floor; not a detector change.'}
cal_path=OUT/'three-channel-source-task-calibration-planning.json'
cal_path.write_text(json.dumps(cal,indent=2)+'\n',encoding='utf-8')
engine=t.SourceTask(cal_path)
remaining={}
for mode in ('private','reuse'):
    result=engine.certify(frozen['cases'][mode]['middle_threshold'])
    assert result['status']=='UNRESOLVED' and result['conditional_aggregate_bounds_positive']
    assert Q(result['automatic_witness_search']['moment_cost'])>t.DEFAULT_BUDGET
    remaining[mode]=result

# One additional aggregate of the SAME bounded joint-bin positive filter on a
# KNOWN unit source v_(2,0) measures E_0, not another unknown-source coordinate.
radius=Q('1e-197')
assert t.pair(engine.protocol['channels']['positive']['raw_test_norm_upper'])==1
assert 32*2**16<=t.DEFAULT_BUDGET  # the controlled unit source itself is admissible
assert fresh[0]+2*radius<threshold<fresh[1]-2*radius
report={'schema':'marici.grothendieck.source-task-acquisition-plan.v1','passed':True,
        'protected_file_hashes':hashes,'planning_calibration_file':cal_path.name,
        'planning_calibration_sha256':digest(cal_path),'threshold_gain_rational':str(threshold),
        'gain_interval':t.describe(fresh),'C_bin_interval':t.describe(c_interval),
        'critical_C_interval':t.describe(critical_interval),
        'gain_at_lower_C':t.describe(low_c_gain),'gain_at_upper_C':t.describe(high_c_gain),
        'remaining_cases':remaining,
        'normalized_gain_display':{'unit':'1e-193','gain_interval':t.describe(tuple(v/Q('1e-193') for v in fresh)),
                                   'threshold':t.describe((threshold/Q('1e-193'),threshold/Q('1e-193')))},
        'repeat_unknown_source_option':{
          'record':'Repeat the SAME positive bounded joint-bin aggregate on the unknown source.',
          'joint_interval':'[max(old_lower,s-radius), min(old_upper,s+radius)]',
          'incompatible_readings':'joint lower > joint upper',
          'source_prior_incompatible':'nonempty joint interval AND joint lower > (499/400)*gain_upper',
          'otherwise':'UNRESOLVED; the robust inner minimum cannot decrease by adding a source constraint.',
          'scope':'Fixed calibration and the present calibration-uniform witness method. This does not exclude self-calibrating sensors or methods exploiting further physical correlations.'},
        'reference_option':{'input':'Known unit source v_(2,0); all other coefficients zero.',
          'record':'Same positive bounded joint-bin aggregate; not one point sample or a product of unknown marginal readings.',
          'total_absolute_error_radius':str(radius),
          'preparation_and_acquisition':'All visible preparation error and acquisition error must be included in this radius.',
          'raw_test_norm_upper':'1',
          'sufficient_response_error_contract':'acquisition error + visible reference-preparation error <= 1e-197 in the declared response norm',
          'outer_center_interval':t.describe((fresh[0]-radius,fresh[1]+radius)),
          'center_branches':[
            {'condition':'s < gain_lower-radius OR s > gain_upper+radius','outcome':'CALIBRATION_INCOMPATIBLE'},
            {'condition':'gain_lower-radius <= s < threshold-radius','outcome':'SOURCE_PRIOR_INCOMPATIBLE'},
            {'condition':'threshold-radius <= s < threshold+radius','outcome':'UNRESOLVED'},
            {'condition':'threshold+radius <= s <= gain_upper+radius','outcome':'TASK_CERTIFIED_CONDITIONAL_ON_VALID_REFERENCE'}],
          'incompatible_center_upper_exclusive':str(threshold-radius),
          'task_center_lower_inclusive':str(threshold+radius),
          'guarantee_for_every_allowed_measurement_error':{
              'source_prior_incompatible_if_true_gain_less_than':str(threshold-2*radius),
              'task_certified_if_true_gain_at_least':str(threshold+2*radius)},
          'scope':'A plan for all real returned centers, conditional on a valid reference-error bound. No reference was acquired; no probability of a branch is asserted.'},
        'decision':'Stop theta-only refinement with this fixed C interval. Tighten the fixed-filter bulk response calibration, or acquire the controlled reference if its total-error contract is achievable. Merely adding unknown-source constraints at fixed calibration cannot restore an empty calibration-uniform witness set.',
        'limitations':'The floor is for this Cartesian enclosure method, not irreducible physical uncertainty. No cost-optimality or finite-precision resolution at the exact threshold is claimed.'}
assert hashes=={p.name:digest(p) for p in protected}
(OUT/'source-task-acquisition-plan.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'remaining_statuses':{m:r['status'] for m,r in remaining.items()},
                  'C_bin':str(C),'critical_C':str(critical),'reference_radius':'1e-197'},indent=2))
