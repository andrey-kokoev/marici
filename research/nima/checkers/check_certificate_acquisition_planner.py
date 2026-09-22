"""Outcome branches are solver calls; all claims pass the independent verifier."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import json
import re
import random
import copy

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'certificates'/file)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


solver=load('solver','diagonal_task_solver.py')
verifier=load('verifier','verify_diagonal_task.py')


def ball(text):
    m=re.fullmatch(r'\[([^ ]+) \+/- ([^\]]+)\]',text)
    if not m:raise ValueError('Expected certified printed Arb ball')
    center,radius=map(F,m.groups());return center-radius,center+radius


def main():
    fixture=json.loads((ROOT/'results/vacuum-outcome-branches.json').read_text())
    cal=json.loads((ROOT/'results/resolved-vacuum-outcomes.json').read_text())
    rawcenter,rawradius=map(F,fixture['old_raw_z0'])
    coarse=ball(cal['calibration_enclosures']['old']);fine=ball(cal['calibration_enclosures']['refined'])
    weights=[F(32),F(8),8*F(3,2)**12,8*F(2)**12,8*F(5,2)**12]
    # Split b4 from the unacquired tail A>=5 so measuring b4 is not double counted.
    base={'model':solver.MODEL,'rows':[
        {'data':[str(rawcenter-rawradius),str(rawcenter+rawradius)],'calibration':list(map(str,coarse)),'weight':str(weights[0])},
        {'data':['9/1000','11/1000'],'calibration':['1','1'],'weight':'8'},
        *[{'data':[str(-F(40)/w),str(F(40)/w)],'calibration':['1','1'],'weight':str(w)} for w in weights[2:]]],
        'budget':'40','target':{'coefficients':['0','1','1','1','1'],'threshold':'0'},
        'metadata':{'coordinate_roles':['a0_at_2','b2','b3','b4','unacquired_vacuum_sum_A_at_least_5'],
                    'last_row':'Prior-derived auxiliary bound, not an acquired reading'}}
    records=[]

    def certify(label,p,parent=None):
        cert=solver.solve(p);verifier.verify(p,cert)
        i=len(records);records.append({'id':i,'label':label,'parent':parent,'problem':p,'certificate':cert})
        return i,cert

    def acquire(parent,row,center,radius):
        p=copy.deepcopy(parent);lo,hi=map(F,p['rows'][row]['data'])
        l=max(lo,center-radius);h=min(hi,center+radius)
        if l>h:raise ValueError('Returned interval contradicts previous interval')
        p['rows'][row]['data']=[str(l),str(h)];return p

    root,_=certify('initial_order_12_state',base)
    zero=acquire(base,2,F(0),F(1,1000))
    iz,cz=certify('A3 vacuum returned near zero',zero,root)
    assert cz['status']=='TARGET_TRUE'
    near=acquire(base,2,F(-1,100),F(1,1000))
    ia,ca=certify('A3 vacuum returned negative-centered',near,root)
    assert ca['status']=='AMBIGUOUS'
    b4=acquire(near,3,F(0),F(1,1000))
    i4,c4=certify('A4 near-zero reading does not resolve this branch',b4,ia)
    assert c4['status']=='AMBIGUOUS'
    refined=acquire(acquire(near,1,F(1,100),F(1,100000)),2,F(-96,10000),F(1,100000))
    ir,cr=certify('conditional refinement of b2 and b3',refined,ia)
    assert cr['status']=='TARGET_TRUE'
    suspect=acquire(base,2,F(12,1000),F(1,1000))
    ic,cc=certify('coarse calibration leaves this outcome open',suspect,root)
    assert cc['status']=='UNRESOLVED'
    tightened=copy.deepcopy(suspect);tightened['rows'][0]['calibration']=list(map(str,fine))
    iff,cf=certify('same observations with refined calibration',tightened,ic)
    assert cf['status']=='INFEASIBLE'
    # Held-out possible returned intervals, generated after the rule was specified.
    rng=random.Random(204919);counts={}
    for k in range(100):
        center=F(rng.randint(-16000,16000),10**6)
        radius=F(rng.randint(1,2000),10**6)
        p=acquire(base,2,center,radius)
        i,c=certify('held_out_A3_'+str(k),p,root)
        if c['status']=='UNRESOLVED':
            tighter=copy.deepcopy(p);tighter['rows'][0]['calibration']=list(map(str,fine))
            _,c=certify('held_out_calibration_refinement_'+str(k),tighter,i)
        counts[c['status']]=counts.get(c['status'],0)+1
    # Independently audit transitions too: no task, budget, coefficient or weight changes.
    for rec in records:
        if rec['parent'] is None:continue
        parent=records[rec['parent']]['problem'];child=rec['problem']
        assert parent['budget']==child['budget'] and parent['target']==child['target']
        for before,after in zip(parent['rows'],child['rows']):
            assert before['weight']==after['weight']
            for field in ('data','calibration'):
                l,h=map(F,before[field]);ll,hh=map(F,after[field])
                assert l<=ll<=hh<=h
    out={'passed':True,'fixed_prior':'sum_A (A/2)^12 p(x_A)<=40',
        'policy':'Classify proposed returned intervals; if unresolved, try supplied tighter calibration. For ambiguous cases compare candidate refinements by their verified outcome certificates.',
        'verified_certificates':len(records),'held_out_outcomes':counts,'records':records,
        'scope':'Finite conditional outcome catalogue, not exhaustive real-outcome coverage or cost-optimal action selection. Observations and analytic calibration are external assumptions. All evidence uses the standalone verifier; no intrinsic module claim is inferred.'}
    (ROOT/'results/certificate-acquisition-planner.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'verified_certificates':len(records),'held_out_outcomes':counts,
                     'example_routes':{'A3_near_zero':cz['status'],'A4_after_ambiguous_A3':c4['status'],
                                       'refine_existing_readings':cr['status'],'refine_calibration':cf['status']}},indent=2))


if __name__=='__main__':main()
