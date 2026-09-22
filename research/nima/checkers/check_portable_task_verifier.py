"""Verifier-only semantic, parser and isolated-execution audit."""
from pathlib import Path
import importlib.util
import hashlib
import json
import copy
import tempfile
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
VERIFY=ROOT/'certificates/verify_diagonal_task.py'
spec=importlib.util.spec_from_file_location('verifier_only',VERIFY)
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)


def checksum(p):return hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def main():
    p=v.strict_load(ROOT/'results/py-bridge-problem.json')
    c=v.strict_load(ROOT/'results/py-bridge-certificate.json')
    m=v.strict_load(ROOT/'results/py-bridge-manifest.json')
    assert v.verify(p,c) and v.verify_py_manifest(p,m)
    corruptions=[]
    def problem_change(fn):
        pp,cc,mm=copy.deepcopy((p,c,m));fn(pp)
        cc['problem_sha256']=checksum(pp);mm['problem_sha256']=checksum(pp)
        corruptions.append((pp,cc,mm))
    def certificate_change(fn):
        pp,cc,mm=copy.deepcopy((p,c,m));fn(cc);corruptions.append((pp,cc,mm))
    def manifest_change(fn):
        pp,cc,mm=copy.deepcopy((p,c,m));fn(mm);corruptions.append((pp,cc,mm))
    problem_change(lambda x:x.update(unrecognized='claim'))
    problem_change(lambda x:x['rows'][0].update(hidden_scale='1'))
    problem_change(lambda x:x.update(budget=32))
    problem_change(lambda x:x.update(budget=32.0))
    problem_change(lambda x:x['rows'][0].update(weight=True))
    problem_change(lambda x:x['target'].update(threshold='1'))
    problem_change(lambda x:x['target'].update(coefficients=['0']))
    problem_change(lambda x:x['rows'][0].update(calibration=['1','1']))
    problem_change(lambda x:x['rows'][0].update(data=['0','0']))
    problem_change(lambda x:x.update(metadata={'unsupported':'claim'}))
    problem_change(lambda x:x.update(metadata={'coordinate_roles':[True]}))
    certificate_change(lambda x:x.update(version=True))
    certificate_change(lambda x:x.update(version=1.0))
    certificate_change(lambda x:x.update(status='UNKNOWN_STATUS'))
    certificate_change(lambda x:x.update(unrecognized='claim'))
    certificate_change(lambda x:x['dual'].update(bound='1'))
    certificate_change(lambda x:x['dual'].update(**{'lambda':'-1'}))
    certificate_change(lambda x:x['dual'].update(unrecognized='claim'))
    certificate_change(lambda x:x.update(witness=['0']))
    certificate_change(lambda x:x.update(witness=[1.0]))
    certificate_change(lambda x:x.update(witness={'kind':'inverse-calibration','numerators':['1']}))
    manifest_change(lambda x:x.update(outer_corner=[2,60061]))
    manifest_change(lambda x:x.update(outer_corner=[True,60060]))
    manifest_change(lambda x:x['seams'][0].__setitem__(0,True))
    manifest_change(lambda x:x['seams'][2].__setitem__(2,'forgotten'))
    manifest_change(lambda x:x.update(equation='z_y=P_y'))
    manifest_change(lambda x:x.update(normalized_coordinate='z_y'))
    manifest_change(lambda x:x.update(receiver_gamma='1'))
    manifest_change(lambda x:x.update(calibration=['1','1']))
    manifest_change(lambda x:x.update(source_class='arbitrary source'))
    manifest_change(lambda x:x.update(external_assumptions=[]))
    manifest_change(lambda x:x.update(filtered_nonvanishing_proved=True))
    manifest_change(lambda x:x['evidence_sha256'].update(calibration='not-a-digest'))
    rejected=0
    for pp,cc,mm in corruptions:
        try:
            v.verify(pp,cc);v.verify_py_manifest(pp,mm)
        except (ValueError,KeyError):rejected+=1
        else:raise AssertionError('Semantic corruption accepted')
    assert rejected==len(corruptions)
    parser_cases=['{"budget":"1","budget":"2"}',
                  '{"nested":{"x":"1","x":"2"}}',
                  '{"value":1.5}','{"value":1e-3}',
                  '{"value":NaN}','{"value":Infinity}','{"value":-Infinity}']
    with tempfile.TemporaryDirectory(prefix='task-verifier-input-') as directory:
        f=Path(directory)/'bad.json'
        for text in parser_cases:
            f.write_text(text,encoding='utf-8')
            try:v.strict_load(f)
            except ValueError:pass
            else:raise AssertionError('Unsafe JSON accepted')
    # Exactly one verifier and three evidence files, outside the repository.
    with tempfile.TemporaryDirectory(prefix='portable-py-bridge-') as directory:
        d=Path(directory);(d/'verify.py').write_bytes(VERIFY.read_bytes())
        for name,obj in [('problem',p),('certificate',c),('manifest',m)]:
            (d/(name+'.json')).write_text(json.dumps(obj),encoding='utf-8')
        assert len(list(d.iterdir()))==4
        run=subprocess.run([sys.executable,'-I',str(d/'verify.py'),str(d/'problem.json'),
                            str(d/'certificate.json'),str(d/'manifest.json')],cwd=d,
                            capture_output=True,text=True,timeout=120)
        assert run.returncode==0,(run.stdout,run.stderr)
        assert 'VALID' in run.stdout
    result={'passed':True,'semantic_corruptions_rejected':rejected,
            'strict_parser_cases_rejected':len(parser_cases),
            'recomputed_problem_digests_tested':True,
            'isolated_four_file_execution':True,
            'scope':'No producer, solver, project source recorder or optional numerical package is loaded. The manifest validates the normalization contract and assumption declarations; linked evidence digests are references, not re-verification of those external proofs.'}
    (ROOT/'results/portable-task-verifier-tests.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
