"""Held-out exact vertex oracle, independent verification, and physical adapters."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import importlib.util
import random
import copy
import json
import re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


s=load('solver',ROOT/'certificates/diagonal_task_solver.py')
v=load('verifier',ROOT/'certificates/verify_diagonal_task.py')


def vertex_oracle(p):
    rows,B,a,threshold=s.parse(p)
    boxes=[(l/e,u/e) for l,u,e,f,w in rows]
    weights=[r[4] for r in rows]
    pieces=[[(lo,F(0)),(F(0),hi)] if lo<0<hi else [(lo,hi)] for lo,hi in boxes]
    values=[]
    for segments in product(*pieces):
        for point in product(*[(lo,hi) for lo,hi in segments]):
            if sum(w*abs(x) for w,x in zip(weights,point))<=B:
                values.append(sum(c*x for c,x in zip(a,point)))
        for free in range(len(rows)):
            others=[i for i in range(len(rows)) if i!=free]
            for endpoints in product(*[segments[i] for i in others]):
                remaining=B-sum(weights[i]*abs(x) for i,x in zip(others,endpoints))
                if remaining<0:continue
                lo,hi=segments[free]
                x=remaining/weights[free]*( -1 if hi<=0 else 1)
                if lo<=x<=hi:
                    values.append(a[free]*x+sum(a[i]*z for i,z in zip(others,endpoints)))
    if not values:return 'INFEASIBLE'
    if min(values)>threshold:return 'TARGET_TRUE'
    if max(values)<=threshold:return 'TARGET_FALSE'
    return 'AMBIGUOUS'


def main():
    rng=random.Random(918273);counts={};records=[];tampered=0
    for case in range(400):
        n=rng.randint(1,3);rows=[]
        for i in range(n):
            lo=F(rng.randint(-9,6),3);hi=lo+F(rng.randint(0,9),3)
            e=F(rng.randint(1,4));upper=e if case<300 else e+F(rng.randint(0,3),4)
            rows.append({'data':[str(lo*e),str(hi*e)],'calibration':[str(e),str(upper)],
                         'weight':str(F(rng.randint(1,4),2))})
        p={'model':s.MODEL,'rows':rows,'budget':str(F(rng.randint(0,18),2)),
           'target':{'coefficients':[str(F(rng.randint(-4,4))) for _ in rows],
                     'threshold':str(F(rng.randint(-5,5),2))}}
        cert=s.solve(p);assert v.verify(p,cert)
        if case<300:assert cert['status']==vertex_oracle(p)
        counts[cert['status']]=counts.get(cert['status'],0)+1
        corrupt=copy.deepcopy(cert);corrupt['problem_sha256']='0'*64
        try:v.verify(p,corrupt)
        except ValueError:tampered+=1
        else:raise AssertionError('Bad digest accepted')
        if cert['status'] in ('TARGET_TRUE','TARGET_FALSE'):
            corrupt=copy.deepcopy(cert);corrupt['dual']['bound']=str(F(corrupt['dual']['bound'])+1)
            try:v.verify(p,corrupt)
            except ValueError:tampered+=1
            else:raise AssertionError('Corrupt bound accepted')
        if cert['status'] in ('TARGET_TRUE','TARGET_FALSE','AMBIGUOUS'):
            corrupt=copy.deepcopy(cert)
            key='true_witness' if cert['status']=='AMBIGUOUS' else 'witness'
            if isinstance(corrupt[key],dict):corrupt[key]['numerators'][0]='999999999'
            else:corrupt[key][0]='999999999'
            try:v.verify(p,corrupt)
            except ValueError:tampered+=1
            else:raise AssertionError('Corrupt witness accepted')
        records.append({'problem':p,'certificate':cert})
    # Existing physical fixture. Import a conservative printed Arb enclosure as INPUT,
    # rather than claiming the rational verifier proves the analytical calibration.
    old=json.loads((ROOT/'results/vacuum-outcome-branches.json').read_text())
    refined=json.loads((ROOT/'results/resolved-vacuum-outcomes.json').read_text())
    match=re.fullmatch(r'\[([^ ]+) \+/- ([^\]]+)\]',refined['calibration_enclosures']['refined'])
    assert match
    ec,er=map(F,match.groups());el,eh=ec-er,ec+er
    m,r=map(F,old['old_raw_z0']);q3=F(3,2)**12;q4=F(2)**12
    physical=[];physical_counts={}
    for case in old['outcomes']:
        center,radius=F(case['center']),F(case['radius'])
        p={'model':s.MODEL,'rows':[
            {'data':[str(m-r),str(m+r)],'calibration':[str(el),str(eh)],'weight':'32'},
            {'data':['9/1000','11/1000'],'calibration':['1','1'],'weight':'8'},
            {'data':[str(center-radius),str(center+radius)],'calibration':['1','1'],'weight':str(8*q3)},
            {'data':[str(-F(40)/(8*q4)),str(F(40)/(8*q4))],
             'calibration':['1','1'],'weight':str(8*q4)}],
           'budget':'40','target':{'coefficients':['0','1','1','1'],'threshold':'0'},
           'metadata':{'auxiliary_row_4':'prior-bounded aggregate unacquired vacuum tail, not a measured coordinate'}}
        cert=s.solve(p);assert v.verify(p,cert)
        physical_counts[cert['status']]=physical_counts.get(cert['status'],0)+1
        physical.append({'center':case['center'],'problem':p,'certificate':cert})
    assert physical_counts=={'INFEASIBLE':6,'AMBIGUOUS':4,'TARGET_TRUE':19}
    for filename,obj in (('diagonal-task-held-out-certificates.json',records),
                         ('diagonal-task-physical-certificates.json',physical)):
        (ROOT/'results'/filename).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    example=next(x for x in physical if x['certificate']['status']=='TARGET_TRUE')
    for key in ('problem','certificate'):
        (ROOT/'results'/('diagonal-task-example-'+key+'.json')).write_text(json.dumps(example[key],indent=2)+'\n',encoding='utf-8')
    summary={'passed':True,'held_out_problems':400,'exact_vertex_oracle_cases':300,
        'held_out_statuses':counts,'rejected_corrupt_certificates':tampered,
        'physical_fixture_counts':physical_counts,
        'scope':'Verifier checks exact rational evidence independently of solver. Source embedding, analytic calibration and physical acquisition remain separately justified inputs.'}
    (ROOT/'results/diagonal-certificate-engine.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
