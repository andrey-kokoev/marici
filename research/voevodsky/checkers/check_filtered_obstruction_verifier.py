"""Positive, malformed and adversarial tests of the independent verifier.

Loads only the verifier and saved evidence, never the producer/discovery code.
"""
from pathlib import Path
import copy,hashlib,importlib.util,json,random,shutil,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[3]
vp=ROOT/'research/voevodsky/certificates/verify_filtered_obstruction.py'
spec=importlib.util.spec_from_file_location('independent_verifier',vp)
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
folder=ROOT/'research/voevodsky/results'
p=v.load(folder/'filtered-obstruction-problem.json')
c=v.load(folder/'filtered-obstruction-certificate.json')
assert v.verify(p,c)['verified']
def rejected(pp,cc):
    try:v.verify(pp,cc)
    except (ValueError,KeyError,TypeError,ZeroDivisionError):return
    raise AssertionError('corrupted evidence accepted')
cases=[]
def change(name,fn):
    pp=copy.deepcopy(p);cc=copy.deepcopy(c);fn(pp,cc);cases.append((name,pp,cc))
change('digest',lambda p,c:c.update(problem_sha256='0'*64))
change('local_rank',lambda p,c:c['local_kernels'][0].update(record_rank=5))
change('missing_local_corner',lambda p,c:c['local_kernels'].pop())
change('wrong_local_relation',lambda p,c:c['local_kernels'][0]['relations'][0][0].update(coefficient='-2'))
change('missing_prefix',lambda p,c:c['prefixes'].pop())
change('duplicate_prefix',lambda p,c:c['prefixes'].append(copy.deepcopy(c['prefixes'][0])))
change('wrong_expansion',lambda p,c:c['prefixes'][0]['terms'][0].update(coefficient='2'))
change('wrong_outer_endpoint',lambda p,c:c['prefixes'][0].update(end=63))
change('old_coefficient',lambda p,c:c['prefixes'][0].update(old_coefficients=['1','1']))
change('right_action',lambda p,c:c['prefixes'][0].update(right_action_values=['1','0']))
change('omitted_kernel_generator',lambda p,c:c['N_prefix_ids'].pop())
change('false_kernel_generator',lambda p,c:c['N_prefix_ids'].append(c['witness']['prefix_id']))
change('witness_value',lambda p,c:c['witness'].update(private_value='0'))
change('witness_suffix',lambda p,c:c['witness'].update(suffix_kind=0))
change('integer_coefficient',lambda p,c:c['prefixes'][0]['terms'][0].update(coefficient=1))
change('boolean_mark',lambda p,c:c['prefixes'][0]['terms'][0]['marks'].__setitem__(0,False))
change('invalid_fraction',lambda p,c:c['prefixes'][0]['terms'][0].update(coefficient='1/0'))
def protocol(pp,cc):
    pp['filtrations']['K'][1]='K';cc['problem_sha256']=v.digest(pp)
change('changed_protocol_even_with_new_digest',protocol)
rng=random.Random(270)
for j in range(16):
    idx=rng.randrange(360);side=rng.randrange(2)
    def mutate(pp,cc,idx=idx,side=side):
        cc['prefixes'][idx]['right_action_values'][side]=str(v.rational(cc['prefixes'][idx]['right_action_values'][side])+1)
    change('seeded_action_'+str(j),mutate)
for name,pp,cc in cases:rejected(pp,cc)
# Benign reordering is accepted: no discovery traversal order is trusted.
shuffled=copy.deepcopy(c)
rng.shuffle(shuffled['local_kernels']);rng.shuffle(shuffled['prefixes']);rng.shuffle(shuffled['N_prefix_ids'])
for prefix in shuffled['prefixes']:rng.shuffle(prefix['terms'])
assert v.verify(p,shuffled)['verified']
# Run with only these three files, in isolated Python, outside the repository.
with tempfile.TemporaryDirectory() as td:
    d=Path(td);shutil.copyfile(vp,d/'verify.py')
    for name,obj in [('problem.json',p),('certificate.json',c)]:
        (d/name).write_text(json.dumps(obj),encoding='utf-8')
    cmd=[sys.executable,'-I',str(d/'verify.py'),str(d/'problem.json'),str(d/'certificate.json')]
    run=subprocess.run(cmd,cwd=d,capture_output=True,text=True)
    assert run.returncode==0,run.stderr
    assert json.loads(run.stdout)['verified']
    # Duplicate keys and floats are rejected at the independent JSON boundary.
    for bad in ('{"schema":"a","schema":"b"}','{"coefficient":1.0}'):
        (d/'certificate.json').write_text(bad,encoding='utf-8')
        run=subprocess.run(cmd,cwd=d,capture_output=True,text=True)
        assert run.returncode!=0 and 'REJECTED:' in run.stderr
result={'passed':True,'valid_bundles_checked':2,'semantic_corruptions_rejected':len(cases),
 'malformed_json_cases_rejected':2,'isolated_three_file_execution':True,
 'scope':'Tests the standalone finite certificate verifier, not external theta calibration or the filtered-category theorem.'}
(folder/'filtered-obstruction-verifier-tests.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
