"""Producer/tests for portable scalar source/observer commuting squares."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import json
import copy
import tempfile
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'certificates'/file)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


s=load('solver','diagonal_task_solver.py')
t=load('transition','verify_diagonal_transition.py')


def transform(p,a,b):
    q=copy.deepcopy(p)
    for i,row in enumerate(q['rows']):
        row['data']=[str(F(x)*b[i]) for x in row['data']]
        row['calibration']=[str(F(x)*b[i]/a[i]) for x in row['calibration']]
        row['weight']=str(F(row['weight'])/a[i])
    q['target']['coefficients']=[str(F(x)/a[i]) for i,x in enumerate(q['target']['coefficients'])]
    return q


def edge(p,q,a,b):
    return {'version':1,'kind':'positive-diagonal-refinement-v1','old_sha256':s.digest(p),
            'new_sha256':s.digest(q),'source_scale':list(map(str,a)),
            'observation_scale':list(map(str,b)),'target_scale':'1'}


def square(base,a,b,source_edit=lambda p:None,observer_edit=lambda p:None):
    n=len(a);ones=[F(1)]*n
    x=transform(base,a,ones);source_edit(x)
    y=transform(base,ones,b);observer_edit(y)
    xy=transform(x,ones,b);observer_edit(xy)
    yx=transform(y,a,ones);source_edit(yx)
    assert xy==yx
    nodes={'00':base,'10':x,'01':y,'11':xy}
    edges={'00->10':edge(base,x,a,ones),'00->01':edge(base,y,ones,b),
           '10->11':edge(x,xy,ones,b),'01->11':edge(y,xy,a,ones)}
    bundle={'version':1,'kind':'diagonal-source-observer-square-v1',
            'nodes':nodes,'node_certificates':{k:s.solve(p) for k,p in nodes.items()},'edges':edges}
    assert t.verify_square(bundle)
    return bundle


def main():
    base={'model':s.MODEL,'rows':[{'data':['-1','1'],'calibration':['1','2'],'weight':'1'} for _ in range(2)],
          'budget':'4','target':{'coefficients':['1','1'],'threshold':'0'}}
    def source_edit(p):p['budget']='2'
    def observer_edit(p):
        for row in p['rows']:
            lo,hi=map(F,row['calibration']);row['calibration'][1]=str((lo+hi)/2)
        p['rows'][0]['data']=['5/2','5'];p['rows'][1]['data']=['-7/10','7/10']
    bundle=square(base,[F(2),F(3)],[F(5),F(7)],source_edit,observer_edit)
    assert {k:c['status'] for k,c in bundle['node_certificates'].items()}=={
        '00':'AMBIGUOUS','10':'AMBIGUOUS','01':'TARGET_TRUE','11':'TARGET_TRUE'}
    # A physical saved source-model problem, with independently declared coordinate changes.
    physical=json.loads((ROOT/'results/diagonal-task-example-problem.json').read_text())
    n=len(physical['rows'])
    physical_square=square(physical,[F(2)]*n,[F(3)]*n)
    # An individually valid edge can still destroy route coherence.
    bad=copy.deepcopy(bundle);e=bad['edges']['10->11']
    e.update(source_scale=['2','2'],observation_scale=['10','14'],target_scale='2')
    assert t.verify_transition(bad['nodes']['10'],bad['nodes']['11'],e)
    try:t.verify_square(bad)
    except ValueError as exc:assert 'routes' in str(exc)
    else:raise AssertionError('Noncommuting square accepted')
    rejected=1
    for field,value in [('source_scale',['0','1']),('observation_scale',['-1','1']),
                        ('target_scale','-1'),('target_scale','2'),('version',True)]:
        altered=copy.deepcopy(bundle);altered['edges']['00->10'][field]=value
        try:t.verify_square(altered)
        except ValueError:rejected+=1
        else:raise AssertionError('Invalid edge accepted')
    # Stronger constraints can empty a previously nonempty, positive task.
    old={'model':s.MODEL,'rows':[{'data':['1','2'],'calibration':['1','1'],'weight':'1'}],
         'budget':'2','target':{'coefficients':['1'],'threshold':'0'}}
    empty=copy.deepcopy(old);empty['budget']='0'
    assert t.verify_transition(old,empty,edge(old,empty,[F(1)],[F(1)]))
    assert s.solve(old)['status']=='TARGET_TRUE' and s.solve(empty)['status']=='INFEASIBLE'
    for name,obj in [('source-observer-square',bundle),('physical-source-observer-square',physical_square)]:
        (ROOT/'results'/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    with tempfile.TemporaryDirectory(prefix='source-observer-square-') as directory:
        d=Path(directory)
        for file in ('verify_diagonal_transition.py','verify_diagonal_task.py'):
            (d/file).write_bytes((ROOT/'certificates'/file).read_bytes())
        (d/'square.json').write_text(json.dumps(bundle),encoding='utf-8')
        run=subprocess.run([sys.executable,'-I',str(d/'verify_diagonal_transition.py'),'--square',str(d/'square.json')],
                           cwd=d,capture_output=True,text=True,timeout=60)
        assert run.returncode==0,(run.stdout,run.stderr)
    summary={'passed':True,'square_node_statuses':{k:c['status'] for k,c in bundle['node_certificates'].items()},
        'squares_verified':2,'invalid_transitions_or_routes_rejected':rejected,
        'valid_edges_do_not_imply_commuting_routes_tested':True,
        'refinement_can_empty_feasible_set_tested':True,'isolated_three_file_verification':True,
        'scope':'Positive diagonal presentation changes and monotone data/calibration/prior refinement only. Physical calibration transport remains an externally justified model identification. No arbitrary tower, new channel, ideal-action or derived-class transport is certified.'}
    (ROOT/'results/source-observer-coherence-tests.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
