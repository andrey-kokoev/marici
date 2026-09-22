"""Portable exact checker for a restricted source/observer change square.

Supports positive diagonal coordinate rescaling, nested calibrated/data intervals,
and sufficient weighted-budget transport. Not a verifier of arbitrary towers.
"""
from fractions import Fraction as F
import hashlib
import json
import sys
from pathlib import Path
import importlib.util


def load_checker():
    path=Path(__file__).with_name('verify_diagonal_task.py')
    spec=importlib.util.spec_from_file_location('task_checker',path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


v=load_checker()


def digest(p):return hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def verify_transition(old,new,c):
    v.fields(c,('version','kind','old_sha256','new_sha256','source_scale','observation_scale','target_scale'))
    v.require(type(c['version']) is int and c['version']==1,'Wrong transition version')
    v.require(c['kind']=='positive-diagonal-refinement-v1','Unsupported transition')
    v.require(c['old_sha256']==digest(old) and c['new_sha256']==digest(new),'Transition digest mismatch')
    # Validate each complete problem without asserting a task outcome.
    for p in (old,new):
        v.verify(p,{'version':1,'problem_sha256':digest(p),'status':'UNRESOLVED'})
    n=len(old['rows']);v.require(len(new['rows'])==n,'Coordinate addition not supported')
    v.array(c['source_scale'],n);v.array(c['observation_scale'],n)
    a=list(map(v.q,c['source_scale']));b=list(map(v.q,c['observation_scale']));g=v.q(c['target_scale'])
    v.require(all(x>0 for x in a+b) and g>0,'Scales must be positive')
    for i,(o,r) in enumerate(zip(old['rows'],new['rows'])):
        # x_new=a*x_old, z_new=b*z_old, E_new=(b/a)*E_old.
        el,eh=map(v.q,o['calibration']);fl,fh=map(v.q,r['calibration'])
        v.require(el<=a[i]*fl/b[i]<=a[i]*fh/b[i]<=eh,'Calibration square/refinement fails')
        dl,dh=map(v.q,o['data']);cl,ch=map(v.q,r['data'])
        v.require(dl<=cl/b[i]<=ch/b[i]<=dh,'Data are not a transported refinement')
        v.require(v.q(o['weight'])/a[i]<=v.q(r['weight']),'Insufficient transported source cost')
    v.require(v.q(new['budget'])<=v.q(old['budget']),'Budget does not imply old prior')
    v.require(all(v.q(new['target']['coefficients'][i])*a[i]==g*v.q(old['target']['coefficients'][i]) for i in range(n)),'Changed target functional')
    v.require(v.q(new['target']['threshold'])==g*v.q(old['target']['threshold']),'Changed target threshold')
    return True


def verify_square(bundle):
    v.fields(bundle,('version','kind','nodes','node_certificates','edges'))
    v.require(type(bundle['version']) is int and bundle['version']==1,'Wrong square version')
    v.require(bundle['kind']=='diagonal-source-observer-square-v1','Unsupported square')
    keys=('00','10','01','11')
    v.fields(bundle['nodes'],keys);v.fields(bundle['node_certificates'],keys)
    edgekeys=('00->10','00->01','10->11','01->11')
    v.fields(bundle['edges'],edgekeys)
    for key in keys:v.verify(bundle['nodes'][key],bundle['node_certificates'][key])
    for key in edgekeys:
        start,end=key.split('->')
        verify_transition(bundle['nodes'][start],bundle['nodes'][end],bundle['edges'][key])
    def compose(first,second):
        a=bundle['edges'][first];b=bundle['edges'][second]
        return tuple(tuple(v.q(x)*v.q(y) for x,y in zip(a[field],b[field]))
                     for field in ('source_scale','observation_scale'))+(v.q(a['target_scale'])*v.q(b['target_scale']),)
    left=compose('00->10','10->11');right=compose('00->01','01->11')
    v.require(left==right,'Source/observer routes do not commute')
    direct={'version':1,'kind':'positive-diagonal-refinement-v1',
        'old_sha256':digest(bundle['nodes']['00']),'new_sha256':digest(bundle['nodes']['11']),
        'source_scale':list(map(str,left[0])),'observation_scale':list(map(str,left[1])),
        'target_scale':str(left[2])}
    verify_transition(bundle['nodes']['00'],bundle['nodes']['11'],direct)
    return True


if __name__=='__main__':
    if len(sys.argv)==3 and sys.argv[1]=='--square':
        verify_square(v.strict_load(sys.argv[2]))
        print('VALID commuting source/observer square, conditional on model assumptions')
    else:
        old,new,c=[v.strict_load(p) for p in sys.argv[1:4]]
        verify_transition(old,new,c)
        print('VALID transition: new feasible sources pull back into old feasible sources')
