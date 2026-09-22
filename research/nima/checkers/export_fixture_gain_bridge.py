"""Fixture-level structural/numerical join with independent portability tests."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import copy
import json
import tempfile
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
STRUCT=ROOT.parent/'voevodsky'


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


s=load('solver',ROOT/'certificates/diagonal_task_solver.py')
b=load('bridge',ROOT/'certificates/verify_fixture_gain_bridge.py')
SV=STRUCT/'certificates/verify_structural_gain_square.py'


def numeric(gains):
    nodes={}
    for key,g in gains.items():
        nodes[key]={'model':s.MODEL,'rows':[{'data':[str(g*F(9,10)),str(g*F(11,10))],
            'calibration':[str(g),str(g)],'weight':'1'}],
            'budget':'2','target':{'coefficients':['1'],'threshold':'1/2'}}
    edges={}
    for start,end in (('00','10'),('00','01'),('10','11'),('01','11')):
        edges[start+'->'+end]={'version':1,'kind':'positive-diagonal-refinement-v1',
            'old_sha256':s.digest(nodes[start]),'new_sha256':s.digest(nodes[end]),
            'source_scale':['1'],'observation_scale':[str(gains[end]/gains[start])],'target_scale':'1'}
    return {'version':1,'kind':'diagonal-source-observer-square-v1','nodes':nodes,
            'node_certificates':{k:s.solve(p) for k,p in nodes.items()},'edges':edges}


def link_for(structural,numerical,gains):
    return {'version':1,'kind':'fixture-private-row-gain-bridge-v1','scope':'finite-structural-fixture-only',
        'structural_sha256':b.digest(structural),'numerical_sha256':b.digest(numerical),
        'normalized_error_bound':'1/10','identifications':{
            key:{'source_witness':['1'],'raw_row':['0','0','0','1','0'],
                 'normalized_row':node['private'][0][:],'raw_factor':str(gains[key]),
                 'raw_center':str(gains[key]),'raw_radius':str(gains[key]/10)}
            for key,node in structural['nodes'].items()}}


def main():
    structural=b.v.strict_load(STRUCT/'results/structural-gain-square.json')
    gains={key:F(node['f'][3][0]) for key,node in structural['nodes'].items()}
    numerical=numeric(gains);link=link_for(structural,numerical,gains)
    assert b.verify_bridge(structural,numerical,link,SV)
    assert all(c['status']=='TARGET_TRUE' for c in numerical['node_certificates'].values())
    corruptions=[]
    # Both independent squares valid; the proposed identification is not.
    other_gains={'00':F(1),'10':F(5),'01':F(7),'11':F(35)}
    other_numeric=numeric(other_gains);assert b.t.verify_square(other_numeric)
    load('structural_verifier',SV).verify(structural)
    corruptions.append((structural,other_numeric,link_for(structural,other_numeric,other_gains)))
    bad=copy.deepcopy(link);bad['identifications']['00']['raw_row'][2]='1'
    # This bad raw row still gives the correct value on f(1).
    assert sum(F(x)*F(r[0]) for x,r in zip(bad['identifications']['00']['raw_row'],structural['nodes']['00']['f']))==1
    corruptions.append((structural,numerical,bad))
    bad=copy.deepcopy(link);bad['identifications']['00']['normalized_row'][2]='1'
    corruptions.append((structural,numerical,bad))
    bad=copy.deepcopy(link);bad['identifications']['10']['source_witness']=['2'];corruptions.append((structural,numerical,bad))
    bad=copy.deepcopy(link);bad['normalized_error_bound']='1/20';corruptions.append((structural,numerical,bad))
    bad=copy.deepcopy(link);bad['scope']='physical-270-row-observer';corruptions.append((structural,numerical,bad))
    wrong_structure=copy.deepcopy(structural)
    wrong_structure['nodes']['10']['left']=copy.deepcopy(structural['nodes']['00']['left'])
    bad=copy.deepcopy(link);bad['structural_sha256']=b.digest(wrong_structure)
    corruptions.append((wrong_structure,numerical,bad))
    rejected=0
    for st,nu,li in corruptions:
        try:b.verify_bridge(st,nu,li,SV)
        except ValueError:rejected+=1
        else:raise AssertionError('Invalid cross-layer identification accepted')
    for name,obj in [('fixture-gain-bridge-structural',structural),('fixture-gain-bridge-numerical',numerical),('fixture-gain-bridge-link',link)]:
        (ROOT/'results'/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    with tempfile.TemporaryDirectory(prefix='fixture-gain-bridge-') as directory:
        d=Path(directory)
        for filename in ('verify_fixture_gain_bridge.py','verify_diagonal_transition.py','verify_diagonal_task.py'):
            (d/filename).write_bytes((ROOT/'certificates'/filename).read_bytes())
        (d/SV.name).write_bytes(SV.read_bytes())
        for filename,obj in [('structural.json',structural),('numerical.json',numerical),('link.json',link)]:
            (d/filename).write_text(json.dumps(obj),encoding='utf-8')
        assert len(list(d.iterdir()))==7
        run=subprocess.run([sys.executable,'-I',str(d/'verify_fixture_gain_bridge.py'),
             str(d/'structural.json'),str(d/'numerical.json'),str(d/'link.json'),str(d/SV.name)],
             cwd=d,capture_output=True,text=True,timeout=120)
        assert run.returncode==0,(run.stdout,run.stderr)
    report={'passed':True,'node_raw_factors':{k:str(g) for k,g in gains.items()},
        'normalized_source_target':'a > 1/2 at every node','normalized_reading_error_bound':'1/10',
        'invalid_identifications_rejected':rejected,'individually_valid_but_mismatched_squares_rejected':True,
        'agreement_on_source_witness_alone_is_insufficient_tested':True,
        'isolated_seven_file_verification':True,
        'scope':'Explicit join of the finite structural fixture and its one-dimensional top-source task. Not an identification with the physical 270-row source, its theta calibration or its terminal-record ideal.'}
    (ROOT/'results/fixture-gain-bridge-tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
