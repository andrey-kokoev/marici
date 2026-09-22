"""Produce and independently replay exact acquisition policies; no observations acquired."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,copy,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
vp=HERE.parent/'certificates'/'verify_order16_acquisition_policy.py'
w=module('policy',vp);t=module('task',HERE/'three_channel_source_task.py')
r=module('reference',HERE/'plan_source_task_acquisition.py')
cal=OUT/'three-channel-source-task-calibration-bulk-norm.json';engine=t.SourceTask(cal)
assert t.pair(engine.protocol['channels']['positive']['raw_test_norm_upper'])==1
frozen_path=OUT/'calibration-refinement-frozen-inputs.json';frozen=json.loads(frozen_path.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protected=[cal,frozen_path,OUT/'order16-vacuum-acquisition-inputs.json',OUT/'three-channel-cubic-protocol.json',OUT/'time-bin-cubic-observer.json']
hashes={p.name:sha(p) for p in protected}
folder=OUT/'order16-acquisition-policy';folder.mkdir(exist_ok=True)
summaries={};policies={};checks=0;error_profiles=0
for mode in ('private','reuse'):
    source=w.v.load(OUT/'order16-vacuum-bridge'/f'{mode}-middle_threshold.json');w.b.verify(source)
    base=source['base'];data=frozen['cases'][mode]['middle_threshold']
    assert base['evidence']['calibration']==sha(cal)
    assert base['raw']=={n:list(map(str,t.interval(data['raw'][n]))) for n in t.NAMES}
    assert base['gains']=={n:list(map(str,g)) for n,g in engine.calibrations(mode).items()}
    assert base['sigma']=={n:list(map(str,g)) for n,g in engine.sigma.items()}
    assert Q(base['tail_multiplier'])==engine.tail_multiplier and Q(base['budget'])==Q(data['budget'])
    assert base['evidence']['protocol']==engine.cal['protocol_sha256'] and base['evidence']['filters']==engine.protocol['filter_manifest_sha256']
    M=Q(base['budget']);lo,hi=t.interval(data['raw']['positive']);glo,ghi=engine.calibrations(mode)['positive']
    fixed=8*2**16*Q(1,100);W=32*2**16;h=lo/((M-fixed)/W);radius=Q('1e-197')
    outer_cost=fixed+W*lo/ghi;robust_cost=fixed+W*lo/glo;cap=M-outer_cost
    p={'version':1,'contract':w.CONTRACT,'base':base,'base_certificate':source['base_certificate'],'bridge':source['bridge'],
       'threshold':str(h),'vacuum_cost_cap':str(cap),'robust_cost_deficit':str(robust_cost-M),
       'reference_radius':str(radius),'worst_case_infeasible_below':str(h-2*radius),'worst_case_task_at_least':str(h+2*radius)}
    assert w.verify(p);policies[mode]=p
    queries={
      'zero_vacuum':{'kind':'vacuum','readings':{'3':['0','0'],'4':['0','0']}},
      'near_zero_vacuum':{'kind':'vacuum','readings':{'3':['-1/10000000','1/10000000'],'4':['-1/1000000000','1/1000000000']}},
      'synthetic_bridge_returns':{'kind':'vacuum','readings':source['readings']}}
    # Exact inclusive budget boundary and perturbations on each axis and a joint face.
    for A in (3,4):
        for label,factor in (('inside',Q(999,1000)),('boundary',Q(1)),('outside',Q(1001,1000))):
            value=cap*factor/(8*A**16);reading={'3':['0','0'],'4':['0','0']};reading[str(A)]=[str(value)]*2
            queries[f'vacuum_{A}_{label}']={'kind':'vacuum','readings':reading}
    queries['joint_boundary']={'kind':'vacuum','readings':{str(A):[str(cap/(16*A**16))]*2 for A in (3,4)}}
    queries['negative_boundary']={'kind':'vacuum','readings':{str(A):[str(-cap/(16*A**16))]*2 for A in (3,4)}}
    queries['opposite_signs_outside']={'kind':'vacuum','readings':{str(A):[str(sign*cap*Q(3,5)/(8*A**16))]*2 for A,sign in ((3,1),(4,-1))}}
    for label,center in {'below_calibration':glo-2*radius,'low_endpoint':glo-radius,
                         'infeasible_interior':h-2*radius,'lower_threshold':h-radius,
                         'threshold':h,'upper_threshold':h+radius,
                         'task_interior':h+2*radius,'high_endpoint':ghi+radius,
                         'above_calibration':ghi+2*radius}.items():
        queries['reference_'+label]={'kind':'reference','center':str(center)}
    results={}
    for name,q in queries.items():
        result=w.decide(p,q);results[name]=result;checks+=1
        if q['kind']=='vacuum':
            cost=sum(8*A**16*t.minimum_abs(tuple(map(Q,q['readings'][str(A)]))) for A in (3,4))
            reduced=copy.deepcopy(data);reduced['budget']=str(M-cost)
            assert M>=cost
            replay=engine.certify(reduced)
            expected='SOURCE_PRIOR_INCOMPATIBLE' if replay['status']=='CERTIFIED_INFEASIBLE' else 'UNRESOLVED'
            assert result['outcome']==expected and replay['status']!='CERTIFIED_FEASIBLE'
            assert Q(result['necessary_cost'])==Q(replay['necessary_moment_cost_lower_bound'])+cost
        elif result['outcome']!='CALIBRATION_INCOMPATIBLE':
            gain=tuple(map(Q,result['conditioned_gain']))
            replay=r._ConditionedGain(engine,mode,gain).certify(data)
            expected={'CERTIFIED_FEASIBLE':'TASK_CERTIFIED_CONDITIONAL_ON_VALID_REFERENCE',
                      'CERTIFIED_INFEASIBLE':'SOURCE_PRIOR_INCOMPATIBLE','UNRESOLVED':'UNRESOLVED'}[replay['status']]
            assert result['outcome']==expected
            if replay['status']=='CERTIFIED_FEASIBLE':assert replay['nonvacuous_positive_task_certificate']
        if 'boundary' in name and q['kind']=='vacuum':assert result['outcome']=='UNRESOLVED'
    assert results['zero_vacuum']['outcome']==results['near_zero_vacuum']['outcome']=='UNRESOLVED'
    assert results['opposite_signs_outside']['outcome']=='SOURCE_PRIOR_INCOMPATIBLE'
    assert results['reference_lower_threshold']['outcome']=='UNRESOLVED'
    assert results['reference_upper_threshold']['positive_task']
    # Worst-case measurement errors: center in [true_gain-radius,true_gain+radius].
    # Algebraic guarantees use TWO radii. Boundary examples show why one is unsound.
    assert w.decide(p,{'kind':'reference','center':str(h-radius)})['outcome']=='UNRESOLVED'
    assert w.decide(p,{'kind':'reference','center':str(h+radius)})['positive_task']
    error_results={};radii={'3':'1/10000000','4':'1/1000000000'}
    profiles={label:{'3':str(value),'4':'0'} for label,value in
              {'zero':Q(0),'boundary':cap/(8*3**16),
               'error_dependent':cap/(8*3**16)+Q(radii['3']),
               'uniform_conflict':cap/(8*3**16)+3*Q(radii['3'])}.items()}
    profiles['signed_joint_boundary']={'3':str(cap/(16*3**16)),'4':str(-cap/(16*4**16))}
    profiles['signed_joint_error_dependent']={'3':str(cap/(16*3**16)+Q(radii['3'])),
                                             '4':str(-cap/(16*4**16)-Q(radii['4']))}
    for label,values in profiles.items():
        query={'kind':'vacuum_error_envelope','true_values':values,'radii':radii}
        envelope=w.decide(p,query);error_results[label]=envelope;error_profiles+=1
        observed=[]
        for closest in (True,False):
            readings={}
            for A in (3,4):
                x=Q(query['true_values'][str(A)]);rho=Q(radii[str(A)]);sign=1 if x>=0 else -1
                center=sign*max(abs(x)-rho,Q(0)) if closest else x+sign*rho
                assert abs(center-x)<=rho
                readings[str(A)]=[str(center-rho),str(center+rho)]
            decision=w.decide(p,{'kind':'vacuum','readings':readings});observed.append(decision['outcome'])
            expected_cost=envelope['minimum_returned_necessary_cost' if closest else 'maximum_returned_necessary_cost']
            assert decision['added_necessary_cost']==expected_cost
            reduced=copy.deepcopy(data);reduced['budget']=str(M-Q(expected_cost))
            replay=engine.certify(reduced)
            assert (replay['status']=='CERTIFIED_INFEASIBLE')==(decision['outcome']=='SOURCE_PRIOR_INCOMPATIBLE')
            checks+=1
        predicted=('ALL_ERRORS_PRIOR_INCOMPATIBLE' if observed[0]=='SOURCE_PRIOR_INCOMPATIBLE' else
                   'ALL_ERRORS_UNRESOLVED' if observed[1]=='UNRESOLVED' else 'ERROR_DEPENDENT')
        assert envelope['outcome']==predicted
    summaries[mode]={'vacuum_error_profiles':error_results,'illustrative_vacuum_error_radii':radii,
                     'vacuum_added_cost_cap':t.describe((cap,cap)),
                     'vacuum_axis_limits':{str(A):t.describe((cap/(8*A**16),cap/(8*A**16))) for A in (3,4)},
                     'robust_cost_deficit':t.describe((robust_cost-M,robust_cost-M)),
                     'normalized_reference':{'unit':'1e-193','gain':t.describe((glo/Q('1e-193'),ghi/Q('1e-193'))),
                                             'threshold':t.describe((h/Q('1e-193'),h/Q('1e-193')))},
                     'query_outcomes':{name:result['outcome'] for name,result in results.items()}}
    (folder/f'{mode}.json').write_text(json.dumps(p,indent=2)+'\n',encoding='utf-8')
    (folder/f'{mode}-examples.json').write_text(json.dumps({'queries':queries,'results':results},indent=2)+'\n',encoding='utf-8')

rejected=[]
def reject(name,change):
    p=copy.deepcopy(policies['private']);change(p)
    try:w.verify(p)
    except ValueError:rejected.append(name)
    else:raise AssertionError('Accepted '+name)
reject('wrong vacuum cost face',lambda p:p.__setitem__('vacuum_cost_cap',str(Q(p['vacuum_cost_cap'])+1)))
reject('wrong robust obstruction',lambda p:p.__setitem__('robust_cost_deficit','0'))
reject('wrong reference threshold',lambda p:p.__setitem__('threshold',str(Q(p['threshold'])+Q('1e-197'))))
reject('one-radius worst-case claim',lambda p:p.__setitem__('worst_case_task_at_least',str(Q(p['threshold'])+Q(p['reference_radius']))))
reject('overly coarse reference precision',lambda p:p.__setitem__('reference_radius','1'))
reject('physical impossibility claim',lambda p:p['contract'].__setitem__('unresolved','physical_impossibility'))
reject('wrong new source gain',lambda p:p['bridge']['rows'][0].__setitem__('gain',['1','2']))
for q in ({'kind':'vacuum','readings':{'3':['1','0'],'4':['0','0']}},
          {'kind':'reference','center':1}, {'kind':'reference','center':'0','radius':'0'},
          {'kind':'vacuum_error_envelope','true_values':{'3':'0','4':'0'},'radii':{'3':'-1','4':'0'}}):
    try:w.decide(policies['private'],q)
    except ValueError:rejected.append('invalid query')
    else:raise AssertionError('Accepted malformed query')
with tempfile.TemporaryDirectory() as directory:
    d=Path(directory)
    for name in (vp.name,'verify_order16_vacuum_bridge.py','verify_source_task_transition.py'):(d/name).write_bytes((vp.parent/name).read_bytes())
    for mode in policies:
        (d/'policy.json').write_bytes((folder/f'{mode}.json').read_bytes())
        run=subprocess.run([sys.executable,'-I',str(d/vp.name),str(d/'policy.json')],cwd=d,capture_output=True,text=True)
        assert run.returncode==0,run.stderr
        for query in ({'kind':'reference','center':str(Q(policies[mode]['threshold'])+Q(policies[mode]['reference_radius']))},
                      {'kind':'vacuum','readings':{'3':['0','0'],'4':['0','0']}},
                      {'kind':'vacuum_error_envelope','true_values':{'3':'0','4':'0'},'radii':{'3':'1e-7','4':'1e-9'}}):
            (d/'query.json').write_text(json.dumps(query),encoding='utf-8')
            run=subprocess.run([sys.executable,'-I',str(d/vp.name),str(d/'policy.json'),str(d/'query.json')],cwd=d,capture_output=True,text=True)
            assert run.returncode==0,run.stderr
            assert json.loads(run.stdout)==w.decide(policies[mode],query)
assert hashes=={p.name:sha(p) for p in protected}
report={'passed':True,'protected_file_hashes':hashes,'modes':summaries,'independent_query_replays':checks,'worst_case_vacuum_profiles':error_profiles,
        'rejected_corruptions':rejected,'isolated_verification':True,
        'decision':'For resolving this middle gate, prefer a controlled gain reference IF its total-error contract is achievable. Vacuum acquisitions can refute the prior or tighten conditional bounds, but cannot supply a calibration-uniform witness at the unchanged calibration.',
        'limitations':'No acquisition, hardware feasibility, cost optimality, physical ambiguity, or guaranteed resolution near the threshold is asserted.'}
(OUT/'order16-acquisition-policy-tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(f'PASS: two complete conditional policies; {checks} independent outcome replays; {len(rejected)} corruptions rejected; isolated verification')
