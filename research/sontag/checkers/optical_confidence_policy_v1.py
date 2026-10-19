"""Conservative Bayesian preparation-mean certificate; no empirical calibration."""
import json
import sys
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from energy_task_reduction import EnergyTaskState
from energy_target_controller import target_gain

def policy(shapes,rates,factors,target,relative_error,delta):
    shapes,rates,factors=[tuple(map(S.sympify,x)) for x in (shapes,rates,factors)]
    target,relative_error,delta=map(S.sympify,(target,relative_error,delta))
    if any(len(x)!=2 for x in (shapes,rates,factors)) or any(x<=0 for x in shapes+rates) or any(not 0<=x<=1 for x in factors):
        raise ValueError('invalid public posterior')
    if not 0<relative_error<1 or not 0<delta<1 or target<0:
        raise ValueError('invalid accuracy task')
    means=tuple(f*k/r for f,k,r in zip(factors,shapes,rates))
    if target>sum(means): return {'status':'abstain','reason':'target outside contraction range','gain':None}
    if target==0: return {'status':'certified','gain':S.Integer(0),'bound':S.Integer(0)}
    # v/h²=sum (mi/h)²/Ki <= 1/min Ki for every nonnegative mixture.
    relative_variance_bound=1/min(shapes)
    probability_bound=relative_variance_bound/relative_error**2
    if probability_bound>delta:
        return {'status':'abstain','reason':'insufficient sufficient certificate','gain':None,
                'bound':probability_bound,'needed_min_shape':1/(delta*relative_error**2)}
    q=target_gain(EnergyTaskState(*means,'public posterior; certified mean task'),target)
    return {'status':'certified','gain':q,'bound':probability_bound}

checks={}; decisions=[]
for name,shapes,rates,factors,h in (
    ('low_information',(2,3),(1,2),(S.Rational(3,4),)*2,S.Rational(1,2)),
    ('concentrated_preparation',(400,400),(400,400),(1,1),1),
    ('infeasible',(400,400),(400,400),(1,1),3),
    ('zero_endpoint',(2,3),(1,2),(S.Rational(3,4),)*2,0)):
    d=policy(shapes,rates,factors,h,S.Rational(1,4),S.Rational(1,20))
    decisions.append({'fixture':name,**{k:str(v) if isinstance(v,S.Basic) else v for k,v in d.items()}})
    expected=name in ('concentrated_preparation','zero_endpoint')
    checks[name+'_disposition']=(d['status']=='certified')==expected
    if not expected: checks[name+'_no_control_emitted']=d['gain'] is None
    else:
        m=[S.sympify(f)*k/r for f,k,r in zip(factors,shapes,rates)]
        q=d['gain']
        checks[name+'_target_mean']=S.simplify(q**2*m[0]+q**4*m[1]-h)==0
        checks[name+'_risk_bound']=bool(d['bound']<=S.Rational(1,20))
checks['needed_shape_threshold']=1/(S.Rational(1,20)*S.Rational(1,4)**2)==320
w=S.symbols('w',real=True)
checks['mixture_bound_identity']=S.simplify(1-(w*w+(1-w)**2)-2*w*(1-w))==0
out={'schema':'marici.sontag.optical-confidence-policy.v1','passed':all(checks.values()),
 'scope':'Bayesian preparation-mean risk under independent Gamma model; no photon-count or calibration guarantee',
 'checks':{k:bool(v) for k,v in checks.items()},'decisions':decisions,
 'abstention_effect':'no further gain; previous physical tap and outcomes remain retained'}
p=ROOT/'research/sontag/results/optical-confidence-policy-v1.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':out['passed'],'checks':len(checks)},indent=2))
raise SystemExit(0 if out['passed'] else 1)
