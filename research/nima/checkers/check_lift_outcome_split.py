"""Verify conditional schemas and outcome gates; never select a parent branch."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
ROOT=Path(__file__).resolve().parents[1]
HOME=Path.home()
source=ROOT/'agda/TickLiftOutcomeSplit.agda'

def active_branches(parent_outcome):
    return {'positive':parent_outcome=='++','negative':parent_outcome=='-+'}

def local_core_consequences(outcome):
    return {'parent_rejection':outcome=='-+',
            'witness_return_test_enabled':outcome=='++',
            'parent_proof':False}

def main():
    # Failed attempts and the unattempted state activate neither implication.
    expected={None:(False,False),'++':(True,False),'+-':(False,False),'-+':(False,True),'--':(False,False)}
    for outcome,pair in expected.items():
        assert tuple(active_branches(outcome).values())==pair
        effects=local_core_consequences(outcome)
        assert effects['parent_rejection']==(outcome=='-+')
        assert effects['witness_return_test_enabled']==(outcome=='++')
        assert effects['parent_proof'] is False
    command=[os.environ.get('NIMA_AGDA',str(HOME/'tools/cubical-agda/agda-2.8.0/agda.exe')),
             '--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for directory in (ROOT/'agda',Path(os.environ.get('NIMA_CUBICAL',str(HOME/'tools/cubical-agda/cubical-0.9')))):
        command+=['-i',str(directory)]
    command.append(str(source))
    paths=[source,Path(__file__).resolve()]
    before={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    try:
        run=subprocess.run(command,capture_output=True,timeout=300)
        output=run.stdout+run.stderr; code=run.returncode
    except subprocess.TimeoutExpired as error:
        output=(error.stdout or b'')+(error.stderr or b''); code=None
    (ROOT/'results/agda-TickLiftOutcomeSplit.log').write_bytes(output)
    stable=all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in before.items())
    result={'status':'pass' if code==0 and stable else ('timeout' if code is None else 'fail'),
            'command':command,'exit_code':code,'fresh_dependency_check':True,'source_sha256':before,
            'conditional_theorems':['positive-branch','negative-branch','local-core-rejection-refutes-full','extend-local-witness'] if code==0 else [],
            'gate_cases_checked':len(expected),'local_core_gate_cases_checked':len(expected),'parent_truth_established':False,
            'scope':'Parametric implication proofs only; the source-derived candidate contract is not instantiated.'}
    (ROOT/'results/lift-outcome-split.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if result['status']=='pass' else 1)
if __name__=='__main__': main()
