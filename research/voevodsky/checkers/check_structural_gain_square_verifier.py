"""Adversarial and isolated tests; imports the verifier, not the producer."""
from pathlib import Path
import copy,json,runpy,shutil,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[3]
vp=ROOT/'research/voevodsky/certificates/verify_structural_gain_square.py'
v=runpy.run_path(str(vp));verify=v['verify'];mul=v['mul'];matrix=v['matrix']
folder=ROOT/'research/voevodsky/results'
bundle=v['load'](folder/'structural-gain-square.json')
assert verify(bundle)['verified']
def rejects(b):
    try:verify(b)
    except (ValueError,TypeError,KeyError,ZeroDivisionError,IndexError) as e:return str(e)
    raise AssertionError('invalid structural square accepted')
# Valid basis changes in a displayed subspace are not protocol changes.
rebased=copy.deepcopy(bundle)
for node in rebased['nodes'].values():
    for row in node['N']:row[0]=str(2*v['F'](row[0]))
assert verify(rebased)['verified']
# Main negative example: gains and both scalar routes still commute, but
# action matrices have incorrectly been kept fixed in changed coordinates.
stale=copy.deepcopy(bundle)
for node in stale['nodes'].values():
    for key in ('left','right'):node[key]=copy.deepcopy(bundle['nodes']['00'][key])
for key,size in [('upper',5),('lower',2),('pushout',8)]:
    e=stale['edges']
    assert mul(matrix(e['10-11'][key],size,size),matrix(e['00-10'][key],size,size))==mul(matrix(e['01-11'][key],size,size),matrix(e['00-01'][key],size,size))
assert 'upper evaluation does not intertwine' in rejects(stale)
cases=[stale]
def corrupt(fn):
    b=copy.deepcopy(bundle);fn(b);cases.append(b)
corrupt(lambda b:b.update(problem_sha256='0'*64))
corrupt(lambda b:b['nodes']['10']['pi'][0].__setitem__(0,'9'))
corrupt(lambda b:b['nodes']['10']['N'][2].__setitem__(0,'0'))
corrupt(lambda b:b['nodes']['10']['graph'][7].__setitem__(0,'1'))
corrupt(lambda b:b['nodes']['10']['private'][0].__setitem__(3,'0'))
corrupt(lambda b:b['edges']['10-11']['upper'][0].__setitem__(0,'9'))
corrupt(lambda b:b['edges']['10-11']['pushout'][7].__setitem__(7,'2'))
corrupt(lambda b:b['nodes']['10']['D'][0].__setitem__(0,'0'))
corrupt(lambda b:b['nodes']['10']['D'][0].__setitem__(0,True))
corrupt(lambda b:b['problem']['dimensions'].__setitem__('B',True))
corrupt(lambda b:b['nodes']['10']['H'][4].__setitem__(0,'0'))
for bad in cases:rejects(bad)
with tempfile.TemporaryDirectory() as td:
    d=Path(td);shutil.copyfile(vp,d/'verify.py')
    (d/'square.json').write_text(json.dumps(bundle),encoding='utf-8')
    cmd=[sys.executable,'-I',str(d/'verify.py'),str(d/'square.json')]
    p=subprocess.run(cmd,cwd=d,capture_output=True,text=True)
    assert p.returncode==0,p.stderr
    assert json.loads(p.stdout)['verified']
    for malformed in ('{"schema":"x","schema":"y"}','{"x":1.0}','{"x":NaN}'):
        (d/'square.json').write_text(malformed,encoding='utf-8')
        p=subprocess.run(cmd,cwd=d,capture_output=True,text=True)
        assert p.returncode!=0 and 'REJECTED:' in p.stderr
result={'passed':True,'valid_bundles':2,'structural_corruptions_rejected':len(cases),
 'malformed_json_rejected':3,'scalar_commuting_but_action_incompatible_square_rejected':True,
 'isolated_two_file_execution':True,
 'scope':'Finite invertible gain-square fixture; no physical identification or noninvertible tail refinement is certified.'}
(folder/'structural-gain-square-verifier-tests.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
