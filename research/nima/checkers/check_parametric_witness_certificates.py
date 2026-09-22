"""Independent verification and corner audits for inverse-calibration witnesses."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import importlib.util
import random
import copy
import json

ROOT=Path(__file__).resolve().parents[1]


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'certificates'/file)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


s=load('solver','diagonal_task_solver.py');v=load('verifier','verify_diagonal_task.py')


def main():
    rng=random.Random(607193);records=[];corner_checks=0;rejected=0
    for k in range(180):
        if k<120:
            n=rng.randint(1,3);rows=[];coefs=[];low=high=F(0);cost=F(0)
            for i in range(n):
                d=F(rng.choice([-3,-2,-1,1,2,3]));e=F(rng.randint(1,3));f=e+F(rng.randint(1,4),4)
                w=F(rng.randint(1,3));a=F(rng.randint(-3,3))
                rows.append({'data':[str(d),str(d)],'calibration':[str(e),str(f)],'weight':str(w)})
                coefs.append(a);cost+=w*abs(d)/e
                ends=(a*d/e,a*d/f);low+=min(ends);high+=max(ends)
            threshold=low-1 if k%2==0 else high+1
            expected='TARGET_TRUE' if k%2==0 else 'TARGET_FALSE'
            B=cost+1
        else:
            e=F(rng.randint(1,4));f=e+1
            rows=[{'data':['1','1'],'calibration':['1','2'],'weight':'1'},
                  {'data':['-1','1'],'calibration':[str(e),str(f)],'weight':'1'}]
            coefs=[F(0),F(1)];threshold=F(0);B=F(2);expected='AMBIGUOUS'
        p={'model':s.MODEL,'rows':rows,'budget':str(B),
           'target':{'coefficients':list(map(str,coefs)),'threshold':str(threshold)}}
        assert s.solve_fixed(p)['status']=='UNRESOLVED'
        c=s.solve(p);assert c['version']==2 and c['status']==expected and v.verify(p,c)
        keys=['witness'] if expected!='AMBIGUOUS' else ['true_witness','false_witness']
        for key in keys:
            numerators=list(map(F,c[key]['numerators']))
            for calibration in product(*[list(map(F,row['calibration'])) for row in rows]):
                x=[d/E for d,E in zip(numerators,calibration)]
                assert sum(F(row['weight'])*abs(z) for row,z in zip(rows,x))<=B
                for row,E,z in zip(rows,calibration,x):
                    l,u=map(F,row['data']);assert l<=E*z<=u
                value=sum(a*z for a,z in zip(coefs,x))
                if expected=='TARGET_TRUE' or key=='true_witness':assert value>threshold
                else:assert value<=threshold
                corner_checks+=1
        mutations=[]
        bad=copy.deepcopy(c);bad['version']=1;mutations.append(bad)
        bad=copy.deepcopy(c);bad['witness_semantics']='one-source-for-all-calibrations';mutations.append(bad)
        bad=copy.deepcopy(c);bad[keys[0]]['kind']='arbitrary-function';mutations.append(bad)
        bad=copy.deepcopy(c);bad[keys[0]]['numerators'][0]='999999';mutations.append(bad)
        for bad in mutations:
            try:v.verify(p,bad)
            except ValueError:rejected+=1
            else:raise AssertionError('Invalid parametric certificate accepted')
        records.append({'problem':p,'certificate':c})
    # Family feasibility does not prove the target for every feasible source.
    p={'model':s.MODEL,'rows':[{'data':['1','3'],'calibration':['1','2'],'weight':'1'}],
       'budget':'3','target':{'coefficients':['1'],'threshold':'1'}}
    forged={'version':2,'problem_sha256':s.digest(p),'status':'TARGET_TRUE',
            'witness_semantics':'for-every-calibration-there-exists-source',
            'witness':{'kind':'inverse-calibration','numerators':['3']},
            'dual':{'lambda':'0','bound':'1/2'}}
    try:v.verify(p,forged)
    except ValueError:rejected+=1
    else:raise AssertionError('Existential target witness mistaken for universal conclusion')
    # Worst-case budget, not a favored calibration endpoint, is required.
    p={'model':s.MODEL,'rows':[{'data':['1','1'],'calibration':['1','2'],'weight':'1'}],
       'budget':'3/4','target':{'coefficients':['1'],'threshold':'0'}}
    forged.update(problem_sha256=s.digest(p),witness={'kind':'inverse-calibration','numerators':['1']})
    try:v.verify(p,forged)
    except ValueError:rejected+=1
    else:raise AssertionError('Endpoint-only feasible policy accepted')
    summary={'passed':True,'version_1_unresolved_cases_resolved':len(records),
             'calibration_corner_checks':corner_checks,'rejected_invalid_certificates':rejected,
             'statuses':{'TARGET_TRUE':60,'TARGET_FALSE':60,'AMBIGUOUS':60},
             'scope':'Fixed numerator policies only; universal target bounds remain independent dual certificates. No arbitrary calibration-dependent program is admitted.'}
    (ROOT/'results/parametric-witness-certificates.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
    (ROOT/'results/parametric-witness-summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
