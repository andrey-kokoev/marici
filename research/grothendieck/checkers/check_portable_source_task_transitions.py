"""Export real saved task refinements; independently verify portable chains."""
from pathlib import Path
import importlib.util,json,hashlib,copy,tempfile,subprocess,sys

HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
VERIFIER=HERE.parent/'certificates'/'verify_source_task_transition.py'
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj
v=module('portable_verifier',VERIFIER)
t=module('task_engine',HERE/'three_channel_source_task.py')
p=module('planning',HERE/'plan_source_task_acquisition.py')
def filehash(path):return hashlib.sha256(path.read_bytes()).hexdigest()
paths=[OUT/name for name in ('three-channel-source-task-calibration.json',
       'three-channel-source-task-calibration-refined.json','three-channel-source-task-calibration-planning.json')]
engines=[t.SourceTask(path) for path in paths]
frozen_path=OUT/'calibration-refinement-frozen-inputs.json'
prior_path=OUT/'three-channel-source-task-fixtures.json'
protected={str(path):filehash(path) for path in paths+[frozen_path,prior_path]}
frozen=json.loads(frozen_path.read_text(encoding='utf-8'))
prior=json.loads(prior_path.read_text(encoding='utf-8'))

def export(engine,data,path):
    problem={'model':'gamma1-real-cubic-order16-v1','mode':data['mode'],
             'raw':{n:list(map(str,t.interval(data['raw'][n]))) for n in t.NAMES},
             'gains':{n:list(map(str,b)) for n,b in engine.calibrations(data['mode']).items()},
             'sigma':{n:list(map(str,b)) for n,b in engine.sigma.items()},
             'tail_multiplier':str(engine.tail_multiplier),'budget':str(data.get('budget',t.DEFAULT_BUDGET)),
             'assumptions':v.ASSUMPTIONS,
             'evidence':{'protocol':engine.cal['protocol_sha256'],
                         'filters':engine.protocol['filter_manifest_sha256'],'calibration':filehash(path)}}
    result=engine.certify(data)
    cert={'version':1,'problem_sha256':v.sha(problem),'status':result['status'],
          'necessary_cost':result['necessary_moment_cost_lower_bound']}
    if result['status']!='CERTIFIED_INFEASIBLE':
        bounds=result['aggregate_readout_enclosures']
        cert['aggregate_bounds']={n:[bounds[k]['lower_rational'],bounds[k]['upper_rational']]
                                 for n,k in [('vacuum','vacuum'),('residual','residual_per_w_squared')]}
        cert['positive_task']=result['nonvacuous_positive_task_certificate']
    if result['status']=='CERTIFIED_FEASIBLE':
        evidence=result['witness_check'] if result.get('witness_check',{}).get('accepted') else result['automatic_witness_search']
        cert['witness']=evidence['coefficients_at_A2']
    v.node(problem,cert)
    return problem,cert

def edge(a,b):return {'version':1,'kind':'identity-calibration-refinement','old_sha256':v.sha(a),'new_sha256':v.sha(b)}
def chain(data):
    pairs=[export(engine,data,path) for engine,path in zip(engines,paths)]
    nodes,certs=map(list,zip(*pairs))
    return {'version':1,'kind':'fixed-data-task-transition-chain-v1','nodes':nodes,'certificates':certs,
            'edges':[edge(a,b) for a,b in zip(nodes,nodes[1:])],'conditional_on_reference':False}

bundles={}
for mode in ('private','reuse'):
    cases=dict(frozen['cases'][mode])
    cases.update({name:prior[mode][name] for name in ('feasible','infeasible')})
    for name,data in cases.items():
        bundle=chain(data);assert not v.verify(bundle)
        bundles[f'{mode}-{name}']=bundle

plan=p.AcquisitionPlan()
for mode in ('private','reuse'):
    for name,offset in [('task',2),('infeasible',-2),('unresolved',0)]:
        center=plan.threshold+offset*plan.radius
        answer=plan.classify_reference(mode,center)
        interval=tuple(map(t.rational,[answer['conditioned_gain_interval']['lower_rational'],answer['conditioned_gain_interval']['upper_rational']]))
        engine=p._ConditionedGain(plan.engine,mode,interval)
        node,cert=export(engine,plan.data[mode],paths[-1])
        bundle=copy.deepcopy(bundles[f'{mode}-middle_threshold']);old=bundle['nodes'][-1]
        e=edge(old,node);e['kind']='controlled-reference-restriction'
        e['reference']={'kind':'hypothetical-known-source-reference-v1','channel':'positive',
                        'source_coefficients':{'positive':'1','crossed':'0','vacuum':'0'},
                        'interval':[str(center-plan.radius),str(center+plan.radius)],
                        'premise':'valid_total_reference_error_including_preparation_and_acquisition'}
        bundle['nodes'].append(node);bundle['certificates'].append(cert);bundle['edges'].append(e)
        bundle['conditional_on_reference']=True
        assert v.verify(bundle)
        bundles[f'{mode}-reference-{name}']=bundle

folder=OUT/'portable-source-task-transitions';folder.mkdir(exist_ok=True)
for name,bundle in bundles.items():
    (folder/f'{name}.json').write_text(json.dumps(bundle,indent=2)+'\n',encoding='utf-8')

# Rebind all digests after mutations: semantic checks must reject, not only hashes.
def rebind(bundle):
    for n,c in zip(bundle['nodes'],bundle['certificates']):c['problem_sha256']=v.sha(n)
    for a,b,e in zip(bundle['nodes'],bundle['nodes'][1:],bundle['edges']):
        e['old_sha256']=v.sha(a);e['new_sha256']=v.sha(b)

def reject(label,bundle,mutate):
    bad=copy.deepcopy(bundle);mutate(bad);rebind(bad)
    try:v.verify(bad)
    except ValueError:rejected.append(label)
    else:raise AssertionError('Accepted corruption: '+label)
rejected=[]
base=bundles['private-middle_threshold'];ref=bundles['private-reference-task']
reject('changed raw data',base,lambda b:b['nodes'][1]['raw']['positive'].__setitem__(1,'1'))
reject('stronger prior is not identity',base,lambda b:b['nodes'][1].__setitem__('budget','1'))
reject('changed target',base,lambda b:b['nodes'][1]['sigma'].__setitem__('positive',['0','1']))
reject('changed physical protocol',base,lambda b:b['nodes'][1]['evidence'].__setitem__('protocol','0'*64))
reject('widened calibration',base,lambda b:b['nodes'][1]['gains']['positive'].__setitem__(1,'1'))
reject('vacuous task flag',base,lambda b:b['certificates'][0].__setitem__('positive_task',True))
reject('false witness',ref,lambda b:b['certificates'][-1]['witness'].__setitem__('positive','0'))
reject('erased reference premise',ref,lambda b:b.__setitem__('conditional_on_reference',False))
reject('unknown reference source',ref,lambda b:b['edges'][-1]['reference']['source_coefficients'].__setitem__('positive','2'))
reject('incorrect reference interval',ref,lambda b:b['edges'][-1]['reference'].__setitem__('interval',['0','1']))
reject('reference evidence laundering',ref,lambda b:b['nodes'][-1]['evidence'].__setitem__('calibration','0'*64))
# A reference cannot silently be relabelled as an analytical edge while retaining
# its evidence fields. Origin authenticity of externally rewritten bundles is
# explicitly not established by this numerical verifier.
reject('reference relabelled retaining external fields',ref,lambda b:b['edges'][-1].__setitem__('kind','identity-calibration-refinement'))
def erase_reference(b):
    b['edges'][-1]['kind']='identity-calibration-refinement'
    del b['edges'][-1]['reference']
    b['conditional_on_reference']=False
reject('reference erased without new analytical evidence',ref,erase_reference)

# Exercise edge checks independently of node certificates.
edge_rejections=[]
for key,value in [('budget','1'),('raw',dict(base['nodes'][1]['raw'],vacuum=['0','0']))]:
    a=copy.deepcopy(base['nodes'][0]);b=copy.deepcopy(base['nodes'][1]);b[key]=value
    try:v.edge(a,b,edge(a,b))
    except ValueError:edge_rejections.append(key)
    else:raise AssertionError('Edge admitted changed '+key)

# Isolated execution: only the standalone verifier and a bundle are copied.
with tempfile.TemporaryDirectory() as directory:
    dest=Path(directory);(dest/VERIFIER.name).write_bytes(VERIFIER.read_bytes())
    for name in ('private-lower_threshold','reuse-reference-task'):
        (dest/'bundle.json').write_bytes((folder/f'{name}.json').read_bytes())
        run=subprocess.run([sys.executable,'-I',str(dest/VERIFIER.name),str(dest/'bundle.json')],cwd=dest,capture_output=True,text=True)
        assert run.returncode==0,run.stderr
    for text in ('{"x":1,"x":2}','{"x":0.1}','{"x":NaN}'):
        path=dest/'bad.json';path.write_text(text,encoding='utf-8')
        try:v.load(path)
        except ValueError:pass
        else:raise AssertionError('Unsafe JSON accepted')
assert all(filehash(Path(path))==value for path,value in protected.items())
report={'passed':True,'bundles':len(bundles),'rejected_corruptions':rejected,
        'independent_edge_rejections':edge_rejections,'isolated_python_verified':True,
        'unchanged_inputs':protected,
        'scope':'Identity calibration chains plus explicitly hypothetical controlled-reference restrictions. Analytical enclosure validity is external. No rescaling square, source action, filtration or derived transport is certified.'}
(OUT/'portable-source-task-transition-tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print('PASS:',len(bundles),'portable chains;',len(rejected),'corruptions rejected; independent edges, strict JSON and isolated execution passed')
