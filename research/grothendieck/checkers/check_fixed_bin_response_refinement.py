"""Exact replay and portable export for fixed-hat refinement (or --bulk-norm)."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,copy,tempfile,subprocess,sys

HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj

t=module('task',HERE/'three_channel_source_task.py')
verifier_path=HERE.parent/'certificates'/'verify_source_task_transition.py'
v=module('verifier',verifier_path)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
if sys.argv[1:] not in ([],['--bulk-norm']):raise SystemExit(__doc__)
bulk=bool(sys.argv[1:])
report_name='bulk-norm-task-refinement' if bulk else 'fixed-hat-response-refinement'
parent_name='three-channel-source-task-calibration-fixed-hat.json' if bulk else 'three-channel-source-task-calibration-planning.json'
input_suffix='-fixed-hat' if bulk else ''
output_suffix='-bulk-norm' if bulk else '-fixed-hat'
report=json.loads((OUT/(report_name+'.json')).read_text(encoding='utf-8'))
for name,value in report['protected_file_hashes'].items():assert digest(OUT/name)==value
path=OUT/report['calibration_file'];assert digest(path)==report['calibration_sha256']
engine=t.SourceTask(path);parent=t.SourceTask(OUT/parent_name)
frozen=json.loads((OUT/'calibration-refinement-frozen-inputs.json').read_text(encoding='utf-8'))
prior=json.loads((OUT/'three-channel-source-task-fixtures.json').read_text(encoding='utf-8'))
bounds=lambda d:(Q(d['lower_rational']),Q(d['upper_rational']))
old_C=bounds(report['C_bin_before']);new_C=bounds(report['C_bin_after'])
assert old_C[0]<new_C[0]<new_C[1]<old_C[1]
assert Q(report['C_bin_width_reduction_factor'])==(old_C[1]-old_C[0])/(new_C[1]-new_C[0])>(1 if bulk else 4)
if bulk:
    norm_path=OUT/'bulk-response-norm-refinement.json'
    assert digest(norm_path)==report['bulk_norm_evidence_sha256']==engine.cal['refinement_evidence']['bulk_norm_evidence_sha256']
    norm=json.loads(norm_path.read_text(encoding='utf-8'))
    previous=json.loads((OUT/'fixed-hat-response-refinement.json').read_text(encoding='utf-8'))
    for old,new in zip(previous['projection_diagnostics'],report['projection_diagnostics']):
        for key in ('projection_dimension','fixed_hat_residual_norm','pairing_center'):assert old[key]==new[key]
    interval=lambda d:(Q(d['lower']),Q(d['upper']))
    common=interval(norm['old_formula_at_new_cutoff']);old_tail=interval(norm['old_tail_bound'])
    assert 0<common[0]<=common[1]<old_tail[0]
    for side,tail in zip(norm['sides'],norm['new_tail_bounds']):
        a=interval(side['old_squared_norm']);b=interval(side['new_squared_norm'])
        assert a[0]<b[0]<b[1]<a[1]
        assert 0<interval(tail)[0]<=interval(tail)[1]<common[0]
        f=Q(side['finite_only_upper_bound']);r=Q(side['resolved_tail_only_upper_bound'])
        drops=[Q(side[k]) for k in ('upper_bound_drop_from_finite_refinement',
                                    'upper_bound_drop_from_resolved_tail','upper_bound_drop_from_sharper_tail_algebra')]
        assert drops==[a[1]-f,f-r,r-b[1]] and min(drops)>0 and sum(drops)==a[1]-b[1]
    end=0
    for band in norm['new_finite_bands']:
        lo,hi=band['range'];rate=band['initial_cells_per_unit'];splits=band['bisected_cells']
        assert lo==end and hi>lo and type(rate) is int and rate>0
        assert band['accepted_cells']==(hi-lo)*rate+splits
        assert band['evaluations']==(hi-lo)*rate+2*splits
        end=hi
    assert end==8192
assert engine.cal['refinement_evidence']['projection_dimension']==136
folder=OUT/'portable-source-task-transitions';produced=[]
for mode in ('private','reuse'):
    cases=dict(frozen['cases'][mode]);cases.update({n:prior[mode][n] for n in ('feasible','infeasible')})
    gains=engine.calibrations(mode);old_gains=parent.calibrations(mode)
    assert old_gains['positive'][0]<gains['positive'][0]<gains['positive'][1]<old_gains['positive'][1]
    assert all(gains[n]==old_gains[n] for n in ('crossed','vacuum'))
    for name,data in cases.items():
        before=parent.certify(data);after=engine.certify(data)
        assert before==report['cases'][mode][name]['before']
        assert after==report['cases'][mode][name]['after']
        if before['status']!='UNRESOLVED':assert before['status']==after['status']
        if after['status']!='CERTIFIED_INFEASIBLE':
            for key,b in after['aggregate_readout_enclosures'].items():
                assert t.contains(bounds(before['aggregate_readout_enclosures'][key]),bounds(b))
        if name=='middle_threshold':
            assert after['status']=='UNRESOLVED' and not after['nonvacuous_positive_task_certificate']
            assert Q(after['necessary_moment_cost_lower_bound'])<t.DEFAULT_BUDGET<Q(after['automatic_witness_search']['moment_cost'])
        bundle=v.load(folder/f'{mode}-{name}{input_suffix}.json');assert not v.verify(bundle)
        old=copy.deepcopy(bundle['nodes'][-1])
        assert old['evidence']['calibration']==digest(OUT/parent_name)
        assert old['raw']=={n:list(map(str,t.interval(data['raw'][n]))) for n in t.NAMES}
        assert old['gains']=={n:list(map(str,b)) for n,b in old_gains.items()}
        new=copy.deepcopy(old)
        new['gains']={n:list(map(str,b)) for n,b in gains.items()}
        new['evidence']['calibration']=digest(path)
        certificate={'version':1,'problem_sha256':v.sha(new),'status':after['status'],
                     'necessary_cost':after['necessary_moment_cost_lower_bound']}
        if after['status']!='CERTIFIED_INFEASIBLE':
            certificate['aggregate_bounds']={n:list(map(str,bounds(after['aggregate_readout_enclosures'][key])))
                                           for n,key in [('vacuum','vacuum'),('residual','residual_per_w_squared')]}
            certificate['positive_task']=after['nonvacuous_positive_task_certificate']
        if after['status']=='CERTIFIED_FEASIBLE':
            w=after['witness_check'] if after.get('witness_check',{}).get('accepted') else after['automatic_witness_search']
            certificate['witness']=w['coefficients_at_A2']
        bundle['edges'].append({'version':1,'kind':'identity-calibration-refinement',
                                'old_sha256':v.sha(old),'new_sha256':v.sha(new)})
        bundle['nodes'].append(new);bundle['certificates'].append(certificate)
        assert not v.verify(bundle)
        destination=folder/f'{mode}-{name}{output_suffix}.json'
        destination.write_text(json.dumps(bundle,indent=2)+'\n',encoding='utf-8');produced.append(destination)
        if name=='middle_threshold':
            bad=copy.deepcopy(bundle);bad['certificates'][-1]['positive_task']=True
            try:v.verify(bad)
            except ValueError:pass
            else:raise AssertionError('Narrower bound promoted unresolved to positive task')
with tempfile.TemporaryDirectory() as directory:
    dest=Path(directory);(dest/verifier_path.name).write_bytes(verifier_path.read_bytes())
    for source in (produced[0],produced[-3]):
        (dest/'bundle.json').write_bytes(source.read_bytes())
        run=subprocess.run([sys.executable,'-I',str(dest/verifier_path.name),str(dest/'bundle.json')],cwd=dest,capture_output=True,text=True)
        assert run.returncode==0,run.stderr
summary={'passed':True,'portable_chains':len(produced),'isolated_verification':True,
         'C_width_reduction_factor':report['C_bin_width_reduction_factor'],
         'gain_width_reduction_factors':report['gain_width_reduction_factors'],
         'middle_statuses':{mode:report['cases'][mode]['middle_threshold']['after']['status'] for mode in ('private','reuse')},
         'scope':'Same physical detector, source, observations and prior; no structural transport claim.'}
(OUT/(report_name+'-tests.json')).write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print('PASS:',report_name,': preserved task certificates, honest unresolved outcomes, 10 portable chains and isolated verification')
