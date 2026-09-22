"""Export/test the minimal retention policy, without changing receiver behavior."""
from pathlib import Path
import hashlib,json,runpy,copy,tempfile,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[3]
manifest=ROOT/'research/grothendieck/results/finite-cubic-observer.json'
vp=ROOT/'research/voevodsky/certificates/verify_minimal_matched_retention.py'
v=runpy.run_path(str(vp))
# The policy is data; the verifier independently checks its structural claim.
policy={'schema':'minimal-matched-retention-v1',
 'manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),
 'raw_row_index':76,
 'raw_shape':[[['e',0,1,1],['e',7,15,0],['e',15,31,0]],[0,1,0,0]],
 'contract':{'retained_products':['combined_scalar_with_existing_error_fields','unscaled_joint_filter_row'],
 'raw_error_rule':'component_error_at_most_total_joint_l1_error',
 'comparison_target':'background-two vacuum acquisition kernel, not complete raw observer',
 'external_hypotheses':['common filter nonzero on windows [2,4] and [4,12]',
 '270 declared private rows have nonzero response factors',
 'fixed labelled source and unchanged first two observer stages',
 'declared acquired readings and error budget are valid']},
 'raw_increment_intervals':[[0,3],[0,4],[0,5],[0,6],[1,5],[1,6]],
 'inherited_filtration_dimensions':[6,5,1,0]}
report=v['verify'](manifest,policy)
assert report['verified']
changes=[lambda x:x.update(manifest_sha256='0'*64),lambda x:x.update(raw_row_index=77),
 lambda x:x.update(raw_row_index=True),lambda x:x['raw_shape'][0][0].__setitem__(3,0),
 lambda x:x['raw_increment_intervals'].pop(),lambda x:x.update(inherited_filtration_dimensions=[6,6,1,0]),
 lambda x:x['contract'].update(comparison_target='complete raw observer'),
 lambda x:x['contract'].update(raw_error_rule='divide total error by the final gain')]
for change in changes:
    bad=copy.deepcopy(policy);change(bad)
    try:v['verify'](manifest,bad)
    except (ValueError,KeyError,TypeError,IndexError):pass
    else:raise AssertionError('bad retention policy accepted')
with tempfile.TemporaryDirectory() as td:
    d=Path(td);shutil.copyfile(vp,d/'verify.py');shutil.copyfile(manifest,d/'manifest.json')
    (d/'policy.json').write_text(json.dumps(policy),encoding='utf-8')
    cmd=[sys.executable,'-I',str(d/'verify.py'),str(d/'manifest.json'),str(d/'policy.json')]
    p=subprocess.run(cmd,cwd=d,capture_output=True,text=True,timeout=120)
    assert p.returncode==0,p.stderr
    assert json.loads(p.stdout)['verified']
    # A manifest change without rebinding is rejected before any source claim.
    changed=json.loads((d/'manifest.json').read_text());changed['rows'][76]['sign']*=-1
    (d/'manifest.json').write_text(json.dumps(changed),encoding='utf-8')
    p=subprocess.run(cmd,cwd=d,capture_output=True,text=True,timeout=120)
    assert p.returncode!=0 and 'manifest digest' in p.stderr
folder=ROOT/'research/voevodsky/results'
(folder/'minimal-matched-retention-policy.json').write_text(json.dumps(policy,indent=2)+'\n',encoding='utf-8')
report.update({'invalid_policies_rejected':len(changes),'manifest_rebinding_required':True,
 'isolated_three_file_execution':True,'receiver_behavior_changed':False})
(folder/'minimal-matched-retention-tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
