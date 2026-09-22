"""Exact audit of the projection conjecture attack and portable task export."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,copy,sys,tempfile,subprocess
HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
vp=HERE.parent/'certificates'/'verify_projection_resolution_attack.py';w=module('floor',vp);v=w.v
t=module('task',HERE/'three_channel_source_task.py')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report_path=OUT/'projection-resolution-conjecture-attack.json';report=v.load(report_path)
for name,h in report['protected_file_hashes'].items():assert sha(OUT/name)==h
path=OUT/report['calibration_file'];assert sha(path)==report['calibration_sha256']
engine=t.SourceTask(path);parent=t.SourceTask(OUT/engine.cal['parent_calibration_file'])
assert engine.cal['refinement_evidence']['projection_dimension']==272
assert engine.cal['refinement_evidence']['projection_bits']==6144
assert engine.cal['refinement_evidence']['theta_cells']==262144
lo,hi=w.mass_floor(report);threshold=Q(report['threshold'])
frozen=v.load(OUT/'calibration-refinement-frozen-inputs.json');prior=v.load(OUT/'three-channel-source-task-fixtures.json')
folder=OUT/'portable-source-task-transitions';produced=[];tasks={}
def bounds(b):return [b['lower_rational'],b['upper_rational']]
for mode in ('private','reuse'):
    cases=dict(frozen['cases'][mode]);cases.update({n:prior[mode][n] for n in ('feasible','infeasible')})
    for name,data in cases.items():
        before=parent.certify(data);after=engine.certify(data)
        if before['status']!='UNRESOLVED':assert after['status']==before['status']
        if before.get('nonvacuous_positive_task_certificate'):assert after['nonvacuous_positive_task_certificate']
        if before['status']!='CERTIFIED_INFEASIBLE' and after['status']!='CERTIFIED_INFEASIBLE':
            for target,b in after['aggregate_readout_enclosures'].items():
                a=before['aggregate_readout_enclosures'][target]
                assert t.contains(tuple(map(Q,bounds(a))),tuple(map(Q,bounds(b))))
        chain=v.load(folder/f'{mode}-{name}-bulk-norm.json');v.verify(chain)
        old=chain['nodes'][-1];new=copy.deepcopy(old)
        assert old['evidence']['calibration']==engine.cal['parent_calibration_sha256']
        assert old['raw']=={n:list(map(str,t.interval(data['raw'][n]))) for n in t.NAMES}
        assert old['gains']=={n:list(map(str,b)) for n,b in parent.calibrations(mode).items()}
        assert old['sigma']=={n:list(map(str,b)) for n,b in engine.sigma.items()}
        assert Q(old['tail_multiplier'])==engine.tail_multiplier and Q(old['budget'])==Q(data.get('budget',t.DEFAULT_BUDGET))
        new['gains']={n:list(map(str,b)) for n,b in engine.calibrations(mode).items()}
        new['evidence']['calibration']=sha(path)
        c={'version':1,'problem_sha256':v.sha(new),'status':after['status'],'necessary_cost':after['necessary_moment_cost_lower_bound']}
        if c['status']!='CERTIFIED_INFEASIBLE':
            c['aggregate_bounds']={n:bounds(after['aggregate_readout_enclosures'][key]) for n,key in (('vacuum','vacuum'),('residual','residual_per_w_squared'))}
            c['positive_task']=after['nonvacuous_positive_task_certificate']
        if c['status']=='CERTIFIED_FEASIBLE':
            witness=after['witness_check'] if after.get('witness_check',{}).get('accepted') else after['automatic_witness_search']
            c['witness']=witness['coefficients_at_A2']
        v.node(new,c)
        chain['edges'].append({'version':1,'kind':'identity-calibration-refinement','old_sha256':v.sha(old),'new_sha256':v.sha(new)})
        chain['nodes'].append(new);chain['certificates'].append(c);v.verify(chain)
        output=folder/f'{mode}-{name}-projection272.json'
        output.write_text(json.dumps(chain,indent=2)+'\n',encoding='utf-8');produced.append(output)
        if name=='middle_threshold':
            assert after==report['middle_cases'][mode] and after['status']=='UNRESOLVED'
            tasks[mode]={'problem':new,'certificate':c}
bundle={'schema':'projection272-fixed-theta-refutation-v1','report':report,'source_tasks':tasks,
        'scope':'Cartesian enclosure obstruction, not physical ambiguity or impossibility of further calibration'}
assert w.verify(bundle)
output=OUT/'projection-resolution-refutation-certificate.json';output.write_text(json.dumps(bundle,indent=2)+'\n',encoding='utf-8')
rejected=[]
def reject(name,change):
    bad=copy.deepcopy(bundle);change(bad)
    try:w.verify(bad)
    except ValueError:rejected.append(name)
    else:raise AssertionError('Accepted '+name)
reject('false success',lambda b:b['report'].__setitem__('verdict','supported_by_certificates'))
reject('physical ambiguity claim',lambda b:b.__setitem__('scope','physical ambiguity proved'))
reject('detached task threshold',lambda b:b['report'].__setitem__('threshold',str(Q(b['report']['threshold'])+Q('1e-193'))))
reject('wrong width reduction',lambda b:b['report'].__setitem__('C_width_reduction','1'))
# Collapsing both mass intervals removes the proven box obstruction.
def collapse(b):
    for name in ('A1','B1'):
        x=b['report']['windows'][name]['X'];x['lower']=x['upper']=str((Q(x['lower'])+Q(x['upper']))/2)
reject('mass uncertainty silently erased',collapse)
with tempfile.TemporaryDirectory() as directory:
    d=Path(directory)
    for source in (vp,vp.with_name('verify_source_task_transition.py')):(d/source.name).write_bytes(source.read_bytes())
    (d/'certificate.json').write_bytes(output.read_bytes())
    result=subprocess.run([sys.executable,'-I',str(d/vp.name),str(d/'certificate.json')],cwd=d,capture_output=True,text=True)
    assert result.returncode==0,result.stderr
    for chain in produced:
        (d/'chain.json').write_bytes(chain.read_bytes())
        result=subprocess.run([sys.executable,'-I',str(d/'verify_source_task_transition.py'),str(d/'chain.json')],cwd=d,capture_output=True,text=True)
        assert result.returncode==0,result.stderr
for name,h in report['protected_file_hashes'].items():assert sha(OUT/name)==h
result={'passed':True,'conjecture_refuted':True,'exact_mass_only_floor':True,
        'lower_corner_below_threshold_margin':str(threshold-lo),'upper_corner_above_threshold_margin':str(hi-threshold),
        'normalized_margin_unit':'1e-193','normalized_margins':[str((threshold-lo)/Q('1e-193')),str((hi-threshold)/Q('1e-193'))],
        'portable_chains':[p.name for p in produced],'refutation_certificate':output.name,
        'rejected_corruptions':rejected,'isolated_verification':True,
        'next_target':'Tighten the completed-theta mass integrals with justified higher-order quadrature; projection-only refinement cannot resolve this fixed-box gate.'}
(OUT/'projection-resolution-conjecture-tests.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('PASS: exact mass-only Cartesian floor, ten nested portable chains, five rejected corruptions and isolated verification')
