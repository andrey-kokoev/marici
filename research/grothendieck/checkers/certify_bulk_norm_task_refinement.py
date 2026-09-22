"""Tighter bulk norms -> same auxiliary projection -> fixed-data task replay."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,runpy,json,hashlib,copy
from flint import arb,ctx

HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj

t=module('task',HERE/'three_channel_source_task.py')
n=module('norm',HERE/'refine_bulk_response_norm.py')
r=module('response',HERE/'refine_fixed_bin_response.py')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def endpoints(x):return Q(str(x.lower().fmpq())),Q(str(x.upper().fmpq()))
def qp(x):return [str(x.numerator),str(x.denominator)]
parent_path=OUT/'three-channel-source-task-calibration-fixed-hat.json'
parent=t.SourceTask(parent_path)
previous_path=OUT/'fixed-hat-response-refinement.json'
previous=json.loads(previous_path.read_text(encoding='utf-8'))
frozen_path=OUT/'calibration-refinement-frozen-inputs.json';prior_path=OUT/'three-channel-source-task-fixtures.json'
protected=[parent_path,previous_path,frozen_path,prior_path,OUT/'three-channel-cubic-protocol.json',
           OUT/'time-bin-cubic-observer.json',OUT/'time-bin-cubic-observer-certificate.json',
           OUT/'three-channel-source-task-calibration.json',OUT/'three-channel-source-task-calibration-refined.json',
           OUT/'three-channel-source-task-calibration-planning.json']
hashes={p.name:digest(p) for p in protected}
bounds,norm_report=n.refine()
C,h,diagnostics=r.refine(bounds,subdivisions=8,bits=3072)
for old,new in zip(previous['projection_diagnostics'],diagnostics):
    # The proof-space, fixed hat, and projected center did not change.
    for key in ('projection_dimension','fixed_hat_residual_norm','pairing_center'):assert old[key]==new[key]
    assert arb(new['bulk_residual_squared_upper'])<arb(old['bulk_residual_squared_upper'])
    assert arb(new['pairing_error_upper'])<arb(old['pairing_error_upper'])
new_C=endpoints(C)
old_C=tuple(Q(previous['C_bin_after'][k]) for k in ('lower_rational','upper_rational'))
assert old_C[0]<new_C[0]<new_C[1]<old_C[1]
C_reduction=(old_C[1]-old_C[0])/(new_C[1]-new_C[0])

legacy=runpy.run_path(str(HERE/'certify_robust_cubic_template_measurement.py'))
window=legacy['window'];g=window.__globals__;ctx.prec=192
assert g['CELLS']==8192 and g['V']==32
g['CELLS']=262144;g['step']=g['V']/g['CELLS']
A=window(2,2,'norm_refined_A1');B=window(12,5,'norm_refined_B1');L=legacy['L']
assert A['mu']-L>0 and B['mu']-L>0
new_gain=endpoints(2*A['X']*B['X']*(C+h*(A['mu']-L))*(C+h*(B['mu']-L)))
cal=copy.deepcopy(parent.cal)
cal['parent_calibration_file']=parent_path.name;cal['parent_calibration_sha256']=digest(parent_path)
gain_reductions={}
for mode in ('private','reuse'):
    old=parent.calibrations(mode)['positive']
    assert old[0]<new_gain[0]<new_gain[1]<old[1]
    gain_reductions[mode]=str((old[1]-old[0])/(new_gain[1]-new_gain[0]))
    cal['diagonal_refinements'][mode]['positive']={'lower':qp(new_gain[0]),'upper':qp(new_gain[1])}
cal['refinement_evidence']={'method':'sharper-bulk-norms-in-unchanged-fixed-hat-projection',
                          'projection_dimension':136,'projection_bits':3072,
                          'rates':'2^(j/8), -40<=j<=96, j!=8',
                          'theta_cells':262144,'theta_bits':192,'scaled_cutoff':32,
                          'norm_arithmetic_bits':80,'norm_frequency_cutoff':8192,
                          'bulk_norm_evidence_sha256':digest(OUT/'bulk-response-norm-refinement.json'),
                          'deployed_filter_sha256':hashes['time-bin-cubic-observer.json'],
                          'frozen_inputs_sha256':hashes[frozen_path.name],
                          'C_bin_lower':qp(new_C[0]),'C_bin_upper':qp(new_C[1])}
path=OUT/'three-channel-source-task-calibration-bulk-norm.json'
path.write_text(json.dumps(cal,indent=2)+'\n',encoding='utf-8')
engine=t.SourceTask(path)
frozen=json.loads(frozen_path.read_text(encoding='utf-8'));prior=json.loads(prior_path.read_text(encoding='utf-8'))
results={}
for mode in ('private','reuse'):
    cases=dict(frozen['cases'][mode]);cases.update({key:prior[mode][key] for key in ('feasible','infeasible')})
    results[mode]={}
    for name,data in cases.items():
        old=parent.certify(data);new=engine.certify(data)
        if old['status']!='UNRESOLVED':assert new['status']==old['status']
        if old.get('nonvacuous_positive_task_certificate'):assert new['nonvacuous_positive_task_certificate']
        if old['status']!='CERTIFIED_INFEASIBLE' and new['status']!='CERTIFIED_INFEASIBLE':
            for target,b in new['aggregate_readout_enclosures'].items():
                a=old['aggregate_readout_enclosures'][target]
                assert Q(a['lower_rational'])<=Q(b['lower_rational'])<=Q(b['upper_rational'])<=Q(a['upper_rational'])
        results[mode][name]={'before':old,'after':new}
assert hashes=={p.name:digest(p) for p in protected}
report={'schema':'marici.grothendieck.bulk-norm-task-refinement.v1','passed':True,
        'protected_file_hashes':hashes,'calibration_file':path.name,'calibration_sha256':digest(path),
        'bulk_norm_evidence_sha256':digest(OUT/'bulk-response-norm-refinement.json'),
        'C_bin_before':t.describe(old_C),'C_bin_after':t.describe(new_C),
        'C_bin_width_reduction_factor':str(C_reduction),
        'positive_gain_after':t.describe(new_gain),'gain_width_reduction_factors':gain_reductions,
        'projection_diagnostics':diagnostics,'cases':results,
        'scope':'Only the bulk norm upper bounds change in the fixed 136-dimensional pairing proof. No deployed filter, source, raw input, prior, target, theta rule or actual detector parameter changes.'}
(OUT/'bulk-norm-task-refinement.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'C_bin':C.str(24),'C_width_reduction_approx':float(C_reduction),
                  'statuses':{mode:{k:v['after']['status'] for k,v in cases.items()} for mode,cases in results.items()}},indent=2))
