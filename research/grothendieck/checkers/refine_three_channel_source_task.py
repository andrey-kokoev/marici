"""Freeze raw inputs, then refine knowledge of the SAME deployed bin filters.

No protocol/filter manifest, raw interval or source prior is rewritten. Only
positive-window quadrature changes from 8192 to 32768 complete cells.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,runpy,json,hashlib,copy
from flint import arb,ctx

HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

t=load_module('source_task',HERE/'three_channel_source_task.py')
baseline_path=OUT/'three-channel-source-task-calibration.json'
baseline=t.SourceTask(baseline_path)
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
protected=[baseline_path,OUT/'three-channel-cubic-protocol.json',
           OUT/'time-bin-cubic-observer.json',OUT/'time-bin-cubic-observer-certificate.json',
           OUT/'three-channel-source-task-fixtures.json']
before={p.name:digest(p) for p in protected}
frozen_path=OUT/'calibration-refinement-frozen-inputs.json'
if frozen_path.exists():
    frozen=json.loads(frozen_path.read_text(encoding='utf-8'))
    assert frozen['baseline_calibration_sha256']==digest(baseline_path), 'Do not regenerate frozen observations after calibration changes'
else:
    cases={}
    b=Q(1,100);cap=(t.DEFAULT_BUDGET/2**16-8*b)/32
    assert cap==Q(499,400)
    for mode in ('private','reuse'):
        lo,hi=baseline.calibrations(mode)['positive']
        cases[mode]={}
        for name,fraction in [('lower_threshold',Q(1,4)),('upper_threshold',Q(3,4)),('middle_threshold',Q(1,2))]:
            threshold=lo+fraction*(hi-lo)
            dlow=cap*threshold;dhigh=2*hi
            cases[mode][name]={'mode':mode,'budget':str(t.DEFAULT_BUDGET),'auto_witness':True,
                              'raw':{'positive':{'center':str((dlow+dhigh)/2),'radius':str((dhigh-dlow)/2)},
                                     'crossed':{'center':'0','radius':'0'},
                                     'vacuum':{'center':'1/100','radius':'0'}}}
    frozen={'schema':'marici.grothendieck.frozen-refinement-inputs.v1',
            'baseline_calibration_sha256':digest(baseline_path),
            'kind':'Synthetic boundary fixtures selected from baseline calibration BEFORE refinement; not measurements',
            'cases':cases}
    frozen_path.write_text(json.dumps(frozen,indent=2)+'\n',encoding='utf-8')
frozen_hash=digest(frozen_path)
old={mode:{name:baseline.certify(data) for name,data in cases.items()} for mode,cases in frozen['cases'].items()}
assert all(result['status']=='UNRESOLVED' for cases in old.values() for result in cases.values())
assert all(result['automatic_witness_search']['accepted'] is False for cases in old.values() for result in cases.values())

# Recompute the old continuum norm bounds and proposal ONLY to identify the
# original filter calibration. Refuse to change any deployed coefficient.
norm=runpy.run_path(str(HERE/'certify_even_response_norm.py'))
fit=load_module('bin_fit',HERE/'build_time_bin_cubic_observer.py')
filters,C,h,_=fit.fit_filters([arb(norm['plus_sq'].upper()),arb(norm['minus_sq'].upper())])
deployed=json.loads((OUT/'time-bin-cubic-observer.json').read_text(encoding='utf-8'))
assert filters==deployed['filters'], 'Refinement must not refit/redeploy a different filter'
legacy=runpy.run_path(str(HERE/'certify_robust_cubic_template_measurement.py'))
window=legacy['window'];globals_=window.__globals__
assert globals_['CELLS']==8192 and globals_['V']==32
ctx.prec=192
# Enclosure computation only; the actual window and original cutoff stay fixed.
globals_['CELLS']=32768;globals_['step']=globals_['V']/32768
A1=window(2,2,'refined_fixed_A1');B1=window(12,5,'refined_fixed_B1')
L=legacy['L']
def response(w):return arb(2).sqrt()*w['X']*(C+h*(w['mu']-L))
E_new=response(A1)*response(B1)
new_interval=(Q(str(E_new.lower().fmpq())),Q(str(E_new.upper().fmpq())))
qp=lambda q:[str(q.numerator),str(q.denominator)]
new=copy.deepcopy(baseline.cal)
new['parent_calibration_file']=baseline_path.name
new['parent_calibration_sha256']=digest(baseline_path)
new['diagonal_refinements']={}
width_ratios={}
for mode in ('private','reuse'):
    original=baseline.calibrations(mode);old_lo,old_hi=original['positive']
    # This is a fresh enclosure strictly INSIDE the old one, not a selected midpoint.
    assert old_lo<new_interval[0]<new_interval[1]<old_hi
    width_ratios[mode]=(old_hi-old_lo)/(new_interval[1]-new_interval[0])
    assert width_ratios[mode]>2
    original['positive']=new_interval
    new['diagonal_refinements'][mode]={n:{'lower':qp(v[0]),'upper':qp(v[1])} for n,v in original.items()}
new['refinement_evidence']={'cells_before':8192,'cells_after':32768,'window_arithmetic_bits':192,
                            'windows':[[2,2],[12,5]],'scaled_cutoff':32,
                            'unchanged_filter_sha256':before['time-bin-cubic-observer.json'],
                            'frozen_inputs_sha256':frozen_hash}
refined_path=OUT/'three-channel-source-task-calibration-refined.json'
refined_path.write_text(json.dumps(new,indent=2)+'\n',encoding='utf-8')
refined=t.SourceTask(refined_path)
after={mode:{name:refined.certify(data) for name,data in cases.items()} for mode,cases in frozen['cases'].items()}
for mode,cases in after.items():
    assert cases['lower_threshold']['status']=='CERTIFIED_FEASIBLE'
    assert cases['upper_threshold']['status']=='CERTIFIED_INFEASIBLE'
    assert cases['middle_threshold']['status']=='UNRESOLVED'
    assert cases['lower_threshold']['automatic_witness_search']['accepted']
    # The formerly conditionally positive upper-threshold case is EMPTY.
    assert old[mode]['upper_threshold']['conditional_aggregate_bounds_positive']
    components={n:Q(v) for n,v in cases['upper_threshold']['necessary_cost_by_channel'].items()}
    assert components['positive']<t.DEFAULT_BUDGET and components['vacuum']<t.DEFAULT_BUDGET
    assert sum(components.values())>t.DEFAULT_BUDGET

# Preserve all older CONCLUSIVE results and their exact finite source witnesses.
prior=json.loads((OUT/'three-channel-source-task-fixtures.json').read_text(encoding='utf-8'))
preserved={}
for mode,cases in prior.items():
    preserved[mode]={}
    for name in ('feasible','infeasible'):
        old_result=baseline.certify(cases[name]);new_result=refined.certify(cases[name])
        assert old_result['status']==new_result['status']
        if name=='feasible':
            assert new_result['witness_check']['accepted'] and new_result['nonvacuous_positive_task_certificate']
            for target,interval in new_result['aggregate_readout_enclosures'].items():
                previous=old_result['aggregate_readout_enclosures'][target]
                assert Q(previous['lower_rational'])<=Q(interval['lower_rational'])
                assert Q(interval['upper_rational'])<=Q(previous['upper_rational'])
        preserved[mode][name]=new_result['status']
assert digest(frozen_path)==frozen_hash
assert before=={p.name:digest(p) for p in protected}
report={'schema':'marici.grothendieck.fixed-data-calibration-refinement.v1','passed':True,
        'protected_file_hashes':before,'frozen_inputs_sha256':frozen_hash,
        'refined_calibration_file':refined_path.name,
        'positive_gain_before':{mode:[str(v) for v in baseline.calibrations(mode)['positive']] for mode in ('private','reuse')},
        'positive_gain_after':[str(v) for v in new_interval],
        'width_reduction_factors':{mode:str(q) for mode,q in width_ratios.items()},
        'before':old,'after':after,'preserved_prior_certificates':preserved,
        'scope':'The same exact raw intervals, prior and deployed rational filters are used on both sides. Refinement changes knowledge only. The middle case remains unresolved; there is no completeness or experimental acquisition claim.'}
(OUT/'fixed-data-calibration-refinement.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'before':{mode:{n:r['status'] for n,r in cases.items()} for mode,cases in old.items()},
                  'after':{mode:{n:r['status'] for n,r in cases.items()} for mode,cases in after.items()}},indent=2))
