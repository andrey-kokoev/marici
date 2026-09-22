"""Portable certificates for unit-calibrated aggregate-tail splitting."""
from pathlib import Path
import importlib.util
import hashlib
import json
import sys
from fractions import Fraction as F

spec=importlib.util.spec_from_file_location('task',Path(__file__).with_name('verify_diagonal_task.py'))
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)


def digest(p):return hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def verify_edge(old,new,e):
    v.fields(e,('version','kind','old_sha256','new_sha256','groups'))
    v.require(type(e['version']) is int and e['version']==1 and e['kind']=='unit-tail-partition-v1','Unsupported tail edge')
    v.require(e['old_sha256']==digest(old) and e['new_sha256']==digest(new),'Digest mismatch')
    for p in (old,new):v.verify(p,{'version':1,'problem_sha256':digest(p),'status':'UNRESOLVED'})
    groups=e['groups'];v.array(groups,len(old['rows']))
    flat=[]
    for group in groups:
        v.array(group);v.require(len(group)>0 and all(type(i) is int for i in group),'Invalid group')
        flat+=group
    v.require(sorted(flat)==list(range(len(new['rows']))),'Groups must partition new coordinates')
    B=v.q(new['budget']);v.require(B<=v.q(old['budget']),'Budget weakened')
    v.require(new['target']['threshold']==old['target']['threshold'],'Threshold changed')
    for i,group in enumerate(groups):
        row=old['rows'][i];w=v.q(row['weight']);lo,hi=map(v.q,row['data'])
        for j in group:
            v.require(v.q(new['rows'][j]['weight'])>=w,'Tail cost understated')
            v.require(v.q(new['target']['coefficients'][j])==v.q(old['target']['coefficients'][i]),'Task not preserved by sum')
        if len(group)==1:
            child=new['rows'][group[0]];a,b=map(v.q,child['data']);el,eh=map(v.q,row['calibration']);fl,fh=map(v.q,child['calibration'])
            v.require(lo<=a<=b<=hi and el<=fl<=fh<=eh,'Singleton does not refine old row')
        else:
            v.require(list(map(v.q,row['calibration']))==[F(1),F(1)],'Aggregate must have unit calibration')
            for j in group:v.require(list(map(v.q,new['rows'][j]['calibration']))==[F(1),F(1)],'Split channel must have unit calibration')
            lower=sum(v.q(new['rows'][j]['data'][0]) for j in group)
            upper=sum(v.q(new['rows'][j]['data'][1]) for j in group)
            v.require((lo<=lower and upper<=hi) or (lo<=-B/w and B/w<=hi),
                      'Split discards an old aggregate observation')
    return True


def verify_bundle(b):
    v.fields(b,('version','kind','nodes','node_certificates','edges'))
    v.require(type(b['version']) is int and b['version']==1 and b['kind']=='tail-refinement-square-v1','Bad bundle')
    keys=('00','10','01','11');edges=('00->10','00->01','10->11','01->11')
    v.fields(b['nodes'],keys);v.fields(b['node_certificates'],keys);v.fields(b['edges'],edges)
    for key in keys:v.verify(b['nodes'][key],b['node_certificates'][key])
    for key in edges:
        a,z=key.split('->');verify_edge(b['nodes'][a],b['nodes'][z],b['edges'][key])
    def compose(a,z):
        return [sorted(k for j in group for k in b['edges'][z]['groups'][j]) for group in b['edges'][a]['groups']]
    left=compose('00->10','10->11');right=compose('00->01','01->11')
    v.require(left==right,'Tail partitions disagree between routes')
    verify_edge(b['nodes']['00'],b['nodes']['11'],{'version':1,'kind':'unit-tail-partition-v1',
        'old_sha256':digest(b['nodes']['00']),'new_sha256':digest(b['nodes']['11']),'groups':left})
    return True


if __name__=='__main__':
    verify_bundle(v.strict_load(sys.argv[1]))
    print('VALID tail-refinement square, conditional on declared source aggregation')
