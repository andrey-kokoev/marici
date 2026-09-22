"""Actual vacuum-tail aggregate model: two splitting orders, one task."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import copy
import json
import tempfile
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'certificates'/file)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


s=load('solver','diagonal_task_solver.py');v=load('tail_verifier','verify_tail_refinement.py')


def problem(weights,data):
    return {'model':s.MODEL,'rows':[{'data':list(map(str,bounds)),
             'calibration':['1','1'],'weight':str(w)} for w,bounds in zip(weights,data)],
            'budget':'40','target':{'coefficients':['1']*len(weights),'threshold':'0'}}


def main():
    w3,w4,w5=(8*F(a,2)**12 for a in (3,4,5))
    cap=lambda w:(-F(40)/w,F(40)/w)
    b3=(F(1,1000),F(2,1000));b4=(F(0),F(1,10000))
    nodes={'00':problem([w3],[cap(w3)]),
           '10':problem([w3,w4],[b3,cap(w4)]),
           '01':problem([w3,w5],[cap(w3),cap(w5)]),
           '11':problem([w3,w4,w5],[b3,b4,cap(w5)])}
    maps={'00->10':[[0,1]],'00->01':[[0,1]],'10->11':[[0],[1,2]],'01->11':[[0,1],[2]]}
    edges={}
    for key,groups in maps.items():
        old,new=key.split('->')
        edges[key]={'version':1,'kind':'unit-tail-partition-v1','old_sha256':s.digest(nodes[old]),
                    'new_sha256':s.digest(nodes[new]),'groups':groups}
    bundle={'version':1,'kind':'tail-refinement-square-v1','nodes':nodes,
            'node_certificates':{k:s.solve(p) for k,p in nodes.items()},'edges':edges}
    assert v.verify_bundle(bundle)
    statuses={k:c['status'] for k,c in bundle['node_certificates'].items()}
    assert statuses=={'00':'AMBIGUOUS','10':'AMBIGUOUS','01':'AMBIGUOUS','11':'TARGET_TRUE'}
    # Missing/duplicated coordinates cannot silently erase a source or its cost.
    bad=copy.deepcopy(bundle);bad['edges']['10->11']['groups']=[[0],[0,2]]
    try:v.verify_bundle(bad)
    except ValueError:pass
    else:raise AssertionError('Invalid partition accepted')
    # A narrow old aggregate observation must not be discarded during splitting.
    old=problem([w3],[(F(0),F(0))]);new=nodes['11']
    e={'version':1,'kind':'unit-tail-partition-v1','old_sha256':s.digest(old),
       'new_sha256':s.digest(new),'groups':[[0,1,2]]}
    try:v.verify_edge(old,new,e)
    except ValueError:pass
    else:raise AssertionError('Old observation erased')
    with tempfile.TemporaryDirectory(prefix='tail-square-') as directory:
        d=Path(directory)
        for file in ('verify_tail_refinement.py','verify_diagonal_task.py'):
            (d/file).write_bytes((ROOT/'certificates'/file).read_bytes())
        (d/'square.json').write_text(json.dumps(bundle),encoding='utf-8')
        run=subprocess.run([sys.executable,'-I',str(d/'verify_tail_refinement.py'),str(d/'square.json')],
                           cwd=d,capture_output=True,text=True,timeout=60)
        assert run.returncode==0,(run.stdout,run.stderr)
    (ROOT/'results/tail-refinement-square.json').write_text(json.dumps(bundle,indent=2)+'\n',encoding='utf-8')
    result={'passed':True,'node_statuses':statuses,'isolated_verification':True,
        'rejected_missing_coordinate_and_erased_observation':True,
        'scope':'Vacuum source aggregate restrictions and sufficient budget/interval transport. Same fixed old detector; no physical calibration sweep, unknown feature mixing, or derived-class transport.'}
    (ROOT/'results/tail-refinement-coherence.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
