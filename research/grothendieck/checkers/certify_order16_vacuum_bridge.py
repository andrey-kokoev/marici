"""Bind the A3/A4 vacuum rows and verify both acquisition orders at order 16."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,copy,subprocess,sys,tempfile

HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results';ROOT=HERE.parents[2]
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj

t=module('task',HERE/'three_channel_source_task.py')
verifier_path=HERE.parent/'certificates'/'verify_order16_vacuum_bridge.py'
w=module('bridge',verifier_path);v=w.v
cal_path=OUT/'three-channel-source-task-calibration-bulk-norm.json'
engine=t.SourceTask(cal_path)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protected=[cal_path,OUT/'calibration-refinement-frozen-inputs.json',OUT/'three-channel-source-task-fixtures.json',
           OUT/'three-channel-cubic-protocol.json',OUT/'time-bin-cubic-observer.json']
hashes={p.name:digest(p) for p in protected}
new_readings={'3':['1/2500','3/5000'],'4':['3/2000000','1/400000']}
inputs={'kind':'synthetic_new_unit_vacuum_intervals','base_calibration_sha256':digest(cal_path),'readings':new_readings}
input_path=OUT/'order16-vacuum-acquisition-inputs.json'
if input_path.exists():assert json.loads(input_path.read_text(encoding='utf-8'))==inputs,'Do not regenerate changed observations'
else:input_path.write_text(json.dumps(inputs,indent=2)+'\n',encoding='utf-8')
input_hash=digest(input_path)

# Fresh owning structural/source audit; the portable verifier independently
# reconstructs the new rows, cubic realizations, bases and packet actions.
checker=ROOT/'research/voevodsky/checkers/check_vacuum_acquisition_increment.py'
run=subprocess.run([sys.executable,str(checker)],cwd=ROOT,capture_output=True,text=True)
assert run.returncode==0,run.stderr
artifact_path=ROOT/'research/voevodsky/results/vacuum-acquisition-increment.json'
artifact=json.loads(artifact_path.read_text(encoding='utf-8'))
bridge={'artifact':artifact,'artifact_sha256':v.sha(artifact),'measured_scalar_count':2,'reconstructed_saturation':False,
        'rows':[{'background':A,'outer_corner':[A,30030*A],'seams':[[A,2*A],[6*A,30*A],[210*A,2310*A]],
                 'source':'forgotten(2,3)*forgotten(5,7)*forgotten(11,13)',
                 'path_cost':'8','gain':['1','1'],'retained_feature_degree':0,'observed_basis_interval':[0,6]} for A in (3,4)]}

def part(start,end,kind,B):
    interval=new_readings[str(start)] if kind=='acquired' else [str(-B/(8*start**16)),str(B/(8*start**16))]
    return {'start':start,'end':end,'kind':kind,'data':interval,'gain':['1','1']}

def certificate(base,base_cert,node):
    raw={n:tuple(map(Q,base['raw'][n])) for n in t.NAMES}
    gains={n:tuple(map(Q,base['gains'][n])) for n in t.NAMES}
    boxes={n:t.divide(raw[n],gains[n]) for n in t.NAMES}
    B=Q(base['budget']);D=Q(base['tail_multiplier'])
    sigma={n:tuple(map(Q,b)) for n,b in base['sigma'].items()}
    lower=2**16*sum(t.WEIGHTS[n]*t.minimum_abs(boxes[n]) for n in t.NAMES)
    lower+=sum(8*row['start']**16*t.minimum_abs(tuple(map(Q,row['data']))) for row in node['parts'])
    c={'node_sha256':v.sha(node),'status':'UNRESOLVED','necessary_cost':str(lower),
       'bounds':None,'tails':None,'witness':None,'positive_task':False}
    if lower>B:c['status']='CERTIFIED_INFEASIBLE';return c
    remaining=B-lower;first=min(row['start'] for row in node['parts'] if row['kind']=='prior')
    vacuum_tail=remaining/(8*first**16);residual_tail=remaining*D/(32*3**16)
    local_u=boxes['vacuum']
    for row in node['parts']:
        if row['kind']=='acquired':local_u=t.add(local_u,tuple(map(Q,row['data'])))
    local_t=t.add(t.multiply(sigma['positive'],boxes['positive']),t.multiply(sigma['crossed'],boxes['crossed']))
    bounds={'vacuum':t.add(local_u,(-vacuum_tail,vacuum_tail)),
            'residual':t.add(local_t,(-residual_tail,residual_tail))}
    c['bounds']={n:list(map(str,b)) for n,b in bounds.items()}
    c['tails']={'remaining_budget':str(remaining),'vacuum_first_unacquired':first,'residual_first_unacquired':3,
                'vacuum_l1_upper':str(vacuum_tail),'residual_l1_upper':str(residual_tail),
                'joint_vacuum_weight':str(8*first**16),'joint_residual_weight':str(Q(32*3**16)/D)}
    if base_cert['status']=='CERTIFIED_FEASIBLE':
        values=[sum(map(Q,row['data']))/2 if row['kind']=='acquired' else Q(0) for row in node['parts']]
        local=base_cert['witness']
        cost=2**16*sum(t.WEIGHTS[n]*abs(Q(local[n])) for n in t.NAMES)
        cost+=sum(8*row['start']**16*abs(value) for row,value in zip(node['parts'],values))
        if cost<=B:
            c['status']='CERTIFIED_FEASIBLE'
            c['witness']={'local':local,'parts':list(map(str,values)),
                          'other_coefficients':'zero; each aggregate realized at its first background'}
    c['positive_task']=c['status']=='CERTIFIED_FEASIBLE' and all(b[0]>0 for b in bounds.values())
    return c

frozen=json.loads((OUT/'calibration-refinement-frozen-inputs.json').read_text(encoding='utf-8'))
fixtures=json.loads((OUT/'three-channel-source-task-fixtures.json').read_text(encoding='utf-8'))
bundles={};summaries={}
for mode in ('private','reuse'):
    for case in ('feasible','middle_threshold'):
        chain=v.load(OUT/'portable-source-task-transitions'/f'{mode}-{case}-bulk-norm.json');v.verify(chain)
        base=chain['nodes'][-1];base_cert=chain['certificates'][-1]
        data=fixtures[mode][case] if case=='feasible' else frozen['cases'][mode][case]
        replay=engine.certify(data)
        assert base['mode']==mode and base['evidence']['calibration']==digest(cal_path)
        assert base['evidence']['protocol']==engine.cal['protocol_sha256']
        assert base['evidence']['filters']==engine.protocol['filter_manifest_sha256']
        assert base['raw']=={n:list(map(str,t.interval(data['raw'][n]))) for n in t.NAMES}
        assert base['gains']=={n:list(map(str,b)) for n,b in engine.calibrations(mode).items()}
        assert base['sigma']=={n:list(map(str,b)) for n,b in engine.sigma.items()}
        assert Q(base['tail_multiplier'])==engine.tail_multiplier
        assert Q(base['budget'])==Q(data.get('budget',t.DEFAULT_BUDGET))
        assert base_cert['status']==replay['status'] and Q(base_cert['necessary_cost'])==Q(replay['necessary_moment_cost_lower_bound'])
        B=Q(base['budget'])
        layouts={'00':[(3,None,'prior')],'10':[(3,3,'acquired'),(4,None,'prior')],
                 '01':[(3,3,'prior'),(4,4,'acquired'),(5,None,'prior')],
                 '11':[(3,3,'acquired'),(4,4,'acquired'),(5,None,'prior')]}
        nodes={key:{'parts':[part(a,z,kind,B) for a,z,kind in layout]} for key,layout in layouts.items()}
        certs={key:certificate(base,base_cert,node) for key,node in nodes.items()}
        assert certs['00']['bounds']==base_cert['aggregate_bounds']
        assert certs['00']['status']==base_cert['status'] and certs['00']['positive_task']==base_cert['positive_task']
        groups={'00->10':[[0,1]],'00->01':[[0,1,2]],'10->11':[[0],[1,2]],'01->11':[[0],[1],[2]]}
        edges={}
        for name,g in groups.items():
            a,z=name.split('->');edges[name]={'old_sha256':v.sha(nodes[a]),'new_sha256':v.sha(nodes[z]),'groups':g}
            if certs[a]['bounds'] is not None and certs[z]['bounds'] is not None:
                assert all(t.contains(tuple(map(Q,certs[a]['bounds'][n])),tuple(map(Q,certs[z]['bounds'][n]))) for n in ('vacuum','residual'))
        bundle={'version':1,'contract':w.CONTRACT,'base':base,'base_certificate':base_cert,
                'bridge':bridge,'readings':new_readings,'nodes':nodes,'certificates':certs,'edges':edges}
        assert w.verify(bundle)
        name=f'{mode}-{case}';bundles[name]=bundle
        if case=='feasible':
            assert all(c['status']=='CERTIFIED_FEASIBLE' and c['positive_task'] for c in certs.values())
            assert Q(certs['11']['tails']['vacuum_l1_upper'])<Q(certs['00']['tails']['vacuum_l1_upper'])
            assert all(c['tails']['residual_first_unacquired']==3 for c in certs.values())
        else:
            assert certs['00']['status']=='UNRESOLVED' and certs['11']['status']=='CERTIFIED_INFEASIBLE'
        summaries[name]={key:{'status':c['status'],'positive_task':c['positive_task'],
                             'bounds':None if c['bounds'] is None else {target:t.describe(tuple(map(Q,b))) for target,b in c['bounds'].items()}}
                         for key,c in certs.items()}
folder=OUT/'order16-vacuum-bridge';folder.mkdir(exist_ok=True)
for name,bundle in bundles.items():(folder/f'{name}.json').write_text(json.dumps(bundle,indent=2)+'\n',encoding='utf-8')

# Explicit admissible source with unmeasured retained features at BOTH A3,A4.
# They are invisible to the new vacuum seeds by homogeneous feature degree.
extra_cost=32*3**16*Q(1,10000)+32*4**16*Q(1,1000000)
for mode in ('private','reuse'):
    b=bundles[mode+'-feasible'];wit=b['certificates']['11']['witness']
    cost=2**16*sum(t.WEIGHTS[n]*abs(Q(wit['local'][n])) for n in t.NAMES)
    cost+=sum(8*row['start']**16*abs(Q(value)) for row,value in zip(b['nodes']['11']['parts'],wit['parts']))
    assert cost+extra_cost<=Q(b['base']['budget'])
feature_counterexample={'additional_positive_feature_A3':'1/10000','additional_positive_feature_A4':'1/1000000',
                        'total_cost_with_final_witness':str(cost+extra_cost),
                        'reason':'New vacuum rows annihilate all retained words. These nonzero feature backgrounds cannot be moved into a tail beginning at A5.'}

rejected=[]
def rebind(b):
    b['bridge']['artifact_sha256']=v.sha(b['bridge']['artifact'])
    for key,node in b['nodes'].items():b['certificates'][key]['node_sha256']=v.sha(node)
    for name,e in b['edges'].items():
        a,z=name.split('->');e['old_sha256']=v.sha(b['nodes'][a]);e['new_sha256']=v.sha(b['nodes'][z])
def reject(label,change):
    b=copy.deepcopy(bundles['private-feasible']);change(b);rebind(b)
    try:w.verify(b)
    except ValueError:rejected.append(label)
    else:raise AssertionError('Accepted: '+label)
reject('background-two misidentified as split block',lambda b:b['bridge']['rows'][0].__setitem__('background',2))
reject('wrong source endpoint',lambda b:b['bridge']['rows'][0]['outer_corner'].__setitem__(1,60060))
reject('wrong vacuum gain',lambda b:b['bridge']['rows'][0].__setitem__('gain',['1','2']))
reject('wrong cubic path cost',lambda b:b['bridge']['rows'][0].__setitem__('path_cost','2'))
reject('thirty states reconstructed from two readings',lambda b:b['bridge'].__setitem__('reconstructed_saturation',True))
reject('altered structural action',lambda b:b['bridge']['artifact']['blocks'][0]['left_forgotten_edge_actions'][0]['entries_row_col_value'][0].__setitem__(2,2))
reject('wrong ideal filtration',lambda b:b['bridge']['artifact']['blocks'][0].__setitem__('M_basis_indices',[]))
reject('residual backgrounds three/four erased',lambda b:b['certificates']['11']['tails'].__setitem__('residual_first_unacquired',5))
reject('missing partition coordinate',lambda b:b['edges']['10->11'].__setitem__('groups',[[0],[1]]))
reject('duplicated partition coordinate',lambda b:b['edges']['00->01'].__setitem__('groups',[[0,1,1,2]]))
reject('unmeasured tail promoted to sensor',lambda b:b['nodes']['11']['parts'][-1].__setitem__('kind','acquired'))
reject('acquired b3 constraint discarded',lambda b:b['nodes']['11']['parts'][0].__setitem__('kind','prior'))
reject('false joint witness',lambda b:b['certificates']['11']['witness']['parts'].__setitem__(0,'1'))
reject('equivariant tail aggregation claimed',lambda b:b['contract'].__setitem__('tail_aggregation','source_equivariant'))

with tempfile.TemporaryDirectory() as directory:
    dest=Path(directory)
    for source in (verifier_path,verifier_path.with_name('verify_source_task_transition.py')):(dest/source.name).write_bytes(source.read_bytes())
    for name in ('private-feasible','reuse-middle_threshold'):
        (dest/'bundle.json').write_bytes((folder/f'{name}.json').read_bytes())
        run=subprocess.run([sys.executable,'-I',str(dest/verifier_path.name),str(dest/'bundle.json')],cwd=dest,capture_output=True,text=True)
        assert run.returncode==0,run.stderr
assert hashes=={p.name:digest(p) for p in protected} and digest(input_path)==input_hash
report={'passed':True,'structural_artifact_file_sha256':digest(artifact_path),'structural_artifact_canonical_sha256':v.sha(artifact),
        'protected_file_hashes':hashes,'new_inputs_sha256':input_hash,'squares':summaries,
        'unmeasured_feature_counterexample':feature_counterexample,'rejected_corruptions':rejected,
        'isolated_verification':True,'scope':w.CONTRACT}
(OUT/'order16-vacuum-bridge-tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print('PASS: four order-16 acquisition squares, actual unit/cubic source bindings, 30-direction artifact/action audit, 14 rejected corruptions and isolated verification')
