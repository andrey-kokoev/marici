"""Finite mixed history with physical scalar calibration, gains and vacuum splits."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import json
import copy
import re
import tempfile
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'certificates'/file)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


s=load('solver','diagonal_task_solver.py');h=load('history','verify_refinement_history.py')


def ball(text):
    match=re.fullmatch(r'\[([^ ]+) \+/- ([^\]]+)\]',text)
    center,radius=map(F,match.groups());return [str(center-radius),str(center+radius)]


def gain(p,factor):
    q=copy.deepcopy(p)
    for row in q['rows']:
        row['data']=[str(F(x)*factor) for x in row['data']]
        row['weight']=str(F(row['weight'])/factor)
    q['target']['coefficients']=[str(F(x)/factor) for x in q['target']['coefficients']]
    return q


def main():
    old=json.loads((ROOT/'results/vacuum-outcome-branches.json').read_text())
    cal=json.loads((ROOT/'results/resolved-vacuum-outcomes.json').read_text())
    m,r=map(F,old['old_raw_z0']);coarse=ball(cal['calibration_enclosures']['old']);fine=ball(cal['calibration_enclosures']['refined'])
    w3,w4,w5=(8*F(a,2)**12 for a in (3,4,5))
    def row(weight,data):return {'data':list(map(str,data)),'calibration':['1','1'],'weight':str(weight)}
    def tail(weight):return row(weight,(-F(40)/weight,F(40)/weight))
    head={'data':[str(m-r),str(m+r)],'calibration':coarse,'weight':'32'}
    def problem(rows):return {'model':s.MODEL,'rows':rows,'budget':'40',
        'target':{'coefficients':['0']+['1']*(len(rows)-1),'threshold':'0'}}
    R=problem([head,row(8,(F(9,1000),F(11,1000))),tail(w3)])
    refined_head={'data':[str(m*(1-F(8,100))),str(m*(1+F(8,100)))],
                  'calibration':fine,'weight':'32'}
    A=problem([refined_head,row(8,(F(9,1000),F(11,1000))),
               row(w3,(F(-11,1000),F(-9,1000))),tail(w4)])
    B=gain(R,F(2));B['rows'][0]['data']=[str(2*m*(1-F(9,100))),str(2*m*(1+F(9,100)))]
    C=gain(A,F(2))
    final=problem([copy.deepcopy(refined_head),row(8,(F(999,100000),F(1001,100000))),
        row(w3,(F(-961,100000),F(-959,100000))),row(w4,(F(-1,10**6),F(1,10**6))),tail(w5)])
    D=gain(final,F(2));E=copy.deepcopy(final)
    problems={'R':R,'A':A,'B':B,'C':C,'F':final,'D':D,'E':E}
    edges=[]
    def add(start,end,groups=None,factor=None):
        p,q=problems[start],problems[end]
        cert={'version':1,'old_sha256':s.digest(p),'new_sha256':s.digest(q)}
        if groups is not None:cert.update(kind='unit-tail-partition-v1',groups=groups)
        else:cert.update(kind='positive-diagonal-refinement-v1',source_scale=[str(factor)]*len(p['rows']),
                         observation_scale=[str(factor)]*len(p['rows']),target_scale='1')
        edges.append({'from':start,'to':end,'certificate':cert})
    add('R','A',groups=[[0],[1],[2,3]])
    add('R','B',factor=F(2))
    add('A','C',factor=F(2))
    add('B','C',groups=[[0],[1],[2,3]])
    add('A','F',groups=[[0],[1],[2],[3,4]])
    add('C','D',groups=[[0],[1],[2],[3,4]])
    add('D','E',factor=F(1,2))
    add('F','E',factor=F(1))
    bundle={'version':1,'kind':'finite-scalar-refinement-history-v1',
        'calibration_contract':'one-fixed-ideal-detector-up-to-declared-coordinate-gains',
        'structural_transport':'not-certified',
        'nodes':[{'id':key,'problem':p,'certificate':s.solve(p)} for key,p in problems.items()],
        'edges':edges}
    report=h.verify_history(bundle)
    assert bundle['nodes'][-1]['certificate']['status']=='TARGET_TRUE'
    assert report['alternative_route_comparisons']>=3
    # Changes invisible to the scalar target still must preserve SOURCE identity.
    bad=copy.deepcopy(bundle)
    edge=next(e for e in bad['edges'] if e['from']=='R' and e['to']=='B')
    edge['certificate']['source_scale'][0]='201/100'
    edge['certificate']['observation_scale'][0]='201/100'
    h.maps(R,B,edge['certificate']) # individually valid; target coefficient here is zero
    try:h.verify_history(bad)
    except ValueError as exc:assert 'Incoherent routes' in str(exc)
    else:raise AssertionError('History ignored a source-map mismatch')
    rejected=1
    for change in ('detector','structural','disconnected','cycle'):
        bad=copy.deepcopy(bundle)
        if change=='detector':bad['calibration_contract']='vary-physical-detectors'
        elif change=='structural':bad['structural_transport']='filtered-class-preserved'
        elif change=='disconnected':bad['edges']=[e for e in bad['edges'] if e['to']!='B']
        else:bad['edges'][0]['from']='E'
        try:h.verify_history(bad)
        except ValueError:rejected+=1
        else:raise AssertionError('Invalid history accepted')
    with tempfile.TemporaryDirectory(prefix='mixed-history-') as directory:
        d=Path(directory)
        for file in ('verify_refinement_history.py','verify_diagonal_transition.py',
                     'verify_tail_refinement.py','verify_diagonal_task.py'):
            (d/file).write_bytes((ROOT/'certificates'/file).read_bytes())
        (d/'history.json').write_text(json.dumps(bundle),encoding='utf-8')
        run=subprocess.run([sys.executable,'-I',str(d/'verify_refinement_history.py'),str(d/'history.json')],
                           cwd=d,capture_output=True,text=True,timeout=120)
        assert run.returncode==0,(run.stdout,run.stderr)
    for name,obj in [('mixed-refinement-history',bundle),('mixed-refinement-history-report',report)]:
        (ROOT/'results'/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    summary={'passed':True,'node_statuses':{x['id']:x['certificate']['status'] for x in bundle['nodes']},
        'nodes':report['nodes'],'edges':report['edges'],
        'alternative_route_comparisons':report['alternative_route_comparisons'],
        'semantic_corruptions_rejected':rejected,'isolated_five_file_verification':True,
        'scope':report['scope']}
    (ROOT/'results/mixed-refinement-history-tests.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
